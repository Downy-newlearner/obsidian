---
created: 2025-11-27
tags: []
aliases:
reference: https://api.flutter.dev/flutter/material/InkWell-class.html
---
둘 다 Flutter에서 나온 “터치/제스처 감지용 위젯”이야.

이름이 헷갈리는데, 역할을 딱 나누면 이렇게 보면 쉬워.

  

먼저 공통점
- 둘 다 “이 영역을 탭하면 뭔가 실행해라” 같은 걸 만들 때 감싸는 위젯.
- child 위젯을 감싸서 onTap, onLongPress 같은 콜백을 받을 수 있음.
    

## 1. InkWell 이 뭐냐

한 줄 정의:

“Material 스타일 물결(ripple) 효과가 있는 터치 영역 위젯”

  

핵심 특징

- 탭하면 물결 효과(splash)가 퍼지는 애니메이션이 자동으로 나옴.
    
- Material Design 전용이라, 위쪽에 Material / Scaffold 같은 게 있어야 정상 동작.
    
- 주로 “버튼처럼 보이고, 눌렀을 때 시각적 피드백이 필요한 영역”에 씀.
    

  

예시:

```dart
InkWell(
  onTap: () {
    print('탭!');
  },
  borderRadius: BorderRadius.circular(8),
  child: Padding(
    padding: const EdgeInsets.all(12),
    child: Text('눌러보기'),
  ),
);
```

→ 사용자는 “아, 눌렸구나”를 물결 애니메이션으로 바로 알 수 있음.

---

## 2. GestureDetector 가 뭐냐

한 줄 정의:

“아무 시각 효과 없이, 제스처만 감지하는 저수준 위젯”

  

핵심 특징

- 기본적으로 그냥 투명한 터치 센서라고 생각하면 됨.
- 탭, 더블탭, 롱프레스, 드래그, 스와이프, 핀치(zoom) 등 더 다양한 제스처를 잡을 수 있음.
- 하지만 InkWell처럼 자동으로 ripple 같은 시각 효과는 안 줌 → 필요하면 네가 직접 애니메이션/색 변경 등을 구현해야 함.
    

  

예시:

```dart
GestureDetector(
  onTap: () {
    print('탭!');
  },
  onDoubleTap: () {
    print('더블 탭!');
  },
  onPanUpdate: (details) {
    print('드래그 중: ${details.delta}');
  },
  child: Container(
    padding: const EdgeInsets.all(12),
    color: Colors.blue,
    child: const Text('제스처 감지 영역'),
  ),
);
```


---
## 3. 언제 뭘 쓰면 되냐

대충 이렇게 기억하면 편해:

- “그냥 버튼/카드/리스트 아이템처럼 눌렀을 때 반짝이는 효과 있으면 좋겠다”
    
    → InkWell (또는 InkResponse, TextButton, ElevatedButton 등)
    
- “커스텀 제스처 처리(드래그, 스와이프, 확대/축소 등)를 하고 싶다”
    
    → GestureDetector
    
- “둘 다 필요한 경우”
    
    → GestureDetector로 제스처를 처리하면서, 별도로 애니메이션/색 변화를 직접 구현
    
    (또는 InkWell 위에 다른 제스처를 얹는 구조 설계)
    

  

정리

- 둘 다 Flutter 위젯이고,
    
- InkWell = Material 스타일의 ‘눌렀을 때 물결 효과까지 포함된 버튼용 레이어’
    
- GestureDetector = 눈에 안 보이는 범용 제스처 센서
    

  

이 정도만 기억해도, 앞으로 UI 만들 때

“아, 이건 InkWell 쓰자 / 이건 GestureDetector구나”가 바로 감 잡힐 거야.
