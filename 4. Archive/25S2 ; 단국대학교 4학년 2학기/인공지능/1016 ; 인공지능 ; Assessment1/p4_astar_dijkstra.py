"""
P4: 가중치 그래프에서 Dijkstra와 A* 구현 및 최단/최장 경로 탐색 스크립트

구성
 1) import
 2) 그래프 로드 (CSV → 인접 리스트)
 3) 휴리스틱 생성 (과제 명세)
 4) Dijkstra (최단)
 5) A* (최단)
 6) 최장 경로: 가중치 음수화 후 Dijkstra/A* 재사용
 7) 결과 출력

실행: python p4_astar_dijkstra.py

주의: CSV는 50x50 가중치 행렬(0 또는 양수). 0은 간선 부재로 간주(대각 제외).
"""

from __future__ import annotations

import os
import math
import heapq
from typing import Dict, List, Tuple, Optional

import numpy as np
import pandas as pd


def resolve_csv_path() -> str:
    """CSV 파일 경로를 추적한다.

    우선 현재 디렉터리의 'G50w.csv', 없으면 'data 2/G50w.csv'를 시도한다.
    두 경로 모두 없으면 FileNotFoundError를 발생시킨다.
    """
    candidates: List[str] = [
        os.path.join(os.getcwd(), "G50w.csv"),
        os.path.join(os.getcwd(), "data 2", "G50w.csv"),
    ]
    for path in candidates:
        if os.path.isfile(path):
            return path
    raise FileNotFoundError("G50w.csv 파일을 현재 디렉터리 또는 'data 2/'에서 찾을 수 없습니다.")


def load_graph_from_csv(csv_path: str) -> Dict[int, Dict[int, float]]:
    """CSV를 인접 리스트 형태로 변환한다.

    지원 형식:
      1) 인접 행렬(정사각, 헤더 유무 무관)
      2) Edge-list: columns in {source,target,weight} (헤더 유무 무관)

    규칙:
      - 0은 간선 없음(행렬형), edge-list는 명시된 간선만 추가
      - 가중치가 양수일 때만 간선으로 추가
    반환: {u: {v: w, ...}, ...}
    """
    # 우선 헤더 포함으로 한 번 읽어본다
    df_try = pd.read_csv(csv_path)
    cols = [c.strip().lower() for c in df_try.columns.tolist()]

    # Edge-list 탐지: 3열이고 source/target/weight 조합인지 확인
    if len(cols) == 3 and set(cols) == {"source", "target", "weight"}:
        df = df_try[[cols[0], cols[1], cols[2]]].copy()
        # 안전하게 숫자 변환
        df = df.apply(pd.to_numeric, errors="coerce")
        df = df.dropna(how="any")
        df = df.astype({cols[0]: int, cols[1]: int, cols[2]: float})

        # 노드 수 추정: 최대 인덱스 + 1 (최소 50 보장)
        max_node = int(max(df[cols[0]].max(), df[cols[1]].max()))
        n = max(50, max_node + 1)
        graph: Dict[int, Dict[int, float]] = {i: {} for i in range(n)}
        for _, row in df.iterrows():
            u = int(row[cols[0]])
            v = int(row[cols[1]])
            w = float(row[cols[2]])
            if u != v and w > 0:
                graph[u][v] = w
        return graph

    # Edge-list가 아니면 인접 행렬로 처리
    try:
        # 헤더 없음 가정
        df = pd.read_csv(csv_path, header=None)
        matrix = df.to_numpy(dtype=float)
    except Exception:
        # 숫자만 남기고 행/열 라벨 제거
        df = df_try.apply(pd.to_numeric, errors="coerce")
        df = df.dropna(how="all", axis=0).dropna(how="all", axis=1)
        df = df.fillna(0.0)
        matrix = df.to_numpy(dtype=float)

    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError(f"CSV가 정사각 행렬이 아닙니다: shape={matrix.shape}")
    n = matrix.shape[0]
    graph: Dict[int, Dict[int, float]] = {i: {} for i in range(n)}
    for i in range(n):
        for j in range(n):
            w = float(matrix[i, j])
            if i != j and w > 0:
                graph[i][j] = w
    return graph


def generate_heuristic(num_nodes: int = 50, seed: int = 42) -> np.ndarray:
    """과제 명세에 따른 A* 휴리스틱 벡터 생성.

    구간별 난수 범위:
      - 노드 0~19: 40 - 40 * U(0,1)
      - 노드 20~39: 30 - 30 * U(0,1)
      - 노드 40~49: 20 - 10 * U(0,1)
    """
    assert num_nodes == 50, "본 과제는 노드 수 50 기준으로 작성되었습니다."
    rng = np.random.default_rng(seed)
    h = np.zeros(num_nodes)
    h[0:20] = 40.0 - 40.0 * rng.random(20)
    h[20:40] = 30.0 - 30.0 * rng.random(20)
    h[40:50] = 20.0 - 10.0 * rng.random(10)
    return h


def reconstruct_path(parent: Dict[int, Optional[int]], start: int, goal: int) -> List[int]:
    """부모 포인터를 이용해 start→goal 경로를 복원한다."""
    path: List[int] = []
    cur = goal
    while cur is not None:
        path.append(cur)
        if cur == start:
            break
        cur = parent.get(cur)
    path.reverse()
    return path


def dijkstra_shortest(graph: Dict[int, Dict[int, float]], start: int, goal: int) -> Tuple[float, List[int]]:
    """Dijkstra: 비음수 가중치 그래프에서 start→goal 최단 경로 비용과 경로를 반환."""
    n = len(graph)
    dist = [math.inf] * n
    parent: Dict[int, Optional[int]] = {start: None}
    dist[start] = 0.0
    pq: List[Tuple[float, int]] = [(0.0, start)]
    visited = [False] * n

    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        if u == goal:
            break
        for v, w in graph[u].items():
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))

    path = reconstruct_path(parent, start, goal)
    return dist[goal], path


def astar_shortest(graph: Dict[int, Dict[int, float]], start: int, goal: int, h: np.ndarray) -> Tuple[float, List[int]]:
    """A*: h는 비음수 추정치(휴리스틱). 반환은 최단 경로 비용과 경로."""
    n = len(graph)
    g = [math.inf] * n  # 실제 시작→노드까지 비용
    parent: Dict[int, Optional[int]] = {start: None}
    g[start] = 0.0

    # 우선순위는 f = g + h
    pq: List[Tuple[float, int]] = [(h[start], start)]
    visited = [False] * n

    while pq:
        f_u, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        if u == goal:
            break

        for v, w in graph[u].items():
            tentative_g = g[u] + w
            if tentative_g < g[v]:
                g[v] = tentative_g
                parent[v] = u
                f_v = g[v] + float(h[v])
                heapq.heappush(pq, (f_v, v))

    path = reconstruct_path(parent, start, goal)
    return g[goal], path


def negate_graph(graph: Dict[int, Dict[int, float]]) -> Dict[int, Dict[int, float]]:
    """모든 간선 가중치를 음수로 변환한 그래프를 반환."""
    return {u: {v: -w for v, w in adj.items()} for u, adj in graph.items()}


def format_result(title: str, shortest: Tuple[float, List[int]], longest: Tuple[float, List[int]], show_abs_for_longest: bool = True) -> None:
    """출력 양식에 맞춰 결과를 인쇄한다."""
    s_cost, s_path = shortest
    l_cost, l_path = longest
    if show_abs_for_longest:
        disp_long = abs(l_cost)
    else:
        disp_long = l_cost

    print(f"=== {title} ===")
    print(f"Shortest: cost={s_cost:.4f}, path={s_path}")
    print(f"Longest: cost={disp_long:.4f}, path={l_path}")
    print()


def main() -> None:
    # 2) 그래프 로드
    csv_path = resolve_csv_path()
    graph = load_graph_from_csv(csv_path)
    num_nodes = len(graph)

    # 3) 휴리스틱 생성 (재현성 고정)
    h = generate_heuristic(num_nodes=num_nodes, seed=42)
    # 확인용: 보고서에 일부 포함 가능
    print("Heuristic sample (first 10):", np.round(h[:10], 4))

    start, goal = 0, num_nodes - 1

    # 4) Dijkstra (최단)
    dj_short_cost, dj_short_path = dijkstra_shortest(graph, start, goal)

    # 5) A* (최단)
    a_star_short_cost, a_star_short_path = astar_shortest(graph, start, goal, h)

    # 6) 최장 경로: 모든 가중치 음수화 후 동일 알고리즘 재사용
    neg_g = negate_graph(graph)

    # Dijkstra 기반 최장 (음수 그래프에서의 최단 = 원 그래프 최장)
    dj_long_cost_neg, dj_long_path = dijkstra_shortest(neg_g, start, goal)

    # A* 기반 최장: 안전하게 h=0 벡터 사용(음수 그래프에 주어진 h를 적용하지 않음)
    zero_h = np.zeros(num_nodes)
    a_star_long_cost_neg, a_star_long_path = astar_shortest(neg_g, start, goal, zero_h)

    # 7) 결과 출력 (요구 형식)
    format_result("Dijkstra", (dj_short_cost, dj_short_path), (dj_long_cost_neg, dj_long_path), show_abs_for_longest=True)
    format_result("A*", (a_star_short_cost, a_star_short_path), (a_star_long_cost_neg, a_star_long_path), show_abs_for_longest=True)


if __name__ == "__main__":
    main()


