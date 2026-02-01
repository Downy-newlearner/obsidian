---
created: 2025-11-22
tags: []
aliases:
reference:
---
```dart
final cached = await _loadFromCache(date);
...
return await _fetchFromServer(
  date: date,
  userAcademyId: userAcademyId,
);
```

- await = “이 Future가 끝날 때까지 **잠깐 멈췄다가**, 결과 값을 받아와서 계속 진행해라”
    
- 전제 조건:
    - 이 키워드는 async가 붙은 함수 안에서만 사용 가능.
    - 그래서 함수 선언에 async가 있는 거야:

- await _loadFromCache(date) 흐름:
	1. _loadFromCache(date)는 Future<List\<Assessment>?>를 리턴.
	2. await가 붙었으니, 캐시 읽기가 끝날 때까지 기다렸다가
	3. 실제 결과 List\<Assessment>?를 cached 변수에 넣어줌.



- return await _fetchFromServer(...) 는
	- _fetchFromServer의 Future가 끝날 때까지 기다렸다가
	- 그 결과(리스트)를 반환하겠다는 뜻.
	- 예외 처리할 땐 await가 붙어 있어야 try/catch에서 에러를 잡을 수 있다는 점도 기억해두면 좋아.