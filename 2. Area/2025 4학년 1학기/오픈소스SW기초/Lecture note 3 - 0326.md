![[Lecture Note 3 - Git_page-0001.jpg]]

![[Lecture Note 3 - Git_page-0002.jpg]]

![[Lecture Note 3 - Git_page-0003.jpg]]

![[Lecture Note 3 - Git_page-0004.jpg]]

![[Lecture Note 3 - Git_page-0005.jpg]]

![[Lecture Note 3 - Git_page-0006.jpg]]

![[Lecture Note 3 - Git_page-0007.jpg]]

![[Lecture Note 3 - Git_page-0008.jpg]]

![[Lecture Note 3 - Git_page-0009.jpg]]

![[Lecture Note 3 - Git_page-0010.jpg]]

![[Lecture Note 3 - Git_page-0011.jpg]]

![[Lecture Note 3 - Git_page-0012.jpg]]

![[Lecture Note 3 - Git_page-0013.jpg]]

![[Lecture Note 3 - Git_page-0014.jpg]]

![[Lecture Note 3 - Git_page-0015.jpg]]

![[Lecture Note 3 - Git_page-0016.jpg]]

![[Lecture Note 3 - Git_page-0017.jpg]]

![[Lecture Note 3 - Git_page-0018.jpg]]

![[Lecture Note 3 - Git_page-0019.jpg]]

![[Lecture Note 3 - Git_page-0020.jpg]]

![[Lecture Note 3 - Git_page-0021.jpg]]

![[Lecture Note 3 - Git_page-0022.jpg]]

![[Lecture Note 3 - Git_page-0023.jpg]]

![[Lecture Note 3 - Git_page-0024.jpg]]

![[Lecture Note 3 - Git_page-0025.jpg]]

![[Lecture Note 3 - Git_page-0026.jpg]]
- 아래 3 줄은 삭제

- git add README
- git commit -m "Add README"
![[Lecture Note 3 - Git_page-0027.jpg]]
- git diff
![[Lecture Note 3 - Git_page-0028.jpg]]
(삭제)
![[Lecture Note 3 - Git_page-0029.jpg]]
reset README
![[Lecture Note 3 - Git_page-0030.jpg]]
이미지에 적힌 작업을 수행하기 위해 필요한 Git 명령어들을 아래와 같이 정리할 수 있어요:

---

### ✅ 1. `README` 파일을 Local repository에 저장하세요.

- 메시지는 `"first"`
    

```bash
git add README
git commit -m "first"
```

---

### ✅ 2. Local repository의 `README` 파일을 Staging area로 내렸다가 다시 Local repository에 저장하세요.

- 메시지는 `"seconds"`
    

```bash
git reset HEAD README     # Staging area에서 README를 내림
git add README            # 다시 Staging area에 올림
git commit -m "seconds"
```

---

### ✅ 3. git의 로그를 확인하세요.

```bash
git log
```

---

필요하면 각 명령어에 대한 설명도 알려줄게요!


![[Lecture Note 3 - Git_page-0032.jpg]]

![[Lecture Note 3 - Git_page-0033.jpg]]

![[Lecture Note 3 - Git_page-0034.jpg]]

![[Lecture Note 3 - Git_page-0035.jpg]]

![[Lecture Note 3 - Git_page-0036.jpg]]

![[Lecture Note 3 - Git_page-0037.jpg]]

![[Lecture Note 3 - Git_page-0038.jpg]]

![[Lecture Note 3 - Git_page-0039.jpg]]

![[Lecture Note 3 - Git_page-0040.jpg]]

![[Lecture Note 3 - Git_page-0041.jpg]]

![[Lecture Note 3 - Git_page-0042.jpg]]

![[Lecture Note 3 - Git_page-0043.jpg]]

![[Lecture Note 3 - Git_page-0044.jpg]]

![[Lecture Note 3 - Git_page-0045.jpg]]