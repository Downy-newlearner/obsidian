---
created: 2024-12-25
tags:
  - 논문
aliases: 
reference: https://www.youtube.com/watch?v=hCWUTvVrG7E
---
![[DETR (1)_page-0001.jpg]]
기존의 객체탐지 기술에 비해 간단하다는 장점이 있다.
또한 강력한 성능을 보인다.

![[DETR (1)_page-0002.jpg]]
이분 매칭 손실 함수를 이용해서 중복 탐지를 막을 수 있다.

![[DETR (1)_page-0003.jpg]]
기존 탐지 모델은 모델링 하는 사람이 미리 알고있으면 좋은 정보인 '사전 지식'이 많이 필요로 했었다.
	bounding box의 형태, bounding box가 겹칠 때의 처리 방법 등을 정해줬어야했음

바운딩 박스를 여러개 두고 NMS 기법을 이용해 최종 bounding box를 만드는 방식을 사용했다.

![[DETR (1)_page-0004.jpg]]
set prediction problem에서 set은 집합을 얘기한다.
	집합은 중복 원소가 없고 순서가 상관없는 특징을 가지고있다.

기존에는 region proposal을 통해 바운딩 박스를 여러개 치고 그것들 중 가장 좋은 것만 남기는 간접적인 방식을 사용했다면 DETR은 set prediction problem을 통해 직접적인 Detection을 하고자 하였다.



![[DETR (1)_page-0005.jpg]]

![[DETR (1)_page-0006.jpg]]

![[DETR (1)_page-0007.jpg]]