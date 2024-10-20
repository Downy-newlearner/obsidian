  
- 2017-2024 20대 인기대출도서 파일 묶기
- 봄(3-5), 여름(6-8), 가을(9-11), 겨울(12-2) 분류
- 계절 별 KDC 분석(000-900)
- 길이가 짧은 건 빈도수 15-35등 분석, 긴 건 30-50등 분석
  
---
### **데이터 불러오기**
```Python
# 데이터 불러오기 
import pandas as pd
file_paths = [
    "/content/drive/MyDrive/도서관 20대 인기대출/2017_2.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2017_3.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2017_4.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2018_1.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2018_2.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2018_3.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2018_4.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2019_1.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2019_2.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2019_3.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2019_4.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2020_1.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2020_2.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2020_3.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2020_4.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2021_1.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2021_2.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2021_3.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2021_4.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2022_1.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2022_2.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2022_3.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2022_4.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2023_1.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2023_2.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2023_3.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2023_4.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2024_1.csv",
    "/content/drive/MyDrive/도서관 20대 인기대출/2024_2.csv",
]
df_list = [pd.read_csv(file, skiprows=12, encoding='cp949') for file in file_paths]
```
```Python
# 계절 정보를 추출
for file, df in zip(file_paths, df_list):
    if '_1.csv' in file:
        season = '봄'
    elif '_2.csv' in file:
        season = '여름'
    elif '_3.csv' in file:
        season = '가을'
    elif '_4.csv' in file:
        season = '겨울'
    else:
        season = '기타'
    df['계절'] = season
data = pd.concat(df_list, ignore_index=True)
data.head()
```
```Python
import numpy as np
# KDC 분류 함수
def categorize_kdc(kdc):
    if kdc == 1000.000:
        return '결측값'
    try:
        kdc_int = int(np.floor(kdc))  # 정수 부분만 사용
        kdc_prefix = str(kdc_int)[0]  # 첫 자리 추출
        if kdc_prefix == '0':
            return '총류'
        elif kdc_prefix == '1':
            return '철학'
        elif kdc_prefix == '2':
            return '종교'
        elif kdc_prefix == '3':
            return '사회과학'
        elif kdc_prefix == '4':
            return '자연과학'
        elif kdc_prefix == '5':
            return '기술과학'
        elif kdc_prefix == '6':
            return '예술'
        elif kdc_prefix == '7':
            return '언어'
        elif kdc_prefix == '8':
            return '문학'
        elif kdc_prefix == '9':
            return '역사'
        else:
            return '기타'
    except (ValueError, TypeError):
        return '기타'
data['Category'] = data['KDC'].apply(categorize_kdc)
data.head()
```
```Python
spring = data[data['계절'] == '봄']
summer = data[data['계절'] == '여름'] 
autumn = data[data['계절'] == '가을']
winter = data[data['계절'] == '겨울']
```
```Python
spring_총류 = spring[spring['Category'] == '총류']
spring_철학 = spring[spring['Category'] == '철학']
spring_종교 = spring[spring['Category'] == '종교']
spring_사회과학 = spring[spring['Category'] == '사회과학']
spring_자연과학 = spring[spring['Category'] == '자연과학']
spring_기술과학 = spring[spring['Category'] == '기술과학']
spring_예술 = spring[spring['Category'] == '예술']
spring_언어 = spring[spring['Category'] == '언어']
spring_문학 = spring[spring['Category'] == '문학']
spring_역사 = spring[spring['Category'] == '역사']
spring_na = spring[spring['Category'] == '결측값']
```
```Python
spring_총류 = spring[spring['Category'] == '총류']
spring_철학 = spring[spring['Category'] == '철학']
spring_종교 = spring[spring['Category'] == '종교']
spring_사회과학 = spring[spring['Category'] == '사회과학']
spring_자연과학 = spring[spring['Category'] == '자연과학']
spring_기술과학 = spring[spring['Category'] == '기술과학']
spring_예술 = spring[spring['Category'] == '예술']
spring_언어 = spring[spring['Category'] == '언어']
spring_문학 = spring[spring['Category'] == '문학']
spring_역사 = spring[spring['Category'] == '역사']
spring_na = spring[spring['Category'] == '결측값']
```
```Python
summer_총류 = summer[summer['Category'] == '총류']
summer_철학 = summer[summer['Category'] == '철학']
summer_종교 = summer[summer['Category'] == '종교']
summer_사회과학 = summer[summer['Category'] == '사회과학']
summer_자연과학 = summer[summer['Category'] == '자연과학']
summer_기술과학 = summer[summer['Category'] == '기술과학']
summer_예술 = summer[summer['Category'] == '예술']
summer_언어 = summer[summer['Category'] == '언어']
summer_문학 = summer[summer['Category'] == '문학']
summer_역사 = summer[summer['Category'] == '역사']
summer_na = summer[summer['Category'] == '결측값']  
```
```Python
summer_총류 = summer[summer['Category'] == '총류']
summer_철학 = summer[summer['Category'] == '철학']
summer_종교 = summer[summer['Category'] == '종교']
summer_사회과학 = summer[summer['Category'] == '사회과학']
summer_자연과학 = summer[summer['Category'] == '자연과학']
summer_기술과학 = summer[summer['Category'] == '기술과학']
summer_예술 = summer[summer['Category'] == '예술']
summer_언어 = summer[summer['Category'] == '언어']
summer_문학 = summer[summer['Category'] == '문학']
summer_역사 = summer[summer['Category'] == '역사']
summer_na = summer[summer['Category'] == '결측값']  
```
```Python
autumn_총류 = autumn[autumn['Category'] == '총류']
autumn_철학 = autumn[autumn['Category'] == '철학']
autumn_종교 = autumn[autumn['Category'] == '종교']
autumn_사회과학 = autumn[autumn['Category'] == '사회과학']
autumn_자연과학 = autumn[autumn['Category'] == '자연과학']
autumn_기술과학 = autumn[autumn['Category'] == '기술과학']
autumn_예술 = autumn[autumn['Category'] == '예술']
autumn_언어 = autumn[autumn['Category'] == '언어']
autumn_문학 = autumn[autumn['Category'] == '문학']
autumn_역사 = autumn[autumn['Category'] == '역사'] 
autumn_na = autumn[autumn['Category'] == '결측값']
```
```Python
winter_총류 = winter[winter['Category'] == '총류']
winter_철학 = winter[winter['Category'] == '철학']
winter_종교 = winter[winter['Category'] == '종교']
winter_사회과학 = winter[winter['Category'] == '사회과학']
winter_자연과학 = winter[winter['Category'] == '자연과학']
winter_기술과학 = winter[winter['Category'] == '기술과학']
winter_예술 = winter[winter['Category'] == '예술']
winter_언어 = winter[winter['Category'] == '언어']
winter_문학 = winter[winter['Category'] == '문학']
winter_역사 = winter[winter['Category'] == '역사']
winter_na = winter[winter['Category'] == '결측값'] 
```
  
---
### **기본 전처리 코드**
```Python
!pip install konlpy
!pip install wordcloud
```
```Python
import re
from konlpy.tag import Hannanum
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# 전처리 함수
def text_cleaning(text):
    words_to_remove = [
        "장편소설", "소설", "에세이", "그림책", "읽기", "이야기", "리커버", "만화", "학습만화", "연작소설", "책",
    ]
    words_pattern = '|'.join(re.escape(word) for word in words_to_remove)
    pattern = r'[:,.\(\)\[\]{}\-=&!?]'  # 특수문자 제거
    pattern = f'({pattern}|{words_pattern})'  # 단어, 숫자 제거
    text = re.sub(pattern, '', text)
    return text
# 분석 및 시각화 함수
def title_visualize(data, category, start=30, end=50):
    # 데이터 필터링
    filtered_data = data[data['Category'] == category]
    
    # 도서명 리스트 생성
    book_titles = filtered_data['서명'].tolist()
    
    # 전처리
    cleaned_titles = [text_cleaning(title) for title in book_titles]
    
    # 명사 추출
    hannanum = Hannanum()
    nouns = []
    for title in cleaned_titles:
        nouns.extend(hannanum.nouns(title))
    
    # 명사 빈도수 계산
    nouns_freq = Counter(nouns)
    all_nouns_freq = nouns_freq.most_common()  # 전체 빈도 목록
    # 범위 설정
    if len(nouns_freq) <= 1000:
        start, end = 15, 35
    
    nouns_range = all_nouns_freq[start:end]
    nouns_range_dict = dict(nouns_range)
    # 워드 클라우드 생성
    wordcloud = WordCloud(width=800,
                          height=400,
                          background_color='white',
                          font_path='/content/drive/MyDrive/Windows 10 맑은 고딕/malgun668.ttf').generate_from_frequencies(nouns_range_dict)
    # 시각화
    plt.figure(figsize=(12, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
```
  
---
### **Spring**
- 000 총류
인기대출도서 목록에 총류가 존재하지 않음
- 100 철학
![[Source/image 49.png|image 49.png]]
- 200 종교
![[Source/image 1 25.png|image 1 25.png]]
- 300 사회과학
![[Source/image 2 24.png|image 2 24.png]]
- 400 자연과학
![[Source/image 3 21.png|image 3 21.png]]
- 500 기술과학
![[Source/image 4 15.png|image 4 15.png]]
- 600 예술
![[Source/image 5 14.png|image 5 14.png]]
- 700 언어
![[Source/image 6 12.png|image 6 12.png]]
- 800 문학
![[Source/image 7 11.png|image 7 11.png]]
- 900 역사
![[Source/image 8 9.png|image 8 9.png]]
  
---
### **Summer**
- 000 총류
인기대출도서 목록에 총류가 존재하지 않음
- 100 철학
![[Source/image 9 8.png|image 9 8.png]]
- 200 종교
![[Source/image 10 7.png|image 10 7.png]]
- 300 사회과학
![[Source/image 11 7.png|image 11 7.png]]
- 400 자연과학
![[Source/image 12 7.png|image 12 7.png]]
- 500 기술과학
![[Source/image 13 7.png|image 13 7.png]]
- 600 예술
![[Source/image 14 7.png|image 14 7.png]]
- 700 언어
![[Source/image 15 7.png|image 15 7.png]]
- 800 문학
![[Source/image 16 7.png|image 16 7.png]]
- 900 역사
![[Source/image 17 7.png|image 17 7.png]]
  
---
### **autumn**
- 000 총류
인기대출도서 목록에 총류가 존재하지 않음
- 100 철학
![[Source/image 18 7.png|image 18 7.png]]
- 200 종교
![[Source/image 19 6.png|image 19 6.png]]
- 300 사회과학
![[Source/image 20 6.png|image 20 6.png]]
- 400 자연과학
![[Source/image 21 6.png|image 21 6.png]]
- 500 기술과학
![[Source/image 22 6.png|image 22 6.png]]
- 600 예술
![[Source/image 23 6.png|image 23 6.png]]
- 700 언어
![[Source/image 24 5.png|image 24 5.png]]
- 800 문학
![[Source/image 25 5.png|image 25 5.png]]
- 900 역사
![[Source/image 26 5.png|image 26 5.png]]
  
---
### **Winter**
- 000 총류
인기대출도서 목록에 총류가 존재하지 않음
- 100 철학
![[Source/image 27 5.png|image 27 5.png]]
- 200 종교
![[Source/image 28 5.png|image 28 5.png]]
- 300 사회과학
![[Source/image 29 4.png|image 29 4.png]]
- 400 자연과학
![[Source/image 30 3.png|image 30 3.png]]
- 500 기술과학
![[Source/image 31 3.png|image 31 3.png]]
- 600 예술
![[Source/image 32 3.png|image 32 3.png]]
- 700 언어
![[Source/image 33 3.png|image 33 3.png]]
- 800 문학
![[Source/image 34 3.png|image 34 3.png]]
- 900 역사
![[Source/image 35 3.png|image 35 3.png]]