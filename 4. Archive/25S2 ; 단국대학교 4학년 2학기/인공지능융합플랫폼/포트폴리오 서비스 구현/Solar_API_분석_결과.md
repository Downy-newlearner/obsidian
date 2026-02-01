# Solar API 사용 실패 원인 분석 보고서

## 🔍 분석 개요

Solar API (Upstage Solar Pro2)가 사용되지 않고 Fallback 모드로 동작한 원인을 엄격히 분석한 결과입니다.

---

## ✅ 확인된 사항

### 1. 환경 설정 상태

- ✅ `.env` 파일 존재: 확인됨
- ✅ `UPSTAGE_API_KEY` 설정: 확인됨 (32자, 형식 정상)
- ✅ `GOOGLE_API_KEY` 설정: 확인됨
- ✅ `python-dotenv` 패키지 설치: 확인됨

### 2. 코드 구조

- ✅ `load_dotenv()` 호출: `text_analysis.py` 18번 줄에서 호출됨
- ✅ API 키 확인 로직: `text_analysis.py` 101-103번 줄에 존재
- ✅ API 호출 로직: `text_analysis.py` 118-140번 줄에 구현됨

---

## ❌ 발견된 핵심 문제

### **문제 1: load_dotenv()의 경로 의존성 문제** ⚠️ **가장 가능성 높음**

**위치**: `Feed_analysis_module/text_analysis.py` 18번 줄

```python
# .env 파일 로드
load_dotenv()  # ❌ 문제: 경로를 명시하지 않음
```

**문제점**:

- `load_dotenv()`는 기본적으로 **현재 작업 디렉토리(Current Working Directory)**에서 `.env` 파일을 찾습니다
- `main.py`를 실행할 때 작업 디렉토리가 프로젝트 루트가 아닐 경우 `.env` 파일을 찾지 못합니다
- 예를 들어, 다른 디렉토리에서 `python /path/to/main.py`로 실행하면 `.env` 파일을 찾지 못합니다

**영향**:

- API 키가 로드되지 않아 `os.getenv("UPSTAGE_API_KEY")`가 `None` 반환
- 103번 줄에서 `ValueError` 발생
- `main.py`의 예외 처리로 인해 Fallback 모드로 전환

**증거**:

- API 로그가 전혀 생성되지 않음 → API 호출 자체가 시도되지 않았음을 의미
- Fallback 결과 파일이 생성됨 → 예외 발생 후 Fallback으로 전환됨

---

### **문제 2: load_dotenv() 중복 호출 및 타이밍 문제**

**위치**:

- `Feed_analysis_module/text_analysis.py` 18번 줄
- `Feed_analysis_module/image_analysis.py` 15번 줄

**문제점**:

- 두 모듈에서 각각 `load_dotenv()`를 호출하지만, 경로를 명시하지 않음
- 모듈이 import되는 시점의 작업 디렉토리에 의존적

---

### **문제 3: main.py에서 load_dotenv() 미호출**

**위치**: `main.py`

**문제점**:

- `main.py`에서 `load_dotenv()`를 호출하지 않음
- 모듈 import 시점에만 의존
- 실행 환경에 따라 불안정할 수 있음

---

## 🔧 해결 방안

### **해결책 1: 명시적 경로 지정 (권장)** ⭐

`text_analysis.py`와 `image_analysis.py`에서 `load_dotenv()` 호출 시 프로젝트 루트의 `.env` 파일 경로를 명시적으로 지정:

```python
# Feed_analysis_module/text_analysis.py
from pathlib import Path
from dotenv import load_dotenv

# 프로젝트 루트 디렉토리 찾기 (이 파일의 상위 디렉토리)
PROJECT_ROOT = Path(__file__).parent.parent
ENV_FILE = PROJECT_ROOT / '.env'

# .env 파일 로드
load_dotenv(dotenv_path=ENV_FILE)
```

**장점**:

- 작업 디렉토리와 무관하게 항상 올바른 `.env` 파일을 찾음
- 실행 환경에 독립적
- 가장 안정적인 방법

---

### **해결책 2: main.py에서 중앙 관리**

`main.py`에서 `load_dotenv()`를 호출하여 보장:

```python
# main.py
from pathlib import Path
from dotenv import load_dotenv

# 프로젝트 루트에서 .env 파일 로드
BASE_DIR = Path(__file__).parent
load_dotenv(dotenv_path=BASE_DIR / '.env')
```

**장점**:

- 중앙 집중식 관리
- 실행 시작 시점에 확실히 로드됨

---

### **해결책 3: find_dotenv() 사용**

`python-dotenv`의 `find_dotenv()` 함수를 사용하여 자동으로 `.env` 파일을 찾기:

```python
from dotenv import load_dotenv, find_dotenv

# 프로젝트 루트에서 .env 파일 찾기
env_path = find_dotenv()
if env_path:
    load_dotenv(dotenv_path=env_path)
else:
    raise FileNotFoundError(".env 파일을 찾을 수 없습니다.")
```

---

## 📊 문제 발생 시나리오 재현

### 시나리오 1: 다른 디렉토리에서 실행

```bash
cd /some/other/directory
python /path/to/project/main.py
```

→ 작업 디렉토리가 `/some/other/directory`이므로 `.env` 파일을 찾지 못함

### 시나리오 2: IDE에서 실행

- IDE의 작업 디렉토리 설정이 프로젝트 루트가 아닐 경우
  → `.env` 파일을 찾지 못함

### 시나리오 3: 스크립트로 실행

- 셸 스크립트에서 다른 디렉토리로 이동 후 실행
  → `.env` 파일을 찾지 못함

---

## 🎯 결론

**Solar API가 사용되지 않은 주요 원인**:

1. **`load_dotenv()`가 경로를 명시하지 않아 작업 디렉토리에 의존적**
2. **실행 시 작업 디렉토리가 프로젝트 루트가 아니었을 가능성**
3. **API 키가 로드되지 않아 `ValueError` 발생 → Fallback 모드로 전환**

**즉시 조치 필요**:

- `text_analysis.py`와 `image_analysis.py`의 `load_dotenv()` 호출을 명시적 경로 지정으로 수정
- 또는 `main.py`에서 중앙 집중식으로 `.env` 파일 로드

---

## 📝 추가 권장사항

1. **로깅 강화**: API 키 로드 실패 시 명확한 에러 메시지 출력
2. **검증 로직 추가**: API 키가 로드되었는지 실행 시작 시점에 확인
3. **환경 변수 확인**: `main.py` 시작 시 필수 환경 변수 존재 여부 확인

---

**분석 일시**: 2025년
**분석자**: AI Assistant
**분석 방법**: 코드 리뷰, 실행 시뮬레이션, 환경 변수 확인
