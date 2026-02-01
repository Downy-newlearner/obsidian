---
created: 2025-07-30
tags: 
aliases:
  - merge
reference:
---
## **git merge**

  

### **📌 개념**

  

두 브랜치를 병합할 때 사용.

→ **기존 커밋 히스토리는 그대로 유지**하고, **새로운 병합 커밋(merge commit)** 을 만듭니다.

  

### **🧪 예시**

```
git checkout main
git merge feature
```

- feature 브랜치의 변경사항을 main에 병합
    
- 변경 내용이 충돌하지 않으면 자동 병합되고 merge commit 생성됨
    

  

### **✅ 장점**

- 브랜치 히스토리가 **정확하게 보존**
    
- 협업 이력 추적에 유리
    

---



---

## **🔄 merge vs rebase 비교**

| **항목**     | git merge            | git rebase            |
| ---------- | -------------------- | --------------------- |
| 히스토리       | 브랜치 구조 유지 (병합 커밋 생김) | 직선형 히스토리로 정리됨         |
| 충돌 해결 방식   | 병합 중 한 번             | 커밋마다 하나씩 순차적으로 해결해야 함 |
| 협업 시 권장 여부 | 협업 브랜치에 권장           | 개인 브랜치나 로컬에서만 권장      |
| 커밋 ID      | 유지됨                  | 변경됨 (재작성되므로 ID 바뀜)    |
| 사용 난이도     | 상대적으로 쉬움             | 신중하게 사용해야 함           |

---

## **📌 실제 예시 흐름**

  

### **git merge**

###  **흐름 (히스토리 예시)**

```
A---B---C main
     \    
      D---E feature

git checkout main
git merge feature
```

결과:

```
A---B---C-------M (merge commit)
     \        /
      D---E-- 
```

---

### **git rebase**

###  **흐름**

```
git checkout feature
git rebase main
```

결과:

```
A---B---C---D'---E'  (feature 브랜치가 main 위로 다시 쌓임)
```

---

## **🛑 rebase 주의사항**

- **공용 브랜치에서 rebase 하지 말 것!**
    
    이미 푸시된 커밋을 rebase하면 협업자들과 **히스토리 충돌**이 생길 수 있음.
    

---

## **✨ 실무 팁**

- 로컬에서 내 브랜치 정리할 땐 → rebase
    
- 협업 브랜치를 main에 병합할 땐 → merge
    
- 병합 전 비교할 땐 → git diff branch1..branch2
    

---

필요하면 merge --no-ff, interactive rebase, 충돌 해결 예제도 알려줄 수 있어요!