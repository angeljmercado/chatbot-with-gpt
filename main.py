from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
from backend import Chatbot
import sys
import threading

class ChatbotWindow(QMainWindow):
    """ Main graphical user interface class """
    def __init__(self):
        super().__init__()

        # Initiate an instance of the Chatbot Class
        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add Send button which will send request
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500 , 340, 100, 40)
        self.button.clicked.connect(self.send_message)
        
        self.show()

    def send_message(self):
        """ Captures user input, and sends it to the chatbot screen """
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()
        
        # Splitting the proccesses so they can happen simultaneously
        response_thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        response_thread.start()
        
    def get_bot_response(self, user_input):
        """ receives Chatbot API response, and displays it in the chatbot main screen """
        response = self.chatbot.get_response(self.user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Bot: {response}</p>")

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())