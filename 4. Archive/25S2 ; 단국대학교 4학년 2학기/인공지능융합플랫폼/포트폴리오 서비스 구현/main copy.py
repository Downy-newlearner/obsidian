import json
import os
import shutil
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


# -------------------------------------
# 경로 설정
# -------------------------------------
HTML_TEMPLATE_PATH = "./portfolio_screen/index.html"
OUTPUT_HTML_PATH = "./portfolio_screen/index_result.html"
OUTPUT_PDF_PATH = "./portfolio_screen/portfolio.pdf"
TEXT_JSON_PATH = "./results/백앤드 시나리오_text_result_20251207_161458.json"
ASSETS_DIR = "./portfolio_screen/assets"


# -------------------------------------
# JSON 로드
# -------------------------------------
def load_json(json_path: str):
    """텍스트 분석 JSON 파일 로드"""
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


# -------------------------------------
# 이미지 복사 및 상대 경로 변환
# -------------------------------------
def copy_image_to_assets(image_path: str, assets_dir=ASSETS_DIR) -> str:
    """
    절대경로로 되어 있는 JSON 이미지 파일을
    HTML에서 접근 가능한 상대경로 ./assets/ 로 자동 변환 및 복사
    """
    if not image_path or not os.path.exists(image_path):
        print(f"⚠️ 경고: 이미지 파일 없음 → {image_path}")
        return "./assets/default.png"

    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

    filename = os.path.basename(image_path)
    target_path = os.path.join(assets_dir, filename)

    # 기존 파일이 없어야 복사함
    if not os.path.exists(target_path):
        shutil.copy(image_path, target_path)
        print(f"📁 이미지 복사 완료: {target_path}")

    return f"./assets/{filename}"


# -------------------------------------
# work-item 생성
# -------------------------------------
def create_work_item(soup, post):
    """JSON post 데이터를 기반으로 새로운 work-item HTML 요소 생성"""

    article = soup.new_tag("article", **{"class": "work-item"})

    # 이미지 복사 + 상대 경로로 변경
    html_image_path = copy_image_to_assets(post["image"]["path"])

    # 이미지 태그
    img_tag = soup.new_tag(
        "img",
        src=html_image_path,
        alt=post["title"],
        **{"class": "work-image"},
    )
    article.append(img_tag)

    # content div
    content_div = soup.new_tag("div", **{"class": "work-content"})

    # 제목
    title_tag = soup.new_tag("h3", **{"class": "work-title"})
    title_tag.string = f"{post['title']} | {post['role']}"
    content_div.append(title_tag)

    # 날짜
    date_tag = soup.new_tag("p", **{"class": "work-date"})
    date_tag.string = post["date"]
    content_div.append(date_tag)

    # 설명
    desc_div = soup.new_tag("div", **{"class": "work-description"})
    p_tag = soup.new_tag("p")
    p_tag.string = post["text"]
    desc_div.append(p_tag)

    content_div.append(desc_div)
    article.append(content_div)

    return article


# -------------------------------------
# HTML 교체 처리
# -------------------------------------
def replace_work_items(html_path: str, output_path: str, posts: list):
    """기존 work-item을 삭제하고 JSON 기반으로 work-item 구성"""

    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    left_column = soup.find("div", {"class": "left-column"})
    if not left_column:
        raise RuntimeError("❌ left-column을 HTML에서 찾을 수 없습니다.")

    for old_item in left_column.find_all("article", {"class": "work-item"}):
        old_item.decompose()

    for post in posts:
        work_item = create_work_item(soup, post)
        left_column.append(work_item)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"🎉 HTML 반영 완료 → {output_path}")


# -------------------------------------
# Playwright PDF 생성
# -------------------------------------
def export_pdf_from_html(html_path: str, output_pdf_path: str):
    """HTML 파일을 브라우저로 렌더링해 PDF로 저장"""
    print("\n🖨  PDF 생성 중...")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # file:// 경로로 HTML 로드
        page.goto(f"file://{os.path.abspath(html_path)}")

        page.pdf(
            path=output_pdf_path,
            format="A4",
            print_background=True
        )

        browser.close()

    print(f"📄 PDF 생성 완료 → {output_pdf_path}")


# -------------------------------------
# 메인 함수
# -------------------------------------
def main():
    print("\n=======================================")
    print("📌 JSON → HTML 변환 + PDF 생성 시작")
    print("=======================================\n")

    data = load_json(TEXT_JSON_PATH)
    posts = data["posts"]

    for post in posts:
        if "image" not in post:
            post["image"] = {"path": "./assets/default.png"}

    replace_work_items(
        HTML_TEMPLATE_PATH,
        OUTPUT_HTML_PATH,
        posts
    )

    export_pdf_from_html(OUTPUT_HTML_PATH, OUTPUT_PDF_PATH)

    print("\n✅ 모든 작업 완료!\n")


if __name__ == "__main__":
    main()