
# **⭐** 

# **슬라이드 1 — page_002.jpeg**

  

## **슬라이드 내용**

- Attention의 일반 개념 소개
    
- Attention = 중요 정보에 집중하고 중요하지 않은 정보를 무시하는 메커니즘
    
- Computer Vision에서 Attention은
    
    - 중요한 영역(객체·엣지·텍스처) 강조
        
    - 의미 없는 영역(배경 등)은 무시
        
    
- 시각화 예시:
    
    - 원본 이미지
        
    - Attention map을 통해 중요한 부분이 하이라이트된 이미지 게재
        
    

  

## **내용 요약**

  

Attention이란 입력 전체를 균일하게 처리하지 않고 **특히 중요한 부분에 초점을 맞추는 메커니즘**이다.

Computer Vision에서는 이미지 내에서 중요한 객체/패턴에 집중함으로써 효율적이고 의미 있는 feature 추출이 가능해진다.

---

# **⭐** 

# **슬라이드 2 — page_003.jpeg**

  

## **슬라이드 내용**

- Motivation: Why Attention?
    
- CNN의 한계 소개
    
    - Convolution filter의 크기(size)가 고정됨
        
    - 모든 공간에 동일한 필터 적용 → **적응적이지 않음**
        
    - 이미지 내용에 따라 “어디를 더 볼지” 결정할 수 없음
        
    - 불필요한 영역에도 동일한 연산 수행 → 계산 낭비
        
    
- 예시 이미지:
    
    - 강아지 이미지에서 CNN은 중요한 facial region을 자동으로 더 보지 못함
        
    - adaptive focusing이 불가능함을 강조
        
    

  

## **내용 요약**

  

CNN은 **고정 크기의 지역적 필터**를 사용하기 때문에 이미지 내용에 따라 초점을 조절하지 못한다.

즉, CNN은 **어디가 중요한지 모르는 상태에서 이미지 전체를 균일하게 처리**하며, 이는 비효율성과 정보 손실을 초래한다.

이 때문에 더 유연하게 “중요 영역을 선택적으로 강조”할 수 있는 Attention이 필요해진다.

---

# **⭐** 

# **슬라이드 3 — page_004.jpeg**

  

## **슬라이드 내용**

- Attention이 필요한 이유: Not all information is equal
    
- 실세계 이미지/영상에서는 일부 영역만 핵심 정보를 포함
    
- 예:
    
    - 개 사진의 attention map → 중요한 영역(개)의 위치만 집중
        
    - 도시 거리 영상에서 보행자/신호등 같은 중요한 객체만 강조
        
    
- 즉, 모든 픽셀이 똑같이 중요하지 않다
    

  

## **내용 요약**

  

이미지에는 **중요한 영역과 중요하지 않은 영역이 섞여 있다**.

모델이 모든 위치를 동일하게 처리하면 비효율적이며, 중요한 정보를 놓칠 수 있다.

Attention은 이러한 비대칭적 정보 중요도를 반영하여 중요 영역을 강조한다.

---

# **⭐** 

# **슬라이드 4 — page_005.jpeg**

  

## **슬라이드 내용**

- Attention의 Motivation (3):
    
    - Global context가 필요한 작업(Scene Understanding, Segmentation, Detection)에서 성능 향상
        
    
- Content-dependent processing 필요
    
    - 모델이 입력에 따라 **어디를 볼지 동적으로 결정해야 함**
        
    - 인간 시각 시스템 analogy
        
        - 중요한 영역은 집중
            
        - 배경은 무시하되 awareness는 유지
            
        
    
- Cityscapes segmentation 문제 예시
    
    - 작은 물체 인식 실패
        
    - 큰 배경 영역 segmentation 실패
        
    

  

## **내용 요약**

  

컴퓨터 비전의 많은 작업은 이미지 전체 문맥(글로벌 컨텍스트)을 필요로 한다.

Attention은 입력을 보고 **중요 영역을 동적으로 선택**할 수 있으므로, 작은 객체, 큰 구조, 복잡한 장면 등 다양한 시각 요소를 더 잘 처리할 수 있다.

이는 인간 시각과 비슷한 “content-dependent focusing” 능력을 제공한다.

---

# **⭐** 

# **슬라이드 5 — page_006.jpeg**

  

## **슬라이드 내용**

  

Attention이 왜 중요한지 총정리:

1. CNN → fixed & local
    
    - 적응적이지 않음
        
    - 전역 정보를 한 번에 처리하지 못함
        
    
2. Attention → adaptive & global
    
    - 입력에 따라 초점이 달라짐
        
    - 전역적 문맥을 한 번에 파악 가능
        
    
3. Attention의 이점
    
    - 중요한 영역에 더 많은 모델 용량 할당
        
    - long-range dependency 처리
        
    - Attention map을 통해 해석 가능성 향상
        
    

  

## **내용 요약**

  

CNN의 한계(고정적·지역적 처리)를 극복하기 위해 Attention은 **적응적이고 전역적인 정보 처리 방식**을 제공한다.

이를 통해 모델은 중요한 region에 더 많은 자원을 투자하고, 멀리 떨어진 요소 간의 관계도 쉽게 학습하며, attention map을 통해 해석 가능성까지 높일 수 있다.

---

# **⭐ 전체 슬라이드 흐름 정리 (Week9 첫 번째 파트: Attention의 필요성)**

  

이 다섯 슬라이드는 모두 다음 메시지를 전달한다:

- CNN은 local & fixed filtering 때문에 중요 영역을 동적으로 선택할 수 없다
    
- 이미지에는 중요 정보가 고르게 분포하지 않는다
    
- Attention은 content-dependent focusing을 가능하게 한다
    
- 이를 통해 long-range dependency 처리, global context 이해, interpretability 향상 등의 이점을 얻는다
    

  

즉, **Attention이 왜 필요한가?**에 대한 배경을 시각적으로·직관적으로 설명하는 슬라이드들이다.

---

필요하면

- 다음 슬라이드 묶음(Attention의 원리 QKV / Vision Attention 종류 / Encoder–Decoder 연결)도 같은 방식으로 정리해줄게.