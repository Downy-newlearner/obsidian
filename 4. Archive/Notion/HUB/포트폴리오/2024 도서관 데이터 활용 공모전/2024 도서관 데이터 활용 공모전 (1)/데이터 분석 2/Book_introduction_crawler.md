### **원본**
---
![[book_introduction_crawler.py]]
```Python
import os
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
# CSV 파일 URL 설정
csv_file_url = './library_data/경제_famous.csv'  # 실제 CSV 파일의 경로로 교체
# 이미지 저장 경로 설정
output_file_path = './crawling_code/경제_famous.csv'
# 파일 이름에 유효하지 않은 문자를 제거하는 함수
def safe_filename(name):
    return re.sub(r'[<>:"/\\\\|?*]', '', name)  # 유효하지 않은 문자 제거
# CSV 파일을 다운로드하고 파싱하여 ISBN 목록을 가져오는 함수
def parse_csv(csv_file_url):
    try:
        df = pd.read_csv(csv_file_url)  # 12번째 줄부터 1001개의 행을 읽음
        df.drop(columns=['Unnamed: 0'], inplace=True)  # 필요없는 열 삭제
        df['설명문'] = ''  # '설명문' 열을 추가
        return df['isbn13'].tolist(), df  # ISBN 컬럼만 가져오기
    except Exception as e:
        print(f"Error fetching or parsing the CSV file: {e}")
        return [], pd.DataFrame()
# 도서 사이트에서 도서를 검색하고 정보를 크롤링하는 함수
def crawl_infos(isbns):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")  # ERROR 레벨로 로그 출력 설정
    service = ChromeService(log_path=os.devnull)  # 로그 출력을 null로 설정하여 숨기기
    driver = webdriver.Chrome(service=service, options=options)
    # driver = webdriver.Chrome()
    descriptions = []  # 리스트로 수정
    try:
        for idx, isbn in enumerate(isbns):
            search_url = f"https://search.kyobobook.co.kr/search?keyword={isbn}"
            print(f"Searching for: {idx} / 200")
            driver.get(search_url)
            # 이미지 태그가 로드될 때까지 대기
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'prod_img_load')))
            except Exception as e:
                print(f"Error waiting for image: {e}")
                descriptions.append("No description found")
                continue
            # 도서 페이지로 이동
            try:
                book_page = driver.find_element(By.CLASS_NAME, 'prod_info').get_attribute('href')
                driver.get(book_page)
            except Exception as e:
                print(f"Error finding book page for ISBN {isbn}: {e}")
                descriptions.append("No description found")
                continue
            # 정보 텍스트 로드 대기
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'info_text')))
            except Exception as e:
                print(f"Error waiting for book info: {e}")
                descriptions.append("No description found")
                continue
            # 책 정보 찾기
            book_info_tags = driver.find_elements(By.CLASS_NAME, 'info_text')
            book_info_bold = book_info_tags[1].text if len(book_info_tags) > 1 else "No information found"
            book_info = book_info_tags[2].text if len(book_info_tags) > 2 else "No information found"
            description = f"{book_info_bold}\n\n{book_info}"
            descriptions.append(description)  # 각 설명 추가
    finally:
        driver.quit()
    return descriptions
# 주요 실행 부분
def main():
    isbns, df = parse_csv(csv_file_url)
    if df.empty:
        print("No data to process.")
        return
    descriptions = crawl_infos(isbns)  # ISBN 목록으로 정보 크롤링
    if len(descriptions) != len(df):
        print("Mismatch between number of descriptions and number of records.")
        # Here you might want to handle the mismatch, e.g., fill with default values or truncate.
    df['설명문'] = descriptions
    df.to_csv(output_file_path, index=False)  # 크롤링 결과 저장
    print(f"Updated file saved at: {output_file_path}")
if __name__ == "__main__":
    main()
```
  
### **수정본**
---
![[book_introduction_crawler_update.py]]
- 정보나루에서 csv파일을 다운로드받은 경우 사용
- 기존 데이터프레임에 불필요한 정보를 삭제하고 설명문을 추가하여 csv파일로 저장
![[Source/Untitled 156.png|Untitled 156.png]]
  
```Python
input_path = 'file_path'                # 정보나루에서 다운로드한 csv 파일들이 저장된 폴더 경로
output_folder = 'library_crawling_data' # 크롤링 결과를 csv파일로 저장할 폴더 경로
os.makedirs(output_folder, exist_ok=True)
```
- 맨 앞쪽에 input_path와 output_folder의 경로만 변경한 뒤 실행하면 된다
  
```Python
def parse_csv(csv_file_url):
    try:
        df = pd.read_csv(csv_file_url, encoding='cp949', skiprows=12, nrows=1001) # 12번째 줄부터 1001개의 행을 읽음
        df.drop(columns=['Unnamed: 10', '순위'], inplace=True)  # 필요없는 열 삭제
        df['설명문'] = ''  # '설명문' 열을 추가
        return df['ISBN'].to_list(), df # ISBN 목록, 데이터프레임 반환
    except Exception as e:
        print(f"Error reading the CSV file {csv_file_url}: {e}")
        return None
```
- 정보나루에서 다운받은 데이터의 경우 데이터가 1000개가 아니라면 parse_csv의 nrows를 수정