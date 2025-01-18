---
Lecture date: 2025-01-18
tags: 
reference: https://www.youtube.com/watch?v=KK2Qdw2122M&list=PLz2iXe7EqJOOt1r8Io-BFAV-SHFWFKYtN&index=16
---
## 14강. SQLite
- SQLite는 외장 DB가 존재하고 파이썬 모듈을 불러와 사용하는 방식이 아니라, 애초에 내장되어있는 것이다.

```
import sqlite3
```


## 15강. DB 테이블 만들기
- 테이블을 만들 때는 커넥션을 생성해야한다.
	- 테이블의 값 생성, 삭제 등 항상 필요한 것이 '커넥션'이다.
- 