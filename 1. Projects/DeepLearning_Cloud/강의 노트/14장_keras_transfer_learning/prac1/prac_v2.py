import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PIL import Image
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions

class ImageLoaderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Image Classifier")
        self.setGeometry(100, 100, 600, 500)

        # 'Load image' 버튼 생성 및 설정
        self.load_button = QPushButton("Load image", self)
        self.load_button.move(10, 10)  # 윈도우 좌상단에 버튼 배치

        # 여기서 버튼의 폰트를 설정합니다.
        # 추천 폰트: Arial, Verdana, Times New Roman, Courier New 중에서 선택해 주세요.
        button_font = QFont("Arial", 10)  # 폰트 이름과 크기를 설정 (추천 폰트 중 하나 선택 가능)
        self.load_button.setFont(button_font)

        self.load_button.clicked.connect(self.load_image)

        # 버튼의 크기 조절
        self.load_button.setFixedSize(120, 40)

        # 이미지를 표시할 라벨 생성
        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 50, 580, 300)  # 이미지 표시 영역 설정

        # 이미지 classification result를 표시할 라벨 생성
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 360, 580, 120)  # 결과 표시 영역 설정
        self.result_label.setWordWrap(True)

        # 결과 라벨의 폰트 설정
        result_font = QFont("Arial", 13)  # 추천 폰트 중 하나 선택 가능
        self.result_label.setFont(result_font)

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
            decoded_predictions = decode_predictions(predictions, top=3)[0]  # 상위 3개 예측 가져오기

            # 결과 표시 (상위 3개의 예측 결과)
            result_text = "Top 3 Predictions:\n"
            for i, (imagenet_id, label, prob) in enumerate(decoded_predictions):
                result_text += f"{i + 1}. {label} with probability {prob:.2f}\n"

            self.result_label.setText(result_text)

# 애플리케이션 실행
app = QApplication(sys.argv)
window = ImageLoaderApp()
window.show()
sys.exit(app.exec_())
