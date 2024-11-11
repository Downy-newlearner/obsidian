---
created: 2024-11-11
tags: 
aliases:
  - Average Precision
---
**AP (Average Precision)**:  
객체 탐지 모델의 정확도를 평가하는 지표로, 다양한 임계값에서의 **Precision-Recall 곡선** 아래의 면적을 계산하여 평균을 낸 값이다. 

**핵심 디테일**:  
AP는 IoU 임계값을 여러 개 설정하여 모든 객체의 탐지 성능을 종합적으로 평가한다. 주로 COCO 데이터셋에서 평가 시 다양한 IoU 임계값 (예: 0.50에서 0.95까지)을 기준으로 AP를 구한다.

**요약**:  
모든 IoU 임계값에서의 평균 Precision-Recall 곡선 아래 면적으로 객체 탐지 모델의 정확도를 평가한다.