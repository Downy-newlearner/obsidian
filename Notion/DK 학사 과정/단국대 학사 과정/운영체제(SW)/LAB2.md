### |LAB2
05.13까지
![[DKU_OS_LAB2_Concurrent_Data_Structure.pdf]]
![[lab2.zip]]
**요구사항**
1. 락이 있는 경우 없는 경우 비교
2. 작은 크기 락, 큰 크기 락 비교
3. 스레드 개수를 다르게 해서 성능 비교
  
**실습 자료구조**
![[Source/Untitled 33.png|Untitled 33.png]]
둘 중 하나로 사용하되, BST로 사용해야 만점을 받을 수 있다.
  
coarse가 더 나쁜 성능을 보여야한다.(이게 의도니까 맞추기)
재귀함수와 lock은 궁합이 맞지 않는다. → 사용하지 않기
→ 반복문으로 만들기
  
![[Source/Untitled 1 21.png|Untitled 1 21.png]]
fine-grained lock에서
10에 접근한 스레드가 있어도 50에 접근하는 스레드는 아무런 영향을 받지 않아야한다. 그럼 락을 어떤 방식으로 걸어야하는지 고민하기
  
[[Log]]