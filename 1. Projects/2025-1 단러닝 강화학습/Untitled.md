**강화학습은 discrete time 에서 stochastic 하게 agent를 control하는 문제이다.**

1. Agent는 Policy에 따라 행동을 결정한다
2. Agent의 행동에 따라 상태가 전이된다
3. 전이된 상태에서의 Reward를 Agent에게 준다
4. Agent는 Reward에 따라 자신의 Policy를 수정한다  
    -> Reward가 높았던 행동은 확률을 높여 다음 번엔 더 많이 하도록 기록 / 낮은 경우는 반대로  
    -> 직접 반복적으로 수행하며 학습된다 / " 시행착오를 통해 배운다" 라고 표현한다

### 1. Agent는 Policy에 따라 행동을 결정한다.
