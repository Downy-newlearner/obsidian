### Diffusion Model 샘플링 과정 정리

1. **Noise에서 Clean한 Data로 역방향 진행**  
    Diffusion Model은 초기 노이즈 샘플 $x_T$에서 시작하여, 점진적으로 노이즈가 제거된 $x_{T-1}, x_{T-2}, \ldots, x_0$를 생성하는 **Reverse Process**를 학습한다. 각 $t$ 단계는 특정 노이즈 레벨에 해당하며, $x_t$는 원본 데이터 $x_0$와 노이즈 $\epsilon$의 합으로 표현된다.
    
2. **Noise Prediction 모델 학습**  
    DDPM에서는 $\epsilon_\theta(x_t, t)$라는 함수로 노이즈를 예측하도록 모델을 설계한다. 학습 데이터는 원본 데이터 $x_0$, timestep $t$, 가우시안 노이즈 $\epsilon \sim \mathcal{N}(0, I)$를 기반으로 만들어진 $x_t$ 샘플을 포함하며, 학습 손실 함수는 다음과 같다:
    
    $\mathcal{L} = || \epsilon_\theta(x_t, t) - \epsilon ||^2$
    
    이 손실은 실제 노이즈 $\epsilon$과 모델이 예측한 노이즈 $\epsilon_\theta$의 Mean Squared Error(MSE)로 정의된다.
    
3. **Conditional Distribution**  
    DDPM에서는 $p_\theta(x_{t-1} | x_t)$를 가우시안 분포 $\mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))$로 가정한다.
    
    - 평균 $\mu_\theta(x_t, t)$는 $\epsilon_\theta(x_t, t)$로부터 계산되며,
    - 분산 $\Sigma_\theta(x_t, t)$는 상수 $\beta_t$ 또는 $\tilde{\beta}_t$로 설정된다.
