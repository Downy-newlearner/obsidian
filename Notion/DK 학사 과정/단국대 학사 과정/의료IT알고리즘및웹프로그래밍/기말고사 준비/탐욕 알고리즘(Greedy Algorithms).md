좋아! '탐욕 알고리즘(Greedy Algorithms)'은 문제 해결 과정에서 항상 현재 상황에서 가장 좋아 보이는 선택을 하는 알고리즘 설계 방법이야. 이러한 각 선택이 최종적인 최적 해를 보장할 수 있는 문제들에 대해 특히 유용해.
### 핵심 내용
1. **기본 개념**
    - **탐욕 선택 속성(Greedy Choice Property)**: 현재 시점에서의 최적 선택이 전체 문제에서도 최적의 해로 이어진다면, 그 선택을 따라가는 속성.
    - **최적 부분 구조(Optimal Substructure)**: 문제의 최적 해가 하위 문제의 최적 해로 구성되는 성질.
2. **중요한 알고리즘 및 사례**
    - **활동 선택 문제(Activity Selection Problem)**: 최대한 많은 활동을 할 수 있도록 겹치지 않는 활동을 선택하는 문제.
    - **단일 출발 최단 경로 문제(Single-Source Shortest Path Problem)**: 각각의 정점까지의 최단 경로를 구하는 다익스트라 알고리즘(Dijkstra's Algorithm).
    - **최소 신장 트리(Minimum Spanning Tree, MST)**: 모든 정점을 포함하면서 사이클이 없는 최소 가중치의 트리를 찾는 문제. 대표적으로 크루스칼(Kruskal)의 알고리즘과 프림(Prim)의 알고리즘이 있음.
    - **위상 정렬(Topological Sorting)**: 방향 그래프에서 각 정점을 선형 순서로 나열하는 문제.
    - **배낭 문제(Knapsack Problem)** 중 **분수 배낭 문제(Fractional Knapsack Problem)**: 물건을 쪼개서 넣을 수 있을 때의 최대 가치 찾기.
3. **탐욕 알고리즘의 특징**
    - 단순하고 직관적인 방법으로 문제 해결.
    - 각 단계에서 부분 문제를 해결하면서 전체 문제의 최적 해를 향해 나아감.
    - 항상 최적 해를 보장하지는 않음. 따라서 탐욕 알고리즘이 적용 가능한 문제인지 확인하는 것이 중요.
### 꼭 풀어봐야 하는 예제문제
1. **활동 선택 문제(Activity Selection Problem)**
    - 문제: 주어진 활동들 중에서 시작 시각과 종료 시각이 주어질 때, 겹치지 않게 최대한 많은 활동을 선택하세요.
    - 목표: 탐욕적 선택 속성을 통해 작업 선택.
2. **다익스트라 알고리즘(Dijkstra's Algorithm)**
    - 문제: 하나의 출발 정점에서 다른 모든 정점까지의 최단 경로를 찾으세요.
    - 목표: 그래프의 최단 경로를 탐욕적으로 찾기.
3. **최소 신장 트리(MST) - 크루스칼 알고리즘(Kruskal's Algorithm)**
    - 문제: 주어진 연결 그래프에서 최소 신장 트리를 찾으세요.
    - 목표: 모든 정점을 포함하면서 최소 가중치 트리 구성.
4. **최소 신장 트리(MST) - 프림 알고리즘(Prim's Algorithm)**
    - 문제: 주어진 연결 그래프에서 임의의 시작점에서 출발하여 최소 신장 트리를 찾으세요.
    - 목표: 계속해서 최소 가중치 간선을 추가하여 최소 신장 트리 구성.
5. **분수 배낭 문제(Fractional Knapsack Problem)**
    - 문제: 각 물건의 무게와 가치가 주어졌을 때, 배낭에 넣을 수 있는 최대 가치를 찾으세요. 물건은 쪼갤 수 있음.
    - 목표: 물건 당 가치 대비 무게 비율을 기준으로 정렬하여 탐욕적으로 선택.
### 예제문제 구현
1. **활동 선택 문제**
```Python
def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    n = len(activities)
    selected_activities = [activities[0]]
    last_end_time = activities[0][1]
    for i in range(1, n):
        if activities[i][0] >= last_end_time:
            selected_activities.append(activities[i])
            last_end_time = activities[i][1]
    return selected_activities
activities = [(1, 3), (2, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
print(activity_selection(activities))
```
1. **다익스트라 알고리즘**
```Python
import heapq
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(dijkstra(graph, 'A'))
```
1. **크루스칼 알고리즘**
```Python
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                if self.rank[root_u] == self.rank[root_v]:
                    self.rank[root_v] += 1
def kruskal(n, edges):
    ds = DisjointSet(n)
    mst = []
    edges.sort(key=lambda x: x[2])
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
    return mst
edges = [
    (0, 1, 1),
    (0, 2, 4),
    (1, 2, 2),
    (1, 3, 5),
    (2, 3, 1)
]
print(kruskal(4, edges))
```
1. **분수 배낭 문제**
```Python
def fractional_knapsack(values, weights, capacity):
    index = list(range(len(values)))
    ratio = [v/w for v, w in zip(values, weights)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    max_value = 0
    fractions = [0] * len(values)
    for i in index:
        if weights[i] <= capacity:
            fractions[i] = 1
            max_value += values[i]
            capacity -= weights[i]
        else:
            fractions[i] = capacity / weights[i]
            max_value += values[i] * fractions[i]
            break
    return max_value, fractions
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(fractional_knapsack(values, weights, capacity))
```
이런 문제들을 통해 탐욕 알고리즘에서 사용하는 개념과 접근 방식을 이해하고 실제로 적용해볼 수 있을 거야. 이렇게 해서 '탐욕 알고리즘'에 대한 설명을 마쳤어. 알고리즘 시험 준비에 큰 도움이 되길 바래! 추가적인 질문이나 도움이 필요한 부분이 있다면 언제든지 물어봐.