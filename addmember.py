import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
from PIL import Image


con=sqlite3.connect("costumer.db")
cur=con.cursor()



defaultImg="store.png"

class AddMember(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Member")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,350,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()


    def widgets(self):
        #############widgets of top layout###########
        self.addMemberImg=QLabel()
        self.img=QPixmap('icons/addmember.png')
        self.addMemberImg.setPixmap(self.img)
        self.addMemberImg.setAlignment(Qt.AlignCenter)
        self.titleText=QLabel("Add Member")
        self.titleText.setAlignment(Qt.AlignCenter)
        ############widgets of bottom layout############
        self.userName=QLineEdit()
        self.userName.setPlaceholderText("Enter name of member")
        self.user_id=QLineEdit()
        self.user_id.setPlaceholderText("enter your id")
        self.password= QLineEdit()
        self.password.setPlaceholderText("Enter password of member")
        self.password.setEchoMode(QLineEdit.Password)
        self.submitBtn=QPushButton("Submit")
        self.submitBtn.clicked.connect(self.addMember)


    def layouts(self):
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout=QFormLayout()
        self.topFrame=QFrame()
        self.bottomFrame=QFrame()
        #############add widgets############
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.addMemberImg)
        self.topFrame.setLayout(self.topLayout)
        self.bottomLayout.addRow(QLabel("user_name: "),self.userName)
        self.bottomLayout.addRow(QLabel("user_id: "),self.user_id)
        self.bottomLayout.addRow(QLabel("Password: "),self.password)
        self.bottomLayout.addRow(QLabel(""),self.submitBtn)
        self.bottomFrame.setLayout(self.bottomLayout)

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        self.setLayout(self.mainLayout)

    def addMember(self):

        user_name = self.userName.text()
        password = self.password.text()


        if (user_name and password !=""):

            try:
                query ="INSERT INTO 'member' (user_id,user_name,password) VALUES(?,?,?)"
                cur.execute(query,(self.user_id.text(),user_name,password))
                con.commit()
                QMessageBox.information(self,"Info","Member has been added!")
                self.userName.setText("")
                self.password.setText("")
                self.user_id.setText("")
            
            except:
            
                QMessageBox.information(self, "Info", "Member has not been added!")

        else:
            QMessageBox.information(self, "Info", "Fields can not be empty!")
