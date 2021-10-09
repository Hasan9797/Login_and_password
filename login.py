
import os
import mysql.connector.connection


class Login:
    def __init__(self, name=None, login=None, password=None, age=None):
        self.name = name
        self.login = login
        self.password = password
        self.age = age
        sel.number = ["1","2","3"]

    def choice(self):
    self.clear()
        self.show()

        number = input("Enter number  [1/2]: ").strip()
        while number not in self.number[:2]:
            self.clear()
            print("you have entered the wrong number, please enter 1 or 2 ")
            number = input("Enter number  [1/2]: ").strip()

        if number == self.number[0]:
            self.registration()
        else:
            self.login_()

    def registration(self):
        pass

    def login_(self):
        pass

    def change_login_and_password(self):
        pass

    def delete_account(self):
        pass

    def log_out(self):
        pass












