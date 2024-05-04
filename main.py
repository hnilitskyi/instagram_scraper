import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from instagpy import InstaGPy
import time
import random


class InstagramScraper(QWidget):
    def __init__(self):
        super().__init__()

        self.accounts = []
        self.followers_count = 0

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        username_label = QLabel("Username for login:")
        self.username_input = QLineEdit()
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)

        password_label = QLabel("Password for login:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)

        add_user_button = QPushButton("Add User for Login")
        add_user_button.clicked.connect(self.add_user)
        layout.addWidget(add_user_button)

        self.accounts_label = QLabel("Accounts for scrap: 0")
        layout.addWidget(self.accounts_label)

        target_username_label = QLabel("Target username:")
        self.target_username_input = QLineEdit()
        layout.addWidget(target_username_label)
        layout.addWidget(self.target_username_input)

        scrap_button = QPushButton("Scrap!")
        scrap_button.clicked.connect(self.scrap_followers)
        layout.addWidget(scrap_button)

        self.output_text = QTextEdit()
        layout.addWidget(self.output_text)

        self.setLayout(layout)
        self.setWindowTitle("Instagram Scraper")

    def add_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username and password:
            self.accounts.append({"username": username, "password": password})
            self.accounts_label.setText("Accounts for scrap: {}".format(len(self.accounts)))
            self.username_input.clear()
            self.password_input.clear()

    def get_followers(self, username, insta):
        followers = []
        has_more = True
        cursor = None
        while has_more:
            try:
                response = insta.get_user_friends(username, followers_list=True, end_cursor=cursor, pagination=False)
                followers.extend(response['data'])
                has_more = response.get('has_next_page')
                if has_more:
                    cursor = response.get('end_cursor')
                time.sleep(random.uniform(7, 10))
            except Exception as error:
                print(error)
                break
        return followers

    def scrap_followers(self):
        target_username = self.target_username_input.text()
        if not target_username:
            return

        for account in self.accounts:
            insta = InstaGPy()
            insta.login(username=account["username"], password=account["password"])
            followers = self.get_followers(target_username, insta)

            filename = "{}_followers.json".format(target_username)
            with open(filename, 'w') as f:
                json.dump(followers, f)

            self.output_text.append("Followers for account {}: {}".format(account["username"], followers))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InstagramScraper()
    ex.show()
    sys.exit(app.exec_())
