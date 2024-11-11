---
created: 2024-11-04 00:57
tags:
  - Object_Detection
aliases:
  - DEtection TRansformer
---
이 블로그 게시물은 DETR (DEtection TRansformer)에 대해 설명한다. DETR은 기존 객체 탐지 파이프라인에서 필요로 하는 수작업 컴포넌트인 [(Non-Maximum Suppression)와 앵커(anchor) 생성 과정을 제거하고, 엔드-투-엔드 방식의 트랜스포머 구조를 사용해 객체 탐지를 set prediction 문제로 접근한다. 주요 특징으로는 encoder-decoder 구조의 트랜스포머를 통해 중복된 예측을 제거하며, COCO 데이터셋에서 Faster R-CNN과 유사한 성능을 보인다. Large object에 강점을 보이나, small object에 대한 성능은 낮아 FPN 적용을 계획 중이다.