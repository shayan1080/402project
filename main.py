import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QEvent,pyqtSignal  
import sqlite3
import addproduct,addmember,style
from PIL import Image
import threading

con=sqlite3.connect("costumer.db")
cur=con.cursor()



class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Manager")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,1400,750)
        self.setFixedSize(self.size())
        self.name = ''
        self.password = ''
        self.user_name = ''
        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.tabWigdet()
        self.widgets()
        self.layouts()
        self.displayProducts()
        self.displayMembers()
        
        # self.getStatistics()
        self.lbl = QLabel('username:',self)
        self.lbl.move(1000,20)
        print('username::::::::::',self.name)
        self.lbl1 = QLabel(self.name , self)
        self.lbl1.move(1010,20) 

    def toolBar(self):
        self.tb=self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        #####################Toolbar Buttons############
        ####################Add Product################
        self.addProduct=QAction(QIcon('icons/add.png'),"Add Product",self)
        self.tb.addAction(self.addProduct)
        self.addProduct.triggered.connect(self.funcAddProduct)
        self.tb.addSeparator()
        ######################Add Member################
        self.addMember=QAction(QIcon('icons/users.png'),"Add Member",self)
        self.tb.addAction(self.addMember)
        self.addMember.triggered.connect(self.funcAddMember)
        self.tb.addSeparator()
        ######################Sell Products###############
        # self.sellProduct = QAction(QIcon('icons/sell.png'),"Sell Product",self)
        # self.tb.addAction(self.sellProduct)
        # # self.sellProduct.triggered.connect(self.funcSellProducts)
        # self.tb.addSeparator()


    def tabWigdet(self):
        self.tabs=QTabWidget()
        self.tabs.blockSignals(True)
        self.tabs.currentChanged.connect(self.tabChanged)
        # self.tabs.currentChanged.connect(self.tabChanged)
        self.setCentralWidget(self.tabs)
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.tab4=QWidget()
        self.tabs.addTab(self.tab1,"Products")
        self.tabs.addTab(self.tab2,"Members")
        # self.tabs.addTab(self.tab3,"Statistics")
        # self.tabs.addTab(self.tab4,'Compare')


    def widgets(self):
        #######################Tab1 Widgets###############
        ####################Main left layout widget##########
        self.productsTable = QTableWidget()
        self.productsTable.setColumnCount(5)
        # self.productsTable.setColumnHidden(0,True)
    
        self.productsTable.setHorizontalHeaderItem(0,QTableWidgetItem("Product Name"))
        self.productsTable.setHorizontalHeaderItem(1,QTableWidgetItem("Manufacturer"))
        self.productsTable.setHorizontalHeaderItem(2,QTableWidgetItem("Price1"))
        self.productsTable.setHorizontalHeaderItem(3,QTableWidgetItem("Price2"))
        self.productsTable.setHorizontalHeaderItem(4,QTableWidgetItem("Price3"))


        self.productsTable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        # self.productsTable.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        # self.productsTable.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.productsTable.doubleClicked.connect(self.selectedProduct)


        ########################Right top layout widgets#######################
        self.searchText=QLabel("Search")
        self.searchEntry=QLineEdit()
        self.searchEntry.setPlaceholderText("Search For Products")
        self.searchButton=QPushButton("Search")
        self.searchButton.clicked.connect(self.searchProducts)
        self.searchButton.setStyleSheet(style.searchButtonStyle())
        ##########################Right middle layout widgets###########
        self.allProducts=QRadioButton("All Products")
        self.Laptop=QRadioButton("Laptop")
        self.Clock=QRadioButton("Clock")
        self.moblie=QRadioButton('Mobile')
        self.Airpod=QRadioButton('Airpod')
        self.Tablet=QRadioButton('Tablet')
        self.listButton=QPushButton("List")
        self.listButton.clicked.connect(self.listProducts)
        self.listButton.setStyleSheet(style.listButtonStyle())
        ########################Tab2 Widgets#########################
        self.membersTable=QTableWidget()
        self.membersTable.setColumnCount(1)
        # self.membersTable.setHorizontalHeaderItem(0,QTableWidgetItem("Member ID"))
        self.membersTable.setHorizontalHeaderItem(0,QTableWidgetItem("Member user_id"))
        self.updatebtn = QPushButton("update")
        self.updatebtn.clicked.connect(self.displayMembers)

        self.membersTable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        # self.membersTable.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        # self.membersTable.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.membersTable.doubleClicked.connect(self.selectedMember)
        # self.memberSearchText=QLabel("Search Members")
        # self.memberSearchEntry=QLineEdit()
        # self.memberSearchButton=QPushButton("Search")
        # self.memberSearchButton.clicked.connect(self.searchMembers)
        ##########################Tab3 widgets#####################
        self.totalProductsLabel=QLabel()
        self.totalMemberLabel=QLabel()
        self.soldProductsLabel=QLabel()
        self.totalAmountLabel=QLabel()


    def layouts(self):
        ######################Tab1 layouts##############
        self.mainLayout=QHBoxLayout()
        self.mainLeftLayout=QVBoxLayout()
        self.mainRightLayout=QVBoxLayout()
        self.rightTopLayout=QHBoxLayout()
        self.rightMiddleLayout=QHBoxLayout()
        self.topGroupBox=QGroupBox("Search Box")
        self.topGroupBox.setStyleSheet(style.searchBoxStyle())
        self.middleGroupBox=QGroupBox("List Box")
        self.middleGroupBox.setStyleSheet(style.listBoxStyle())
        self.bottomGroupBox=QGroupBox()
        #################Add widgets###################
        ################Left main layout widget###########
        self.mainLeftLayout.addWidget(self.productsTable)
        ########################Right top layout widgets#########
        self.rightTopLayout.addWidget(self.searchText)
        self.rightTopLayout.addWidget(self.searchEntry)
        self.rightTopLayout.addWidget(self.searchButton)
        self.topGroupBox.setLayout(self.rightTopLayout)
        #################Right middle layout widgets##########
        self.rightMiddleLayout.addWidget(self.allProducts)
        self.rightMiddleLayout.addWidget(self.Laptop)
        self.rightMiddleLayout.addWidget(self.Tablet)
        self.rightMiddleLayout.addWidget(self.moblie)
        self.rightMiddleLayout.addWidget(self.Clock)
        self.rightMiddleLayout.addWidget(self.Airpod)

        self.rightMiddleLayout.addWidget(self.listButton)
        self.middleGroupBox.setLayout(self.rightMiddleLayout)

        self.mainRightLayout.addWidget(self.topGroupBox,20)
        self.mainRightLayout.addWidget(self.middleGroupBox,20)
        self.mainRightLayout.addWidget(self.bottomGroupBox,60)
        self.mainLayout.addLayout(self.mainLeftLayout,70)
        self.mainLayout.addLayout(self.mainRightLayout,30)
        self.tab1.setLayout(self.mainLayout)
        ######################Tab2 Layouts#####################
        self.memberMainLayout=QHBoxLayout()
        self.memberLeftLayout=QHBoxLayout()
        self.memberRightLayout=QHBoxLayout()
        # self.memberRightGroupBox=QGroupBox("Search For Members")
        # self.memberRightGroupBox.setContentsMargins(10,10,10,600)
        # self.memberRightLayout.addWidget(self.memberSearchText)
        # self.memberRightLayout.addWidget(self.memberSearchEntry)
        # self.memberRightLayout.addWidget(self.memberSearchButton)
        # self.memberRightGroupBox.setLayout(self.memberRightLayout)

        self.memberLeftLayout.addWidget(self.membersTable)
        self.memberMainLayout.addLayout(self.memberLeftLayout,70)
        self.memberMainLayout.addWidget(self.updatebtn,10)
        # self.memberMainLayout.addWidget(self.memberRightGroupBox,30)
        self.tab2.setLayout(self.memberMainLayout)

        #####################Tab3 layouts########################
        # self.statisticsMainLayout=QVBoxLayout()
        # self.statisticsLayout=QFormLayout()
        # self.statisticsGroupBox=QGroupBox("Statistics")
        # self.statisticsLayout.addRow("Total Products:",self.totalProductsLabel)
        # self.statisticsLayout.addRow("Total Member:",self.totalMemberLabel)
        # self.statisticsLayout.addRow("Sold Products:",self.soldProductsLabel)
        # self.statisticsLayout.addRow("Total Amount:",self.totalAmountLabel)

        # self.statisticsGroupBox.setLayout(self.statisticsLayout)
        # self.statisticsGroupBox.setFont(QFont("Arial",20))
        # self.statisticsMainLayout.addWidget(self.statisticsGroupBox)
        # self.tab3.setLayout(self.statisticsMainLayout)
        # self.tabs.blockSignals(False)

        self.btn = QPushButton('Favorite',self)
        self.btn.move(990,46)
        self.btn.clicked.connect(self.showFavorite)



    def showFavorite(self):
        self.a = Favorite()
        self.a.show()

    def funcAddProduct(self):
        self.newProduct=addproduct.AddProduct()

    def funcAddMember(self):
        self.newMember=addmember.AddMember()

    def displayProducts(self):

        self.productsTable.setFont(QFont("Times", 12))
        for i in reversed(range(self.productsTable.rowCount())):
            self.productsTable.removeRow(i)

        query = cur.execute("SELECT product_name,product_manufacturer,price1,price2,price3 FROM mobile")
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)



        query = cur.execute("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Tablet")
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        query = cur.execute("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Airpod")
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)


        query = cur.execute("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Clock")
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
    
        query = cur.execute("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Laptop")
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def displayMembers(self):
        self.membersTable.setFont(QFont("Times",12))
        for i in reversed(range(self.membersTable.rowCount())):
            self.membersTable.removeRow(i)

        members=cur.execute("SELECT * FROM member")
        
        for row_data in members:
            row_number = self.membersTable.rowCount()
            self.membersTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.membersTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))

        self.membersTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.lbl = QLabel('username:',self)
        # self.lbl.move(1000,20)
        # self.lbl1 = QLabel(self.name , self)
        # self.lbl1.move(1010,20) 

    display_window = []
    def selectedProduct(self):
        global productId
        global product_name
        listProduct=[]
        for i in range(0,4):
            listProduct.append(self.productsTable.item(self.productsTable.currentRow(),i).text())

        productId=listProduct[1]
        product_name = listProduct[0]
        print(product_name)
        # print(productId)

        display = DisplayProduct()
        Main.display_window.append(display)  # Add the instance to the list
        display.show()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonDblClick and obj == self.widget:
            self.widget.handle_input()
        return super().eventFilter(obj, event)

    def selectedMember(self):
        global user_name

        # def handle_password(password):

        #     # Use the password as needed

        #     global user_name
        #     self.id = 0
        #     b= cur.execute(f"SELECT user_name FROM member WHERE password = '{password}'")
        #     b = list(b)
        #     self.name = self.membersTable.item(self.membersTable.currentRow(), self.id).text()
        #     if b != []:
        #         print('done')
        #         self.id = 0
        #         self.name = self.membersTable.item(self.membersTable.currentRow(), self.id).text()
        #         if self.name != b[0]:
        #             d = cur.execute(f"SELECT user_name FROM member WHERE user_id = '{self.name}'")
        #             self.updateNameLabel()
        #             d = list(d)
        #             self.user_name = d[0]
        #             self.name = d[0]
        #             # print(user_name)
                    
        #         else:
        #             QMessageBox.information(self, "Info", "wrong password")
        #     else:
        #         QMessageBox.information(self, "Info", "wrong password")

        
        self.widget = CustomWidget(self.handle_password)
        self.widget.show()

    def handle_password(self, password):


        global user_name
        self.id = 0
        b= cur.execute(f"SELECT user_name FROM member WHERE password = '{password}'")
        b = list(b)
        self.name = self.membersTable.item(self.membersTable.currentRow(), self.id).text()
        if b != []:
            print('done')
            self.id = 0
            self.name = self.membersTable.item(self.membersTable.currentRow(), self.id).text()
            if self.name != b[0]:
                d = cur.execute(f"SELECT user_name FROM member WHERE user_id = '{self.name}'")
                self.updateNameLabel()
                d = list(d)
                self.user_name = d[0][0]
                self.name = d[0][0]
                self.updateNameLabel()
                print('self.username:',self.user_name)
                
            else:
                QMessageBox.information(self, "Info", "wrong password")
        else:
            QMessageBox.information(self, "Info", "wrong password")

    def updateNameLabel(self):
        print('username:',self.name)
        
        # self.name = self.user_name
        self.lbl1.setText(self.name)
        self.lbl1.move(1065,20)


    def searchProducts(self):

        value=self.searchEntry.text()
        if value == "":
            QMessageBox.information(self,"Warning","Search query cant be empty!!!")

        else:
            results = []
            self.searchEntry.setText("")

            query=("SELECT product_name,product_manufacturer,price1,price2,price3 FROM mobile WHERE product_name LIKE ? or product_manufacturer LIKE ?")
            results1=cur.execute(query,('%' + value + '%','%' + value + '%')).fetchall()
            query=("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Airpod WHERE product_name LIKE ? or product_manufacturer LIKE ?")
            results2=cur.execute(query,('%' + value + '%','%' + value + '%')).fetchall()
            query=("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Tablet WHERE product_name LIKE ? or product_manufacturer LIKE ?")
            results3=cur.execute(query,('%' + value + '%','%' + value + '%')).fetchall()
            query=("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Clock WHERE product_name LIKE ? or product_manufacturer LIKE ?")
            results4=cur.execute(query,('%' + value + '%','%' + value + '%')).fetchall()
            query=("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Laptop WHERE product_name LIKE ? or product_manufacturer LIKE ?")
            results5=cur.execute(query,('%' + value + '%','%' + value + '%')).fetchall()
            results.extend(results1)
            results.extend(results3)
            results.extend(results2)
            results.extend(results5)
            results.extend(results4)


            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)
            for row_data in results:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(row_number,column_number,QTableWidgetItem(str(data))) 


    def listProducts(self):
        if self.allProducts.isChecked() == True:
            self.displayProducts()

        elif self.moblie.isChecked():
            query=("SELECT product_name,product_manufacturer,price1,price2,price3 FROM mobile")
            products=cur.execute(query).fetchall()


            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)

            for row_data in products:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        elif self.Tablet.isChecked():
            query=("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Tablet")
            products = cur.execute(query).fetchall()
 

            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)

            for row_data in products:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        elif self.Laptop.isChecked():
            query=("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Laptop")
            products = cur.execute(query).fetchall()
            

            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)

            for row_data in products:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        elif self.Clock.isChecked():
            query=("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Clock")
            products = cur.execute(query).fetchall()
            

            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)

            for row_data in products:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        elif self.Airpod.isChecked():
            query=("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Airpod")
            products = cur.execute(query).fetchall()
            

            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)

            for row_data in products:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def tabChanged(self):
        # self.getStatistics()
        self.displayProducts()
        self.displayMembers()


class CustomWidget(QWidget):
    def __init__(self, password_callback):
        super().__init__()
        self.password_callback = password_callback
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Double Click Window')
        layout = QVBoxLayout(self)

        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)
        self.text_input.setPlaceholderText('Enter password...')
        self.text_input.setEchoMode(QLineEdit.Password)
        button = QPushButton('Submit', self)
        layout.addWidget(button)
        button.clicked.connect(self.handle_input)

    def handle_input(self):
        password = self.text_input.text()
        self.password_callback(password)
        self.close()  

class DisplayProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Details")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,350,600)
        self.setFixedSize(self.size())
        self.UI()
        self.show()



    def UI(self):
        self.productDetails()
        print('hi:',self.productManufacturer)
        if self.productManufacturer == 'Mobile':
            self.productDetails()
            self.widgets()
            self.layouts()
            text1 = QLabel('name:',self)
            text1.move(20,385)
            tex1 = QLabel(self.productName,self)
            tex1.move(60,385)
            tex1.resize(200,30)
            text2 = QLabel('battery:',self)
            text2.move(20,400)
            tex2 = QLabel(self.battery,self)
            tex2.move(70,400)
            tex2.resize(130,25)
            text3 = QLabel('size:',self)
            text3.move(20,420)
            tex3 = QLabel(self.mobileSize,self)
            tex3.move(0,418)
            text4 = QLabel('cores:',self)
            text4.move(20,435)
            tex4 = QLabel(self.cores,self)
            tex4.move(10,435)
            text5 = QLabel('memory:',self)
            text5.move(20,455)
            tex5 = QLabel(self.memory , self)
            tex5.move(30,456)
            tex5.resize(200,25)
            text6 = QLabel('Ram:',self)
            text6.move(20,472)
            tex6 = QLabel(self.ram , self)
            tex6.move(40,476)
            tex6.resize(175,15)
            text7 = QLabel('weight:',self)
            text7.move(20,488)
            tex7 = QLabel(self.weight,self)
            tex7.move(25,488)
            text8 = QLabel('camera:',self)
            text8.move(20,505)
            tex8 = QLabel(self.camera,self)
            tex8.move(50,505)
            text9 = QLabel('operating system:',self)
            text9.move(20,525)
            text9.resize(140,20)
            tex9 = QLabel(self.operating,self)
            tex9.move(60,519)
            text10 = QLabel('colors:',self)
            text10.move(20,535)
            tex10 = QLabel(self.colors,self)
            tex10.move(70,542)
            tex10.resize(150 , 25)
            text11 = QLabel('Digikala:',self)
            text11.move(20,550)
            tex11 = QLabel(self.price1 , self)
            tex11.move(70,550)
            text12 = QLabel('Divar:',self)
            text12.move(20,565)
            tex12 = QLabel(self.price2,self)
            tex12.move(52,565)
            text13 = QLabel('Third Website:',self)
            text13.move(160,565)
            tex13 = QLabel(self.price3,self)
            tex13.move(250,565)
        if self.productManufacturer == 'Tablet':
            self.productDetails()
            self.widgets()
            self.layouts()
            text1 = QLabel('name:',self)
            text1.move(20,385)
            tex1 = QLabel(self.productName,self)
            tex1.move(60,385)
            tex1.resize(200,30)
            text2 = QLabel('battery:',self)
            text2.move(20,400)
            tex2 = QLabel(self.battery,self)
            tex2.move(70,400)
            tex2.resize(130,25)
            text3 = QLabel('size:',self)
            text3.move(20,420)
            tex3 = QLabel(self.mobileSize,self)
            tex3.move(0,418)
            text4 = QLabel('cores:',self)
            text4.move(20,437)
            tex4 = QLabel(self.cores,self)
            tex4.move(10,435)
            text5 = QLabel('memory:',self)
            text5.move(20,453)
            tex5 = QLabel(self.memory , self)
            tex5.move(33,455)
            tex5.resize(250,25)
            text6 = QLabel('Ram:',self)
            text6.move(20,472)
            tex6 = QLabel(self.ram , self)
            tex6.move(40,476)
            tex6.resize(175,15)
            text7 = QLabel('chip:',self)
            text7.move(20,488)
            tex7 = QLabel(self.chip,self)
            tex7.move(50,492)
            tex7.resize(250,20)
            text8 = QLabel('camera:',self)
            text8.move(20,505)
            tex8 = QLabel(self.camera,self)
            tex8.move(50,505)
            text9 = QLabel('material:',self)
            text9.move(20,520)
            # text9.resize(140,20)
            tex9 = QLabel(self.material,self)
            tex9.move(60,519)
            text10 = QLabel('colors:',self)
            text10.move(20,535)
            tex10 = QLabel(self.colors,self)
            tex10.move(70,542)
            tex10.resize(200 , 25)
            text11 = QLabel('Digikala:',self)
            text11.move(20,550)
            tex11 = QLabel(self.price1 , self)
            tex11.move(70,550)
            text12 = QLabel('Divar:',self)
            text12.move(20,565)
            tex12 = QLabel(self.price2,self)
            tex12.move(52,565)
            text13 = QLabel('Third Website:',self)
            text13.move(160,565)
            tex13 = QLabel(self.price3,self)
            tex13.move(250,565)

        if self.productManufacturer == 'Airpod':
            self.productDetails()
            self.widgets()
            self.layouts()
            text1 = QLabel('name:',self)
            text1.move(20,385)
            tex1 = QLabel(self.productName,self)
            tex1.move(60,385)
            tex1.resize(200,30)
            text2 = QLabel('type:',self)
            text2.move(20,400)
            tex2 = QLabel(self.type,self)
            tex2.move(50,400)
    
            text3 = QLabel('acostic_type:',self)
            text3.move(20,420)
            tex3 = QLabel(self.acostic,self)
            tex3.move(45,425)
            tex3.resize(200,20)
            text4 = QLabel('connection:',self)
            text4.move(20,437)
            tex4 = QLabel(self.connection,self)
            tex4.move(40,435)
            # text5 = QLabel('airpod_type:',self)
            # text5.move(20,453)
            # tex5 = QLabel(self.airpodType , self)
            # tex5.move(40,455)
            # tex5.resize(350,25)
            text6 = QLabel('noisecancelling:',self)
            text6.move(20,472)
            tex6 = QLabel(self.noiseCancelling , self)
            tex6.move(40,472)

            text7 = QLabel('blutooth:',self)
            text7.move(20,488)
            tex7 = QLabel(self.blutooth,self)
            tex7.move(70,488)
            # tex7.resize(250,20)
            text8 = QLabel('color:',self)
            text8.move(20,505)
            tex8 = QLabel(self.color,self)
            tex8.move(50,507)
            tex8.resize(120,20)
            text11 = QLabel('Digikala:',self)
            text11.move(20,550)
            tex11 = QLabel(self.price1 , self)
            tex11.move(70,550)
            text12 = QLabel('Divar:',self)
            text12.move(20,565)
            tex12 = QLabel(self.price2,self)
            tex12.move(52,565)
            text13 = QLabel('Third Website:',self)
            text13.move(20,535)
            tex13 = QLabel(self.price3,self)
            tex13.move(110,535)

        if self.productManufacturer == 'Clock':
            self.productDetails()
            self.widgets()
            self.layouts()
            text1 = QLabel('name:',self)
            text1.move(20,385)
            tex1 = QLabel(self.productName,self)
            tex1.move(60,385)
            tex1.resize(200,30)
            text2 = QLabel('screen_type:',self)
            text2.move(20,400)
            tex2 = QLabel(self.screenType,self)
            tex2.move(90,400)
    
            text3 = QLabel('screen_size:',self)
            text3.move(20,420)
            tex3 = QLabel(self.screenSize,self)
            tex3.move(45,420)
 
            text4 = QLabel('resolution:',self)
            text4.move(20,437)
            tex4 = QLabel(self.resolution,self)
            tex4.move(100,435)
            tex4.resize(100,25)
            text5 = QLabel('color:',self)
            text5.move(20,453)
            tex5 = QLabel(self.color , self)
            tex5.move(50,453)
            tex5.resize(200,25)
            text6 = QLabel('weight:',self)
            text6.move(20,472)
            tex6 = QLabel(self.weight , self)
            tex6.move(80,472)
            tex6.resize(120,25)

            text7 = QLabel('battery:',self)
            text7.move(20,493)
            tex7 = QLabel(self.battery,self)
            tex7.move(25,482)
            tex7.resize(310,50)
            text8 = QLabel('dimension:',self)
            text8.move(20,520)
            tex8 = QLabel(self.dimension,self)
            tex8.move(90,523)
            tex8.resize(170,20)
            text11 = QLabel('Digikala:',self)
            text11.move(20,550)
            tex11 = QLabel(self.price1 , self)
            tex11.move(70,550)
            text12 = QLabel('Divar:',self)
            text12.move(20,565)
            tex12 = QLabel(self.price2,self)
            tex12.move(52,565)
            text13 = QLabel('Third Website:',self)
            text13.move(20,535)
            tex13 = QLabel(self.price3,self)
            tex13.move(110,535)

        if self.productManufacturer == 'Laptop':
            self.productDetails()
            self.widgets()
            self.layouts()
            text1 = QLabel('name:',self)
            text1.move(20,385)
            tex1 = QLabel(self.productName,self)
            tex1.move(60,385)
            tex1.resize(200,30)
            text2 = QLabel('size:',self)
            text2.move(20,400)
            tex2 = QLabel(self.laptopSize,self)
            tex2.move(40,400)
            tex2.resize(220,25)
            text3 = QLabel('weight:',self)
            text3.move(20,420)
            tex3 = QLabel(self.weight,self)
            tex3.move(40,418)
            text4 = QLabel('ram:',self)
            text4.move(20,435)
            tex4 = QLabel(self.ram,self)
            tex4.move(20,435)
            text5 = QLabel('memory:',self)
            text5.move(20,455)
            tex5 = QLabel(self.memory , self)
            tex5.move(50,456)
            # tex5.resize(200,25)
            text6 = QLabel('battery:',self)
            text6.move(20,472)
            tex6 = QLabel(self.battery , self)
            tex6.move(30,476)
            tex6.resize(300,15)
            text7 = QLabel('screen_size:',self)
            text7.move(20,488)
            tex7 = QLabel(self.screenSize,self)
            tex7.move(50,488)
            text8 = QLabel('processor:',self)
            text8.move(20,505)
            tex8 = QLabel(self.processor,self)
            tex8.move(90,507)
            tex8.resize(150,20)
            text9 = QLabel('resolution:',self)
            text9.move(20,520)
            # text9.resize(140,20)
            tex9 = QLabel(self.resolution,self)
            tex9.move(80,520)
            text10 = QLabel('Digikala:',self)
            text10.move(20,535)
            tex10 = QLabel(self.price1,self)
            tex10.move(70,535)
            # tex10.resize(150 , 25)
            text11 = QLabel('Divar:',self)
            text11.move(20,550)
            tex11 = QLabel(self.price2 , self)
            tex11.move(70,550)
            text12 = QLabel('Third Website:',self)
            text12.move(20,565)
            tex12 = QLabel(self.price3,self)
            tex12.move(120,565)

    def productDetails(self):
        global productId
        print('aaaaaaaaaaaa:',productId)
        print('productname',product_name)
        if productId == 'Mobile':
            query=("SELECT * FROM mobile WHERE product_name=?")
            product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,)
            # print("product",product)
            self.productName=product[0]
            self.productManufacturer=product[1]
            self.battery = product[2]
            self.mobileSize = product[3]
            self.cores = product[4]
            self.memory = product[5]
            self.ram = product[6]
            self.weight = product[7]
            self.camera = product[8]
            self.operating = product[9]
            self.colors = product[10]
            self.price1 = product[11]
            self.price2 = product[12]
            self.price3 = product[13]

        if productId == 'Tablet':
            query=("SELECT * FROM Tablet WHERE product_name=?")
            product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,)
            self.productName=product[0]
            self.productManufacturer=product[1]
            self.battery = product[2]
            self.mobileSize = product[3]
            self.cores = product[4]
            self.memory = product[5]
            self.ram = product[6]
            self.chip = product[7]
            self.camera = product[8]
            self.material = product[9]
            self.colors = product[10]
            self.price1 = product[11]
            self.price2 = product[12]
            self.price3 = product[13]

        if productId == 'Airpod':
            query=("SELECT * FROM Airpod WHERE product_name=?")
            product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,)
            self.productName=product[0]
            self.productManufacturer=product[1]
            self.type = product[2]
            self.acostic = product[3]
            self.connection = product[4]
            self.airpodType = product[5]
            self.noiseCancelling = product[6]
            self.blutooth = product[7]
            self.color = product[8]
            self.price1 = product[9]
            self.price2 = product[10]
            self.price3 = product[11]

        if productId == 'Clock':
            query=("SELECT * FROM Clock WHERE product_name=?")
            product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,)
            self.productName=product[0]
            self.productManufacturer=product[1]
            self.screenType = product[2]
            self.screenSize = product[3]
            self.resolution = product[4]
            self.weight = product[5]
            self.battery = product[6]
            self.dimension = product[7]
            self.color = product[8]
            self.price1 = product[9]
            self.price2 = product[10]
            self.price3 = product[11]  

        if productId == 'Laptop':
            query=("SELECT * FROM Laptop WHERE product_name=?")
            product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,)
            self.productName=product[0]
            self.productManufacturer=product[1]
            self.laptopSize = product[2]
            self.weight = product[3]
            self.ram = product[4]
            self.memory = product[5]
            self.battery = product[6]
            self.screenSize = product[7]
            self.processor = product[8]
            self.resolution = product[9]
            self.price1 = product[10]
            self.price2 = product[11]
            self.price3 = product[12]

        # self.productName=product[0]
        # self.productManufacturer=product[1]

        # self.productPrice=product[3]
        print('self.productname',self.productName)
        # self.productQouta=product[4]
        # self.productImg=product[5]
        # self.productStatus=product[6]



    def widgets(self):
        #################Top layouts wigdets#########
        self.product_Img=QLabel(self)
        self.product_Img.setPixmap(QPixmap('a.png'))
        self.product_Img.move(100,100)
        self.product_Img.resize(300,300)
        # self.img=QPixmap('img/{}'.format(self.productImg))
        # self.product_Img.setPixmap(self.img)
        # self.product_Img.setAlignment(Qt.AlignCenter)
        self.titleText=QLabel("Update Product")
        # self.titleText.setAlignment(Qt.AlignCenter)
        # print('ggggg:',self.productManufacturer)

        ##############Bottom Layout's widgets###########
        # self.nameEntry=QLineEdit()
        # self.nameEntry.setText(self.productName)
        # self.manufacturerEntry=QLineEdit()
        # self.manufacturerEntry.setText(self.productManufacturer)
        # self.priceEntry=QLineEdit()
        # self.priceEntry.setText(str(self.productPrice))
        # self.qoutaEntry=QLineEdit()
        # self.qoutaEntry.setText(str(self.productQouta))
        # self.availabilityCombo=QComboBox()
        # self.availabilityCombo.addItems(["Available","UnAvailable"])
        # self.uploadBtn=QPushButton("Upload")
        # self.uploadBtn.clicked.connect(self.uploadImg)
        self.addFavoritebtn=QPushButton("add to favorite")
        self.addFavoritebtn.clicked.connect(self.favoriteProduct)
        # self.updateBtn=QPushButton("Update")
        # self.updateBtn.clicked.connect(self.updateProduct)
        # self.text = QLabel()
        # self.text.setText(self.productName)




    def layouts(self):
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout=QFormLayout()
        self.topFrame=QFrame()
        # self.topFrame.setStyleSheet(style.productTopFrame())
        self.bottomFrame=QFrame()
        self.bottomFrame.setStyleSheet(style.productBottomFrame())
        ###############add widgets###########
        # self.topLayout.addWidget(self.titleText)
        # self.topLayout.addWidget(self.product_Img)
        self.topFrame.setLayout(self.topLayout)
        # self.bottomLayout.addRow(QLabel("Name: "),self.nameEntry)
        # self.bottomLayout.addRow(QLabel("Manufacturer: "),self.manufacturerEntry)
        # self.bottomLayout.addRow(QLabel("Price: "),self.priceEntry)
        # self.bottomLayout.addRow(QLabel("Qouta: "),self.qoutaEntry)
        # self.bottomLayout.addRow(QLabel("Status: "),self.availabilityCombo)
        # self.bottomLayout.addRow(QLabel("Image: "),self.uploadBtn)
       
        self.bottomLayout.addRow(QLabel(""),self.addFavoritebtn)
        # self.bottomLayout.addRow(QLabel(""),self.updateBtn)
        self.bottomFrame.setLayout(self.bottomLayout)
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)


        self.setLayout(self.mainLayout)


    def favoriteProduct(self):
        global favoriteProductsName
        
        favoriteProductsName = self.productName
        query = cur.execute('SELECT product_manufacturer FROM mobile WHERE product_name = ?',(favoriteProductsName,)).fetchone()
 
        try:
            print('username',user_name)
            print('FavoriteProcductname:',favoriteProductsName)
            query = cur.execute('SELECT product_manufacturer FROM mobile WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            print('query[0]:',query)
            if query != None:
                if query[0] == 'Mobile':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(user_name,)).fetchone()
                    print('favaorite column:',a)
            query = cur.execute('SELECT product_manufacturer FROM Tablet WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            print('none type:',query)
            if query != None:
                if query[0] == 'Tablet':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(user_name,)).fetchone()
                    print('favaorite column:',a)
            query = cur.execute('SELECT product_manufacturer FROM Airpod WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            if query != None:
                if query[0] == 'Airpod':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(user_name,)).fetchone()
                    print('favaorite column:',a)

            query = cur.execute('SELECT product_manufacturer FROM Clock WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            if query != None:
                if query[0] == 'Clock':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(user_name,)).fetchone()
                    print('favaorite column:',a)

            query = cur.execute('SELECT product_manufacturer FROM Laptop WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            if query != None:
                if query[0] == 'Laptop':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(user_name,)).fetchone()
                    print('favaorite column:',a)


            if a[0] == None:
                favoriteProductsName = self.productName
            else:
                favoriteProductsName = a[0] + ','+ self.productName
            cur.execute(f'UPDATE member SET favorite= ? WHERE user_name = ?',(favoriteProductsName,user_name))
            con.commit()
        except :

            QMessageBox.information(self, "Info", "log in to your panel first")
        # query = "SELECT * FROM mobile WHERE product_name = ?"
        # cur.execute(query, (self.name,))
        # favoriteProducts = cur.fetchone()


#         else:
#             QMessageBox.information(self, "Info", "Fields can not be empty!")


        
class Favorite(QWidget):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Product Details")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(455,150,900,600)
        self.setFixedSize(self.size())
        self.UI()
        self.show()
    
    def UI(self):

        self.wigdet()
        self.layouts()
        self.displayProducts()
    

    def wigdet(self):
        self.productsTable = QTableWidget(self)
        self.productsTable.setColumnCount(5)
        # self.productsTable.setColumnHidden(0,True)
    
        self.productsTable.setHorizontalHeaderItem(0,QTableWidgetItem("Product Name"))
        self.productsTable.setHorizontalHeaderItem(1,QTableWidgetItem("Manufacturer"))
        self.productsTable.setHorizontalHeaderItem(2,QTableWidgetItem("Digikala"))
        self.productsTable.setHorizontalHeaderItem(3,QTableWidgetItem("Divar"))
        self.productsTable.setHorizontalHeaderItem(4,QTableWidgetItem("Third Website"))


        self.productsTable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        # self.productsTable.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.productsTable.doubleClicked.connect(self.selectedProduct)
    
    def layouts(self):

        self.mainLayout=QHBoxLayout(self)
        
        self.mainLayout.addWidget(self.productsTable)

    def displayProducts(self):

        self.productsTable.setFont(QFont("Times", 12))
        # for i in reversed(range(self.productsTable.rowCount())):
        #     self.productsTable.removeRow(i)

        # query = cur.execute('''SELECT product_id, product_name, product_manufacturer, product_price FROM mobile''')
        # query = "SELECT * FROM mobile WHERE product_name = ?"
        # qry = cur.execute(query, (favoriteProductsName,))
        try:
            query = cur.execute('SELECT favorite FROM member WHERE user_name=?',(user_name,)).fetchone()
            lis = query[0].split(',')
            lis = set(lis)
            lis = list(lis)
            print('lis',lis)
            for item in lis:
                query = cur.execute('SELECT product_manufacturer FROM mobile WHERE product_name = ?',(item,)).fetchone()
                if query != None:
                    if query[0] == 'Mobile':
                        query = cur.execute('SELECT product_name,product_manufacturer,price1,price2,price3 FROM mobile WHERE product_name = ?',(item,))
                        for row_data in query:
                            row_number = self.productsTable.rowCount()
                            self.productsTable.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                query = cur.execute('SELECT product_manufacturer FROM Tablet WHERE product_name = ?',(item,)).fetchone()
                if query != None:
                    if query[0] == 'Tablet':
                        query = cur.execute('SELECT product_name,product_manufacturer,price1,price2,price3 FROM Tablet WHERE product_name = ?',(item,))
                        for row_data in query:
                            row_number = self.productsTable.rowCount()
                            self.productsTable.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                query = cur.execute('SELECT product_manufacturer FROM Airpod WHERE product_name = ?',(item,)).fetchone()
                if query != None:
                    if query[0] == 'Airpod':
                        query = cur.execute('SELECT product_name,product_manufacturer,price1,price2,price3 FROM Airpod WHERE product_name = ?',(item,))
                        for row_data in query:
                            row_number = self.productsTable.rowCount()
                            self.productsTable.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                query = cur.execute('SELECT product_manufacturer FROM Clock WHERE product_name = ?',(item,)).fetchone()
                if query != None:
                    if query[0] == 'Clock':
                        query = cur.execute('SELECT product_name,product_manufacturer,price1,price2,price3 FROM Clock WHERE product_name = ?',(item,))
                        for row_data in query:
                            row_number = self.productsTable.rowCount()
                            self.productsTable.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                query = cur.execute('SELECT product_manufacturer FROM Laptop WHERE product_name = ?',(item,)).fetchone()
                if query != None:
                    if query[0] == 'Laptop':
                        query = cur.execute('SELECT product_name,product_manufacturer,price1,price2,price3 FROM Laptop WHERE product_name = ?',(item,))
                        for row_data in query:
                            row_number = self.productsTable.rowCount()
                            self.productsTable.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        except :
            pass

        

    def selectedProduct(self):
        global productId
        global product_name
        
        listProduct=[]
        for i in range(0,4):
            listProduct.append(self.productsTable.item(self.productsTable.currentRow(),i).text())

        productId=listProduct[1]
        product_name = listProduct[0]
        print('ssssssssS:',productId)
        print('line881:',product_name)

        self.display = DisplayProduct()

        self.display.show()

def main():
    App=QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()

    