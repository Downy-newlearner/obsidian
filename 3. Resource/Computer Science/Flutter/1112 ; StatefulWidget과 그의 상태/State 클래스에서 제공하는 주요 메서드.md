| **메서드**                         | **설명**                                                               | **사용 시점**           |
| ------------------------------- | -------------------------------------------------------------------- | ------------------- |
| **initState()**                 | 위젯이 최초로 생성될 때 한 번만 호출됨. 비동기 초기화, API 요청, controller 초기화 등을 처리할 때 사용. | 위젯 생성 직후 (build 이전) |
| **build(BuildContext context)** | 위젯의 UI를 구성하는 핵심 메서드. setState()로 상태가 변경되면 다시 호출되어 UI를 갱신함.           | 상태가 바뀔 때마다 자동 호출    |
| **setState(VoidCallback fn)**   | State 내부의 변수를 변경하고, 그 변경사항을 반영하기 위해 UI를 재렌더링시킴.                      | 상태 변경이 필요한 모든 시점    |
| **dispose()**                   | State가 위젯 트리에서 제거될 때 호출됨. controller, stream 등 메모리 자원을 해제할 때 사용.     | 위젯이 화면에서 사라질 때      |
| **didUpdateWidget(oldWidget)**  | 부모 위젯이 rebuild되어 새로운 configuration이 전달될 때 호출됨.                       | 부모 위젯이 업데이트될 때      |
| **didChangeDependencies()**     | InheritedWidget(예: Theme, MediaQuery)의 값이 바뀌면 호출됨.                   | 외부 의존성이 바뀔 때        |
| **deactivate()**                | State가 트리에서 임시로 제거될 때 호출됨. (다시 추가될 수도 있음)                            | 위젯 트리 재구성 시         |
| **reassemble()**                | hot reload 시 호출됨. 디버깅용 코드에서만 사용.                                     | 개발 중 hot reload 시   |

```dart
setState(() {
  _registeredAcademies.clear();
  _registeredAcademies.addAll(academyItems);
  _hasLoadedOnce = true;
  _isLoading = false;
});
```

이 구문은 다음과 같은 일을 합니다:

1. \_registeredAcademies 리스트를 최신 학원 목록(academyItems)으로 갱신
    
2. \_hasLoadedOnce를 true로 바꿔 “이미 한 번 로드됨” 표시
    
3. \_isLoading을 false로 바꿔 [[로딩 스피너]] 제거
    
4. 마지막으로 setState()가 호출되었으므로
    
    → Flutter가 build()를 다시 실행해서 UI를 새로 그림