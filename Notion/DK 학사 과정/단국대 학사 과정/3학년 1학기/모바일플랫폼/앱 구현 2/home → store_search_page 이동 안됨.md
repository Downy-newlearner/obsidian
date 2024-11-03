코드 자체에는 큰 문제가 없어 보이지만, 버튼을 클릭할 때 페이지가 이동하지 않는 문제는 여러 가지 원인이 있을 수 있습니다. 몇 가지 확인 해볼 사항과 함께 수정이 필요할 수 있는 부분을 설명드리겠습니다.
### 몇 가지 확인 사항
1. **패키지 경로 확인**: `home_page.dart`와 `store_search_page.dart` 파일이 올바르게 불러와졌는지 확인 합니다.
2. **Navigator 사용법**: `Navigator.push`를 사용할 때 `context`가 올바르게 전달되고 있는지 확인합니다.
아래는 필요한 경우 코드를 약간 수정하여 제공해 드립니다.
### `StoreSearchPage`가 포함된 코드를 수정
```Dart
import 'package:flutter/material.dart';
import 'home_page.dart';
class StoreSearchPage extends StatelessWidget {
  const StoreSearchPage({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () => Navigator.pop(context),
        ),
      ),
      body: Column(
        children: [
          Expanded(
            child: Image.asset(
              'assets/images/map.jpg', // 지도 이미지 파일 경로
              fit: BoxFit.cover,
              width: double.infinity,
            ),
          ),
        ],
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
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const HomePage()),
            );
          } else if (index == 1) {
            // My Info 페이지로 이동
            // Navigator.push(
            //   context,
            //   MaterialPageRoute(builder: (context) => const MyInfoPage()),
            // );
          }
        },
      ),
    );
  }
}
```
### `HomePage` 코드의 확인 및 수정
특히 `ElevatedButton` 위젯의 `onPressed` 속성의 Navigator 코드를 확인해주세요.
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
                      padding: const EdgeInsets.symmetric(vertical: 60),
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
                          size: 120,
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
                      padding: const EdgeInsets.symmetric(vertical: 60),
                    ),
                    child: const Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Icon(
                          Icons.store,
                          color: Colors.white,
                          size: 120,
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
위의 코드에서 `StoreSearchPage`와 `StoreRegisterPage`가 올바르게 불러와졌는지 확인하고, 각 파일이 정확히 설정되어 있는지 확인하세요. 필요시 앱을 재시작하거나 캐시를 지워보시기도 바랍니다. 또한, 에러 로그가 있다면 그 내용을 확인해 보시기 바랍니다.
---
이 오류는 비동기 처리를 하는 동안 `BuildContext`를 사용하면 발생합니다. Dart에서는 `BuildContext`가 변경되거나 소멸될 수 있기 때문에 가능한 한 비동기 호출 후에 `BuildContext`를 사용할 때 주의해야 합니다.
이 문제를 해결하려면 비동기 작업 후 `mounted` 속성을 확인하여 위젯이 여전히 빌드 중인지 확인하는 것입니다.
아래는 수정된 `login_page.dart` 예제입니다:
```Dart
// login_page.dart
import 'package:flutter/material.dart';
import 'home_page.dart';
import 'signup_page.dart'; // 회원가입 페이지로 이동하도록 import 추가
import 'database_helper.dart';
class LoginPage extends StatefulWidget {
  const LoginPage({super.key});
  @override
  LoginPageState createState() => LoginPageState();
}
class LoginPageState extends State<LoginPage> {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  void signIn() async {
    String email = emailController.text;
    String password = passwordController.text;
    // 데이터베이스에서 사용자 정보를 가져옵니다.
    List<Map<String, dynamic>> users = await DatabaseHelper().getUsers();
    // 입력한 email과 password가 데이터베이스에 존재하는지 확인합니다.
    bool userExists = users
        .any((user) => user['userId'] == email && user['password'] == password);
    if (!mounted) return; // Widget이 여전히 빌드 상태인지 확인
    if (userExists) {
      // 로그인 성공 시 my_app3로 이동
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => const HomePage()),
      );
    } else {
      // 로그인 실패 시 경고 메시지
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Invalid email or password")),
      );
    }
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Column(
          children: [
            Container(
              height: 250.0,
              decoration: const BoxDecoration(
                image: DecorationImage(
                  image: AssetImage('assets/images/fork_background.png'), // 포크 배경 이미지
                  fit: BoxFit.cover,
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    "Login",
                    style: TextStyle(fontSize: 32.0, fontWeight: FontWeight.bold),
                  ),
                  const SizedBox(height: 16.0),
                  TextField(
                    controller: emailController,
                    decoration: const InputDecoration(
                      prefixIcon: Icon(Icons.email),
                      labelText: "Email",
                      border: OutlineInputBorder(),
                    ),
                  ),
                  const SizedBox(height: 16.0),
                  TextField(
                    controller: passwordController,
                    obscureText: true,
                    decoration: const InputDecoration(
                      prefixIcon: Icon(Icons.lock),
                      labelText: "Password",
                      border: OutlineInputBorder(),
                    ),
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      TextButton(
                        onPressed: () {}, // 아이디 찾기 기능 추가 가능
                        child: const Text("아이디 찾기"),
                      ),
                      TextButton(
                        onPressed: () {}, // 비밀번호 찾기 기능 추가 가능
                        child: const Text("비밀번호 찾기"),
                      ),
                    ],
                  ),
                  const SizedBox(height: 16.0),
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                      onPressed: signIn,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.purple,
                        padding: const EdgeInsets.symmetric(vertical: 16.0),
                      ),
                      child: const Text("Sign In"),
                    ),
                  ),
                  const SizedBox(height: 16.0),
                  const Center(child: Text("Or")),
                  const SizedBox(height: 16.0),
                  OutlinedButton(
                    onPressed: () {
                      // 회원가입 페이지로 이동
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => const SignupPage()),
                      );
                    },
                    style: OutlinedButton.styleFrom(
                      padding: const EdgeInsets.symmetric(vertical: 16.0),
                    ),
                    child: const Text("Sign up"),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```
위 코드에서는 비동기 작업 후 `mounted` 속성을 확인하여, 현재 위젯이 여전히 활성화되어 있는지 확인했습니다. 이로써 비동기 작업 후에 `BuildContext`를 안전하게 사용할 수 있습니다.
```C++
//login_page.dart
import 'package:flutter/material.dart';
import 'home_page.dart';
import 'signup_page.dart'; // 회원가입 페이지로 이동하도록 import 추가
import 'database_helper.dart';
class LoginPage extends StatefulWidget {
  const LoginPage({super.key});
  @override
  LoginPageState createState() => LoginPageState();
}
class LoginPageState extends State<LoginPage> {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  void signIn() async {
    // 여기에 실제 로그인 로직을 추가하세요 (ex. Firebase Auth)
    String email = emailController.text;
    String password = passwordController.text;
    // 데이터베이스에서 사용자 정보를 가져옵니다.
    List<Map<String, dynamic>> users = await DatabaseHelper().getUsers();
    // 입력한 email과 password가 데이터베이스에 존재하는지 확인합니다.
    bool userExists = users
        .any((user) => user['userId'] == email && user['password'] == password);
    if (userExists) {
      // 로그인 성공 시 my_app3로 이동
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => const HomePage()),
      );
    } else {
      // 로그인 실패 시 경고 메시지
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Invalid email or password")),
      );
    }
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Column(
          children: [
            Container(
              height: 250.0,
              decoration: const BoxDecoration(
                image: DecorationImage(
                  image: AssetImage(
                      'assets/images/fork_background.png'), // 포크 배경 이미지
                  fit: BoxFit.cover,
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    "Login",
                    style:
                        TextStyle(fontSize: 32.0, fontWeight: FontWeight.bold),
                  ),
                  const SizedBox(height: 16.0),
                  TextField(
                    controller: emailController,
                    decoration: const InputDecoration(
                      prefixIcon: Icon(Icons.email),
                      labelText: "Email",
                      border: OutlineInputBorder(),
                    ),
                  ),
                  const SizedBox(height: 16.0),
                  TextField(
                    controller: passwordController,
                    obscureText: true,
                    decoration: const InputDecoration(
                      prefixIcon: Icon(Icons.lock),
                      labelText: "Password",
                      border: OutlineInputBorder(),
                    ),
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      TextButton(
                        onPressed: () {}, // 아이디 찾기 기능 추가 가능
                        child: const Text("아이디 찾기"),
                      ),
                      TextButton(
                        onPressed: () {}, // 비밀번호 찾기 기능 추가 가능
                        child: const Text("비밀번호 찾기"),
                      ),
                    ],
                  ),
                  const SizedBox(height: 16.0),
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                      onPressed: signIn,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.purple,
                        padding: const EdgeInsets.symmetric(vertical: 16.0),
                      ),
                      child: const Text("Sign In"),
                    ),
                  ),
                  const SizedBox(height: 16.0),
                  const Center(child: Text("Or")),
                  const SizedBox(height: 16.0),
                  OutlinedButton(
                    onPressed: () {
                      // 회원가입 페이지로 이동
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (context) => const SignupPage()),
                      );
                    },
                    style: OutlinedButton.styleFrom(
                      padding: const EdgeInsets.symmetric(vertical: 16.0),
                    ),
                    child: const Text("Sign up"),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```
---
`sign_up` 메서드에서 `BuildContext`를 비동기 호출 후에 사용하고 있기 때문에, `mounted` 속성을 확인하여 위젯이 여전히 빌드 상태인지 확인하는 것이 좋습니다. 이를 해결하려면, 비동기 작업 후에 `mounted` 속성을 확인하는 코드를 추가하면 됩니다.
아래는 수정된 `signup_page.dart` 코드입니다:
```Dart
// signup_page.dart
import 'package:flutter/material.dart';
import 'login_page.dart';
import 'database_helper.dart'; // Import the database helper class
import 'users_page.dart'; // Import the users page class
class SignupPage extends StatefulWidget {
  const SignupPage({super.key});
  @override
  SignupPageState createState() => SignupPageState();
}
class SignupPageState extends State<SignupPage> {
  final TextEditingController nameController = TextEditingController();
  final TextEditingController birthController = TextEditingController();
  final TextEditingController idController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  String profileImage = 'assets/images/default_profile.jpg';
  void updateProfileImage() {
    setState(() {
      profileImage = 'assets/images/setting_profile.jpg';
    });
  }
  void signUp() async {
    String name = nameController.text;
    String birth = birthController.text;
    String userId = idController.text;
    String password = passwordController.text;
    if (name.isEmpty || birth.isEmpty || userId.isEmpty || password.isEmpty) {
      _showErrorDialog('Please fill all fields');
      return;
    }
    // Prepare the user data
    Map<String, dynamic> user = {
      'name': name,
      'birth': birth,
      'userId': userId,
      'password': password,
    };
    try {
      // Insert the user data into the database
      await DatabaseHelper().insertUser(user);
      if (!mounted) return; // Widget이 여전히 빌드 상태인지 확인
      // Navigate to the login page or show success message
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => const LoginPage()),
      );
    } catch (e) {
      _showErrorDialog('Failed to sign up. Please try again.');
    }
  }
  void _showErrorDialog(String message) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Error'),
          content: Text(message),
          actions: [
            TextButton(
              child: const Text('OK'),
              onPressed: () {
                Navigator.of(context).pop();
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
        title: const Text('Sign Up'),
        actions: [
          IconButton(
            icon: const Icon(Icons.list),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const UsersPage()),
              );
            },
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: nameController,
              decoration: const InputDecoration(labelText: 'Name'),
            ),
            TextField(
              controller: birthController,
              decoration: const InputDecoration(labelText: 'Birth Date'),
            ),
            TextField(
              controller: idController,
              decoration: const InputDecoration(labelText: 'User ID'),
            ),
            TextField(
              controller: passwordController,
              decoration: const InputDecoration(labelText: 'Password'),
              obscureText: true,
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: signUp,
              child: const Text('Sign Up'),
            ),
          ],
        ),
      ),
    );
  }
}
```
위 코드에서는 비동기 작업(`signUp` 메서드) 후에 `mounted` 속성을 확인하여, 현재 위젯이 여전히 활성화되어 있는지 확인했습니다. 이를 통해 비동기 작업 후에 `BuildContext`를 안전하게 사용할 수 있습니다.
```C++
//signup_page.dart
import 'package:flutter/material.dart';
import 'login_page.dart';
import 'database_helper.dart'; // Import the database helper class
import 'users_page.dart'; // Import the users page class
class SignupPage extends StatefulWidget {
  const SignupPage({super.key});
  @override
  SignupPageState createState() => SignupPageState();
}
class SignupPageState extends State<SignupPage> {
  final TextEditingController nameController = TextEditingController();
  final TextEditingController birthController = TextEditingController();
  final TextEditingController idController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  String profileImage = 'assets/images/default_profile.jpg';
  void updateProfileImage() {
    setState(() {
      profileImage = 'assets/images/setting_profile.jpg';
    });
  }
  void signUp() async {
    String name = nameController.text;
    String birth = birthController.text;
    String userId = idController.text;
    String password = passwordController.text;
    if (name.isEmpty || birth.isEmpty || userId.isEmpty || password.isEmpty) {
      _showErrorDialog('Please fill all fields');
      return;
    }
    // Prepare the user data
    Map<String, dynamic> user = {
      'name': name,
      'birth': birth,
      'userId': userId,
      'password': password,
    };
    try {
      // Insert the user data into the database
      await DatabaseHelper().insertUser(user);
      // Navigate to the login page or show success message
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => const LoginPage()),
      );
    } catch (e) {
      _showErrorDialog('Failed to sign up. Please try again.');
    }
  }
  void _showErrorDialog(String message) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Error'),
          content: Text(message),
          actions: [
            TextButton(
              child: const Text('OK'),
              onPressed: () {
                Navigator.of(context).pop();
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
        title: const Text('Sign Up'),
        actions: [
          IconButton(
            icon: const Icon(Icons.list),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const UsersPage()),
              );
            },
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: nameController,
              decoration: const InputDecoration(labelText: 'Name'),
            ),
            TextField(
              controller: birthController,
              decoration: const InputDecoration(labelText: 'Birth Date'),
            ),
            TextField(
              controller: idController,
              decoration: const InputDecoration(labelText: 'User ID'),
            ),
            TextField(
              controller: passwordController,
              decoration: const InputDecoration(labelText: 'Password'),
              obscureText: true,
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: signUp,
              child: const Text('Sign Up'),
            ),
          ],
        ),
      ),
    );
  }
}
```
---
```C++
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
                      padding:
                          const EdgeInsets.symmetric(vertical: 30), // 패딩 60
                    ),
                    child: const Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Padding(
                          padding: EdgeInsets.only(left: 60),
                          child: Text(
                            "매장 찾기",
                            style: TextStyle(color: Colors.white, fontSize: 30),
                            textAlign: TextAlign.left,
                          ),
                        ),
                        Padding(
                          padding: EdgeInsets.only(right: 60),
                          child: Icon(
                            Icons.map,
                            color: Colors.white,
                            size: 80, // 기본 크기의 5배
                          ),
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
                      padding:
                          const EdgeInsets.symmetric(vertical: 30), // 패딩 60
                    ),
                    child: const Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Padding(
                          padding: EdgeInsets.only(left: 60),
                          child: Icon(
                            Icons.store,
                            color: Colors.white,
                            size: 80, // 기본 크기의 5배
                          ),
                        ),
                        Padding(
                          padding: EdgeInsets.only(right: 60),
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
            
```