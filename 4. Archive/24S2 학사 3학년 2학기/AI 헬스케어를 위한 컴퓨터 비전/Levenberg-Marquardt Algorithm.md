### 2. **Levenberg-Marquardt Algorithm**

- **목적**: Gauss-Newton 알고리즘과 Gradient Descent의 장점을 결합하여 비선형 최소자승문제를 해결합니다.
- **핵심 아이디어**:
    - Gauss-Newton 방법을 기본으로 하지만, **가중치를 도입**하여 안정성을 높입니다.
    - 초기 단계에서는 Gradient Descent처럼 작동하고, 최적화가 진행되면서 Gauss-Newton으로 전환됩니다.
- **절차**:
    1. Gauss-Newton의 선형화 방식을 따르되, 가중치 λ\lambdaλ를 추가하여 업데이트 식을 계산합니다.
    2. λ\lambdaλ 값은 반복 과정에서 조정됩니다:
        - 성능이 개선되면 λ\lambdaλ를 감소시켜 Gauss-Newton 방식에 가까워집니다.
        - 성능이 악화되면 λ\lambdaλ를 증가시켜 Gradient Descent 방식에 가까워집니다.
    3. 수렴 조건을 만족할 때까지 반복합니다.
- **장점**: 초기 값의 민감도를 줄이고 더 안정적으로 수렴합니다.
- **단점**: Gauss-Newton보다 계산량이 많습니다.