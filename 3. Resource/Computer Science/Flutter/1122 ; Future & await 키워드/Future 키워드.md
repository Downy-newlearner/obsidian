---
created: 2025-11-22
tags: []
aliases:
reference:
---
```dart
Future<List<Assessment>> getAssessmentsForDate(...) async { ... }
```
- Future\<T> = “나중에 T 타입 값을 줄게” 라는 약속(비동기 결과 객체).
- 지금 당장 List\<Assessment>를 못 주고,
    - 서버 호출 / 디스크 읽기 / SharedPreferences 접근처럼 시간이 걸리는 작업을
    - “끝나면 결과를 줄게” 라고 감싸놓은 타입이야.
        
    
- 그래서 이 함수는:
    - “지금 바로 List를 주는 게 아니라,
        나중에(비동기로) List\<Assessment>를 담아서 돌려주는 함수” 라는 뜻.