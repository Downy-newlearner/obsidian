![[image_collector_v2.py]]
![[training.ipynb]]
## 구상
사람들이 책의 표지를 보고 읽고싶은 마음을 갖게 되는 부분이 무엇인가?
이미지로 얻어내고 싶은 것 → 표지의 어떤 부분이 사람들을 끌어당기는가?
그 “어떤 부분”을 찾아서 각 표지에 “어떤 부분”이 얼마나 포함되어있는지 평가하고, 높이 평가된 책들을 도서관 이용자들이 잘 볼 수 있는 곳에 비치하자는 맥락이다.
  
책의 표지에 대한 “점수”를 매기기
  
## 구현 계획
1. 출판사에서 가지는 표지를 만드는 기준을 찾아보기
2. 그 기준들을 책 표지에서 어떻게 평가할 수 있는지 방안 생각하기
3. 서점 사이트 또는 도서관 사이트에서 표지 이미지들 크롤링하기
  
  
  
## 자연어 처리 파트들과 합칠 수 있는 부분 고려
자연어 처리에서 고려하고 있는 것은 ==인기 도서들의 계절별 주요 키워드==이다.
인기 도서들의 계절별 주요 키워드 + 표지의 점수 → 합리적인 평가 지표를 마련하여 도서들을 모두 평가하고, 계절에 맞는 높은 점수의 도서들을 밀어준다.
  
### 어떻게 밀어주는가?
1. 도서관 중앙 또는 이용자에게 잘 보이는 곳에 책 비치하기
2. 도서관 추천 도서라는 키워드를 붙여 간접적으로 권유.(도서관 추천 도서라는 키워드가 이용자들에게 호의적인 키워드일지 고려해보기)
3. 도서관 도서 검색 사이트에 추천 배너 만들기
4. 도서관 도서 검색 컴퓨터 바탕화면을 주기적으로 추천 도서 소개로 설정하기
---
# 책 표지 디자인은 어떻게 하는가?
- **첫인상**: 독자의 시선을 즉시 끌어야 합니다.
- **명확한 정보 전달**: 책의 제목, 저자명, 그리고 주요 메시지를 명확히 보여줘야 합니다.
- **타겟 독자 반영**: 책의 내용과 맞는 디자인으로 타겟 독자의 관심을 유도해야 합니다.
- **일관성**: 글자체, 색상, 이미지 등이 일관되어야 합니다.
- **독창성**: 다른 책과 차별화되는 독창적인 디자인이어야 합니다.
  
# 표지 디자인의 평가 기준
### 1. 계절별로 표지에서 중요한 점수 기준 설정
각 계절마다 선호되는 디자인 요소를 기준으로 평가 항목을 설정합니다.
- **봄**:
    - 색상: 밝고 화사한 색상 (파스텔 톤, 밝은 녹색, 분홍색)
    - 이미지: 꽃, 새싹, 자연의 생동감 있는 이미지
    - 분위기: 경쾌하고 따뜻한 느낌
- **여름**:
    - 색상: 시원한 색상 (파란색, 청록색, 밝은 노란색)
    - 이미지: 바다, 해변, 햇빛, 열대 과일
    - 분위기: 활기차고 에너제틱한 느낌
- **가을**:
    - 색상: 따뜻하고 깊이 있는 색상 (주황색, 갈색, 짙은 녹색)
    - 이미지: 낙엽, 수확, 따뜻한 음료
    - 분위기: 포근하고 성숙한 느낌
- **겨울**:
    - 색상: 차가운 색상 (흰색, 파란색, 회색)
    - 이미지: 눈, 겨울 스포츠, 따뜻한 실내 장면
    - 분위기: 차분하고 고요한 느낌
  
# 표지 이미지들 크롤링
### 1. 표지 이미지를 크롤링하는 파이썬 코드의 흐름
1. **라이브러리 설치 및 불러오기**:
    - 필요한 라이브러리 설치 (`requests`, `BeautifulSoup`, `Selenium`, `Pillow` 등)
    - 라이브러리 불러오기
2. **웹페이지 요청 및 파싱**:
    - `requests` 또는 `Selenium`을 사용하여 웹페이지 HTML 가져오기
    - `BeautifulSoup`을 사용하여 HTML 파싱
3. **표지 이미지 URL 추출**:
    - 특정 HTML 태그 및 속성을 기준으로 표지 이미지 URL 추출
    - `BeautifulSoup` 또는 정규 표현식을 사용하여 이미지 URL 추출
4. **이미지 다운로드**:
    - `requests`를 사용하여 이미지 파일 다운로드
    - 이미지를 로컬 저장소에 저장
5. **이미지 전처리**:
    - `Pillow`를 사용하여 이미지 크기 조정, 색상 변환 등의 전처리 수행
6. **결과 저장**:
    - 다운로드한 이미지와 메타 데이터를 CSV 파일 또는 데이터베이스에 저장
  
# 표지 이미지들에서 평가 기준에 매치되는 요소들 추출 또는 즉시 평가하기(점수 산출)
### 딥러닝을 활용한 표지 이미지 점수 산출 프로세스
### 1. 데이터 수집 및 전처리
- **이미지 수집**: 웹 크롤러를 사용하여 각 계절에 해당하는 표지 이미지를 수집합니다.
- **레이블링**: 각 이미지를 계절별로 레이블링 (봄, 여름, 가을, 겨울).
- **전처리**: 이미지 크기 조정, 색상 보정, 정규화 등.
### 2. 모델 설계
- **모델 선택**: Convolutional Neural Network (CNN) 사용.
- **구조 설계**:
    - 입력 레이어: 표지 이미지 (예: 224x224x3).
    - 여러 층의 Convolutional Layer와 Max-Pooling Layer.
    - Flatten Layer.
    - Dense Layer (Fully Connected Layer).
    - 출력 레이어: 4개의 노드 (계절별 분류) 또는 다중 점수 산출 노드 (색상, 이미지, 분위기별 점수).
### 3. 모델 학습
- **데이터 분할**: 학습, 검증, 테스트 데이터셋으로 분할.
- **손실 함수 및 옵티마이저**: Cross-Entropy Loss, Adam Optimizer.
- **학습**: 모델 학습 및 검증, 하이퍼파라미터 튜닝.
### 4. 모델 평가
- **정확도 평가**: 학습된 모델의 분류 정확도 평가.
- **혼동 행렬**: 각 계절별로 모델의 분류 성능을 시각화.
### 5. 점수 산출
- **계절별 점수**:
    - **색상**: Color Histogram 분석, 계절별 선호 색상과의 유사도 측정.
    - **이미지**: 이미지 내용 분석, 계절별 특징과의 매칭 점수.
    - **분위기**: Scene Classification, 계절별 분위기와의 일치 점수.
- **통합 점수**: 각 평가 항목별 점수를 합산하여 총점 산출.
### 프로세스 세부 단계
1. **데이터 수집 및 전처리**
    
    ```Python
    from PIL import Image
    import requests
    from io import BytesIO
    import os
    
    def download_image(url, save_path):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((224, 224))
        img.save(save_path)
    
    # 예제 URL 리스트
    image_urls = [
        "<https://example.com/spring1.jpg>",
        "<https://example.com/summer1.jpg>",
        # ...
    ]
    
    for idx, url in enumerate(image_urls):
        download_image(url, f"images/image_{idx}.jpg")
    ```
    
2. **모델 설계 및 학습**
    
    ```Python
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
    
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(4, activation='softmax')  # 계절 분류
    ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    # 학습 데이터 및 라벨 로드
    train_images, train_labels = # Load your data here
    model.fit(train_images, train_labels, epochs=10, validation_split=0.2)
    ```
    
3. **모델 평가 및 점수 산출**
    
    ```Python
    # 예측 및 평가
    test_images, test_labels = # Load your test data here
    predictions = model.predict(test_images)
    
    # 점수 산출
    def calculate_score(predictions, labels):
        # 각 계절별로 점수 계산
        scores = []
        for pred, label in zip(predictions, labels):
            score = 0
            if pred == label:
                score += 10  # 일치 점수
            # 추가적인 기준별 점수 계산
            scores.append(score)
        return scores
    
    test_scores = calculate_score(predictions, test_labels)
    ```
    
이와 같은 프로세스로 딥러닝을 활용하여 표지 이미지의 계절별 점수를 산출할 수 있습니다.