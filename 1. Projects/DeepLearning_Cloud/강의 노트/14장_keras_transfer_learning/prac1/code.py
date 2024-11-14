import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMessageBox

# 슬롯 함수 정의
def on_button_click():
    msg = QMessageBox()
    msg.setText("버튼이 클릭되었습니다!")
    msg.exec_()

# 메인 윈도우 클래스 정의
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("시그널과 슬롯 예제")
        self.setGeometry(100, 100, 300, 200)

        # 버튼 생성 및 설정
        button = QPushButton("클릭하세요", self)
        button.clicked.connect(on_button_click)  # 버튼 클릭 시 on_button_click 함수 호출
        button.move(100, 80)

# 애플리케이션 실행
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
