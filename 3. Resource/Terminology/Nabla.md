---
created: 2024-12-02
tags: 
aliases:
  - nabla
  - del
  - del operator
  - 뒤집힌 삼각형
reference:
---

# 뒤집힌 삼각형(∇) 기호와 Gradient

뒤집힌 삼각형 기호(∇)는 **델 연산자(Del operator)** 또는 **나블라(Nabla)** 라고 불리며, 
벡터 미적분학에서 중요한 연산을 나타냅니다. 이 기호는 **Gradient**를 포함한 여러 연산에서 사용됩니다.

## Gradient (그라디언트)
- ∇는 스칼라 함수 \( f(x, y, z) \)의 **그라디언트**를 나타냅니다.
- **표현**:  
  
$\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right)$
- **의미**:  
  - 스칼라 필드 $f$의 각 점에서 **최대 변화율의 방향**과 크기를 나타내는 벡터입니다.
  - 예를 들어, 온도 분포 $f(x, y, z)$에서 그라디언트는 가장 빠르게 온도가 변하는 방향을 가리킵니다.

## Divergence (발산)
- 벡터 필드 $\mathbf{F}$에서 **발산(Divergence)** 을 계산할 때 사용됩니다.
- **표현**:  
  $$
  \nabla \cdot \mathbf{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}
  $$
- **의미**:  
  - 벡터 필드가 주어진 점에서 얼마나 퍼져나가는지를 나타냅니다.


## Curl (회전)
- 벡터 필드 $\mathbf{F}$의 **회전(Curl)** 을 계산할 때 사용됩니다.
- **표현**:  
  $$
  \nabla \times \mathbf{F} = \begin{vmatrix}
  \mathbf{i} & \mathbf{j} & \mathbf{k} \\
  \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
  F_x & F_y & F_z
  \end{vmatrix}
  $$
- **의미**:  
  - 벡터 필드가 주어진 점에서 얼마나 회전하는지를 나타내는 또 다른 벡터 필드입니다.

## 요약
뒤집힌 삼각형(∇)은 **그라디언트**뿐 아니라 **발산**, **회전** 같은 여러 벡터 미적분 연산에서 사용됩니다.
그러나 맥락에 따라 의미가 달라질 수 있으므로, 주어진 식이나 방정식에서 어떤 연산을 의미하는지 확인해야 합니다.
