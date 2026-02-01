---
created: 2025-07-30
tags: 
aliases: 
reference:
---

## git reset

## : 브랜치의 HEAD(커밋 포인터)를 다른 커밋으로 이동

  

### **📌 개념**

- 현재 브랜치의 HEAD를 지정한 커밋으로 **강제로 이동**시킵니다.
    
- 옵션에 따라 워킹 디렉토리(파일 상태)와 staging 영역(index)도 함께 변경됨.
    

---

### **✋ reset의 세 가지 주요 옵션**

| **명령어**       | **의미**                          | **영향 받는 영역**                  |
| ------------- | ------------------------------- | ----------------------------- |
| --soft        | HEAD만 이동                        | ✔ staging O / ✔ working dir O |
| --mixed (기본값) | HEAD + staging 초기화              | ❌ staging X / ✔ working dir O |
| --hard        | HEAD + staging + working 모두 초기화 | ❌ staging X / ❌ working dir X |

---

### **🧪 예시**

```
git reset --soft HEAD~1
```

- 마지막 커밋을 취소하고, 코드는 그대로지만 add 상태로 돌아감
    

```
git reset --mixed HEAD~1
```

- 마지막 커밋을 취소하고, staging도 초기화됨 (변경 파일은 그대로 존재)
    

```
git reset --hard HEAD~1
```

- **마지막 커밋과 코드까지 모두 삭제됨** (복구 불가 주의)
    

---

## **✅ 실무에서 자주 쓰는 조합**

```
git fetch origin
git reset --hard origin/main
```

- 원격 저장소(origin/main) 상태로 **로컬 브랜치를 완전히 초기화** (주의: 변경사항 삭제됨)