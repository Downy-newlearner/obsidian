---
created: 2024-11-23
tags: 
aliases:
  - 쿠다
reference:
---
CUDA를 사용할 때 알아야 할 배경지식과 주요 내용을 아래에 정리했습니다. 이 중에서 더 알고 싶은 내용을 말씀해 주시면 자세히 설명드릴게요!

---

### **1. CUDA 기본 개념**

- **CUDA**: NVIDIA가 개발한 병렬 컴퓨팅 플랫폼 및 API로, GPU를 활용하여 연산을 가속화합니다.
- **GPU 병렬 처리**: CPU와 달리, GPU는 수많은 코어를 사용하여 대량의 데이터를 동시에 처리합니다.
- **CUDA 드라이버와 런타임**: CUDA 애플리케이션 실행에는 NVIDIA 드라이버와 [[CUDA Toolkit]]이 필요합니다.

---

### **2. 하드웨어 요구사항**

- **GPU 지원 여부**: NVIDIA GPU여야 하며, CUDA를 지원하는 모델인지 확인해야 합니다.
- **CUDA Compute Capability**: GPU마다 지원하는 연산 능력을 의미하며, 지원되는 CUDA 버전을 결정합니다.
    - 예: MX250는 Compute Capability 6.1을 지원.

---

### **3. CUDA와 소프트웨어 스택**

- **CUDA Toolkit**: GPU 연산을 지원하는 소프트웨어 개발 키트(SDK).
- **cuDNN**: 딥러닝 연산 가속을 위한 CUDA 기반 라이브러리.
- **PyTorch/TensorFlow와의 연동**: PyTorch, TensorFlow 같은 딥러닝 프레임워크는 CUDA를 통해 GPU 연산을 수행합니다.

---

### **4. CUDA 드라이버와 설치**

- **NVIDIA 드라이버**: GPU가 CUDA 연산을 수행할 수 있게 해주는 필수 소프트웨어.
- **CUDA Toolkit 설치**:
    - OS와 GPU 모델에 맞는 버전 선택.
    - 드라이버 버전이 Toolkit과 호환되는지 확인 필요.
- **설치 확인**: `nvcc --version` 명령으로 CUDA 버전 확인.

---

### **5. PyTorch에서 CUDA 사용**

- **CUDA 활성화 여부 확인**:
    - `torch.cuda.is_available()`: CUDA가 활성화되어 있는지 확인.
    - `torch.cuda.get_device_name()`: 사용 가능한 GPU 이름 출력.
- **CUDA 텐서로 변환**:
    - GPU에서 실행하려면 데이터를 `.to("cuda")`로 변환.

---

### **6. GPU 메모리 관리**

- **VRAM(비디오 메모리)**:
    - GPU 연산에는 VRAM이 필요하며, 부족하면 OOM(Out of Memory) 오류 발생.
- **메모리 관리 함수**:
    - `torch.cuda.empty_cache()`: 사용하지 않는 메모리를 해제.
    - `torch.cuda.memory_allocated()`: 현재 사용 중인 메모리 확인.

---

### **7. CUDA 연산 최적화**

- **FP16/FP32 연산**:
    - FP16(half precision)은 VRAM 사용량을 줄이고 속도를 높임.
    - PyTorch에서 `torch.float16`로 설정.
- **멀티 GPU 활용**:
    - 데이터 병렬 처리로 여러 GPU를 사용할 수 있음 (`torch.nn.DataParallel` 또는 `torch.nn.DistributedDataParallel`).

---

### **8. CUDA 디버깅 및 문제 해결**

- **호환성 문제**:
    - 드라이버와 CUDA Toolkit, PyTorch의 버전 호환성을 항상 확인.
- **OOM(Out of Memory) 오류**:
    - 입력 크기 축소, 배치 크기 줄이기, FP16으로 전환.
- **CUDA 오류 확인**:
    - `torch.cuda.get_device_properties()`로 GPU 상태 확인.
    - PyTorch 에러 메시지 해석.

---

### **9. 병렬 처리와 커널 실행**

- **스레드와 블록**:
    - GPU에서 연산은 스레드(thread)가 블록(block)으로 구성되어 병렬적으로 실행.
- **CUDA 스트림**:
    - 여러 작업을 동시에 실행하여 병렬 성능을 극대화.

---

### **10. 기타 실무 팁**

- **NVIDIA Nsight Tools**: CUDA 연산 성능을 분석하고 디버깅할 수 있는 툴.
- **Tensor Core 활용**: 최신 GPU에서 텐서 연산을 가속화하는 기능.

---

위 내용 중에서 궁금한 항목을 말씀해 주시면, 자세히 설명드리겠습니다!