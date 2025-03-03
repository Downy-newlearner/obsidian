---
created: 2024-12-25
tags:
  - Paper
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

기존에는 region proposal을 통해 바운딩 박스를 여러개 치고 그것들 중 가장 좋은 것만 남기는 간접적인 방식을 사용했다면 DETR은 *set prediction problem*을 통해 직접적인 Detection을 하고자 하였다.

매칭 로스가 줄어드는 방향으로 매칭한 후 학습을 진행한다.

N값을 충분히 크게 만드는 것이 이런 접근에서 필요한 과정이다.

결론: *기존 NMS 방식* -> *이분 매칭*


![[DETR (1)_page-0005.jpg]]
- Transformer가 왜 사용되었는가
	- attention 매커니즘을 통해 각 픽셀들이 서로의 스코어를 만든다.
		- 이 과정에서 인스턴스가 분리되고, 인스턴스 서로의 interaction 정도를 파악할 수 있다.
	- 거리가 먼 픽셀 간의 연관성을 파악하기에 용이하다.(멀리 떨어져있는 단어를 잘 처리하는 트랜스포머의 특징과 같은 맥락이다.)

- Encoder
	- 내부적으로 self attention과 같은 과정을 통해 이미지의 feature 정보가 들어오고 서로 연관관계를 파악할 수 있다.

- Decoder
	- N개 까지 인스턴스를 구분할 수 있도록 하여, 인코딩된 정보를 받아 전체 컨텍스트를 파악하는 것이다.

임베팅 정보로 image feature를 사용하고 이미지에 대한 위치 정보를 positional encoding을 통해 처리한다.
N개의 object queries를 통해 각각 서로 다른 인스턴스를 구분할 수 있다.



![[DETR (1)_page-0006.jpg]]
d는 임베딩이라고 볼 수 있다.(feature 정보)



![[DETR (1)_page-0007.jpg]]
말단 부분은 경계선으로 볼 수 있고 이 부분의 attention Score 값을 높게 형성한다.

