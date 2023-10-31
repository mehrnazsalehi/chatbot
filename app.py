from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
from chat import get_response, bot_name
import sys


class ChatbotApplication(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chatbot")
        self.setFixedSize(470, 550)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layouts
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        input_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)

        # Head label
        head_label = QLabel("Chatbot")
        head_label.setStyleSheet("background-color: #17202A; color: #EAECEE; font: bold 13px;")
        head_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(head_label)

        # Text widget
        self.text_widget = QTextEdit()
        self.text_widget.setReadOnly(True)
        self.text_widget.setStyleSheet("background-color: #17202A; color: #EAECEE; font: 14px;")
        main_layout.addWidget(self.text_widget)

        # Message entry box
        self.msg_entry = QTextEdit()
        self.msg_entry.setStyleSheet("background-color: #2C3E50; color: #EAECEE; font: 14px;")
        self.msg_entry.setMaximumHeight(60)
        input_layout.addWidget(self.msg_entry)

        # Send button
        send_button = QPushButton("Send")
        send_button.setStyleSheet("background-color: #ABB2B9; color: #17202A; font: bold 13px;")
        send_button.setMaximumHeight(60)
        send_button.clicked.connect(self._on_send_button_clicked)
        input_layout.addWidget(send_button)
        self.show()

    def _on_send_button_clicked(self):
        msg = self.msg_entry.toPlainText()
        if msg:
            self._insert_message(msg, "You")
            self.msg_entry.clear()

    def _insert_message(self, msg, sender):
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.insertPlainText(msg1)

        response = get_response(msg)  
        msg2 = f"{bot_name}: {response}\n\n"
        self.text_widget.insertPlainText(msg2)

        self.text_widget.moveCursor(QTextCursor.End)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_app = ChatbotApplication()
    
    app.exec_()
