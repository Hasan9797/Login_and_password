
import os
import mysql.connector.connection


class Login:
    def __init__(self, name=None, login=None, password=None, age=None):
        self.name = name
        self.login = login
        self.password = password
        self.age = age
        sel.number = ["1","2","3"]
        self.my_db = mysql.connector.connect(host="localhost", user="demo",
                                             passwd="12345678", database="DANG")
        self.my_cursor = self.my_db.cursor()
        self.my_cursor.execute("CREATE TABLE IF NOT EXISTS account(id int(6) unsigned auto_increment primary key,"
"name varchar(30), login varchar(30), password varchar(30), age int(3))")

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
        new_user_name = input("Enter your name: ").strip().capitalize()
        while not new_user_name.isalpha():
            self.clear()
            print("You made a mistake, Please try again")
            new_user_name = input("Enter your name: ").strip().capitalize()

        new_user_login = input("Enter your login: ").strip()
        while not new_user_login.isalnum():
            self.clear()
            print("You made a mistake, Please try again")
            new_user_login = input("Enter your login: ").strip()

        new_user_password = input("Enter your password: ").strip()
        new_user_check_password = input("Enter your check password: ").strip()
        while new_user_password == "" or new_user_password != new_user_check_password:
            self.clear()
            print("You made a mistake, Please try again")
            new_user_password = input("Enter your password: ").strip()
            new_user_check_password = input("Enter your check password: ").strip()

        new_user_age = input("Enter your age: ").strip()
        while not new_user_age.isdigit():
            self.clear()
            print("You made a mistake, Please try again")
            new_user_age = input("Enter your name: ").strip()

        self.name = new_user_name
        self.login = new_user_login
        self.password = new_user_password
        self.age = new_user_age
        self.writ_db()

    def writ_db(self):
        self.my_cursor.execute(f"insert into account(name, login, password, age)                  values ('{self.name}','{self.login}',"
                   f"'{self.password}', {self.age})")
        self.my_db.commit()

    def login_(self):
        pass

    def change_login_and_password(self):
        pass

    def delete_account(self):
        pass

    def log_out(self):
        pass



result = Login()
result.choice()









