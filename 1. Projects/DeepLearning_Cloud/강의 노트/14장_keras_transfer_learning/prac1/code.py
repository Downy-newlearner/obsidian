import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

# 애플리케이션 객체 생성
app = QApplication(sys.argv)

# 메인 윈도우 생성
window = QMainWindow()
window.setWindowTitle('PyQt5 예제')
window.setGeometry(100, 100, 600, 400)

# 라벨 추가
label = QLabel('안녕하세요, PyQt5!', window)
label.move(200, 200)

# 윈도우 표시
window.show()

# 애플리케이션 실행
sys.exit(app.exec_())
