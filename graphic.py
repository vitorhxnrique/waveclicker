import sys
import threading
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
)
from PyQt5.QtGui import QFont
import autoclicker  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WaveClicker")
        self.setGeometry(600, 300, 700, 500)

        
        self.ac_thread = None

        self.initUI()

    def initUI(self):
        
        self.button = QPushButton("", self)
        self.button.setGeometry(250, 260, 200, 100)
        self.button.clicked.connect(self.on_click)

        
        self.label = QLabel("Choose click speed", self)
        self.label.setFont(QFont("Arial", 16))
        self.label.setGeometry(200, 200, 400, 40)

        
        self.delay_input = QLineEdit(self)
        self.delay_input.setGeometry(250, 180, 200, 25)
        self.delay_input.setPlaceholderText("click delay")
        self.delay_input.setText("0.2")  

    def on_click(self):
        
        if self.ac_thread and self.ac_thread.is_alive():
            self.label.setText("F8 to toggle on/off")
            return

        
        try:
            delay = float(self.delay_input.text())
            if delay < 0.01:
                raise ValueError("invalid input")
        except Exception as e:
            self.label.setText("invalid input")
            return

        self.label.setText("F8 to toggle on/off")

        
        self.ac_thread = threading.Thread(
            target=autoclicker.clicks,
            args=(delay,),
            daemon=True
        )
        self.ac_thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
