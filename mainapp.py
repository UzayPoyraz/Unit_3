from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QTableWidgetItem
import sys

from untitled2 import Ui_MainWindow as mainW
from login import Ui_Dialog as loginD
from register import Ui_Dialog as regD
from Draftsketch1 import Ui_list as listD
import csv

import hashlib, binascii, os


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64: -1]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


class mainWindowApp(QMainWindow, mainW):
    def __init__(self, parent=None):
        super(mainWindowApp, self).__init__(parent)
        self.setupUi(self)
        self.list_button.clicked.connect(self.listapplication)
        self.exit.clicked.connect(self.exitApp)
        logVar = logInApp(self)
        logVar.show()
    def exitApp(self):
        logVar = logInApp(self)
        logVar.show()

    def listapplication(self):
        listvar = listApp(self)
        listvar.show()


class logInApp(loginD):
    def __init__(self, parent=None):
        super(logInApp, self).__init__(parent)
        self.setupUi(self)

        self.exit.clicked.connect(self.exitApp)
        self.register_2.clicked.connect(self.regApp)
        self.confirm.clicked.connect(self.try_login)

    def exitApp(self):
        sys.exit(0)

    def regApp(self):
        regVar = registerApp(self)
        regVar.show()

    def try_login(self):
        username = self.username.text()
        password = self.password.text()
        print("Hashing", username + password)
        correct_password = username + password
        with open('Output.txt', "r") as output_file:
            for stored_password in output_file:
                if verify_password(stored_password, correct_password):
                    self.username.setStyleSheet("border: 3px solid green")
                    self.password.setStyleSheet("border: 3px solid green")
                    self.close()

                else:
                    self.username.setStyleSheet("border: 3px solid red")
                    self.password.setStyleSheet("border: 3px solid red")

    def users(self):
        userVar = mainWindowApp(self)
        userVar.show()

    def loginapp(self):
        logVar = logInApp(self)
        logVar.show()


class registerApp(regD):
    def __init__(self, parent=None):
        super(registerApp, self).__init__(parent)
        self.setupUi(self)

        self.mainpage_1.clicked.connect(self.exitApp)
        self.reg_1.clicked.connect(self.try_register)

    def exitApp(self):
        sys.exit(0)

    def try_register(self):
        if self.validate_registration():
            self.store()
            self.close()

    def store(self):
        username = self.username_1.text()
        password = self.pass_1.text()
        print("Hashing", username + password)
        msg = hash_password(username + password)
        with open('Output.txt', "a") as output_file:
            output_file.write('{}\n'.format(msg))
        self.close()

    def password_validation(self):
        password = self.pass_1.text()
        confpass = self.pass_2.text()
        if password != confpass:
            self.pass_1.setStyleSheet("border: 3px solid red")
            self.pass_2.setStyleSheet("border: 3px solid red")
            return False
        else:
            self.pass_1.setStyleSheet("border: 3px solid green")
            self.pass_2.setStyleSheet("border: 3px solid green")
            return True

    def validate_registration(self):
        username = self.username_1.text()
        password = self.password_validation()
        print(username, password)
        return username and password

    def users(self):
        userVar = mainWindowApp
        userVar.show()


class listApp(listD):
    def __init__(self, parent=None):
        super(listApp, self).__init__(parent)
        self.setupUi(self)

        self.exit.clicked.connect(self.exitApp)
        self.data = self.load_data()
        self.tableWidget.cellChanged.connect(self.changeDB)
        self.changes_btn.setDisabled(False)
        self.revert_btn.setDisabled(False)
        self.changes_btn.clicked.connect(self.save)
        self.revert_btn.clicked.connect(self.cancel)

    def load_data(self):
        data = []
        with open('data.csv') as database:
            file = csv.reader(database, delimiter=",")
            for o, row in enumerate(file):
                for l, col in enumerate(row):
                    data.append([o, l, col])
                    self.tableWidget.setItem(o, l, QTableWidgetItem(col))

        return data

    def exitApp(self):
        MainVar = mainWindowApp(self)
        MainVar.show()
    def changeDB(self):
        item = self.tableWidget.currentItem()
        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        self.tableWidget.item(row, col).setBackground(QtGui.QColor(255, 255, 255))
        print(item.text())

    def save(self):
        with open("data.csv", "w", newline="") as database:
            file = csv.writer(database)
            rowc = self.tableWidget.rowCount()
            colc = self.tableWidget.colorCount()
            for row in range (rowc):
                line = []
                for col in range(colc):
                    data = self.tableWidget.item(row, col)
                    if data is not None:
                        line.append(data.text())
                file.writerow(line)

    def cancel(self):
        print("Reload the table")
        self.load_data()


container = QApplication(sys.argv)
main = mainWindowApp()
main.show()
container.exec_()


