---
created: 2025-07-30
tags: 
aliases: 
reference:
---
## **git rebase**

  

### **📌 개념**

  

한 브랜치의 커밋을 다른 브랜치의 **끝에 다시 쌓는 것처럼** 재작성

→ **히스토리를 깔끔하게 만들지만, 커밋 ID가 바뀝니다.**

  

### **🧪 예시**

```
git checkout feature
git rebase main
```

- feature 브랜치의 커밋들을 main의 최신 커밋 뒤에 **붙여서 재작성**
    

  

### **✅ 장점**

- 커밋 히스토리가 **직선형으로 깔끔해짐**
    
- 리뷰할 때 한눈에 보기 쉬움
    