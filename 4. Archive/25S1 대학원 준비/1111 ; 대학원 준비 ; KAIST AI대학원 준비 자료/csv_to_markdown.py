import csv
import os
import re
from pathlib import Path

def sanitize_filename(title):
    """파일명으로 사용할 수 있도록 문자열 정리"""
    if not title or title.strip() == '':
        return "untitled"
    # 파일명에 사용할 수 없는 문자 제거
    title = re.sub(r'[<>:"/\\|?*]', '', title)
    # 이모지와 특수문자 제거 (선택사항)
    title = re.sub(r'[^\w\s-]', '', title)
    # 공백을 언더스코어로 변경
    title = re.sub(r'\s+', '_', title.strip())
    # 길이 제한
    if len(title) > 100:
        title = title[:100]
    return title

def csv_to_markdown(csv_file_path, output_dir="markdown_output"):
    """
    CSV 파일을 읽어서 각 행을 마크다운 파일로 변환
    
    Args:
        csv_file_path: 입력 CSV 파일 경로
        output_dir: 마크다운 파일을 저장할 디렉토리
    """
    # 출력 디렉토리 생성
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for idx, row in enumerate(reader, start=1):
            # 제목 (Statistic / Probability 컬럼)
            title = row.get('Statistic / Probability ', '').strip()
            if not title:
                title = f"Document_{idx}"
            
            # 내용 컬럼들
            answer_link = row.get('정답 링크 3시간', '').strip()
            formal_answer = row.get('형식적 답', '').strip()
            my_understanding = row.get('내가 이해한 정답으로 하기', '').strip()
            ai_answer = row.get('AI답 (저장)', '').strip()
            
            # 마크다운 내용 생성
            markdown_content = f"# {title}\n\n"
            
            if answer_link:
                markdown_content += f"## 정답 링크\n\n{answer_link}\n\n"
            
            if formal_answer:
                markdown_content += f"## 형식적 답\n\n{formal_answer}\n\n"
            
            if my_understanding:
                markdown_content += f"## 내가 이해한 정답\n\n{my_understanding}\n\n"
            
            if ai_answer:
                markdown_content += f"## AI 답변\n\n{ai_answer}\n\n"
            
            # 파일명 생성
            safe_title = sanitize_filename(title)
            filename = f"{idx:04d}_{safe_title}.md"
            filepath = os.path.join(output_dir, filename)
            
            # 마크다운 파일 저장
            with open(filepath, 'w', encoding='utf-8') as md_file:
                md_file.write(markdown_content)
            
            print(f"생성됨: {filename}")
    
    print(f"\n총 {idx}개의 마크다운 파일이 '{output_dir}' 디렉토리에 생성되었습니다.")

if __name__ == "__main__":
    csv_file = "KAIST AI대학원 준비 - 지식 벼락치기.csv"
    csv_to_markdown(csv_file, "/Users/downy/Documents/markdown_output")
