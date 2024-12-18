---
created: 2024-11-20
tags: 
aliases:
---
Agent는 LangChain에서 질문이 들어오면 해당 자연어 질문을 처리하기 위해 Tools를 동적으로 선택하고 실행하는 구성 요소이다.
다시 말해, Agent는 *"질문 분석 -> 질문을 해결하기 위해 필요한 Tools 선택 및 실행 -> 결과 분석 후 필요하다면 추가 Tools 선택 및 실행 -> 최종 답변 생성"* 의 과정을 가진다.

### Agent의 사용 사례

- **SQLDatabaseTool과 통합**: 자연어 질문을 SQL 쿼리로 변환하여 데이터베이스 조회.
- **검색 및 QA**: 문서 검색기를 사용하여 특정 정보를 찾아 응답.
- **멀티 도구 작업**: 여러 도구를 조합하여 복잡한 요청 처리 (예: 계산 + 검색).


### Agent와 긴밀하게 연결되어있는 개념들
1. **Agent**는 사용자 입력을 분석하고 **Tools**와 상호작용합니다.
2. **Prompt Templates**는 Agent의 작업 흐름을 결정합니다.
3. **Memory**는 Agent가 대화의 맥락을 유지하는 데 필요합니다.
4. **Chains**는 Agent를 워크플로우의 일부로 통합하여 작업을 구조화합니다.
5. **Observations**는 실행 결과를 분석해 에이전트의 동적 결정을 지원합니다.
6. **Retrieval QA**는 비정형 데이터 검색을 통해 에이전트의 능력을 확장합니다.
7. **Execution Control**은 여러 도구와의 상호작용을 최적화합니다.
8. **Debugging and Monitoring**은 Agent의 안정성과 성능을 개선합니다.
9. **Deployment**는 에이전트를 실사용 가능한 형태로 만듭니다.

Tools
Prompt Templates
Memory
Chains
Observations
Retrieval QA
Execution Control
Debugging and Monitoring
Deployment