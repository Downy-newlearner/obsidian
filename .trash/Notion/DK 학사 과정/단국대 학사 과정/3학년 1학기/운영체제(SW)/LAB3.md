[[시도]]
[[배운점]]
파일시스템 만들어야함
스토리지 필요
스토리지는
1. 메모리 중에 일부를 디스크처럼 보이게 하는 ramdisk 소프트웨어를 사용
2. ram disk 위에 파일시스템 만들고 마운트해서 접근가능하게 만들기
3. 조교가 만든 스크립트를 실행할 수 있도록 한다.
    1. 디렉토리, 파일을 만들면 나에게 할당
4. 나에게 할당된 디스크 블록 번호를 찾는 것이 과제이다.
5. 루트디렉토리 → 아이노드 → 데이터 정보 → 내 디렉토리 접근 → 내가 찾는 파일 접근 → 그 파일의 아이노드 찾기 → 블록 번호 찾기
  
보고서만 제출하면 된다.
6월 6일 수요일까지
  
보너스
리눅스 OS를 수정하는 작업
리눅스에는 모듈이 있는데, 모듈을 만들면 커널로 들어가서 동작한다.
Ext2 소스코드를 받으면 특정위치에다 내 이름,학번 집어넣고, 모듈 마운트.