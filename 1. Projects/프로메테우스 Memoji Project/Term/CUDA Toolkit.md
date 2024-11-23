---
created: 2024-11-23
tags: 
aliases: 
reference:
---
### **CUDA Toolkit에 대한 간단 설명**

1. **CUDA 애플리케이션 개발 키트**
    
    - NVIDIA GPU를 활용한 병렬 컴퓨팅 애플리케이션을 개발하기 위한 소프트웨어 개발 키트(SDK).
    - GPU 가속 연산을 위한 API, 라이브러리, 컴파일러(`nvcc`) 등을 포함.
2. **기본 구성 요소**
    
    - **CUDA 드라이버**: GPU와의 통신을 담당하며, CUDA 프로그램 실행에 필요.
    - **라이브러리**: `cuBLAS`, `cuDNN`, `cuFFT` 등 다양한 수학 및 딥러닝 가속 라이브러리.
    - **nvcc 컴파일러**: CUDA 커널 코드를 컴파일해 GPU에서 실행 가능하도록 변환.
3. **PyTorch, TensorFlow와 같은 딥러닝 프레임워크 지원**
    
    - CUDA Toolkit은 딥러닝 프레임워크에서 GPU를 활용할 수 있게 해주는 기반 소프트웨어.
    - GPU에서 모델 학습 및 추론 속도를 크게 향상시킴.