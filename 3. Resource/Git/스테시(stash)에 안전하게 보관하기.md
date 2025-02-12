---
created: 2025-02-12
tags:
  - Terminology
aliases: 
reference: https://mylko72.gitbooks.io/git/content/%EB%A6%AC%EB%B2%A0%EC%9D%B4%EC%8A%A4rebase.html
---
- 어떤 브랜치에서 파일을 수정하거나 추가한 후 커밋하지 않은 상태일 때는 다른 브랜치로 checkout이 불가능하다.
- 이는 수정사항을 잃어버리지 않도록 하려는 Git의 매커니즘이다.
- 하지만 작업해야하는 브랜치를 착각해 다른 브랜치에서 작업중이었거나, 핫픽스 요청이 들어와서 당장 다른 브랜치로 이동해 코드를 확인해야하는 경우 commit하기 참 애매하다.
- 이런 경우에 stash를 사용한다.

- stash의 사전적 의미는 다음과 같다.
	![[Pasted image 20250212151807.png]]

## 현재 수정사항 확인하기
```
git status
```
- 현재 수정사항을 확인할 수 있다.
- 수정사항이 있다면 체크아웃이 불가능하다.

## 스테시로 안전하게 보관
```
git stash
```
- stash는 임시 저장소이다.
- 현재 수정사항을 보관할 수 있다.
- `git stash`이후 `git status`를 확인해보면 수정사항이 없다고 표시된다.

## 스테시 목록 조회
```
git stash list
```
- 현재 stash area에 저장되어 있는 변경사항들을 모두 조회 가능하다.
- 목록 앞의 stash@{0}은 stash ID로 각각의 저장 내용을 구별짓는 번호이다.
- stash는 스택 방식으로 동작하므로 가장 최근에 저장한 stash가 가장 먼저 나오게 된다.

## 저장 내용을 복구
```
git stash pop
```
- 가장 최근에 stash한 저장 내용을 `git stash pop`명령을 통해 현재 브랜치에 적용할 수 있다.

## stash에 저장된 내용 삭제
```
git stash drop (stash@{0})
```
- 명시한 ID의 stash를 삭제한다.
- ID를 명시하지 않으면 가장 최근 stash가 삭제된다.