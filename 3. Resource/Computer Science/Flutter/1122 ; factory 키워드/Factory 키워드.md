factory 키워드는 Dart에서

“일반 생성자랑 조금 다른 방식으로 객체를 만들어도 돼”라고 허용해주는 **팩토리 생성자**를 만들 때 쓰는 키워드야.

```dart
factory UserAcademyResponse.fromJson(Map<String, dynamic> json) {
  return UserAcademyResponse(
    academyName: json['academyName'] ?? '',
    academyRoadAddress: json['academyRoadAddress'] ?? '',
    registerStatus: json['registerStatus'] ?? 'P',
    academyId: json['academyId'] != null
        ? (json['academyId'] is int
              ? json['academyId']
              : int.tryParse(json['academyId'].toString()))
        : null,
  );
}
```

여기서 중요한 포인트만 딱 4개:

1. factory 생성자는 “일반 생성자랑 다른 규칙을 갖는 생성자”

- 보통 생성자는 이렇게 생겼다.
```dart
UserAcademyResponse({
  required this.academyName,
  ...
});
```

- 이건 필드 초기화만 가능하고, return을 직접 쓸 수 없어.
    
- 근데 factory가 붙으면:
    - 함수처럼 return SomeInstance를 쓸 수 있고
    - 조건문, 캐싱, 다른 타입 반환 같은 **복잡한 로직**도 가능함.
        

2. 그래서 fromJson 같은 “변환용 생성자”에 잘 어울림
    

- JSON → 객체로 바꾸는 로직이 필요하니까:
    - null 처리
    - 타입 체크 (is int)
    - 문자열 → int 변환 (int.tryParse(...))
    
- 이걸 일반 생성자(initializer list)로 쓰면 코드가 꽤 지저분해지는데,
    factory로 만들면 안에서 그냥 깔끔하게 return UserAcademyResponse(...) 해버릴 수 있음.


3. 이 코드는 “JSON Map을 받아서 UserAcademyResponse를 만들어주는 팩토리 생성자”
    

- 사용 코드는 이렇게 됨:
```dart
final academy = UserAcademyResponse.fromJson(jsonMap);
```

- 겉으로 보면 그냥 fromJson이라는 이름의 생성자를 호출하는 것처럼 보이지만,
    실제로 내부에서는 factory가 붙어 있어서 함수처럼 동작하면서 마지막에 객체를 return하는 구조.
    


4. 일반 생성자 vs factory 생성자 감각 정리
    
- 일반 생성자
    - 항상 **새 인스턴스**를 만듦
    - this.field = ... 같은 초기화만 가능, return 없음
    
- factory 생성자
    - 새 인스턴스를 만들 수도 있고,
        이미 만든 인스턴스를 돌려주거나, 다른 타입을 돌려주는 것도 가능
    - 내부에 if/else, try/catch, 캐시 로직, 파싱 로직 등 자유롭게 작성 가능
    - 마지막에 return Something;으로 값 반환
        

한 줄로 요약하면:

factory UserAcademyResponse.fromJson(...) 는

“JSON을 받아서, 내부에서 파싱 로직을 돌리고, 그 결과로 UserAcademyResponse 인스턴스를 반환하는 **특수한 생성자**”라고 보면 된다.