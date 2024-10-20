#### 딥러닝&파이썬 용어 정리
|책 이름|이름|설명|
|---|---|---|
|딥러닝/클라우드|[[Gini impurity]]||
|딥러닝/클라우드|[[시계열 데이터]]|데이터의 변화가 시간의 변화에 따라 표현되는 데이터|
  
  
![[chap05_DT_RF_SVM_page-0033.jpg]]
보통 분류 알고리즘은 목표가 클래스와 클래스를 가장 잘 나눌 수 있는 경계(hyperplane)를 찾는 것이다.
SVM은 이 경계를 찾을 때 클래스의 몇 개의 점들만 활용한다.
support vector를 찾는 것이 중요함
SVM은 차원을 높이는 아이디어가 활용됨
파이라고 부르는 변수를 활용해 차원을 하나 높여서 경계를 더 쉽게 찾도록 한다.
다른 알고리즘은 모든 데이터들을 활용해 경계를 찾음.
![[chap05_DT_RF_SVM_page-0034.jpg]]
생략
![[chap05_DT_RF_SVM_page-0035.jpg]]
NuSVC 커널을 어떤 것을 사용하냐에 따라 다른 구현 활용
svm.SVC(classification), svm.SVR(Regression) 모델을 활용한다.
![[chap05_DT_RF_SVM_page-0036.jpg]]
SVM은 학습 데이터의 규모가 커지면, 시간이 많이 소요된다.
하지만 강력한 알고리즘이라 지금도 많이 사용된다.
![[chap05_DT_RF_SVM_page-0037.jpg]]
![[chap05_DT_RF_SVM_page-0038.jpg]]
![[chap05_DT_RF_SVM_page-0039.jpg]]
차원을 높여주는 kernel은 하이퍼파라미터이다.
SVM은 하이퍼파라미터가 많지 않다.
![[chap05_DT_RF_SVM_page-0040.jpg]]
- C는 과적합과 관련이 있다.
    - 찾은 경계가 복잡할 수록 과적합이 발생할 확률이 높다.
    - 많이 건드리지는 않는 하이퍼파라미터
- kernel을 많이 건드린다.
![[chap05_DT_RF_SVM_page-0041.jpg]]
시간에 따라 plane이 다르게 형성됨
![[chap05_DT_RF_SVM_page-0042.jpg]]
![[chap05_DT_RF_SVM_page-0043.jpg]]
![[chap05_DT_RF_SVM_page-0044.jpg]]
![[chap05_DT_RF_SVM_page-0045.jpg]]
전체 데이터에서 데이터를 뽑는다.(샘플링)
샘플링한 데이터에 대해 모델링을 하고 예측결과를 취합한다.
  
![[chap05_DT_RF_SVM_page-0046.jpg]]
모델 만들기 → 발생한 에러에 가중치를 둠 → 데이터를 새로 만듦 → 모델 만들기 → 가중치를 둠 … 반복
  
![[chap05_DT_RF_SVM_page-0047.jpg]]
![[chap05_DT_RF_SVM_page-0048.jpg]]
취합 방법은 여러개가 있다.
그림에서는 다수결로 취합한다.
  
![[chap05_DT_RF_SVM_page-0049.jpg]]
![[chap05_DT_RF_SVM_page-0050.jpg]]
![[chap05_DT_RF_SVM_page-0051.jpg]]
![[chap05_DT_RF_SVM_page-0052.jpg]]
n_estimators는 생성할 트리의 개수이다.
보통 500개 정도가 적당하다고 알려져있다.
![[chap05_DT_RF_SVM_page-0053.jpg]]
![[chap05_DT_RF_SVM_page-0054.jpg]]
  
![[chap05_DT_RF_SVM_page-0055.jpg]]
![[chap05_DT_RF_SVM_page-0056.jpg]]
오분류에서 가중치를 두고 다시 모델링하는 것을 반복한다.
![[chap05_DT_RF_SVM_page-0057.jpg]]
![[chap05_DT_RF_SVM_page-0058.jpg]]
![[chap05_DT_RF_SVM_page-0059.jpg]]
인풋데이터의 포맷이 scikit-learn 때와 조금 다르다.
![[chap05_DT_RF_SVM_page-0060.jpg]]
“오분류 가중치 → 모델링”의 반복 횟수를 steps로 정의한다.
![[chap05_DT_RF_SVM_page-0061.jpg]]
  
![[chap05_DT_RF_SVM_page-0062.jpg]]
random_seed를 하이퍼파라미터라고 부르긴 애매한 면이 있지만, 그래도 성능에 영향을 주기 때문에 10개 정도의 random_seed를 돌려보는 과정이 필요하다.
![[chap05_DT_RF_SVM_page-0063.jpg]]
![[chap05_DT_RF_SVM_page-0064.jpg]]