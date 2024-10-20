---
책 이름: 세미나
설명: Detection에서 사용되는 기본 틀이 Anchor box이고 실제 디텍션해낸 결과가 바운딩 박스이다.
챕터/날짜: 24.08.28
---
> [!info] 앵커박스(Anchor-box)와 바운딩 박스(Bounding-box)의 차이  
> Object detection 논문에서 'Box regression' 이라는 표현이 등장하곤 하는데, 매번 등장할때마다 대충 넘어갔던 개념!  
> [https://ploradoaa.tistory.com/121](https://ploradoaa.tistory.com/121)  
```Plain
앵커 박스는 Object Detection 모델이 다양한 크기와 비율의 객체를 효과적으로 탐지할 수 있도록 돕기 위해 미리 정의된 여러 크기와 비율의 박스이다.
```
  
```Plain
바운딩 박스는 실제 이미지 내 객체의 위치와 크기를 나타내는 사각형의 박스이다.
```