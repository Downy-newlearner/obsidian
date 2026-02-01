import os
import json
import google.generativeai as genai
from datetime import datetime
from pathlib import Path

# Gemini API 설정
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 사용할 모델
MODEL_NAME = "models/gemini-2.5-flash"


def analyze_text_with_gemini(json_file_path: str) -> str:
    """
    Gemini API를 사용하여 텍스트 분석 수행.
    JSON 피드 → {user, posts: [{id, title, date, role, text}]} 구조 생성
    """

    # 입력 JSON 읽기
    with open(json_file_path, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    feed_posts = input_data.get("feed", {}).get("posts", [])

    # 모델 로드 (JSON 모드)
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        generation_config={"response_mime_type": "application/json"}
    )

    # 프롬프트 구성
    prompt = f"""
당신은 포트폴리오 작성 전문가입니다.
아래 feed 데이터를 기반으로 title, date, role, text 요약을 생성하세요.
각 text는 200자 이하 핵심 요약이어야 합니다.

입력:
{json.dumps(input_data, ensure_ascii=False)}

출력 JSON 형식은 다음과 같아야 합니다(절대 변경 금지):

{{
  "user": "user",
  "posts": [
    {{
      "id": "0",
      "title": "",
      "date": "",
      "role": "",
      "text": ""
    }}
  ]
}}
"""

    try:
        print("Gemini 텍스트 분석 실행 중...")

        response = model.generate_content(prompt)

        # Gemini JSON 모드 → response.text 가 정확한 JSON을 포함
        output_json = json.loads(response.text)

        # 저장 파일 경로를 results/ 디렉토리로 지정하고, 파일명에 타임스탬프 추가
        from datetime import datetime
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = results_dir / (
            Path(json_file_path).stem + f"_text_result_{timestamp}.json"
        )

        # JSON 저장
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_json, f, ensure_ascii=False, indent=2)

        print(f"텍스트 분석 결과 저장: {output_path}")
        return str(output_path)

    except Exception as e:
        print("Gemini 분석 오류 발생:", e)
        raise e