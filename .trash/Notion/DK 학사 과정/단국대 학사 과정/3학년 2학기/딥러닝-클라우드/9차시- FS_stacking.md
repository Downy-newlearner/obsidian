#### 딥러닝&파이썬 용어 정리
|책 이름|챕터/날짜|이름|설명|
|---|---|---|---|
|딥러닝/클라우드||[[Gini impurity]]||
|딥러닝/클라우드||[[시계열 데이터]]|데이터의 변화가 시간의 변화에 따라 표현되는 데이터|
  
  
오늘은 미미하지만 성능을 올릴 수는 있는 방법에 대해 알아본다.
  
![[chap07_FS_stacking_page-0033.jpg]]
![[chap07_FS_stacking_page-0034.jpg]]
![[chap07_FS_stacking_page-0035.jpg]]
![[chap07_FS_stacking_page-0036.jpg]]
![[chap07_FS_stacking_page-0037.jpg]]
![[chap07_FS_stacking_page-0038.jpg]]
![[chap07_FS_stacking_page-0039.jpg]]
예를 들어 Level0 모델에서 각각 환자일 확률이 몇 퍼센트인지 우선 예측하고, 그 예측들을 모아 Level1 모델에서 학습 후 최종 예측을 한다. 이 방법이 효과적임이 알려져있다.
![[chap07_FS_stacking_page-0040.jpg]]
![[chap07_FS_stacking_page-0041.jpg]]
![[chap07_FS_stacking_page-0042.jpg]]
![[chap07_FS_stacking_page-0043.jpg]]
![[chap07_FS_stacking_page-0044.jpg]]
![[chap07_FS_stacking_page-0045.jpg]]
![[chap07_FS_stacking_page-0046.jpg]]
![[chap07_FS_stacking_page-0047.jpg]]
최종
테스트, 트레인 데이터를 나눈 뒤, 성능이 좋게 나오는 하이퍼파라미터, 모델, 구조 등을 찾는다.
최종 모델을 만든 후 모든 데이터를 이용해 훈련한다.
![[chap07_FS_stacking_page-0048.jpg]]