import os
import json
import base64
from pathlib import Path
from playwright.sync_api import sync_playwright


# ---------------------------------------
# Base64 변환 함수 (절대경로 자동 변환 추가)
# ---------------------------------------
def img_to_base64(path: str):
    try:
        path = Path(path).expanduser().resolve()  # ← 절대경로 자동 변환

        if not path.exists():
            print(f"[WARN] 이미지 파일 없음: {path}")
            return ""

        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"

    except Exception as e:
        print(f"[WARN] 이미지 로드 실패: {path} - {e}")
        return ""


# ---------------------------------------
# HTML 생성 함수
# ---------------------------------------
def generate_html(user, posts, css_text):
    # 사용자 프로필 이미지 Base64 변환
    profile_img_b64 = img_to_base64(user.get("profile_image", ""))

    # WORKS 아이콘 이미지 Base64 변환
    works_images = [
        img_to_base64(path)
        for path in user.get("works_images", [])
    ]

    # WORKS 이미지 HTML
    works_icon_html = "".join(
        f'<img src="{img}" style="width:120px; height:120px; margin:10px;" />'
        for img in works_images
    )

    # Representative Works 카드 HTML 구성
    posts_html = ""
    for post in posts["posts"]:
        img_b64 = img_to_base64(post["image"]["path"])

        posts_html += f"""
        <div class="work-card">
            <img class="work-img" src="{img_b64}" />
            <div class="work-title-row">
                <div class="work-title">{post['title']} | {post['role']}</div>
                <div class="work-date">{post['date']}</div>
            </div>
            <div class="work-desc">{post['text']}</div>
        </div>
        """

    # Skills
    skills_html = "".join(
        f'<div class="skill-badge">{skill}</div>'
        for skill in user["skills"]
    )

    # Licenses
    licenses_html = "<br>".join(user["licenses"])

    # Education
    education_html = "<br>".join(
        f"{edu['degree']} — {edu['school']}"
        for edu in user["education"]
    )

    # Languages
    languages_html = "<br>".join(
        f"{lang['name']} — {lang['level']}"
        for lang in user["languages"]
    )

    # Achievements
    achievements_html = "<br>".join(user["achievements"])

    # 최종 HTML 생성
    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            {css_text}
        </style>
    </head>
    <body>

        <!-- Header -->
        <div class="header">
            <img class="profile-img" src="{profile_img_b64}">
            <div class="header-info">
                <div class="header-name">{user['name']}</div>
                <div class="header-title">{user['job_title']}</div>
                <div class="header-summary">{user['summary']}</div>
            </div>
        </div>

        <!-- Contact -->
        <div class="contact-bar">
            📧 {user['contact']['email']}
            📞 {user['contact']['phone']}
            📍 {user['contact']['location']}
            🌐 {user['contact']['github']}
        </div>

        <!-- Representative Works -->
        <div class="section-title">REPRESENTATIVE WORKS</div>
        <div class="works-grid">
            {posts_html}
        </div>

        <!-- Sidebar -->
        <div class="sidebar">
            <div class="sidebar-section-title">LICENSES</div>
            <div class="sidebar-list">{licenses_html}</div>

            <div class="sidebar-section-title">WORKS</div>
            <div style="display:flex; flex-wrap:wrap;">
                {works_icon_html}
            </div>

            <div class="sidebar-section-title" style="margin-top:40px;">SKILLS</div>
            <div class="skill-badges">{skills_html}</div>

            <div class="sidebar-section-title" style="margin-top:60px;">EDUCATION</div>
            <div class="sidebar-list">{education_html}</div>

            <div class="sidebar-section-title">LANGUAGES</div>
            <div class="sidebar-list">{languages_html}</div>

            <div class="sidebar-section-title">ACHIEVEMENTS</div>
            <div class="sidebar-list">{achievements_html}</div>
        </div>

        <div class="page-number">1</div>

    </body>
    </html>
    """

    return html


# ---------------------------------------
# PDF 생성 (Playwright)
# ---------------------------------------
def generate_pdf(html: str, output_path="portfolio.pdf"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.set_content(html, wait_until="networkidle")

        page.pdf(
            path=output_path,
            width="2480px",
            height="3508px",
            print_background=True
        )

        browser.close()
        print(f"[PDF 생성 완료] {output_path}")


# ---------------------------------------
# Main
# ---------------------------------------
def main():
    ROOT = Path(__file__).parent

    # 사용자 정보 JSON
    user = json.load(open(ROOT / "data" / "user_info.json", encoding="utf-8"))

    # 이미지 매칭이 완료된 최신 JSON 파일 선택
    results_dir = ROOT / "results"
    matched_files = sorted(results_dir.glob("*image_matched.json"))

    if not matched_files:
        raise FileNotFoundError("⚠️ *_image_matched.json 파일이 없습니다.")

    posts = json.load(open(matched_files[-1], encoding="utf-8"))

    # CSS 불러오기
    css_text = open(ROOT / "portfolio_screen" / "full_css.css", encoding="utf-8").read()

    # HTML 생성
    html = generate_html(user, posts, css_text)

    # PDF 생성
    output_pdf_path = ROOT / "generated_portfolio.pdf"
    generate_pdf(html, output_pdf_path)


if __name__ == "__main__":
    main()