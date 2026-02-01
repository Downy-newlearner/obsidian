---
created: 
tags: 
aliases:
  - Harris
reference:
---
### Harris 코너 검출기 (Harris Corner Detector)

1. **핵심 아이디어**
    
    - 이미지에서 코너는 강한 그래디언트 변화가 여러 방향에서 발생하는 영역.
    - 작은 창을 이동시켰을 때 강도 변화가 큰 지점을 코너로 간주.
2. **작동 원리**
    
    ![[Pasted image 20241205220707.png]]
3. **코너 판단 기준**
    
    - 행렬 MMM의 고유값(λ1,λ2\lambda_1, \lambda_2λ1​,λ2​)을 통해 판단:
        - λ1,λ2\lambda_1, \lambda_2λ1​,λ2​가 모두 크면: 코너.
        - 한쪽만 크면: 에지.
        - 둘 다 작으면: 평탄한 영역.