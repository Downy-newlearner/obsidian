---
created: 2025-06-24
tags: 
reference:
---

## ✅ 1. 설치 여부 확인 명령어

```bash
node -v
```

- 설치 시 버전 출력 (예: v18.17.1)
- 미설치 시 "command not found" 메시지

추가로 npm 확인:

```bash
npm -v
```

---

## ✅ 2. Node.js 설치 명령어 (nvm 권장 이용)

Node.js는 **nvm (Node Version Manager)** 을 통해 설치하는 것이 가장 유연하고 안전합니다.

### nvm 설치:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

설치 후 터미널 재시작 또는 아래 명령 실행:

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

### Node.js 설치 (LTS 버전):

```bash
nvm install --lts
nvm use --lts
```