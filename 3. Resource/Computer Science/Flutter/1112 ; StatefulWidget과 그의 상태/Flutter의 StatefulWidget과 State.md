
## StatefulWidget
> "화면이 변할 수 있는 위젯"을 만들 때 사용하는 클래스

``` Dart
class AcademyPage extends StatefulWidget {
  const AcademyPage({super.key});

  @override
  State<AcademyPage> createState() => _AcademyPageState();
}
```

StatefulWidget은 두 개의 클래스가 짝을 이룬다.
- AcademyPage
	- 위젯의 틀
	- 불변적이며 재사용이 가능하다.====
- \_AcademyPageState
	- 위젯의 상태정보(state)를 담는 실행 인스턴스
	- 가변적이고 동적으로 바뀐다.


## State
예를 들어, \_hasLoadedOnce나 \_registeredAcademies는 \_AcademyPageState 클래스 안에 선언되어야 한다.

``` dart
class _AcademyPageState extends State<AcademyPage> {
  bool _hasLoadedOnce = false; // 한 번이라도 로드했는지 표시
  List<AcademyItem> _registeredAcademies = []; // 학원 목록
}
```


## State 변수들이 저장되는 위치
이 변수들은,
- 클래스의 필드(field)로 존재하고,
- 위젯이 화면에 그려지는 동안(State 객체가 유지되는 동안) Dart 메모리(Heap)에 저장된다.

즉, 페이지를 벗어나면 State 객체가 사라지고, 그 안의 \_hasLoadedOnce와 \_registeredAcademies도 같이 없어진다.

```
_hasLoadedOnce == true && _registeredAcademies.isNotEmpty
```
즉, 이 조건문의 의미는

1. \_hasLoadedOnce == true -> 이미 한 번 서버에서 학원 목록을 불러왔다.
2. \_registeredAcademies.isNotEmpty -> 불러온 결과가 비어 있지 않다.

즉, "학원 목록을 한 번 이상 로드했고, 데이터가 있다면 리스트를 보여줘라"라는 논리를 표현한 것이다.