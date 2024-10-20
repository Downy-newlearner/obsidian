#### 딥러닝&파이썬 용어 정리
|책 이름|챕터/날짜|이름|설명|
|---|---|---|---|
|딥러닝/클라우드||[[시계열 데이터]]|데이터의 변화가 시간의 변화에 따라 표현되는 데이터|
|딥러닝/클라우드||[[Gini impurity]]||
  
  
![[chap06_cross_validation_page-0001.jpg]]
![[chap06_cross_validation_page-0002.jpg]]
![[chap06_cross_validation_page-0003.jpg]]
Bias는 특정 부분에만 집중하는 경향이고, Variance는 전체 부분에서 너무 세밀하게 집중하는 경향이다.
![[14.png]]
$f(x)$﻿는 입력 데이터 x에 대한 실제 정답이고, $\hat{f}(x)$﻿는 예측값이다.
![[12.png]]
예측값과 실제 정답과의 차이의 평균
  
![[13.png]]
다양한 데이터 셋에 대하여 예측값이 얼만큼 변화할 수 있는 지에 대한 양
![[16.png]]
![[chap06_cross_validation_page-0004.jpg]]
![[chap06_cross_validation_page-0005.jpg]]
![[chap06_cross_validation_page-0006.jpg]]
![[chap06_cross_validation_page-0007.jpg]]
![[chap06_cross_validation_page-0008.jpg]]
![[chap06_cross_validation_page-0009.jpg]]
![[chap06_cross_validation_page-0010.jpg]]
![[chap06_cross_validation_page-0011.jpg]]
![[chap06_cross_validation_page-0012.jpg]]
![[chap06_cross_validation_page-0013.jpg]]
![[chap06_cross_validation_page-0014.jpg]]
![[chap06_cross_validation_page-0015.jpg]]
![[chap06_cross_validation_page-0016.jpg]]
KFold 함수보다 이게 더 간단하다.
![[chap06_cross_validation_page-0017.jpg]]
![[chap06_cross_validation_page-0018.jpg]]
만약 Inbalance data에서는 Accuracy 평가 지표가 무의미하다.
Inbalance data는 타겟이 A인 것 90%, B인 것 10%과 같은 경우이다.
![[chap06_cross_validation_page-0019.jpg]]
Cross Validation은 모델을 만드는 최종 과정이 아니라, 모델을 만들어가는 과정이다.
“모델을 완성한다면 이정도 성능을 낼 것이다.”를 얘기할 때 사용한다.
  
모델 생성 → (CV → HT)(반복) → 최종 파라미터 완성 → 최종 파라미터를 갖고, 모든 데이터를 train 데이터로 하는 모델이 최종 모델이다.
![[chap06_cross_validation_page-0020.jpg]]
![[chap06_cross_validation_page-0021.jpg]]
![[chap06_cross_validation_page-0022.jpg]]
![[chap06_cross_validation_page-0023.jpg]]
![[chap06_cross_validation_page-0024.jpg]]
![[chap06_cross_validation_page-0025.jpg]]
![[chap06_cross_validation_page-0026.jpg]]
![[chap06_cross_validation_page-0027.jpg]]
![[chap06_cross_validation_page-0028.jpg]]
디폴트보다 점수가 낮다면 그냥 디폴트를 사용하면 된다.
![[chap06_cross_validation_page-0029.jpg]]
![[chap06_cross_validation_page-0030.jpg]]
![[chap06_cross_validation_page-0031.jpg]]
![[chap06_cross_validation_page-0032.jpg]]
![[chap06_cross_validation_page-0033.jpg]]
![[chap06_cross_validation_page-0034.jpg]]
![[chap06_cross_validation_page-0035.jpg]]
![[chap06_cross_validation_page-0036.jpg]]
![[chap06_cross_validation_page-0037.jpg]]
![[chap06_cross_validation_page-0038.jpg]]
n_iter가 GridSearch와 다른 점이다.
optuna에서 iter 값 조절하는 것과 같다.
![[chap06_cross_validation_page-0039.jpg]]
![[chap06_cross_validation_page-0040.jpg]]
![[chap06_cross_validation_page-0041.jpg]]
![[chap06_cross_validation_page-0042.jpg]]
![[chap06_cross_validation_page-0043.jpg]]
![[chap06_cross_validation_page-0044.jpg]]
![[chap06_cross_validation_page-0045.jpg]]
![[chap06_cross_validation_page-0046.jpg]]
![[chap06_cross_validation_page-0047.jpg]]
![[chap06_cross_validation_page-0048.jpg]]
![[chap06_cross_validation_page-0049.jpg]]
![[chap06_cross_validation_page-0050.jpg]]
![[chap06_cross_validation_page-0051.jpg]]
![[chap06_cross_validation_page-0052.jpg]]
![[chap06_cross_validation_page-0053.jpg]]
![[chap06_cross_validation_page-0054.jpg]]
![[chap06_cross_validation_page-0055.jpg]]
![[chap06_cross_validation_page-0056.jpg]]
![[chap06_cross_validation_page-0057.jpg]]
![[chap06_cross_validation_page-0058.jpg]]
![[chap06_cross_validation_page-0059.jpg]]
![[chap06_cross_validation_page-0060.jpg]]
![[chap06_cross_validation_page-0061.jpg]]