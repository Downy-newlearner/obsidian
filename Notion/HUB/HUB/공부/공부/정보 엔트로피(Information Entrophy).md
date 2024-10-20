---
태그:
  - Base Knowledge
설명: 정보량의 기댓값
---
> [!info] 정보 엔트로피(information entropy) - 공돌이의 수학정리노트 (Angelo's Math Notes)  
> 정보란 무엇인가?  
> [https://angeloyeo.github.io/2020/10/26/information_entropy.html](https://angeloyeo.github.io/2020/10/26/information_entropy.html)  
## ‘정보’와 ‘정보량’
정보란 데이터를 쉽게 사용할 수 있도록 가공한 것을 의미한다.(이 관점은 다분히 computer science의 관점에 따른 것인데, 데이터를 사용하는 입장에서 생각할 수 있는 추상적인 정보의 개념이라고 할 수 있다.)
  
필자는 통계학에서 말하는 정보량을 **“깜놀도”**라고 말하고 싶다. 깜짝 놀랄만한 정도를 줄여서 말이다.
즉, 통계학에서는 놀랄만한 내용일수록 정보량이 많다고 얘기한 것이다.
이 개념은 확률의 개념을 재해석 한 것으로도 볼 수 있는데, 다시 말해 확률이 낮은 사건일 수록 정보량은 높다. 거의 일어나지 않을 일이기 때문이다.
## 정보 엔트로피
정보량의 기댓값이 information entropy(정보 엔트로피)이다.
기댓값: 각 사건이 벌어졌을 때의 이득과 그 사건이 벌어질 확률을 곱한 것을 전체 사건에 대해 합한 값
이산 랜덤변수 XX의 샘플 공간이 {x1,x2,⋯,xn}{x1,x2,⋯,xn}이라고 할 때 정보 엔트로피는 아래와 같다.
![[Source/image 13.png|image 13.png]]
여기서 E[⋅]E[⋅]은 기댓값 연산자를 의미한다.