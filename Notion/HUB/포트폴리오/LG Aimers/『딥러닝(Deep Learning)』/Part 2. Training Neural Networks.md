![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0001.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0002.jpg]]
neural network에서 최적화하고자 하는 파라미터가 존재할 것이고, 그 파라미터와 학습 데이터를 입력으로 집어넣고, ground truths와 비교하여 로스함수를 낸다.
그 로스함수 값을 최저로 하도록 학습한다.
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0003.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0004.jpg]]
gradient descent의 변형 기법들이 있다.
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0005.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0006.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0007.jpg]]
Back Propagation을 통해 각 파라미터들의 로스함수에 대한 편미분값을 얻어, 적당한 학습률과 함께 파라미터들을 각각 조절한다.
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0008.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0009.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0010.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0011.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0012.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0013.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0014.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0015.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0016.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0017.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0018.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0019.jpg]]
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0020.jpg]]
기원은 계단함수이다.
계단 함수를 부드러운 형태로 근사한 것이 시그모이드 함수이다.
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0021.jpg]]
시그모이드의 도함수는 $\{y|0<y<\frac{1}{4}\}$﻿를 치역으로 가지므로, back propagation을 진행할 수록 gradient가 점차 작아지는 양상을 보인다.
이는 기울기 소실 문제를 발생시킨다.(Gradient Vanishing)
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0022.jpg]]
기울기 소실 문제를 해결하기 위한 활성화 함수1
그러나 tanh의 도함수 역시 치역이 0에서 1/2 사이이므로 여전히 기울기 소실 문제가 있다.
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0023.jpg]]
기울기 소실 문제를 해결하기 위한 활성화 함수2
ReLU함수의 도함수는 0을 기준으로 왼쪽은 0, 오른쪽은 x라서 기울기 소실 문제를 해결할 수 있다.
하지만 만약 데이터아이템의 값들이 모두 음수라면 기울기가 모두 0이 되어서 학습에 큰 차질이 생긴다.
데이터아이템의 값들이 모두 음수라는 것이 어떤 경우일까?
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0024.jpg]]
특정 활성함수를 썼을 떄 학습을 용이하게 하는 레이어를 생각할 수 있는데 그것이 배치 노멀라이제이션이다.
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0025.jpg]]
가령 tanh라는 활성함수를 생각해보자.
이 함수는 입력값이 0에서 멀어질수록 기울기가 0에 가까워지는 기울기 소실 문제가 발생한다.
그러므로 forward propagation할 때 활성 함수들의 입력으로 주어지는 값들의 대략적인 범위를 0 근처로 제한할 수 있는 방법이 있다면 기울기 소실 문제없이 학습이 잘 될것이고, 이것이 Batch Normalization의 아이디어가 될 것이다.
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0026.jpg]]
미니배치가 주어졌을 때, 특정 노드를 통과하기 직전 입력으로 발생하는 값을 모아 평균과 분산을 계산하고 평균이 0이 되도록, 분산이 1이 되도록 정규화 과정을 수행하면, 노드의 입력으로 주어지는 대략적인 값의 범위를 0 근처로 만들 수 있을 것이다.
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0027.jpg]]
BN이 Batch Normalization이다.
만약 FC 이후 출력값들이 고유한 평균과 분산을 가지고있는데, 이것이 모델이 학습해야하는 유의미한 정보를 담고있다면 BN 과정을 통해서 이 의미를 묵살할 수 있다.
그러므로 BN에서 묵살된 정보를 복원하는 과정이 BN의 두번쨰 과정이다.
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0028.jpg]]
neural network 과정에서 추가로 학습한 감마, 베타 값을 이용하여 평균을 베타로, 분산을 감마제곱으로 가지게 된다.
이러한 두 번째 변환을 통해서 딥러닝을 통해 최적의 평균,분산 값을 스스로 결정하게 한다.
- 정리
    
    Batch Normalization (배치 정규화)은 딥러닝 모델의 학습을 가속화하고 안정화시키기 위해 사용되는 기법입니다. Batch Normalization의 주된 과정은 다음 두 가지 단계로 나눌 수 있습니다:
    
    ### 1. 학습 단계 (Training Phase)
    
    - **균일한 분포로 정규화**:
        - *입력값 \( x \)**가 있는 층에서 미니배치(예: 배치 크기)가 주어지면 해당 배치의 평균(\( \mu \))과 분산(\( \sigma^2 \))을 계산합니다.
        - 평균과 분산을 사용하여 배치의 각 데이터 포인트를 정규화합니다:  
            \[  
            \hat{x} = \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}}  
            \]  
            여기서 \( \epsilon \)은 분모의 수치적 안정성을 위해 작은 상수입니다.  
            
    - **스케일링 및 시프팅**:
        - 정규화된 값 \(\hat{x}\)에 대해 learnable parameters인 \(\gamma\) (스케일링)와 \(\beta\) (시프팅)를 적용합니다:  
            \[  
            y = \gamma \hat{x} + \beta  
            \]  
            
        - 이렇게 하면 신경망이 데이터의 분포를 더 효과적으로 모델링하는 데 필요한 자유도를 보장합니다.
    
    ### 2. inference 단계 (Inference Phase)
    
    - **학습된 통계값 사용**:
        - 테스트 또는 예측 중에는 각 배치에 대한 평균과 분산을 계산하는 대신, 학습 중에 얻은 전체 데이터셋의 평균(\( \mu_{running} \))과 분산(\( \sigma^2_{running} \))을 사용합니다.
        - 사용자가 지정한 주기마다 업데이트되는 이 통계값은 이전 배치들의 평균과 분산 활용을 통해 모멘텀을 적용하여 계산합니다:  
            \[  
            \mu_{running} = \alpha \mu_{running} + (1 - \alpha) \mu  
            \]  
            \[  
            \sigma^2_{running} = \alpha \sigma^2_{running} + (1 - \alpha) \sigma^2  
            \]  
            
        - 새로운 입력 데이터가 들어올 경우, 이전에 계산한 평균과 분산을 사용하여 다음과 같이 적용합니다:  
            \[  
            \hat{x}  
            _{test} = \frac{x - \mu_{running}}{\sqrt{\sigma^2_{running} + \epsilon}}  
            \]  
            
        - 이후, 같은 스케일링과 시프팅을 적용합니다:  
            \[  
            y = \gamma \hat{x}_{test} + \beta  
            \]  
            
    
    이러한 두 가지 단계는 Batch Normalization이 모델의 신뢰성과 성능을 향상시키는 데 도움을 주며, 더 빠른 학습 속도와 더 나은 일반화 성능을 제공합니다.
    
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0029.jpg]]
BN의 pseudo code이다.
![[%E3%80%8E%EB%94%A5%EB%9F%AC%EB%8B%9D(Deep_Learning)%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download_cut_page-0030.jpg]]