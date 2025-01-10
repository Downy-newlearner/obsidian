---
Lecture date: 2025-01-10
tags: 
reference:
---
### 7. **훈련 파라미터 설정**

- `train_batch_size`: 배치 크기를 설정합니다.
- `cross_attention`: 교차 주의(attention) 방법을 설정합니다. `sdpa` 또는 `xformers` 중 선택할 수 있습니다.
- `mixed_precision`: 혼합 정밀도를 설정합니다. `fp16` 또는 `bf16`을 선택할 수 있습니다.