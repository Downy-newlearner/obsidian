

언젠가 처음 이 기능을 사용해볼 내가 어떤 알 수 없는 에러를 겪게 될 수 있겠지. 그 때 체크해볼 체크리스트를 만들어줘. 예를들어. 아래와 같이.

---
- Default Repository의 경로를 잘못 설정하거나 설정하지 않으면 Background Agent가 시작할 수 없습니다.


물론입니다! Cursor의 Slack 연동 기능을 처음 사용할 때 발생할 수 있는 **잠재적 오류 상황과 점검 체크리스트**를 아래와 같이 정리해드릴게요.

---

## **🧩 Cursor - Slack 연동 기능 오류 발생 시 체크리스트**

1. **🔗 Default Repository 설정 여부 확인**
    
    - Default Repository의 경로를 잘못 설정하거나 설정하지 않으면 Background Agent가 시작할 수 없습니다.
        
        @cursor settings 명령어로 확인하세요.
        
    
2. **📍 Default Branch 설정 확인**
    
    - 기본 브랜치가 main, master 등이 아닌 경우 @cursor settings에서 잘못 지정되어 있을 수 있습니다.
        
    
3. **🔒 Slack 권한 부족**
    
    - Slack 앱에 **멘션 읽기, 채널 히스토리 접근 권한**이 충분히 부여되지 않으면 메시지를 인식하지 못할 수 있습니다.
        
        → Slack 관리자의 앱 권한 확인 필요
        
    
4. **🧠 Agent Context 길이 초과**
    
    - 너무 많은 메시지가 달린 스레드에서 실행하면 context overflow가 발생할 수 있습니다.
        
        → 메시지 길이/스레드 깊이 제한 확인
        
    
5. **🛠️ GitHub 액세스 토큰 설정 누락**
    
    - 에이전트가 PR 생성 등을 못할 경우, GitHub 권한 설정 또는 액세스 토큰 연동이 누락되었을 수 있습니다.
        
    
6. **📁 프로젝트 루트 디렉토리 오류**
    
    - .cursor 설정 파일이 존재하지 않거나, 지정된 프로젝트 루트가 Git 리포지토리 루트가 아닐 경우
        
        → .cursor/config.json 내 path를 확인하세요.
        
    
7. **📌 Agent 이름 또는 명령어 오타**
    
    - 예: @cursor fix the bug in foo.ts와 같은 명령에서 파일명이 잘못되었거나 존재하지 않을 수도 있습니다.
        
    
8. **📄 PR 생성 실패**
    
    - PR 생성 후 Slack 메시지로 링크가 안 뜰 경우 → 브랜치 권한, GitHub rate limit, GitHub 연동 실패 가능성 체크
        
    
9. **⚠️ Cursor 서버 상태**
    
    - Cursor 서버가 일시적으로 응답하지 않을 수도 있음
        
        → Cursor 공식 상태 페이지 또는 Discord 커뮤니티 참고
        
    

---

## **✅ 추천 기본 명령어**

- @cursor settings : 현재 연결된 repo, branch, model 확인
    
- @cursor list my agents : 실행 중인 에이전트 목록 확인
    
- @cursor help : 사용 가능한 명령어 확인
    

---

필요하다면 **문제 발생 시 스크린샷 예시**나 **커스텀 에이전트 설정 체크리스트**도 만들어줄 수 있어요.

사용 전에 이걸 .md 파일로 저장해두면 훗날 유용할 거예요!