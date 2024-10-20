## |Java Collections Framework(JCF)
- 컬렉션(Collection) : 데이터의 집합, 그룹
- JCF : 컬렉션과 이를 구현하는 클래스를 정의하는 인터페이스
    
    ![[Source/Untitled 142.png|Untitled 142.png]]
    
    - JCF의 상속 구조
  
### |Collection 인터페이스의 특징
|인터페이스|구현클래스|특징|
|---|---|---|
|Set|HashSet  <br>TreeSet|순서를 유지하지 않는 데이터의 집합으로 데이터의 중복을 허용하지 않는다.|
|List|LinkedList  <br>Vector  <br>ArrayList|순서가 있는 데이터의 집합으로 데이터의 중복을 허용한다.|
|Queue|LinkedList  <br>PriorityQueue|List와 유사|
|Map|Hashtable  <br>HashMap  <br>TreeMap|키(Key), 값(Value)의 쌍으로 이루어진 데이터으 집합으로,  <br>순서는 유지되지 않으며 키(Key)의 중복을 허용하지 않으나 값(Value)의 중복은 허용한다.|
1. Set 인터페이스
    - **HashSet**
        - 가방 빠른 임의 접근 속도
        - 순서를 예측할 수 없음
    - **TreeSet**
        
        - 정렬방법을 지정할 수 있음
        
          
        
2. List 인터페이스
    - **LinkedList**
        - 양방향 포인터 구조로 데이터의 삽입, 삭제가 빈번할 경우 데이터의 위치정보만 수정하면 되기에 유용
        - 스택, 큐, 양방향 큐 등을 만들기 위한 용도로 쓰임
    - **Vector**
        - 과거에 대용량 처리를 위해 사용했으며, 내부에서 자동으로 동기화처리가 일어나 비교적 성능이 좋지 않고 무거워 잘 쓰이지 않음
    - **ArrayList**
        - 단방향 포인터 구조로 각 데이터에 대한 인덱스를 가지고 있어 조회 기능에 성능이 뛰어남
3. Map 인터페이스
    - **Hashtable**
        - HashMap보다는 느리지만 동기화 지원
        - null불가
    - **HashMap**
        - 중복과 순서가 허용되지 않으며 null값이 올 수 있다.
    - **TreeMap**
        - 정렬된 순서대로 키(Key)와 값(Value)을 저장하여 검색이 빠름
  
## |Collection의 특징
- 컬렉션에서 다룰 수 있는 데이터는 기본적으로 객체만 가능하다
- char, int, float와 같은 기본형은 사용할 수 없고 Weapper 클래스를 사용해야한다.
    
    |**기본 타입**|**래퍼 클래스**|
    |---|---|
    |byte|Byte|
    |short|Short|
    |int|**Integer**|
    |long|Long|
    |float|Float|
    |double|Double|
    |char|**Character**|
    |boolean|Boolean|
    
- Collection 인터페이스의 주요 메서드
    
    |메소드|설명|
    |---|---|
    |**boolean add(E e)**|현재 컬렉션에 데이터 객체 e를 추가합니다.|
    |**boolean addAll(Collection<? extends E> c)**|현재 컬렉션에 컬렉션 c의 모든 데이터를 추가합니다.|
    |**boolean contains(Object o)**|현재 컬렉션에 객체 o의 포함 여부를 반환합니다.|
    |**boolean containsAll(Collection<?> c)**|현재 컬렉션에 컬렉션 c의 모든 데이터가 포함되어있는지 여부를 반환합니다.|
    |**boolean remove(Object o)**|현재 컬렉션에서 객체 o를 삭제합니다.|
    |**boolean removeAll(Collection<?> c)**|현재 컬렉션에서 컬렉션 c와 일치하는 데이터를 삭제합니다.|
    |**boolean retainAll(Collection<?> c)**|현재 컬렉션에서 컬렉션 c와 일치하는 데이터만 남기고 나머지는 삭제합니다.|
    |**void clear( )**|현재 컬렉션의 모든 데이터를 삭제합니다.|
    |**int size( )**|현재 컬렉션에 포함된 데이터 개수를 반환합니다.|
    |**boolean isEmpty( )**|현재 컬렉션이 비어있는지 여부를 반환합니다.|
    |**Iterator<E> iterator( )**|현재 컬렉션의 모든 요소에 대한 iterator를 반환합니다.|
    |**Object[ ] toArray( )**|현재 컬렉션에 저장된 데이터를 Object 배열로 반환합니다.|
    |**<T> T[ ] toArray(T[ ] a )**|현재 컬렉션에 저장된 데이터를 배열 a에 담고 배열 a를 반환합니다.|