---
책 이름: 세미나
설명: 신경망에서 주로 특징 추출을 담당하는 기본 네트워크 구조이다. 특징 추출과 전이 학습의 역할을 한다.
챕터/날짜: "07.25"
---
## 설명💫
1. **특징 추출 (Feature Extraction)**:
    
    - Backbone은 입력 이미지나 데이터를 받아서 유의미한 특징을 추출하는 부분입니다. 이를 통해 추출된 특징 맵은 후속 네트워크나 작업(e.g., 분류, 탐지, 세그멘테이션 등)에 사용됩니다.
    
      
    
2. **전이 학습 (Transfer Learning)**:
    - 사전 학습된 모델의 Backbone을 사용하여 새로운 작업에 적응시킬 수 있습니다. 이때, Backbone은 일반적으로 광범위한 데이터셋에서 학습되어 널리 사용됩니다.
## 예시📝
1. **이미지 분류 (Image Classification)**:
    - Backbone: ResNet50
    - 네트워크의 처음 몇 레이어로 ResNet50을 사용하여 이미지의 특성을 추출하고, 멀티-레이어 퍼셉트론(MLP)을 통해 분류 작업 수행.
2. **객체 탐지 (Object Detection)**:
    - Backbone: VGG16, ResNet50
    - Faster R-CNN, YOLO 등이 Backbone으로 사용하여 대상 객체의 특징을 추출하고, 추출된 특징을 기반으로 탐지 작업 수행.
3. **이미지 세그멘테이션 (Image Segmentation)**:
    - Backbone: ResNet101
    - FCN(Full Convolutional Networks), U-Net 등에서 사용하여 이미지의 각 픽셀별 클래스를 예측.