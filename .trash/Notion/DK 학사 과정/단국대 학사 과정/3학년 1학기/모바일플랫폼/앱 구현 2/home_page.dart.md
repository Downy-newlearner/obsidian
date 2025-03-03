아이콘 크기를 5배로 키우고, 패딩을 60으로 설정한 코드를 제공해드리겠습니다. 아래에서 `Icon` 위젯의 `size` 속성을 사용하여 아이콘 크기를 키우고, 패딩을 변경할 수 있습니다.
```Dart
// home_page.dart
import 'package:flutter/material.dart';
import 'store_search_page.dart';
import 'store_register_page.dart';
class HomePage extends StatefulWidget {
  const HomePage({super.key});
  @override
  _HomePageState createState() => _HomePageState();
}
class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: false,
        title: Row(
          children: [
            const CircleAvatar(
              backgroundImage: AssetImage(
                  'assets/images/default_profile.jpeg'), // 프로필 이미지 경로
            ),
            const SizedBox(width: 10),
            const Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text("정다훈"),
                Text("미식가", style: TextStyle(fontSize: 12)),
              ],
            ),
            const Spacer(),
            IconButton(
              icon: const Icon(Icons.notifications),
              onPressed: () {
                // 아무 기능도 없음
              },
            ),
          ],
        ),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            const Padding(
              padding: EdgeInsets.all(16.0),
              child: TextField(
                decoration: InputDecoration(
                  prefixIcon: Icon(Icons.search),
                  hintText: "지금 생각나는 음식이 있나요?",
                  border: OutlineInputBorder(),
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                children: [
                  ElevatedButton(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => const StoreSearchPage(),
                        ),
                      );
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.purple,
                      padding: const EdgeInsets.symmetric(vertical: 60), // 패딩 60
                    ),
                    child: const Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Padding(
                          padding: EdgeInsets.only(left: 10),
                          child: Text(
                            "매장 찾기",
                            style: TextStyle(color: Colors.white, fontSize: 30),
                            textAlign: TextAlign.left,
                          ),
                        ),
                        Icon(
                          Icons.map,
                          color: Colors.white,
                          size: 120, // 기본 크기의 5배
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 10),
                  ElevatedButton(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => const StoreRegisterPage(),
                        ),
                      );
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.purple,
                      padding: const EdgeInsets.symmetric(vertical: 60), // 패딩 60
                    ),
                    child: const Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Icon(
                          Icons.store,
                          color: Colors.white,
                          size: 120, // 기본 크기의 5배
                        ),
                        Padding(
                          padding: EdgeInsets.only(right: 10),
                          child: Text(
                            "매장 등록",
                            style: TextStyle(color: Colors.white, fontSize: 30),
                            textAlign: TextAlign.right,
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      const Text("우리 동네 이벤트",
                          style: TextStyle(
                              fontSize: 18, fontWeight: FontWeight.bold)),
                      TextButton(
                        onPressed: () {
                          // 아무 기능도 없음
                        },
                        child: const Text("view more"),
                      ),
                    ],
                  ),
                  _buildEventList(),
                ],
              ),
            ),
          ],
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: "Home",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: "My Info",
          ),
        ],
        currentIndex: 0,
        onTap: (index) {
          if (index == 0) {
            // HomePage로 이동하는 코드가 이미 있음
          } else if (index == 1) {
            // My Info 페이지로 이동하는 코드를 추가해야 함
          }
        },
      ),
    );
  }
  Widget _buildEventList() {
    return Column(
      children: [
        _buildEventItem(
            'assets/images/store1.png', "복신", "시험기간 묵음밥 할인 이벤트!!", 4.8),
        const SizedBox(height: 10),
        _buildEventItem(
            'assets/images/store2.png', "고수찜닭", "3인분 이상 주문시 치즈토핑 무료!", 4.5),
      ],
    );
  }
  Widget _buildEventItem(
      String imagePath, String storeName, String description, double rating) {
    return Row(
      children: [
        Image.asset(
          imagePath,
          height: 60,
          width: 60,
          fit: BoxFit.cover,
        ),
        const SizedBox(width: 10),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                storeName,
                style:
                    const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
              Text(description),
            ],
          ),
        ),
        Row(
          children: [
            const Icon(Icons.star, color: Colors.yellow),
            Text(rating.toString()),
          ],
        ),
      ],
    );
  }
}
```
각 버튼에 패딩을 60으로 설정하고 아이콘의 크기를 기본의 5배인 120으로 설정했습니다. 이렇게 하면 텍스트가 버튼 중앙에 더 잘 맞고, 아이콘도 더 눈에 띄게 됩니다.