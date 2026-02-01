"""
이미지 분석 및 매칭 모듈 (Gemini 기반)
"""

import os
import json
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv

# .env 불러오기
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR.parent / ".env"
load_dotenv(ENV_FILE)

API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

MODEL_NAME = "models/gemini-2.0-flash-lite"

def log(msg):
    print(f"[image_analysis] {msg}")

def analyze_single_image(image_path: str) -> str:
    """
    이미지 하나를 분석해 caption 생성
    """
    log(f"이미지 분석 중: {image_path}")

    model = genai.GenerativeModel(MODEL_NAME)

    with open(image_path, "rb") as img_file:
        image_bytes = img_file.read()

    prompt = """
    당신은 포트폴리오 이미지 분석 전문가입니다.
    이미지의 핵심 내용을 1~2줄로 요약한 캡션만 작성하세요.
    불필요한 설명 없이 캡션만 반환하세요.
    """

    response = model.generate_content(
        [
            {"mime_type": "image/jpeg", "data": image_bytes},
            prompt
        ]
    )

    caption = response.text.strip()
    log(f"캡션 생성 완료: {caption}")

    return caption


def match_images_to_posts(text_result_file: str, image_dir: str):
    """
    분석된 텍스트 결과(JSON)와 이미지 디렉토리를 기반으로
    각 포스트에 적절한 이미지를 매칭 후 JSON 파일 생성
    """
    log("이미지 매칭 시작")

    # 텍스트 분석 결과 로드
    with open(text_result_file, "r", encoding="utf-8") as f:
        text_data = json.load(f)

    posts = text_data.get("posts", [])
    image_files = sorted([
        str(Path(root) / file)
        for root, _, files in os.walk(image_dir)
        for file in files
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    ])

    log(f"이미지 파일 {len(image_files)}개 발견")

    matched_posts = []

    for idx, post in enumerate(posts):
        img_index = idx % len(image_files) if image_files else None
        image_path = image_files[img_index] if img_index is not None else None

        if image_path:
            caption = analyze_single_image(image_path)
        else:
            caption = "이미지 없음"

        matched_posts.append({
            "id": post["id"],
            "title": post["title"],
            "date": post["date"],
            "role": post["role"],
            "text": post["text"],
            "image": {
                "path": image_path,
                "caption": caption
            }
        })

    # 저장 파일 경로
    out_path = Path(text_result_file).with_name(
        Path(text_result_file).stem + "_image_matched.json"
    )

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"posts": matched_posts}, f, ensure_ascii=False, indent=2)

    log(f"이미지 매칭 결과 저장 완료: {out_path}")
    return str(out_path)