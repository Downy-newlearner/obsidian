import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap

class ImageLoaderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Loader")
        self.setGeometry(100, 100, 600, 400)

        # 'Load image' 버튼 생성 및 설정
        self.load_button = QPushButton("Load image", self)
        self.load_button.move(10, 10)  # 윈도우 좌상단에 버튼 배치
        self.load_button.clicked.connect(self.load_image)

        # 이미지를 표시할 라벨 생성
        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 50, 580, 330)  # 이미지 표시 영역 설정

    def load_image(self):
        # 파일 선택 대화 상자 열기
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name:  # 파일이 선택되었을 때
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.width(), self.image_label.height()))

# 애플리케이션 실행
app = QApplication(sys.argv)
window = ImageLoaderApp()
window.show()
sys.exit(app.exec_())
