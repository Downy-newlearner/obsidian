[[이전 시도]]
## 4차 시도
- 코드
    
    ```C++
    \#include "bst_impl.h"
    \#include <pthread.h>
    \#include <stack>
    
    void BST::insert(int key, int value)
    {
    	Node **curr = &root->right;
    	while (*curr)
    	{
    		Node *node = *curr;
    		// key 값을 가진 노드를 찾은 경우
    		if (key == node->key)
    		{
    			node->value += value;
    			node->upd_cnt++;
    			return;
    		}
    		curr = (key < node->key) ? &node->left : &node->right;
    	}
    	// key 값을 가진 노드를 찾지 못한 경우
    	*curr = new Node{key, value, 0, nullptr, nullptr};
    }
    
    int BST::lookup(int key)
    {
    	// Todo
    	Node *curr = root;
    	while (curr)
    	{
    		if (key == curr->key)
    			return curr->value;
    		curr = (key < curr->key) ? curr->left : curr->right;
    	}
    	return 0; // 키를 찾지 못한 경우
    }
    
    void BST::remove(int key)
    {
    	Node **curr = &root, *nodeToDelete;
    	Node *prev = nullptr;
    
    	while (*curr)
    	{
    		Node *node = *curr;
    
    		if (key == node->key)
    		{
    			if (!node->left && !node->right)
    			{ // 자식이 없는 경우
    				nodeToDelete = *curr;
    				*curr = nullptr;
    			}
    			else if (node->left && !node->right)
    			{ // 왼쪽 자식만 있는 경우
    				nodeToDelete = *curr;
    				*curr = node->left;
    			}
    			else if (!node->left && node->right)
    			{ // 오른쪽 자식만 있는 경우
    				nodeToDelete = *curr;
    				*curr = node->right;
    			}
    			else
    			{ // 두 자식이 모두 있는 경우
    				Node **succ = &node->right;
    				while ((*succ)->left)
    				{
    					succ = &((*succ)->left);
    				}
    				// 후속자의 값을 현재 노드에 복사
    				node->key = (*succ)->key;
    				node->value = (*succ)->value;
    				node->upd_cnt = (*succ)->upd_cnt;
    
    				nodeToDelete = *succ;
    				*succ = (*succ)->right; // 후속자의 오른쪽 자식을 후속자의 부모와 연결
    			}
    			delete nodeToDelete; // 노드 삭제
    			return;
    		}
    
    		prev = node;
    
    		if (key < node->key)
    		{
    			curr = &node->left;
    		}
    		else
    		{
    			curr = &node->right;
    		}
    	}
    }
    
    void BST::inOrderTraversal(Node *node, KVC *arr, int &index)
    {
    	std::stack<Node *> stack;
    	Node *current = node;
    
    	while (!stack.empty() || current != nullptr)
    	{
    		// 현재 노드에서 가장 왼쪽 노드로 이동
    		while (current != nullptr)
    		{
    			stack.push(current);
    			current = current->left;
    		}
    
    		// 현재 노드는 스택의 최상위 노드
    		current = stack.top();
    		stack.pop();
    
    		// 방문 처리: 여기서는 배열에 현재 노드의 정보를 저장
    		arr[index++] = {current->key, current->value, current->upd_cnt};
    
    		// 오른쪽 서브트리로 이동
    		current = current->right;
    	}
    }
    
    void BST::traversal(KVC *arr)
    {
    	int index = 0;
    	inOrderTraversal(root->right, arr, index);
    }
    
    void CoarseBST::insert(int key, int value)
    {
    	pthread_mutex_lock(&mutex_lock);
    	Node **curr = &root->right;
    	while (*curr)
    	{
    		Node *node = *curr;
    		// key 값을 가진 노드를 찾은 경우
    		if (key == node->key)
    		{
    			node->value += value;
    			node->upd_cnt++;
    			pthread_mutex_unlock(&mutex_lock);
    			return;
    		}
    		curr = (key < node->key) ? &node->left : &node->right;
    	}
    	// key 값을 가진 노드를 찾지 못한 경우
    	*curr = new Node{key, value, 0, nullptr, nullptr};
    	pthread_mutex_unlock(&mutex_lock);
    }
    
    int CoarseBST::lookup(int key)
    {
    	pthread_mutex_lock(&mutex_lock);
    
    	Node *curr = root;
    	while (curr)
    	{
    		if (key == curr->key)
    		{
    			pthread_mutex_unlock(&mutex_lock);
    			return curr->value;
    		}
    
    		curr = (key < curr->key) ? curr->left : curr->right;
    	}
    	pthread_mutex_unlock(&mutex_lock);
    	return 0; // 키를 찾지 못한 경우
    }
    
    void CoarseBST::remove(int key)
    {
    	pthread_mutex_lock(&mutex_lock);
    	Node **curr = &root, *nodeToDelete;
    	Node *prev = nullptr;
    
    	while (*curr)
    	{
    		Node *node = *curr;
    
    		if (key == node->key)
    		{
    			if (!node->left && !node->right)
    			{ // 자식이 없는 경우
    				nodeToDelete = *curr;
    				*curr = nullptr;
    			}
    			else if (node->left && !node->right)
    			{ // 왼쪽 자식만 있는 경우
    				nodeToDelete = *curr;
    				*curr = node->left;
    			}
    			else if (!node->left && node->right)
    			{ // 오른쪽 자식만 있는 경우
    				nodeToDelete = *curr;
    				*curr = node->right;
    			}
    			else
    			{ // 두 자식이 모두 있는 경우
    				Node **succ = &node->right;
    				while ((*succ)->left)
    				{
    					succ = &((*succ)->left);
    				}
    				// 후속자의 값을 현재 노드에 복사
    				node->key = (*succ)->key;
    				node->value = (*succ)->value;
    				node->upd_cnt = (*succ)->upd_cnt;
    
    				nodeToDelete = *succ;
    				*succ = (*succ)->right; // 후속자의 오른쪽 자식을 후속자의 부모와 연결
    			}
    			delete nodeToDelete; // 노드 삭제
    			pthread_mutex_unlock(&mutex_lock);
    			return;
    		}
    
    		prev = node;
    
    		if (key < node->key)
    		{
    			curr = &node->left;
    		}
    		else
    		{
    			curr = &node->right;
    		}
    	}
    	pthread_mutex_unlock(&mutex_lock);
    }
    
    void CoarseBST::inOrderTraversal(Node *node, KVC *arr, int &index)
    {
    
    	std::stack<Node *> stack;
    	Node *current = node;
    
    	while (!stack.empty() || current != nullptr)
    	{
    		// 현재 노드에서 가장 왼쪽 노드로 이동
    		while (current != nullptr)
    		{
    			stack.push(current);
    			current = current->left;
    		}
    
    		// 현재 노드는 스택의 최상위 노드
    		current = stack.top();
    		stack.pop();
    
    		// 방문 처리: 여기서는 배열에 현재 노드의 정보를 저장
    		arr[index++] = {current->key, current->value, current->upd_cnt};
    
    		// 오른쪽 서브트리로 이동
    		current = current->right;
    	}
    }
    
    void CoarseBST::traversal(KVC *traverse_arr)
    {
    	pthread_mutex_lock(&mutex_lock);
    	int index = 0;
    	inOrderTraversal(root->right, traverse_arr, index);
    	pthread_mutex_unlock(&mutex_lock);
    }
    
    void FineBST::insert(int key, int value)
    {
    	// Todo
    }
    
    int FineBST::lookup(int key)
    {
    	// Todo
    	return 0;
    }
    
    void FineBST::remove(int key)
    {
    	// Todo
    }
    
    void FineBST::traversal(KVC *traverse_arr)
    {
    	// Todo
    }
    ```
    
- 채점
    
    - [x] BstSingleThreadTest.Single/0
    - [x] BstSingleThreadTest.Single/1
    - [x] BstSingleThreadTest.Single/2
    
      
    
    - [x] BstSingleThreadTest.Coarse/0
    - [x] BstSingleThreadTest.Coarse/1
    - [x] BstSingleThreadTest.Coarse/2
    
      
    
    - [x] BstSingleThreadTest.Fine/0
    - [x] BstSingleThreadTest.Fine/1
    - [x] BstSingleThreadTest.Fine/2
    
    ---
    
    - [x] BstMultiThreadTest.Coarse/0
    - [x] BstMultiThreadTest.Coarse/1
    - [x] BstMultiThreadTest.Coarse/2
    - [x] BstMultiThreadTest.Coarse/3
    - [x] BstMultiThreadTest.Coarse/4
    - [x] BstMultiThreadTest.Coarse/5
    - [x] BstMultiThreadTest.Coarse/6
    - [x] BstMultiThreadTest.Coarse/7
    - [x] BstMultiThreadTest.Coarse/8
    
    ---
    
    - [ ] BstMultiThreadTest.Fine/0
    - [ ] BstMultiThreadTest.Fine/1
    - [ ] BstMultiThreadTest.Fine/2
    - [ ] BstMultiThreadTest.Fine/3
    - [ ] BstMultiThreadTest.Fine/4
    - [ ] BstMultiThreadTest.Fine/5
    - [x] BstMultiThreadTest.Fine/6
    - [x] BstMultiThreadTest.Fine/7
    - [x] BstMultiThreadTest.Fine/8
    
      
    
## Fine insert 이전 22:00
```C++
void FineBST::insert(int key, int value)
{
	FineNode *curr = root->right;
	while (curr)
	{
		FineNode *node = curr;
		pthread_mutex_lock(&node->mutex_lock);
		// key 값을 가진 노드를 찾은 경우
		if (key == node->key)
		{
			node->value += value;
			node->upd_cnt++;
			pthread_mutex_unlock(&node->mutex_lock);
			return;
		}
		curr = (key < node->key) ? node->left : node->right;
		pthread_mutex_unlock(&node->mutex_lock);
	}
	// key 값을 가진 노드를 찾지 못한 경우
	FineNode *temp;
	temp->key = key;
	temp->value = value;
	temp->upd_cnt = 0;
	temp->left = nullptr;
	temp->right = nullptr;
	curr = temp;
	std::ios::sync_with_stdio(false);
	std::cout.tie(NULL);
	std::cout << curr->value << ", " << curr->upd_cnt << '\n';
}
```
  
Single Fine2에서 오류가 발생한다
Fine remove 코드를 읽어보니 코드를 최적화 할 수 있을 것 같다.
Coarse remove부터 최적화하고 Fine으로 가져와 Fine락을 걸자
  
Multi Coarse0에서 malloc(): corrupted top size Aborted (core dumped)가 발생한다.
Coarse insert를 다시 확인해보자.
  
## Coarse 코드 뒤집기
이전 coarse-insert 코드 05.14 16:31
```C++
void CoarseBST::insert(int key, int value)
{
	pthread_mutex_lock(&mutex_lock);
	// 1. 필요한 변수 선언
	Node **curr = &root->right;
	// 2. key 값을 가진 노드를 찾을 때까지 while문 반복
	while (*curr)
	{
		Node *node = *curr;
		// 2.1 key 값을 가진 노드를 찾은 경우
		if (key == node->key)
		{
			node->value += value;
			node->upd_cnt++;
			pthread_mutex_unlock(&mutex_lock);
			return;
		}
		// 2.2 현재 curr의 key 값이 찾는 key 값과 달라 다음 노드로 넘어가기
		curr = (key < node->key) ? &node->left : &node->right;
	}
	// 3. key 값을 가진 노드를 찾지 못한 경우
	*curr = new Node{key, value, 0, nullptr, nullptr};
	pthread_mutex_unlock(&mutex_lock);
}
```
  
### Fine remove 이전 코드
```C++
void FineBST::remove(int key)
{
	FineNode *curr = root, *nodeToDelete;
	FineNode *prev = nullptr;
	pthread_mutex_lock(&curr->mutex_lock);
	while (curr)
	{
		FineNode *node = curr;
		pthread_mutex_lock(&node->mutex_lock);
		// 삭제할 노드를 찾음
		if (key == node->key)
		{
			if (!node->left && !node->right)
			{ // 자식이 없는 경우
				nodeToDelete = curr;
				curr = nullptr;
			}
			else if (node->left && !node->right)
			{ // 왼쪽 자식만 있는 경우
				nodeToDelete = curr;
				curr = node->left;
			}
			else if (!node->left && node->right)
			{ // 오른쪽 자식만 있는 경우
				nodeToDelete = curr;
				curr = node->right;
			}
			else
			{ // 두 자식이 모두 있는 경우
				FineNode *succ = node->right;
				while (succ->left)
				{
					succ = succ->left;
				}
				// 후속자의 값을 현재 노드에 복사
				node->key = succ->key;
				node->value = succ->value;
				node->upd_cnt = succ->upd_cnt;
				nodeToDelete = succ;
				succ = succ->right; // 후속자의 오른쪽 자식을 후속자의 부모와 연결
			}
			delete nodeToDelete; // 노드 삭제
			return;
		}
		prev = node;
		if (key < node->key)
		{
			curr = node->left;
		}
		else
		{
			curr = node->right;
		}
	}
}
```
  
고려해야하는 remove 경우의 수
찾는 노드 = r라면 이름 앞에 r을 붙인다.
  
1. 삭제 노드가 자식 없는 경우
2. r삭제 노드가 자식 없는 경우
3. 삭제 노드가 왼 자식만 있는 경우
4. r삭제 노드가 왼 자식만 있는 경우
5. 삭제 노드가 오른 자식만 있는 경우
6. r삭제 노드가 오른 자식만 있는 경우
7. 삭제 노드가 두 자식이 있는 경우
8. r삭제 노드가 두 자식이 있는 경우
### fine remove 수정 전
```C++
void FineBST::remove(int key)
{
	//
	FineNode *curr = root->right, *nodeToDelete;
	FineNode *prev = root, *temp;
	// 삭제 노드 찾기
	pthread_mutex_lock(&prev->mutex_lock);
	pthread_mutex_lock(&curr->mutex_lock);
	while (curr)
	{
		if (key < curr->key)
		{
			temp = prev;
			prev = curr;
			curr = curr->left;
			if (curr != nullptr)
				pthread_mutex_lock(&curr->mutex_lock);
			pthread_mutex_unlock(&temp->mutex_lock);
		}
		else if (key > curr->key)
		{
			temp = prev;
			prev = curr;
			curr = curr->right;
			if (curr != nullptr)
				pthread_mutex_lock(&curr->mutex_lock);
			pthread_mutex_unlock(&temp->mutex_lock);
		}
		else if (key == curr->key)
		{
			break;
		}
	}
	// curr과 prev에 락이 걸린 상태로 다음 작업권을 넘겨받는다.
	while (curr)
	{
		FineNode *node = curr;
		if (!node->left && !node->right)
		{ // 자식이 없는 경우
			
			nodeToDelete = curr;
			curr = nullptr;
		}
		else if (node->left && !node->right)
		{ // 왼쪽 자식만 있는 경우
			nodeToDelete = curr;
			curr = node->left;
		}
		else if (!node->left && node->right)
		{ // 오른쪽 자식만 있는 경우
			nodeToDelete = curr;
			curr = node->right;
		}
		else
		{ // 두 자식이 모두 있는 경우
			FineNode **succ = &node->right;
			while ((*succ)->left)
			{
				succ = &((*succ)->left);
			}
			// 후속자의 값을 현재 노드에 복사
			node->key = (*succ)->key;
			node->value = (*succ)->value;
			node->upd_cnt = (*succ)->upd_cnt;
			nodeToDelete = *succ;
			*succ = (*succ)->right; // 후속자의 오른쪽 자식을 후속자의 부모와 연결
		}
		delete nodeToDelete; // 노드 삭제
		pthread_mutex_unlock(&curr->mutex_lock);
		pthread_mutex_unlock(&prev->mutex_lock);
		return;
		// prev = node;
		// if (key < node->key)
		// {
		// 	curr = &node->left;
		// }
		// else
		// {
		// 	curr = &node->right;
		// }
	}
}
```
  
## 코드 중간 저장
```C++
\#include "bst_impl.h"
\#include <pthread.h>
\#include <stack>
\#include <iostream>
void BST::insert(int key, int value)
{
	Node **curr = &root->right;
	while (*curr)
	{
		Node *node = *curr;
		// key 값을 가진 노드를 찾은 경우
		if (key == node->key)
		{
			node->value += value;
			node->upd_cnt++;
			return;
		}
		curr = (key < node->key) ? &node->left : &node->right;
	}
	// key 값을 가진 노드를 찾지 못한 경우
	*curr = new Node{key, value, 0, nullptr, nullptr};
}
int BST::lookup(int key)
{
	// Todo
	Node *curr = root;
	while (curr)
	{
		if (key == curr->key)
			return curr->value;
		curr = (key < curr->key) ? curr->left : curr->right;
	}
	return 0; // 키를 찾지 못한 경우
}
void BST::remove(int key)
{
	Node **curr = &root, *nodeToDelete;
	Node *prev = nullptr;
	while (*curr)
	{
		Node *node = *curr;
		if (key == node->key)
		{
			if (!node->left && !node->right)
			{ // 자식이 없는 경우
				nodeToDelete = *curr;
				*curr = nullptr;
			}
			else if (node->left && !node->right)
			{ // 왼쪽 자식만 있는 경우
				nodeToDelete = *curr;
				*curr = node->left;
			}
			else if (!node->left && node->right)
			{ // 오른쪽 자식만 있는 경우
				nodeToDelete = *curr;
				*curr = node->right;
			}
			else
			{ // 두 자식이 모두 있는 경우
				Node **succ = &node->right;
				while ((*succ)->left)
				{
					succ = &((*succ)->left);
				}
				// 후속자의 값을 현재 노드에 복사
				node->key = (*succ)->key;
				node->value = (*succ)->value;
				node->upd_cnt = (*succ)->upd_cnt;
				nodeToDelete = *succ;
				*succ = (*succ)->right; // 후속자의 오른쪽 자식을 후속자의 부모와 연결
			}
			delete nodeToDelete; // 노드 삭제
			return;
		}
		prev = node;
		if (key < node->key)
		{
			curr = &node->left;
		}
		else
		{
			curr = &node->right;
		}
	}
}
void BST::inOrderTraversal(Node *node, KVC *arr, int &index)
{
	std::stack<Node *> stack;
	Node *current = node;
	while (!stack.empty() || current != nullptr)
	{
		// 현재 노드에서 가장 왼쪽 노드로 이동
		while (current != nullptr)
		{
			stack.push(current);
			current = current->left;
		}
		// 현재 노드는 스택의 최상위 노드
		current = stack.top();
		stack.pop();
		// 방문 처리: 여기서는 배열에 현재 노드의 정보를 저장
		arr[index++] = {current->key, current->value, current->upd_cnt};
		// 오른쪽 서브트리로 이동
		current = current->right;
	}
}
void BST::traversal(KVC *arr)
{
	int index = 0;
	inOrderTraversal(root->right, arr, index);
}
void CoarseBST::insert(int key, int value)
{
	pthread_mutex_lock(&mutex_lock);
	// 1. 필요한 변수 선언
	Node **curr = &root->right;
	// 2. key 값을 가진 노드를 찾을 때까지 while문 반복
	while (*curr)
	{
		Node *node = *curr;
		// 2.1 key 값을 가진 노드를 찾은 경우
		if (key == node->key)
		{
			node->value += value;
			node->upd_cnt++;
			pthread_mutex_unlock(&mutex_lock);
			return;
		}
		// 2.2 현재 curr의 key 값이 찾는 key 값과 달라 다음 노드로 넘어가기
		curr = (key < node->key) ? &node->left : &node->right;
	}
	// 3. key 값을 가진 노드를 찾지 못한 경우
	*curr = new Node{key, value, 0, nullptr, nullptr};
	pthread_mutex_unlock(&mutex_lock);
}
int CoarseBST::lookup(int key)
{
	pthread_mutex_lock(&mutex_lock);
	Node *curr = root;
	while (curr)
	{
		if (key == curr->key)
		{
			pthread_mutex_unlock(&mutex_lock);
			return curr->value;
		}
		curr = (key < curr->key) ? curr->left : curr->right;
	}
	pthread_mutex_unlock(&mutex_lock);
	return 0; // 키를 찾지 못한 경우
}
void CoarseBST::remove(int key)
{
	//
	pthread_mutex_lock(&mutex_lock);
	Node **curr = &root, *nodeToDelete;
	Node *prev = nullptr;
	
	while (*curr)
	{
		Node *node = *curr;
		if (key == node->key)
		{
			if (!node->left && !node->right)
			{ // 자식이 없는 경우
				nodeToDelete = *curr;
				*curr = nullptr;
			}
			else if (node->left && !node->right)
			{ // 왼쪽 자식만 있는 경우
				nodeToDelete = *curr;
				*curr = node->left;
			}
			else if (!node->left && node->right)
			{ // 오른쪽 자식만 있는 경우
				nodeToDelete = *curr;
				*curr = node->right;
			}
			else
			{ // 두 자식이 모두 있는 경우
				Node **succ = &node->right;
				while ((*succ)->left)
				{
					succ = &((*succ)->left);
				}
				// 후속자의 값을 현재 노드에 복사
				node->key = (*succ)->key;
				node->value = (*succ)->value;
				node->upd_cnt = (*succ)->upd_cnt;
				nodeToDelete = *succ;
				*succ = (*succ)->right; // 후속자의 오른쪽 자식을 후속자의 부모와 연결
			}
			delete nodeToDelete; // 노드 삭제
			pthread_mutex_unlock(&mutex_lock);
			return;
		}
		prev = node;
		if (key < node->key)
		{
			curr = &node->left;
		}
		else
		{
			curr = &node->right;
		}
	}
	pthread_mutex_unlock(&mutex_lock);
}
void CoarseBST::inOrderTraversal(Node *node, KVC *arr, int &index)
{
	std::stack<Node *> stack;
	Node *current = node;
	while (!stack.empty() || current != nullptr)
	{
		// 현재 노드에서 가장 왼쪽 노드로 이동
		while (current != nullptr)
		{
			stack.push(current);
			current = current->left;
		}
		// 현재 노드는 스택의 최상위 노드
		current = stack.top();
		stack.pop();
		// 방문 처리: 여기서는 배열에 현재 노드의 정보를 저장
		arr[index++] = {current->key, current->value, current->upd_cnt};
		// 오른쪽 서브트리로 이동
		current = current->right;
	}
}
void CoarseBST::traversal(KVC *traverse_arr)
{
	int index = 0;
	inOrderTraversal(root->right, traverse_arr, index);
}
void FineBST::insert(int key, int value)
{
	FineNode *prev = root;
	FineNode *curr = root->right;
	pthread_mutex_lock(&prev->mutex_lock);
	if (curr != nullptr)
		pthread_mutex_lock(&curr->mutex_lock);
	while (curr)
	{
		if (key == curr->key)
		{
			curr->value += value;
			curr->upd_cnt++;
			pthread_mutex_unlock(&curr->mutex_lock);
			pthread_mutex_unlock(&prev->mutex_lock);
			return;
		}
		pthread_mutex_unlock(&prev->mutex_lock);
		prev = curr;
		curr = (key < curr->key) ? curr->left : curr->right;
		if (curr != nullptr)
			pthread_mutex_lock(&curr->mutex_lock);
	}
	// 주어진 key 값을 가진 노드를 찾지 못했을 때, 새 노드를 동적 할당하여 삽입힌다.
	FineNode *newNode = new FineNode(key, value);
	if (key < prev->key)
		prev->left = newNode;
	else
		prev->right = newNode;
	pthread_mutex_unlock(&prev->mutex_lock); // Don't forget to unlock the last locked mutex
}
int FineBST::lookup(int key)
{
	FineNode *curr = root->right;
	if (curr == nullptr)
		return 0;
	pthread_mutex_lock(&curr->mutex_lock);
	while (curr)
	{
		if (key == curr->key)
		{
			int retVal = curr->value;
			pthread_mutex_unlock(&curr->mutex_lock);
			return retVal;
		}
		FineNode *next = (key < curr->key) ? curr->left : curr->right;
		if (next != nullptr)
			pthread_mutex_lock(&next->mutex_lock);
		pthread_mutex_unlock(&curr->mutex_lock);
		curr = next;
	}
	return 0;
}
// void FineBST::remove(int key)
// {
// 	// 1. 필요한 변수 선언: curr, nodeToDelete, prev
// 	// 현재 노드 -> curr, 삭제할 노드 -> nodeToe Delete, 이전 노드(부모) -> prev
// 	FineNode *curr = root, *nodeToDelete;
// 	FineNode *prev = nullptr; // 만약 루트노드의 key가 찾는 key였다면 prev는 nullptr이다.
// 	// 2. key값이 일치하는, 즉 삭제할 노드를 찾을 때까지 탐색하고 찾으면 노드를 삭제한다.
// 	while (curr)
// 	{
// 		// curr을 node에 담고 한 루프 동안 curr이 아닌 node 변수를 사용한다.
// 		// 이렇게 함으로써
// 		// node에 락 -> 다음 노드로 옮겨가면서 새로 락 -> 이전 node 언락
// 		// node 찾았다면 -> 삭제 ->
// 		// 삭제의 동작이 끝난다면 트리에서 node에 걸어놓은 락 때문에 동작을 방해받을 일이 없다.
// 		FineNode *node = curr;
// 		pthread_mutex_lock(&node->mutex_lock);
// 		// FineNode *node = curr;
// 		// 삭제할 노드를 찾음
// 		if (key == node->key)
// 		{
// 			if (!node->left && !node->right)
// 			{ // 자식이 없는 경우
// 				// 부모가 nullptr(node가 루트노드)인 경우
// 				nodeToDelete = node;
// 				node = nullptr;
// 				delete nodeToDelete; // 노드 삭제
// 				pthread_mutex_unlock(&node->mutex_lock);
// 				return;
// 			}
// 			else if (node->left && !node->right)
// 			{ // 왼쪽 자식만 있는 경우
// 				nodeToDelete = node;
// 				node = node->left;
// 				delete nodeToDelete; // 노드 삭제
// 				pthread_mutex_unlock(&node->mutex_lock);
// 				return;
// 			}
// 			else if (!node->left && node->right)
// 			{ // 오른쪽 자식만 있는 경우
// 				nodeToDelete = node;
// 				node = node->right;
// 				delete nodeToDelete; // 노드 삭제
// 				pthread_mutex_unlock(&node->mutex_lock);
// 				return;
// 			}
// 			else
// 			{ // 두 자식이 모두 있는 경우
// 				FineNode *succ = node->right;
// 				pthread_mutex_lock(&succ->mutex_lock);
// 				while (succ->left)
// 				{
// 					pthread_mutex_unlock(&succ->mutex_lock);
// 					succ = succ->left;
// 					pthread_mutex_lock(&succ->mutex_lock);
// 				}
// 				// 후속자의 값을 현재 노드에 복사
// 				node->key = succ->key;
// 				node->value = succ->value;
// 				node->upd_cnt = succ->upd_cnt;
// 				nodeToDelete = succ;
// 				succ = succ->right;	 // 후속자의 오른쪽 자식을 후속자의 부모와 연결
// 				delete nodeToDelete; // 노드 삭제
// 				pthread_mutex_unlock(&node->mutex_lock);
// 				return;
// 			}
// 		}
// 		// 다음 노드를
// 		prev = node;
// 		if (key < node->key)
// 		{
// 			curr = node->left;
// 			pthread_mutex_unlock(&node->mutex_lock);
// 		}
// 		else
// 		{
// 			curr = node->right;
// 			pthread_mutex_unlock(&node->mutex_lock);
// 		}
// 	}
// }
void FineBST::remove(int key)
{
	FineNode *curr = root->right;
	FineNode *prev = root;
	FineNode *temp, *nodeToDelete;
	pthread_mutex_lock(&prev->mutex_lock);
	if (curr != nullptr)
		pthread_mutex_lock(&curr->mutex_lock);
	// 삭제 노드 찾기
	while (curr)
	{
		if (key < curr->key)
		{
			temp = prev;
			prev = curr;
			curr = curr->left;
			// 삭제할 노드가 존재하지 않음.
			if (curr == nullptr)
			{
				pthread_mutex_unlock(&temp->mutex_lock);
				pthread_mutex_unlock(&prev->mutex_lock);
				return;
			}
			pthread_mutex_lock(&curr->mutex_lock);
			pthread_mutex_unlock(&temp->mutex_lock);
		}
		else if (key > curr->key)
		{
			temp = prev;
			prev = curr;
			curr = curr->right;
			// 삭제할 노드가 존재하지 않음.
			if (curr == nullptr)
			{
				pthread_mutex_unlock(&temp->mutex_lock);
				pthread_mutex_unlock(&prev->mutex_lock);
				return;
			}
			pthread_mutex_lock(&curr->mutex_lock);
			pthread_mutex_unlock(&temp->mutex_lock);
		}
		else if (key == curr->key)
		{
			break;
		}
	}
	// curr과 prev에 락이 걸린 상태로 다음 작업권을 넘겨받는다.
	if (curr)
	{
		FineNode *node = curr;
		if (!node->left && !node->right)
		{ // 자식이 없는 경우
			if (prev->left == node)
			{
				prev->left = nullptr;
			}
			else
			{
				prev->right = nullptr;
			}
			nodeToDelete = node;
			pthread_mutex_unlock(&node->mutex_lock);
		}
		else if (node->left && !node->right)
		{ // 왼쪽 자식만 있는 경우
			if (prev->left == node)
			{
				prev->left = node->left;
			}
			else
			{
				prev->right = node->left;
			}
			nodeToDelete = node;
			pthread_mutex_unlock(&node->mutex_lock);
		}
		else if (!node->left && node->right)
		{ // 오른쪽 자식만 있는 경우
			if (prev->left == node)
			{
				prev->left = node->right;
			}
			else
			{
				prev->right = node->right;
			}
			nodeToDelete = node;
			pthread_mutex_unlock(&node->mutex_lock);
		}
		else
		{ // 두 자식이 모두 있는 경우
			FineNode *succ = node->right, *temp;
			pthread_mutex_lock(&succ->mutex_lock);
			while (succ->left)
			{
				temp = succ->left;
				pthread_mutex_lock(&temp->mutex_lock);
				pthread_mutex_unlock(&succ->mutex_lock);
				succ = temp;
			}
			// while문을 마치면 succ(계승노드)와 prev, curr이 lock 상태이다.
			// 후속자의 값을 현재 노드에 복사
			node->key = succ->key;
			node->value = succ->value;
			node->upd_cnt = succ->upd_cnt;
			nodeToDelete = succ;
			succ = succ->right; // 후속자의 오른쪽 자식을 후속자의 부모와 연결
			pthread_mutex_unlock(&succ->mutex_lock);
		}
		pthread_mutex_unlock(&node->mutex_lock);
		delete nodeToDelete; // 노드 삭제
		pthread_mutex_unlock(&prev->mutex_lock);
		return;
	}
	if (curr != nullptr)
		pthread_mutex_unlock(&curr->mutex_lock);
	pthread_mutex_unlock(&prev->mutex_lock);
	return;
}
void FineBST::inOrderTraversal(FineNode *node, KVC *arr, int &index)
{
	std::stack<FineNode *> stack;
	FineNode *current = node;
	while (!stack.empty() || current != nullptr)
	{
		// 현재 노드에서 가장 왼쪽 노드로 이동
		while (current != nullptr)
		{
			stack.push(current);
			current = current->left;
		}
		// 현재 노드는 스택의 최상위 노드
		current = stack.top();
		stack.pop();
		// 방문 처리: 여기서는 배열에 현재 노드의 정보를 저장
		arr[index++] = {current->key, current->value, current->upd_cnt};
		// 오른쪽 서브트리로 이동
		current = current->right;
	}
}
void FineBST::traversal(KVC *traverse_arr)
{
	// Todo
	int index = 0;
	inOrderTraversal(root->right, traverse_arr, index);
}
```
  
  
```C++
void FineBST::remove(int key)
{
	FineNode **curr = &root->right;
	FineNode *prev = nullptr;
	FineNode *temp, *nodeToDelete;
	pthread_mutex_lock(&prev->mutex_lock);
	if (curr != nullptr)
		pthread_mutex_lock(&(*curr)->mutex_lock);
	// 삭제 노드 찾기
	while (curr)
	{
		FineNode *node = *curr;
		if (key < node->key)
		{
			temp = prev;
			prev = node;
			curr = node->left;
			node = curr;
			// 삭제할 노드가 존재하지 않음.
			if (node == nullptr)
			{
				pthread_mutex_unlock(&temp->mutex_lock);
				pthread_mutex_unlock(&prev->mutex_lock);
				return;
			}
			pthread_mutex_lock(&curr->mutex_lock);
			pthread_mutex_unlock(&temp->mutex_lock);
		}
		else if (key > node->key)
		{
			temp = prev;
			prev = node;
			curr = node->right;
			node = curr;
			// 삭제할 노드가 존재하지 않음.
			if (node == nullptr)
			{
				pthread_mutex_unlock(&temp->mutex_lock);
				pthread_mutex_unlock(&prev->mutex_lock);
				return;
			}
			pthread_mutex_lock(&curr->mutex_lock);
			pthread_mutex_unlock(&temp->mutex_lock);
		}
		else if (key == node->key)
		{
			break;
		}
	}
	// curr과 prev에 락이 걸린 상태로 다음 작업권을 넘겨받는다.
	if (curr)
	{
		FineNode *node = curr;
		if (!node->left && !node->right)
		{ // 자식이 없는 경우
			if (prev->left == node)
			{
				prev->left = nullptr;
			}
			else
			{
				prev->right = nullptr;
			}
			nodeToDelete = node;
			// pthread_mutex_unlock(&node->mutex_lock);
		}
		else if (node->left && !node->right)
		{ // 왼쪽 자식만 있는 경우
			if (prev->left == node)
			{
				prev->left = node->left;
			}
			else
			{
				prev->right = node->left;
			}
			nodeToDelete = node;
			// pthread_mutex_unlock(&node->mutex_lock);
		}
		else if (!node->left && node->right)
		{ // 오른쪽 자식만 있는 경우
			if (prev->left == node)
			{
				prev->left = node->right;
			}
			else
			{
				prev->right = node->right;
			}
			nodeToDelete = node;
			// pthread_mutex_unlock(&node->mutex_lock);
		}
		else
		{ // 두 자식이 모두 있는 경우
			FineNode *succ = node->right, *next, *local_prev;
			pthread_mutex_lock(&succ->mutex_lock);
			while (succ->left)
			{
				next = succ->left;
				//'succ->left != nullptr'을 조건으로 하는 while문 안에서는 next는 항상 nullptr이 아니다.
				pthread_mutex_lock(&next->mutex_lock);
				if (next->left != nullptr)
					pthread_mutex_unlock(&succ->mutex_lock);
				local_prev = succ;
				succ = next;
				pthread_mutex_unlock(&local_prev->mutex_lock);
			}
			// while문을 마치면 succ(계승노드)와 local_prev, curr이 lock 상태이다.
			// 후속자의 값을 현재 노드에 복사
			node->key = succ->key;
			node->value = succ->value;
			node->upd_cnt = succ->upd_cnt;
			nodeToDelete = succ;
			// if (succ->right != nullptr)
			// 	local_prev->left = succ->right; // 후속자의 오른쪽 자식을 후속자의 부모와 연결
			pthread_mutex_unlock(&nodeToDelete->mutex_lock);
		}
		pthread_mutex_unlock(&node->mutex_lock);
		// delete nodeToDelete; // 노드 삭제
		pthread_mutex_unlock(&prev->mutex_lock);
		return;
	}
	pthread_mutex_unlock(&prev->mutex_lock);
	if (curr != nullptr)
		pthread_mutex_unlock(&curr->mutex_lock);
	return;
}
```