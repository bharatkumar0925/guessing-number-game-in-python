import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMessageBox

class GuessNumberGame(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 10
        self.random_number = random.randint(1, 1000)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Guess the Number")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("Guess the number between 1 to 1000")
        self.chances_label = QLabel("You have {} chances".format(self.count))
        self.user_input = QLineEdit()
        self.guess_button = QPushButton("Guess")
        self.guess_button.clicked.connect(self.check_guess)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.chances_label)
        vbox.addWidget(self.user_input)
        vbox.addWidget(self.guess_button)

        self.setLayout(vbox)

    def check_guess(self):
        user_input = self.user_input.text()

        if self.count == 0:
            QMessageBox.information(self, "Game Over", "The right answer is: {}".format(self.random_number))
            self.close()

        if not user_input.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")
            self.user_input.clear()
            return
        user_input = int(user_input)

        if user_input > self.random_number:
            self.count -= 1
            self.chances_label.setText("Your number is greater. You have {} chances".format(self.count))
        elif user_input < self.random_number:
            self.count -= 1
            self.chances_label.setText("Your number is smaller. You have {} chances".format(self.count))
        elif user_input == self.random_number:
            QMessageBox.information(self, "Congratulations", "Yes, you did it! You won")
            self.close()

        self.user_input.clear()
        self.user_input.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = GuessNumberGame()
    game.show()
    sys.exit(app.exec_())
