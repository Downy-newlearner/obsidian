import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from googletrans import Translator

# 윈도우 생성 클래스
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # UI 디자인 함수
    def initUI(self):
        # 텍스트 박스와 버튼 생성
        self.text_query = QTextEdit(self)
        self.text_query.setFixedWidth(300)  # 텍스트 박스의 폭
        self.text_query.setFixedHeight(30)  # 텍스트 박스의 높이

        self.btn_translate = QPushButton('Translate', self)
        self.btn_translate.setFixedWidth(80)  # 버튼의 폭
        self.btn_translate.clicked.connect(self.btn_translate_clicked)  # 버튼 클릭 연결

        self.text_answer = QTextEdit(self)
        self.text_answer.setFixedWidth(300)  # 텍스트 박스의 폭
        self.text_answer.setFixedHeight(300)  # 텍스트 박스의 높이
        self.text_answer.setReadOnly(True)  # 결과창은 읽기 전용

        # 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addWidget(self.text_query)
        vbox.addWidget(self.btn_translate)
        vbox.addWidget(self.text_answer)

        self.setLayout(vbox)
        self.setWindowTitle('Simple Chatting App')
        self.setGeometry(300, 300, 400, 400)  # 창 크기와 위치
        self.show()

    # 버튼 클릭시 처리 함수
    def btn_translate_clicked(self):
        input_text = self.text_query.toPlainText()  # 입력 텍스트 가져오기
        translator = Translator()
        translated_text = translator.translate(input_text, src='ko', dest='en')  # 한->영 번역

        # 기존 결과에 새로운 질의-응답 추가
        previous_text = self.text_answer.toPlainText()  # 기존 기록 가져오기
        result_text = f"{previous_text}\nQuery: {input_text}\nAnswer: {translated_text.text}"
        self.text_answer.setPlainText(result_text.strip())  # 결과 출력


# 프로그램 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
