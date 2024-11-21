이 코드를 기능별로 여러 개의 모듈로 나누겠습니다. 각 파일의 역할을 명확히 하여 관리하기 쉽도록 하겠습니다.
### main.dart
```Dart
import 'package:flutter/material.dart';
import 'package:restaurant_app/app.dart';
void main() {
  runApp(MyApp());
}
```
### app.dart
```Dart
import 'package:flutter/material.dart';
import 'package:restaurant_app/pages/restaurant_page.dart';
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: RestaurantPage(),
    );
  }
}
```
### pages/restaurant_page.dart
```Dart
import 'package:flutter/material.dart';
import 'package:restaurant_app/tabs/menu_tab.dart';
import 'package:restaurant_app/tabs/community_tab.dart';
import 'package:restaurant_app/pages/reservation_page.dart';
class RestaurantPage extends StatefulWidget {
  @override
  _RestaurantPageState createState() => _RestaurantPageState();
}
class _RestaurantPageState extends State<RestaurantPage> with SingleTickerProviderStateMixin {
  late TabController _tabController;
  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
    _tabController.addListener(() {
      setState(() {});
    });
  }
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        appBar: AppBar(
          title: Container(),
          leading: IconButton(
            icon: Image.asset('assets/images/back_button.png'), // 뒤로가기 버튼 이미지 경로
            onPressed: () {
              // 뒤로가기 기능 구현
            },
          ),
        ),
        body: Column(
          children: [
            Image.asset('assets/images/top_pizza_image.png', fit: BoxFit.cover),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Text(
                '고래한입피자 단국대점',
                style: TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            PreferredSize(
              preferredSize: Size.fromHeight(48.0),
              child: Column(
                children: [
                  TabBar(
                    controller: _tabController,
                    tabs: [
                      Tab(text: '메뉴'),
                      Tab(text: '커뮤니티'),
                    ],
                  ),
                  Container(
                    color: Colors.purple,
                    height: 4.0,
                  ),
                ],
              ),
            ),
            Expanded(
              child: TabBarView(
                controller: _tabController,
                children: [
                  MenuTab(),
                  CommunityTab(),
                ],
              ),
            ),
          ],
        ),
        floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
        floatingActionButton: _tabController.index == 0
            ? ElevatedButton(
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => ReservationPage()),
            );
          },
          child: Text('예약하기'),
        )
            : null,
      ),
    );
  }
}
```
### tabs/menu_tab.dart
```Dart
import 'package:flutter/material.dart';
import 'package:restaurant_app/widgets/menu_item.dart';
class MenuTab extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: EdgeInsets.all(8.0),
      children: [
        MenuItem(
          imagePath: 'assets/images/bulgogi_pizza.png',
          name: '불고기 피자',
          description: '불고기 맛나는 피자',
          price: '7,000원',
          initialLikes: 105,
        ),
        MenuItem(
          imagePath: 'assets/images/pepperoni_pizza.png',
          name: '페페로니 피자',
          description: '짭짤한 페페로니가 잔뜩 들어간 피자',
          price: '8,500원',
          initialLikes: 99,
        ),
        MenuItem(
          imagePath: 'assets/images/mexican_pizza.png',
          name: '멕시칸 피자',
          description: '톡톡 튀는 토마토의 풍미를 더한 피자',
          price: '8,500원',
          initialLikes: 45,
        ),
      ],
    );
  }
}
```
### tabs/community_tab.dart
```Dart
import 'package:flutter/material.dart';
import 'package:restaurant_app/pages/community_page.dart';
class CommunityTab extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return CommunityPage();
  }
}
```
### pages/community_page.dart
```Dart
import 'package:flutter/material.dart';
import 'package:restaurant_app/models/review.dart';
import 'package:restaurant_app/pages/write_review_page.dart';
import 'package:restaurant_app/widgets/review_widget.dart';
class CommunityPage extends StatefulWidget {
  @override
  _CommunityPageState createState() => _CommunityPageState();
}
class _CommunityPageState extends State<CommunityPage> {
  List<Review> reviews = [
    Review(profileImage: 'assets/images/profile1.png', rating: 4.0, title: '사장님이 너무 친절해요!', content: '음식도 맛있고 알바생분들도 너무 이뻐요!', likes: 20),
    Review(profileImage: 'assets/images/profile2.png', rating: 2.0, title: '화장실 잠금장치 ㅠㅠ', content: '화장실 문 안잠겨요 고쳐주세요 ㅠㅠ', likes: 99),
    Review(profileImage: 'assets/images/profile3.png', rating: 5.0, title: '아이고 사장님', content: '서비스를 너무 많이 주셨어요 ㅠㅠㅠㅠ', likes: 5),
  ];
  void _addReview(Review review) {
    setState(() {
      reviews.insert(0, review);
    });
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: reviews.length,
              itemBuilder: (context, index) {
                return ReviewWidget(
                  review: reviews[index],
                  onLike: () {
                    setState(() {
                      reviews[index].likes += 1;
                    });
                  },
                );
              },
            ),
          ),
        ],
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      floatingActionButton: ElevatedButton(
        onPressed: () async {
          final result = await Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => WriteReviewPage()),
          );
          if (result != null && result is Review) {
            _addReview(result);
          }
        },
        child: Text('글쓰기'),
      ),
    );
  }
}
```
### pages/write_review_page.dart
```Dart
import 'package:flutter/material.dart';
import 'package:restaurant_app/models/review.dart';
class WriteReviewPage extends StatefulWidget {
  @override
  _WriteReviewPageState createState() => _WriteReviewPageState();
}
class _WriteReviewPageState extends State<WriteReviewPage> {
  double rating = 0.0;
  TextEditingController titleController = TextEditingController();
  TextEditingController contentController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("커뮤니티 글 작성"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: List.generate(5, (index) {
                return IconButton(
                  icon: Icon(
                    index < rating ? Icons.star : Icons.star_border,
                    color: Colors.yellow,
                  ),
                  onPressed: () {
                    setState(() {
                      rating = index + 1.0;
                    });
                  },
                );
              }),
            ),
            TextField(
              controller: titleController,
              decoration: InputDecoration(labelText: '제목을 입력해주세요.'),
            ),
            TextField(
              controller: contentController,
              decoration: InputDecoration(labelText: '내용을 입력해주세요.'),
              maxLines: 5,
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                final newReview = Review(
                  profileImage: 'assets/images/default_profile.jpeg',
                  rating: rating,
                  title: titleController.text,
                  content: contentController.text,
                  likes: 0,
                );
                Navigator.pop(context, newReview);
              },
              child: Text('완료'),
            ),
          ],
        ),
      ),
    );
  }
}
```
### pages/reservation_page.dart
```Dart
import 'package:flutter/material.dart';
import 'package:restaurant_app/models/table_status.dart';
class ReservationPage extends StatefulWidget {
  @override
  _ReservationPageState createState() => _ReservationPageState();
}
class _ReservationPageState extends State<ReservationPage> {
  List<TableStatus> tableStatuses = [
    TableStatus(id: 1, seats: 12, maxSeats: 13, status: TableState.available, shape: TableShape.rectangle),
    TableStatus(id: 2, seats: 6, maxSeats: 7, status: TableState.unavailable, shape: TableShape.rectangle),
    TableStatus(id: 3, seats: 4, maxSeats: 4, status: TableState.available, shape: TableShape.square),
    TableStatus(id: 4, seats: 6, maxSeats: 7, status: TableState.available, shape: TableShape.rectangle),
    TableStatus(id: 5, seats: 6, maxSeats: 7, status: TableState.available, shape: TableShape.rectangle),
    TableStatus(id: 6, seats: 2, maxSeats: 3, status: TableState.available, shape: TableShape.square),
    TableStatus(id: 7, seats: 6, maxSeats: 7, status: TableState.available, shape: TableShape.rectangle),
    TableStatus(id: 8, seats: 6, maxSeats: 7, status: TableState.available, shape: TableShape.rectangle),
    TableStatus(id: 9, seats: 4, maxSeats: 6, status: TableState.available, shape: TableShape.square),
    TableStatus(id: 10, seats: 4, maxSeats: 6, status: TableState.available, shape: TableShape.square),
    TableStatus(id: 11, seats: 4, maxSeats: 6, status: TableState.available, shape: TableShape.square),
    TableStatus(id: 12, seats: 4, maxSeats: 6, status: TableState.available, shape: TableShape.square)
  ];
  int? selectedTableId;
  void _showReservationDialog(int tableId) {
    final table = tableStatuses.firstWhere((table) => table.id == tableId);
    TextEditingController timeController = TextEditingController();
    TextEditingController peopleController = TextEditingController();
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text("예약 정보 입력"),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              TextField(
                controller: timeController,
                decoration: InputDecoration(labelText: "방문 시간"),
              ),
              TextField(
                controller: peopleController,
                decoration: InputDecoration(labelText: "방문 인원수"),
              ),
            ],
          ),
          actions: [
            TextButton(
              child: Text("취소"),
              onPressed: () {
                setState(() {
                  selectedTableId = null;
                });
                Navigator.of(context).pop();
              },
            ),
            TextButton(
              child: Text("확정"),
              onPressed: () {
                int peopleCount = int.tryParse(peopleController.text) ?? 0;
                if (peopleCount > table.maxSeats) {
                  showDialog(
                    context: context,
                    builder: (BuildContext context) {
                      return AlertDialog(
                        title: Text("오류"),
                        content: Text("테이블의 최대 인원수를 확인해주세요."),
                        actions: [
                          TextButton(
                            child: Text("확인"),
                            onPressed: () {
                              Navigator.of(context).pop();
                            },
                          ),
                        ],
                      );
                    },
                  );
                } else {
                  setState(() {
                    table.status = TableState.myReserved;
                    table.visitTime = timeController.text;
                    table.visitPeople = peopleController.text;
                    selectedTableId = null;
                  });
                  Navigator.of(context).pop();
                }
              },
            ),
          ],
        );
      },
    );
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("테이블 예약"),
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
      body: Center(
        child: Container(
          color: Color(0xFFE0BEE0),
          child: Stack(
            children: [
              buildTable(tableStatuses[0], 20, 20, width: 380, height: 80), // Large rectangle
              buildTable(tableStatuses[1], 120, 20, width: 80, height: 160), // Tall rectangle
              buildTable(tableStatuses[2], 120, 130, width: 80, height: 80), // Rectangle
              buildTable(tableStatuses[3], 120, 240, width: 160, height: 80), // Square
              buildTable(tableStatuses[4], 240, 240, width: 160, height: 80), // Rectangle
              buildTable(tableStatuses[5], 300, 20, width: 80, height: 80), // Rectangle
              buildTable(tableStatuses[6], 400, 20, width: 80, height: 160), // Square
              buildTable(tableStatuses[7], 580, 20, width: 80, height: 160), // Square
              buildTable(tableStatuses[8], 480, 200, width: 80, height: 80), // Square
              buildTable(tableStatuses[9], 480, 300, width: 80, height: 80), // Square
              buildTable(tableStatuses[10], 580, 200, width: 80, height: 80),
              buildTable(tableStatuses[11], 580, 300, width: 80, height: 80),// Tall rectangle
              Positioned(
                bottom: 20,
                left: 160,
                child: Text(
                  "출입구",
                  style: TextStyle(fontSize: 18, color: Colors.red),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
  Widget buildTable(TableStatus table, double top, double left,
      {double width = 80, double height = 80}) {
    Color tableColor;
    switch (table.status) {
      case TableState.available:
        tableColor = Colors.white;
        break;
      case TableState.unavailable:
        tableColor = Colors.pink;
        break;
      case TableState.reserved:
        tableColor = Colors.red;
        break;
      case TableState.myReserved:
        tableColor = Colors.green;
        break;
      default:
        tableColor = Colors.white;
        break;
    }
    return Positioned(
      top: top,
      left: left,
      child: GestureDetector(
        onTap: table.status == TableState.available
            ? () {
          setState(() {
            selectedTableId = table.id;
            _showReservationDialog(table.id);
          });
        }
            : table.status == TableState.myReserved
            ? () {
          showDialog(
            context: context,
            builder: (BuildContext context) {
              return AlertDialog(
                title: Text("내 예약 정보"),
                content: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text("방문 시간: ${table.visitTime}"),
                    Text("방문 인원수: ${table.visitPeople}"),
                  ],
                ),
                actions: [
                  TextButton(
                    child: Text("예약 취소하기"),
                    onPressed: () {
                      setState(() {
                        table.status = TableState.available;
                      });
                      Navigator.of(context).pop();
                    },
                  ),
                  TextButton(
                    child: Text("확인"),
                    onPressed: () {
                      Navigator.of(context).pop();
                    },
                  ),
                ],
              );
            },
          );
        }
            : null,
        child: Container(
          width: width,
          height: height,
          decoration: BoxDecoration(
            color: table.id == selectedTableId ? Colors.orange : tableColor,
            borderRadius: BorderRadius.circular(10.0),
            border: Border.all(color: Colors.black),
          ),
          child: Center(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  "${table.seats}",
                  style: TextStyle(fontSize: 24),
                ),
                Text(
                  "~${table.maxSeats}",
                  style: TextStyle(fontSize: 12),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
```
### widgets/menu_item.dart
```Dart
import 'package:flutter/material.dart';
class MenuItem extends StatefulWidget {
  final String imagePath;
  final String name;
  final String description;
  final String price;
  final int initialLikes;
  MenuItem({
    required this.imagePath,
    required this.name,
    required this.description,
    required this.price,
    required this.initialLikes,
  });
  @override
  _MenuItemState createState() => _MenuItemState();
}
class _MenuItemState extends State<MenuItem> {
  late int likes;
  bool isLiked = false;
  @override
  void initState() {
    super.initState();
    likes = widget.initialLikes;
  }
  void _toggleLike() {
    setState(() {
      isLiked = !isLiked;
      likes += isLiked ? 1 : -1;
    });
  }
  @override
  Widget build(BuildContext context) {
    return Card(
      margin: EdgeInsets.symmetric(vertical: 4.0),
      child: ListTile(
        leading: Image.asset(widget.imagePath, width: 50, height: 50, fit: BoxFit.cover),
        title: Text(widget.name),
        subtitle: Text(widget.description),
        trailing: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(widget.price, style: TextStyle(fontWeight: FontWeight.bold)),
            SizedBox(height: 4.0),
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                IconButton(
                  icon: Icon(
                    isLiked ? Icons.favorite : Icons.favorite_border,
```
### widgets/menu_item.dart (계속)
```Dart
                    color: isLiked ? Colors.red : Colors.grey,
                    size: 20.0,
                  ),
                  onPressed: _toggleLike,
                ),
                SizedBox(width: 4.0),
                Text(likes.toString()),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
```
### widgets/review_widget.dart
```Dart
import 'package:flutter/material.dart';
import 'package:restaurant_app/models/review.dart';
class ReviewWidget extends StatelessWidget {
  final Review review;
  final VoidCallback onLike;
  ReviewWidget({required this.review, required this.onLike});
  @override
  Widget build(BuildContext context) {
    return Card(
      margin: EdgeInsets.symmetric(vertical: 8.0),
      child: ListTile(
        leading: Image.asset(review.profileImage, width: 50, height: 50, fit: BoxFit.cover),
        title: Row(
          children: [
            Icon(Icons.star, color: Colors.yellow, size: 16.0),
            SizedBox(width: 4.0),
            Text(review.rating.toString()),
            SizedBox(width: 8.0),
            Expanded(
              child: Text(
                review.title,
                overflow: TextOverflow.ellipsis,
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
            ),
          ],
        ),
        subtitle: Text(review.content),
        trailing: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            IconButton(
              icon: Icon(Icons.favorite, color: Colors.red),
              onPressed: onLike,
            ),
            Text(review.likes.toString()),
          ],
        ),
      ),
    );
  }
}
```
### models/review.dart
```Dart
class Review {
  final String profileImage;
  final double rating;
  final String title;
  final String content;
  int likes;
  Review({
    required this.profileImage,
    required this.rating,
    required this.title,
    required this.content,
    required this.likes,
  });
}
```
### models/table_status.dart
```Dart
enum TableShape {
  square,
  rectangle,
}
enum TableState {
  available,
  unavailable,
  reserved,
  myReserved,
}
class TableStatus {
  final int id;
  final int seats;
  final int maxSeats;
  final TableShape shape;
  TableState status;
  String visitTime;
  String visitPeople;
  TableStatus({
    required this.id,
    required this.seats,
    required this.maxSeats,
    required this.status,
    required this.shape,
    this.visitTime = '',
    this.visitPeople = '',
  });
}
```
이렇게 각 기능별로 파일을 분리했습니다. 필요에 따라 디렉토리를 더 세분화 하여 관리할 수도 있습니다. 예를 들어, `tabs` 폴더에 있는 파일들을 `menu_tab.dart`와 `community_tab.dart` 폴더 아래에 각각의 서브 디렉토리를 만들 수 있습니다.
이 구조를 사용하면 코드 모듈화가 잘 되어 있어 유지보수가 용이하고, 기능별로 코드를 작성하거나 업데이트하는 것이 더 쉬워질 것입니다. 또한, 팀 단위로 작업할 때 각 팀원이 자신의 작업영역을 명확히 할 수 있어 충돌을 줄일 수 있습니다.
  
네, `widgets/menu_item.dart` 파일을 다시 제공해드리겠습니다.
### widgets/menu_item.dart
```Dart
import 'package:flutter/material.dart';
class MenuItem extends StatefulWidget {
  final String imagePath;
  final String name;
  final String description;
  final String price;
  final int initialLikes;
  MenuItem({
    required this.imagePath,
    required this.name,
    required this.description,
    required this.price,
    required this.initialLikes,
  });
  @override
  _MenuItemState createState() => _MenuItemState();
}
class _MenuItemState extends State<MenuItem> {
  late int likes;
  bool isLiked = false;
  @override
  void initState() {
    super.initState();
    likes = widget.initialLikes;
  }
  void _toggleLike() {
    setState(() {
      isLiked = !isLiked;
      likes += isLiked ? 1 : -1;
    });
  }
  @override
  Widget build(BuildContext context) {
    return Card(
      margin: EdgeInsets.symmetric(vertical: 4.0),
      child: ListTile(
        leading: Image.asset(widget.imagePath, width: 50, height: 50, fit: BoxFit.cover),
        title: Text(widget.name),
        subtitle: Text(widget.description),
        trailing: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(widget.price, style: TextStyle(fontWeight: FontWeight.bold)),
            SizedBox(height: 4.0),
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                IconButton(
                  icon: Icon(
                    isLiked ? Icons.favorite : Icons.favorite_border,
                    color: isLiked ? Colors.red : Colors.grey,
                    size: 20.0,
                  ),
                  onPressed: _toggleLike,
                ),
                SizedBox(width: 4.0),
                Text(likes.toString()),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
```
이 파일은 `MenuItem`이라는 Stateful 위젯을 정의합니다. 메뉴 아이템 이미지를 보여주고, 메뉴 이름과 설명을 표시하며, 좋아요(likes)를 추가하거나 제거할 수 있는 기능을 제공합니다. 이 위젯은 `ListView`와 같은 컨테이너에서 여러 개의 메뉴 아이템들을 독립적으로 관리하며 사용할 수 있도록 설계되었습니다.