import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap
from PIL import Image
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions


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
        self.image_label.setGeometry(10, 50, 580, 250)  # 이미지 표시 영역 설정

        # 이미지 classification result를 표시할 라벨 생성
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 310, 580, 80)  # 결과 표시 영역 설정
        self.result_label.setWordWrap(True)

        # 미리 학습된 EfficientNet 모델 불러오기
        self.model = EfficientNetB0(weights="imagenet")

    def load_image(self):
        # 파일 선택 대화 상자 열기
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name:  # 파일이 선택되었을 때
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.width(), self.image_label.height()))

            # 이미지 Classification 코드 추가 (Keras EfficientNet 사용)
            # PIL 이미지 로드 및 전처리
            image = Image.open(file_name).convert('RGB')
            image = image.resize((224, 224))  # 모델 입력 크기에 맞게 조정
            image_array = np.array(image)
            image_array = np.expand_dims(image_array, axis=0)  # 배치 차원 추가
            image_array = preprocess_input(image_array)  # EfficientNet 전용 전처리

            # 모델을 사용하여 예측
            predictions = self.model.predict(image_array)
            decoded_predictions = decode_predictions(predictions, top=1)[0]

            # 결과 표시
            result_text = f"Prediction: {decoded_predictions[0][1]} with probability {decoded_predictions[0][2]:.2f}"
            self.result_label.setText(result_text)

# 애플리케이션 실행
app = QApplication(sys.argv)
window = ImageLoaderApp()
window.show()
sys.exit(app.exec_())
