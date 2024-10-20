---
태그:
  - Git
---
#### Git 용어
|이름|태그|
|---|---|
|[[깃 저장소(Git Repostory)]]||
|[[add, commit, push의 차이]]||
|[[사용자 정보 설정하기(커밋을 위함)]]||
  
  
  
  
  
## Git 명령어
## 코드 업데이트하기
```C++
git add .
git commit -m "[수정 사항 이름]"
git push origin [업데이트할 branch 이름]
```
  
## 수정된 코드 받아오기
```C++
git pull --rebase origin [branch 이름]
```
  
## 현재 branch 변경하기
```C++
git checkout [변경할 branch]
```
  
## push된 commit 삭제하는 법
```C++
1. git log를 통해 삭제할 commit 찾기
2. git reset을 통해 commit 삭제하기
     - 최근의 commit을 삭제하고 싶을 땐 git reset HEAD^
     - 최근의 n개의 commi을 삭제하고싶을땐 git reset HEAD~n 
3. git push -f origin "branch name"을 통해 github에 commit 삭제를 알리기
```
1. **git init**
    
    - 새 Git 저장소를 초기화합니다. 빈 폴더를 Git 저장소로 만들고 싶을 때 사용합니다.
    
    ```Shell
    git init
    ```
    
2. **git clone**
    
    - 원격 저장소를 복제(clone)하여 로컬에 Git 저장소를 생성합니다.
    
    ```Shell
    git clone <repository_url>
    ```
    
3. **git status**
    
    - 현재 작업 디렉토리의 상태를 확인하고, 어떤 파일이 수정되었는지, 스테이징 되었는지, 커밋되지 않았는지를 보여줍니다.
    
    ```Shell
    git status
    ```
    
4. **git add**
    
    - 파일을 스테이징(staging) 영역에 추가하여 커밋할 준비를 합니다. `.`을 사용하면 현재 디렉토리의 모든 변경사항을 추가할 수 있습니다.
    
    ```Shell
    git add <filename>
    # 또는 모든 파일 추가
    git add .
    ```
    
5. **git commit**
    
    - 스테이징 영역에 있는 변경 사항을 커밋합니다. `m` 옵션을 사용하면 커밋 메시지를 한 줄로 작성할 수 있습니다.
    
    ```Shell
    git commit -m "Commit message"
    ```
    
6. **git push**
    
    - 로컬 저장소의 커밋을 원격 저장소에 푸시(push)하여 변경 사항을 반영합니다.
    
    ```Shell
    git push origin <branch_name>
    ```
    
7. **git pull**
    
    - 원격 저장소의 변경 사항을 로컬 저장소로 가져와 병합합니다.
    
    ```Shell
    git pull origin <branch_name>
    ```
    
8. **git branch**
    
    - 현재 저장소의 브랜치 목록을 확인하거나 새로운 브랜치를 생성합니다.
    
    ```Shell
    git branch  # 현재 브랜치 목록 보기
    git branch <new_branch_name>  # 새로운 브랜치 생성
    ```
    
9. **git checkout**
    
    - 다른 브랜치로 전환하거나 특정 커밋을 체크아웃합니다.
    
    ```Shell
    git checkout <branch_name>
    ```
    
10. **git merge**
    
    - 다른 브랜치의 변경 사항을 현재 브랜치에 병합합니다.
    
    ```Shell
    git merge <branch_name>
    ```
    
11. **git log**
    
    - 커밋 이력을 보여줍니다.
    
    ```Shell
    git log
    ```