---
created: 
tags: 
aliases:
  - Difference of Gaussians
  - DoG
reference:
---
### DoG (Difference of Gaussians)

1. **핵심 아이디어**
    
    - LoG를 효율적으로 근사한 방법.
    - 서로 다른 스케일의 가우시안 블러를 빼서 특징 검출.
2. **작동 원리**
    
    - 두 가우시안 블러를 빼는 연산: DoG(x,y)=G(x,y,kσ)−G(x,y,σ)DoG(x, y) = G(x, y, k\sigma) - G(x, y, \sigma)DoG(x,y)=G(x,y,kσ)−G(x,y,σ)
        - kσ,σk\sigma, \sigmakσ,σ: 스케일.
    - 스케일-스페이스에서 지역 극값(local extrema)을 탐색하여 특징점 검출.
3. **장점**
    
    - LoG보다 계산이 빠르고 효율적.
    - SIFT 알고리즘에서 특징점 검출에 활용.