import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton
from googletrans import Translator

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 텍스트 박스와 버튼 생성
        self.text_query = QTextEdit(self)
        self.text_query.setFixedWidth(300)
        self.text_query.setFixedHeight(30)
        self.text_query.installEventFilter(self)  # 이벤트 필터 설치

        self.btn_translate = QPushButton('Translate', self)
        self.btn_translate.setFixedWidth(80)
        self.btn_translate.clicked.connect(self.btn_translate_clicked)

        self.btn_reset = QPushButton('Reset', self)
        self.btn_reset.setFixedWidth(80)
        self.btn_reset.clicked.connect(self.btn_reset_clicked)

        self.text_answer = QTextEdit(self)
        self.text_answer.setFixedWidth(300)
        self.text_answer.setFixedHeight(300)
        self.text_answer.setReadOnly(True)

        # 버튼 레이아웃 (Translate와 Reset 버튼을 같은 줄에 배치)
        hbox = QHBoxLayout()
        hbox.addWidget(self.btn_translate)
        hbox.addWidget(self.btn_reset)

        # 전체 레이아웃
        vbox = QVBoxLayout()
        vbox.addWidget(self.text_query)
        vbox.addLayout(hbox)  # 버튼 레이아웃 추가
        vbox.addWidget(self.text_answer)

        self.setLayout(vbox)
        self.setWindowTitle('Simple Chatting App')
        self.setGeometry(300, 300, 400, 400)
        self.show()

    # 버튼 클릭 시 처리 함수
    def btn_translate_clicked(self):
        input_text = self.text_query.toPlainText()
        translator = Translator()
        translated_text = translator.translate(input_text, src='ko', dest='en')

        previous_text = self.text_answer.toPlainText()
        result_text = f"{previous_text}\nQuery: {input_text}\nAnswer: {translated_text.text}"
        self.text_answer.setPlainText(result_text.strip())

        self.text_query.clear()

    # Reset 버튼 클릭 시 처리 함수
    def btn_reset_clicked(self):
        self.text_query.clear()
        self.text_answer.clear()

    # 이벤트 필터 설정
    def eventFilter(self, source, event):
        if source == self.text_query and event.type() == event.KeyPress:
            if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                self.btn_translate_clicked()  # 엔터 키 입력 시 함수 실행
                return True
        return super().eventFilter(source, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
