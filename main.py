import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QEvent
import sqlite3
import addproduct,addmember,style
import webbrowser
import dinamicsearch

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
        self.lbl = QLabel('username:',self)
        self.lbl.move(1000,20)
        self.lbl1 = QLabel(self.name , self)
        self.lbl1.move(1010,20) 

    def toolBar(self):
        self.tb=self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        #####################Toolbar Buttons############
        ####################Add Product################
        self.addProduct=QAction(QIcon('icons/add.png'),"Search for a link results",self)
        self.tb.addAction(self.addProduct)
        self.addProduct.triggered.connect(self.funcAddProduct)
        self.tb.addSeparator()
        ######################Add Member################
        self.addMember=QAction(QIcon('icons/users.png'),"Add Member",self)
        self.tb.addAction(self.addMember)
        self.addMember.triggered.connect(self.funcAddMember)
        self.tb.addSeparator()

    def tabWigdet(self):
        self.tabs=QTabWidget()
        self.tabs.blockSignals(True)
        self.tabs.currentChanged.connect(self.tabChanged)
        self.setCentralWidget(self.tabs)
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.tab4=QWidget()
        self.tabs.addTab(self.tab1,"Products")
        self.tabs.addTab(self.tab2,"Members")

    def widgets(self):
        #######################Tab1 Widgets###############
        ####################Main left layout widget##########
        self.productsTable = QTableWidget()
        self.productsTable.setColumnCount(5)
        self.productsTable.setHorizontalHeaderItem(0,QTableWidgetItem("Product Name"))
        self.productsTable.setHorizontalHeaderItem(1,QTableWidgetItem("Manufacturer"))
        self.productsTable.setHorizontalHeaderItem(2,QTableWidgetItem("Price1"))
        self.productsTable.setHorizontalHeaderItem(3,QTableWidgetItem("Price2"))
        self.productsTable.setHorizontalHeaderItem(4,QTableWidgetItem("Price3"))
        self.productsTable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)

        self.productsTable.doubleClicked.connect(self.selectedProduct)

        ########################Right top layout widgets#######################
        self.searchText=QLabel("Search")
        self.searchEntry=QLineEdit()
        self.searchEntry.setPlaceholderText("Search For Products")
        self.searchButton=QPushButton("Search")
        self.searchButton.clicked.connect(self.searchProducts)

        self.suggestionText = QLabel("Suggestions:")
        self.suggestionEntry = QLineEdit()
        self.suggestionEntry.setPlaceholderText("Enter a price1-price2-category(e.g:4000000-5000000-mobile)")
        self.suggestionButton = QPushButton("Suggest")
        self.suggestionButton.clicked.connect(self.suggest)
        self.suggestionButton.setStyleSheet(style.suggestionBtnStyle())
        self.search = QLabel("Search Online:")
        self.searchOnlineEntry = QLineEdit()
        self.searchOnlineEntry.setPlaceholderText("give a link")
        self.searchOnlineBtn = QPushButton("Find link")
        self.searchOnlineBtn.clicked.connect(self.searchlink)
        self.searchOnlineBtn.setStyleSheet(style.suggestionBtnStyle())
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
        self.membersTable.setHorizontalHeaderItem(0,QTableWidgetItem("Member user_id"))
        self.updatebtn = QPushButton("update")
        self.updatebtn.clicked.connect(self.displayMembers)
        self.membersTable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.membersTable.doubleClicked.connect(self.selectedMember)
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
        self.rightDownLayout =QHBoxLayout()
        self.rightUplayout = QHBoxLayout()
        self.topGroupBox=QGroupBox("Search Box")
        self.topGroupBox.setStyleSheet(style.searchBoxStyle())
        self.middleGroupBox=QGroupBox("List Box")
        self.middleGroupBox.setStyleSheet(style.listBoxStyle())
        self.downGroupbox = QGroupBox('Suggestion')
        self.searchOnline = QGroupBox('Search for a link')
        self.bottomGroupBox=QGroupBox()
        self.searchOnline.setStyleSheet(style.suggestionBoxStyle())
        #################Add widgets###################
        ################Left main layout widget###########
        self.mainLeftLayout.addWidget(self.productsTable)
        self.rightDownLayout.addWidget(self.suggestionText)
        self.rightDownLayout.addWidget(self.suggestionEntry)
        self.rightDownLayout.addWidget(self.suggestionButton)

        self.rightUplayout.addWidget(self.search)
        self.rightUplayout.addWidget(self.searchOnlineEntry)
        self.rightUplayout.addWidget(self.searchOnlineBtn)
        self.searchOnline.setLayout(self.rightUplayout)
        
        self.downGroupbox.setLayout(self.rightDownLayout)
        self.mainRightLayout.addWidget(self.downGroupbox,20)
        self.mainRightLayout.addWidget(self.searchOnline,20)
        self.downGroupbox.setStyleSheet(style.searchOnlineBoxStyle())
        
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

        self.memberLeftLayout.addWidget(self.membersTable)
        self.memberMainLayout.addLayout(self.memberLeftLayout,70)
        self.memberMainLayout.addWidget(self.updatebtn,10)
 
        self.tab2.setLayout(self.memberMainLayout)

        self.btn = QPushButton('Favorite',self)
        self.btn.move(990,46)
        self.btn.clicked.connect(self.showFavorite)


    def searchlink(self):
        x = self.searchOnlineEntry.text()
        dinamicsearch.search(x)

    def suggest(self):
        lis = []
        x = self.suggestionEntry.text()
        x = x.split('-')
        price1,price2 =int(x[0]),int(x[1])
        productName = x[2]
        productName = productName.lower()
        if productName == 'mobile':
            res = cur.execute('SELECT price2 FROM mobile')
            res = list(res)
            for tup in res:
                for item in tup:
                    i = int(item.replace(',', ''))
                    if i >= price1 and price2 >= i:
                        lis.append(item)

            self.productsTable.setFont(QFont("Times", 12))
            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)
            
            for item in lis:
                query = cur.execute('SELECT product_name,product_manufacturer,price1,price2,price3 FROM mobile WHERE price2 = ?',(item,))
                for row_data in query:
                    row_number = self.productsTable.rowCount()
                    self.productsTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        if productName == 'tablet':
            res = cur.execute('SELECT price2 FROM Tablet')
            res = list(res)
            for tup in res:
                for item in tup:
                    i = int(item.replace(',', ''))
                    if i >= price1 and price2 >= i:
                        lis.append(item)

            self.productsTable.setFont(QFont("Times", 12))
            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)
            
            for item in lis:
                query = cur.execute('SELECT product_name,product_manufacturer,price1,price2,price3 FROM Tablet WHERE price2 = ?',(item,))
                for row_data in query:
                    row_number = self.productsTable.rowCount()
                    self.productsTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        if productName == 'laptop':
            res = cur.execute('SELECT price2 FROM Laptop')
            res = list(res)
            for tup in res:
                for item in tup:
                    i = int(item.replace(',', ''))
                    if i >= price1 and price2 >= i:
                        lis.append(item)
        
            self.productsTable.setFont(QFont("Times", 12))
            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)
            
            for item in lis:
                query = cur.execute('SELECT product_name,product_manufacturer,price1,price2,price3 FROM Laptop WHERE price2 = ?',(item,))
                for row_data in query:
                    row_number = self.productsTable.rowCount()
                    self.productsTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)      
            
        if productName == 'airpod':
            res = cur.execute('SELECT price2 FROM Airpod')
            res = list(res)
            for tup in res:
                for item in tup:
                    i = int(item.replace(',', ''))
                    if i >= price1 and price2 >= i:
                        lis.append(item)
        
            self.productsTable.setFont(QFont("Times", 12))
            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)
            
            for item in lis:
                query = cur.execute('SELECT product_name,product_manufacturer,price1,price2,price3 FROM Airpod WHERE price2 = ?',(item,))
                for row_data in query:
                    row_number = self.productsTable.rowCount()
                    self.productsTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        if productName == 'clock':
            res = cur.execute('SELECT price2 FROM Clock')
            res = list(res)
            for tup in res:
                for item in tup:
                    i = int(item.replace(',', ''))
                    if i >= price1 and price2 >= i:
                        lis.append(item)
       
            self.productsTable.setFont(QFont("Times", 12))
            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)
            
            for item in lis:
                query = cur.execute('SELECT product_name,product_manufacturer,price1,price2,price3 FROM Clock WHERE price2 = ?',(item,))
                for row_data in query:
                    row_number = self.productsTable.rowCount()
                    self.productsTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
    def showFavorite(self):
        self.a = Favorite()
        self.a.show()

    def funcAddProduct(self):
        self.newProduct=addproduct.SearchByLink()

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

    display_window = []
    def selectedProduct(self):
        global productId
        global product_name
        listProduct=[]
        for i in range(0,4):
            listProduct.append(self.productsTable.item(self.productsTable.currentRow(),i).text())

        productId=listProduct[1]
        product_name = listProduct[0]

        display = DisplayProduct()
        Main.display_window.append(display)  # Add the instance to the list
        display.show()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonDblClick and obj == self.widget:
            self.widget.handle_input()
        return super().eventFilter(obj, event)

    def selectedMember(self):        
        self.widget = CustomWidget(self.handle_password)
        self.widget.show()

    def handle_password(self, password):

        self.id = 0
        b= cur.execute(f"SELECT user_name FROM member WHERE password = '{password}'")
        b = list(b)
        self.name = self.membersTable.item(self.membersTable.currentRow(), self.id).text()
        if b != []:
            self.id = 0
            self.name = self.membersTable.item(self.membersTable.currentRow(), self.id).text()
            if self.name != b[0]:
                d = cur.execute(f"SELECT user_name FROM member WHERE user_id = '{self.name}'")
                self.updateNameLabel()
                d = list(d)
                self.user_name = d[0][0]
                self.name = d[0][0]
                self.updateNameLabel()
                
            else:
                QMessageBox.information(self, "Info", "wrong password")
        else:
            QMessageBox.information(self, "Info", "wrong password")

    def updateNameLabel(self):
        global user_name
        user_name = self.name
        
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

    def Digikala(self):
        if self.productName == 'SAMSUNG GALAXY S22 ULTRA 5G':
            webbrowser.open('https://www.digikala.com/product/dkp-10261550/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-s22-ultra-5g-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-12-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%86%D8%B3%D8%AE%D9%87-%D8%A7%D8%B3%D9%86%D9%BE%D8%AF%D8%B1%D8%A7%DA%AF%D9%88%D9%86-%D9%88%DB%8C%D8%AA%D9%86%D8%A7%D9%85/')  # Go to example.com
        if self.productName == 'SAMSUNG GALAXY F13':
            webbrowser.open('https://www.digikala.com/product/dkp-9666954/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-f13-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%87%D9%86%D8%AF/')
        if self.productName == 'XIAOMI POCO X4 PRO 5G':
            webbrowser.open('"https://www.digikala.com/product/dkp-8123707/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-poco-x4-pro-5g-2201116pg-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/')
        if self.productName == 'SAMSUNG GALAXY A53 5G':
            webbrowser.open('https://www.digikala.com/product/dkp-8119459/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-a53-5g-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D8%A7%DA%A9%D8%AA%DB%8C%D9%88/')
        if self.productName == 'SAMSUNG GALAXY S21 FE 5G':
            webbrowser.open('https://www.digikala.com/product/dkp-7475119/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-s21-fe-5g-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/')
        if self.productName == 'SAMSUNG GALAXY TAB S8':
            webbrowser.open("https://www.digikala.com/product/dkp-8417820/%D8%AA%D8%A8%D9%84%D8%AA-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-tab-s8-5g-sm-x706b-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-128-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/")
        if self.productName == 'APPLE IPAD PRO 11 2022':
            webbrowser.open("https://www.digikala.com/product/dkp-9834648/%D8%AA%D8%A8%D9%84%D8%AA-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-ipad-pro-11-2022-wifi-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-128-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/")
        if self.productName == 'SAMSUNG GALAXY TAB S6 LITE 2022':
            webbrowser.open("https://www.digikala.com/product/dkp-9936864/%D8%AA%D8%A8%D9%84%D8%AA-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-tab-s6-lite-2022-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-%DA%86%D9%87%D8%A7%D8%B1-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/")
        if self.productName == 'XIAOMI REDMI PAD':
            webbrowser.open("https://www.digikala.com/product/dkp-11511750/%D8%AA%D8%A8%D9%84%D8%AA-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-redmi-pad-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-128-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-6-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D8%A8%D9%87-%D9%87%D9%85%D8%B1%D8%A7%D9%87-%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D9%88-%DA%A9%DB%8C%D9%81-%D9%88-%D9%85%D8%AD%D8%A7%D9%81%D8%B8-%D8%B5%D9%81%D8%AD%D9%87-%D9%86%D9%85%D8%A7%DB%8C%D8%B4/")
        if self.productName == 'SAMSUNG GALAXY TAB A7 LITE':
            webbrowser.open("https://www.digikala.com/product/dkp-5549287/%D8%AA%D8%A8%D9%84%D8%AA-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-tab-a7-lite-t225-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-32-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/")
        if self.productName == 'QCY T19':
            webbrowser.open("https://www.digikala.com/product/dkp-9349961/%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D8%A8%DB%8C-%D8%B3%DB%8C%D9%85-%DA%A9%DB%8C%D9%88-%D8%B3%DB%8C-%D9%88%D8%A7%DB%8C-%D9%85%D8%AF%D9%84-rak-new-bt-item-t19-2022/")
        if self.productName == 'QCY T13':
            webbrowser.open("https://www.digikala.com/product/dkp-5856710/%D9%87%D8%AF%D9%81%D9%88%D9%86-%D8%A8%D9%84%D9%88%D8%AA%D9%88%D8%AB%DB%8C-%DA%A9%DB%8C%D9%88-%D8%B3%DB%8C-%D9%88%D8%A7%DB%8C-%D9%85%D8%AF%D9%84-t13-tws/")
        if self.productName == 'SAMSUNG GALAXY BUDS2 PRO':
            webbrowser.open("https://www.digikala.com/product/dkp-9188766/%D9%87%D8%AF%D9%81%D9%88%D9%86-%D8%A8%D9%84%D9%88%D8%AA%D9%88%D8%AB%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-buds2-pro/")
        if self.productName == 'XIAOMI REDMI BUDS 3 PRO':
            webbrowser.open("https://www.digikala.com/product/dkp-9555069/%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D8%A8%D9%84%D9%88%D8%AA%D9%88%D8%AB%DB%8C-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-thi-global-earbuds-redmi-buds-3-pro-reduction/")
        if self.productName == 'APPLE AIRPODS (3RD GENERATION)':
            webbrowser.open("https://www.digikala.com/product/dkp-6801162/%D9%87%D8%AF%D9%81%D9%88%D9%86-%D8%A8%DB%8C-%D8%B3%DB%8C%D9%85-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-airpods-3-%D9%87%D9%85%D8%B1%D8%A7%D9%87-%D8%A8%D8%A7-%D9%85%D8%AD%D9%81%D8%B8%D9%87-%D8%B4%D8%A7%D8%B1%DA%98/")
        if self.productName == 'SAMSUNG GALAXY WATCH 5 40MM':
            webbrowser.open("https://www.digikala.com/product/dkp-9270334/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-watch-5-40mm/")
        if self.productName == 'XIAOMI MI BAND 7 PRO':
            webbrowser.open("https://www.digikala.com/product/dkp-9962415/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-mi-band-7-pro/")
        if self.productName == 'XIAOMI MIBRO LITE':
            webbrowser.open("https://www.digikala.com/product/dkp-7199868/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D9%85%DB%8C%D8%A8%D8%B1%D9%88-%D9%85%D8%AF%D9%84-lite-smartwatch/")
        if self.productName == 'XIAOMI WATCH S1 ACTIVE':
            webbrowser.open("https://www.digikala.com/product/dkp-8738616/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-s1-active-%D8%A8%D9%86%D8%AF-%D8%B3%D9%84%DB%8C%DA%A9%D9%88%D9%86%DB%8C/")
        if self.productName == 'XIAOMI REDMI WATCH 2 LITE':
            webbrowser.open("https://www.digikala.com/product/dkp-7380557/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-redmi-watch-2-lite-%D8%A8%D9%86%D8%AF-%D8%B3%D9%84%DB%8C%DA%A9%D9%88%D9%86%DB%8C/")
        if self.productName == 'APPLE MACBOOK PRO 14 2021 M1 PRO':
            webbrowser.open("https://www.digikala.com/product/dkp-8687163/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-142-%D8%A7%DB%8C%D9%86%DA%86-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-macbook-mkgp3-m1-pro-2021/")
        if self.productName == 'ASUS VIVOBOOK R565EP':
            webbrowser.open("https://www.digikala.com/product/dkp-11152888/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-156-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-%D9%85%D8%AF%D9%84-vivobook-r565ep-ej615-i5-16gb-512ssd-mx330-%DA%A9%D8%A7%D8%B3%D8%AA%D9%88%D9%85-%D8%B4%D8%AF%D9%87-clone-1-of-11050158/")
        if self.productName == 'MICROSOFT SURFACE LAPTOP GO':
            webbrowser.open("https://www.digikala.com/product/dkp-5341288/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-124-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA-%D9%85%D8%AF%D9%84-surface-laptop-go-b/")
        if self.productName == 'ASUS VIVOBOOK X515EP':
            webbrowser.open("https://www.digikala.com/product/dkp-9723829/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-156-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-%D9%85%D8%AF%D9%84-vivobook-x515ep-ej338-i5-16gb-1ssd-mx330-%DA%A9%D8%A7%D8%B3%D8%AA%D9%88%D9%85-%D8%B4%D8%AF%D9%87/")
        if self.productName == 'ASUS ROG STRIX G15 G513RC':
            webbrowser.open("https://www.digikala.com/product/dkp-9734995/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-156-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-%D9%85%D8%AF%D9%84-rog-strix-g513rc-hn136/")

    def Divar(self):
        if self.productName == 'SAMSUNG GALAXY S22 ULTRA 5G':
            webbrowser.open("https://divar.ir/goods/mobile/prices?q=s22")
        if self.productName == 'SAMSUNG GALAXY F13':
            webbrowser.open("https://divar.ir/goods/mobile/prices?q=F13")
        if self.productName == 'XIAOMI POCO X4 PRO 5G':
            webbrowser.open("https://divar.ir/goods/mobile/prices?q=poco%20x4")
        if self.productName == 'SAMSUNG GALAXY A53 5G':
            webbrowser.open("https://divar.ir/goods/mobile/prices?q=A53")
        if self.productName == 'SAMSUNG GALAXY S21 FE 5G':
            webbrowser.open("https://divar.ir/goods/mobile/prices?q=S21")
        if self.productName == 'SAMSUNG GALAXY TAB S8':
            webbrowser.open("https://divar.ir/s/tehran/tablet?goods-business-type=all&q=Samsung%20Galaxy%20Tab%20S8")
        if self.productName == 'APPLE IPAD PRO 11 2022':
            webbrowser.open("https://divar.ir/s/tehran/tablet?goods-business-type=all&q=Apple%20iPad%20Pro%2011%202022")
        if self.productName == 'SAMSUNG GALAXY TAB S6 LITE 2022':
            webbrowser.open("https://divar.ir/s/tehran/tablet?goods-business-type=all&q=Samsung%20Galaxy%20Tab%20S6%20Lite")
        if self.productName == 'XIAOMI REDMI PAD':
            webbrowser.open("https://divar.ir/s/tehran?q=redmi%20pad")
        if self.productName == 'SAMSUNG GALAXY TAB A7 LITE':
            webbrowser.open("https://divar.ir/s/tehran?q=Samsung%20Galaxy%20Tab%20A7%20Lite")
        if self.productName == 'QCY T19':
            webbrowser.open("https://divar.ir/s/tehran/mobile-tablet-accessories?q=t%2019")
        if self.productName == 'QCY T13':
            webbrowser.open("https://divar.ir/s/tehran/mobile-tablet-accessories?goods-business-type=all&q=t13%20tws")
        if self.productName == 'SAMSUNG GALAXY BUDS2 PRO':
            webbrowser.open("https://divar.ir/s/tehran/mobile-tablet-accessories?goods-business-type=all&q=buds2%20pro")
        if self.productName == 'XIAOMI REDMI BUDS 3 PRO':
            webbrowser.open("https://divar.ir/s/tehran?q=BUDS%203%20PRO")
        if self.productName == 'APPLE AIRPODS (3RD GENERATION)':
            webbrowser.open("https://divar.ir/s/tehran/mobile-tablet-accessories?goods-business-type=all&q=airpods%203")
        if self.productName == 'SAMSUNG GALAXY WATCH 5 40MM':
            webbrowser.open("https://divar.ir/s/tehran?q=SAMSUNG%20GALAXY%20WATCH%205")
        if self.productName == 'XIAOMI MI BAND 7 PRO':
            webbrowser.open("https://divar.ir/s/tehran?q=MI%20BAND%207%20PRO")
        if self.productName == 'XIAOMI MIBRO LITE':
            webbrowser.open("https://divar.ir/s/tehran?q=MIBRO%20LITE")
        if self.productName == 'XIAOMI WATCH S1 ACTIVE':
            webbrowser.open("https://divar.ir/s/tehran?q=s1%20active")
        if self.productName == 'XIAOMI REDMI WATCH 2 LITE':
            webbrowser.open("https://divar.ir/s/tehran?q=REDMI%20WATCH%202%20LITE")
        if self.productName == 'APPLE MACBOOK PRO 14 2021 M1 PRO':
            webbrowser.open("https://divar.ir/s/tehran?q=macbook%20m1%20pro%202021")
        if self.productName == 'ASUS VIVOBOOK R565EP':
            webbrowser.open("https://divar.ir/s/tehran?q=ASUS%20VIVOBOOK%20R565EP")
        if self.productName == 'MICROSOFT SURFACE LAPTOP GO':
            webbrowser.open("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&q=surface%20laptop%20go")
        if self.productName == 'ASUS VIVOBOOK X515EP':
            webbrowser.open("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&q=VIVOBOOK%20X515EP")
        if self.productName == 'ASUS ROG STRIX G15 G513RC':
            webbrowser.open("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&q=G513RC")


    def third_website(self):
        if self.productName == 'SAMSUNG GALAXY S22 ULTRA 5G':
            webbrowser.open("https://www.technolife.ir/product-10032/-%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-%DA%AF%D9%84%DA%A9%D8%B3%DB%8C-s22-ultra-5g-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D8%B1%D9%85-12-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D9%88%DB%8C%D8%AA%D9%86%D8%A7%D9%85")
        if self.productName == 'SAMSUNG GALAXY F13':
            webbrowser.open("https://www.technolife.ir/product-7658/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-f13-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA?utm_source=ZoomitDB&utm_medium=PriceList")
        if self.productName == 'XIAOMI POCO X4 PRO 5G':
            webbrowser.open("https://www.technolife.ir/product-5165/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-poco-x4-pro-5g-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA")
        if self.productName == 'SAMSUNG GALAXY A53 5G':
            webbrowser.open("https://www.technolife.ir/product-3704/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-%DA%AF%D9%84%DA%A9%D8%B3%DB%8C-a53-5g-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA")
        if self.productName == 'SAMSUNG GALAXY S21 FE 5G':
            webbrowser.open("https://www.technolife.ir/product-4107/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-s21-fe-5g-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA")
        if self.productName == 'SAMSUNG GALAXY TAB S8':
            webbrowser.open("https://darsoo.com/product/%D8%AA%D8%A8%D9%84%D8%AA-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-Samsung-Galaxy-Tab-S8-%D8%A8%D8%A7128-%DA%AF%DB%8C%DA%AF-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-%D8%AF%D8%A7%D8%AE%D9%84%DB%8C-%D9%88-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/")
        if self.productName == 'APPLE IPAD PRO 11 2022':
            webbrowser.open("https://darsoo.com/product/ipad-pro-10-9-inches-2022-wifi-128GB-8Ram/")
        if self.productName == 'SAMSUNG GALAXY TAB S6 LITE 2022':
            webbrowser.open("https://darsoo.com/product/Samsung-Galaxy-Tab-S6-Lite-(2022-P619)-64-ram-4/")
        if self.productName == 'XIAOMI REDMI PAD':
            webbrowser.open("https://darsoo.com/product/xiaomi-redmi-pad-128g-6g/")
        if self.productName == 'SAMSUNG GALAXY TAB A7 LITE':
            webbrowser.open("https://www.technolife.ir/product-2900/-%D8%AA%D8%A8%D9%84%D8%AA-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-tab-a7-lite-sm-t225-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-32-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D8%B1%D9%85-3-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-")
        if self.productName == 'QCY T19':
            webbrowser.open("https://www.technolife.ir/product-5829/%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D8%A8%DB%8C-%D8%B3%DB%8C%D9%85-%DA%A9%DB%8C%D9%88-%D8%B3%DB%8C-%D9%88%D8%A7%DB%8C-%D9%85%D8%AF%D9%84-t19-")
        if self.productName == 'QCY T13':
            webbrowser.open("https://www.technolife.ir/product-3163/%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D8%A8%DB%8C-%D8%B3%DB%8C%D9%85-%DA%A9%DB%8C%D9%88-%D8%B3%DB%8C-%D9%88%D8%A7%DB%8C-%D9%85%D8%AF%D9%84-t13-")
        if self.productName == 'SAMSUNG GALAXY BUDS2 PRO':
            webbrowser.open("https://www.technolife.ir/product-7383/-%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D8%A8%DB%8C-%D8%B3%DB%8C%D9%85-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-buds-2-pro")
        if self.productName == 'XIAOMI REDMI BUDS 3 PRO':
            webbrowser.open("https://hamechionline.ir/xiaomi-redmi-airdots-3-pro")
        if self.productName == 'APPLE AIRPODS (3RD GENERATION)':
            webbrowser.open("https://www.technolife.ir/product-3544/%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D8%A8%DB%8C-%D8%B3%DB%8C%D9%85-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-airpods-3")
        if self.productName == 'SAMSUNG GALAXY WATCH 5 40MM':
            webbrowser.open("https://www.technolife.ir/product-7219/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-watch5-40mm")
        if self.productName == 'XIAOMI MI BAND 7 PRO':
            webbrowser.open("https://www.technolife.ir/product-8315/-%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-band-7-pro")
        if self.productName == 'XIAOMI MIBRO LITE':
            webbrowser.open("https://www.technolife.ir/product-3946/-%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-mibro-lite-")
        if self.productName == 'XIAOMI WATCH S1 ACTIVE':
            webbrowser.open("https://www.technolife.ir/product-6648/-%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-s1-active")
        if self.productName == 'XIAOMI REDMI WATCH 2 LITE':
            webbrowser.open("https://www.technolife.ir/product-5029/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-redmi-watch-2-lite")
        if self.productName == 'APPLE MACBOOK PRO 14 2021 M1 PRO':
            webbrowser.open("https://amitis-group.com/product/%d8%a7%d9%be%d9%84-%d9%85%d8%af%d9%84-%d9%85%da%a9-%d8%a8%d9%88%da%a9-%d9%be%d8%b1%d9%88-mkgr3-1%db%b4-inch/")
        if self.productName == 'ASUS VIVOBOOK R565EP':
            webbrowser.open("https://www.technolife.ir/product-10637/%D9%84%D9%BE%E2%80%8C-%D8%AA%D8%A7%D9%BE-15.6-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-%D9%85%D8%AF%D9%84-vivobook-r565ep-ej615")
        if self.productName == 'MICROSOFT SURFACE LAPTOP GO':
            webbrowser.open("https://adak.shop/product/laptop-microsoft-surface-laptop-go/")
        if self.productName == 'ASUS VIVOBOOK X515EP':
            webbrowser.open("https://www.technolife.ir/product-11556/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-15.6-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D9%85%D8%AF%D9%84-vivobook-x515ep-ej338")
        if self.productName == 'ASUS ROG STRIX G15 G513RC':
            webbrowser.open("https://www.technolife.ir/product-7794/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-15.6-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-%D9%85%D8%AF%D9%84-rog-strix-g15-g513rc-hn101-")


    def UI(self):
        self.productDetails()
        if self.productManufacturer == 'Mobile':
            self.productDetails()
            self.widgets()
            self.layouts()
            if self.productName == 'SAMSUNG GALAXY S22 ULTRA 5G':
                img = QLabel(self)
                img.setPixmap(QPixmap('mobiles/samsung-galaxy-s22-ultra-5g-burgundy.png'))
                img.move(0,0)
                img.resize(350,300)


            if self.productName == 'SAMSUNG GALAXY F13':
                img = QLabel(self)
                img.setPixmap(QPixmap('mobiles/samsung-galaxy-f13-.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'XIAOMI POCO X4 PRO 5G':
                img = QLabel(self)
                img.setPixmap(QPixmap('mobiles/xiaomi-poco-x4-pro-5g-graphite-.png'))
                img.move(0,0)
                img.resize(350,300)               
            
            if self.productName == 'SAMSUNG GALAXY A53 5G':
                img = QLabel(self)
                img.setPixmap(QPixmap('mobiles/samsung-galaxy-a53-.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'SAMSUNG GALAXY S21 FE 5G':
                img = QLabel(self)
                img.setPixmap(QPixmap('mobiles/samsung-galaxy-s21-fe-5g-.png'))
                img.move(0,0)
                img.resize(350,300)

            btn = QPushButton('Digikala',self)
            btn.move(20,345)
            btn.clicked.connect(self.Digikala)

            btn = QPushButton('Divar',self)
            btn.move(120,345)
            btn.clicked.connect(self.Divar)

            btn = QPushButton('Third Website',self)
            btn.move(220,345)
            btn.clicked.connect(self.third_website)

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
            text13.move(140,565)
            tex13 = QLabel(self.price3,self)
            tex13.move(225,565)
        if self.productManufacturer == 'Tablet':
            self.productDetails()
            self.widgets()
            self.layouts()

            if self.productName == 'SAMSUNG GALAXY TAB S8':
                img = QLabel(self)
                img.setPixmap(QPixmap('tablets/samsung-galaxy-tab-s8-.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'APPLE IPAD PRO 11 2022':
                img = QLabel(self)
                img.setPixmap(QPixmap('tablets/apple-ipad-pro-2022-.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'SAMSUNG GALAXY TAB S6 LITE 2022':
                img = QLabel(self)
                img.setPixmap(QPixmap('tablets/samsung-galaxy-tab-s6-lite-2022.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'XIAOMI REDMI PAD':
                img = QLabel(self)
                img.setPixmap(QPixmap('tablets/xiaomi-redmi-pad.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'SAMSUNG GALAXY TAB A7 LITE':
                img = QLabel(self)
                img.setPixmap(QPixmap('tablets/samsung-galaxy-tab-a7-lite.png'))
                img.move(0,0)
                img.resize(350,300)

            btn = QPushButton('Digikala',self)
            btn.move(20,345)
            btn.clicked.connect(self.Digikala) 

            btn = QPushButton('Divar',self)
            btn.move(120,345)
            btn.clicked.connect(self.Divar)

            btn = QPushButton('Third Website',self)
            btn.move(220,345)
            btn.clicked.connect(self.third_website)

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

            if self.productName == 'QCY T19':
                img = QLabel(self)
                img.setPixmap(QPixmap('airpods/qcy-t19.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'QCY T13':
                img = QLabel(self)
                img.setPixmap(QPixmap('airpods/qcy-t13.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'SAMSUNG GALAXY BUDS2 PRO':
                img = QLabel(self)
                img.setPixmap(QPixmap('airpods/samsung-galaxy-buds2-pro-.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'XIAOMI REDMI BUDS 3 PRO':
                img = QLabel(self)
                img.setPixmap(QPixmap('airpods/xiaomi-redmi-airdots-3-pro-.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'APPLE AIRPODS (3RD GENERATION)':
                img = QLabel(self)
                img.setPixmap(QPixmap('airpods/apple-airpods-3rd-generation-.png'))
                img.move(0,0)
                img.resize(350,300)   

            btn = QPushButton('Digikala',self)
            btn.move(20,345)
            btn.clicked.connect(self.Digikala)

            btn = QPushButton('Divar',self)
            btn.move(120,345)
            btn.clicked.connect(self.Divar)

            btn = QPushButton('Third Website',self)
            btn.move(220,345)
            btn.clicked.connect(self.third_website)

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
            text6 = QLabel('noisecancelling:',self)
            text6.move(20,472)
            tex6 = QLabel(self.noiseCancelling , self)
            tex6.move(40,472)
            text7 = QLabel('blutooth:',self)
            text7.move(20,488)
            tex7 = QLabel(self.blutooth,self)
            tex7.move(70,488)
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

            if self.productName == 'SAMSUNG GALAXY WATCH 5 40MM':
                img = QLabel(self)
                img.setPixmap(QPixmap('watches/samsung-galaxy-watch5-.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'XIAOMI MI BAND 7 PRO':
                img = QLabel(self)
                img.setPixmap(QPixmap('watches/xiaomi-mi-band-7-pro-.png'))
                img.move(0,0)
                img.resize(350,300) 

            if self.productName == 'XIAOMI MIBRO LITE':
                img = QLabel(self)
                img.setPixmap(QPixmap('watches/xiaomi-mibro-lite-.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'XIAOMI WATCH S1 ACTIVE':
                img = QLabel(self)
                img.setPixmap(QPixmap('watches/xiaomi-watch-s1-active.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'XIAOMI REDMI WATCH 2 LITE':
                img = QLabel(self)
                img.setPixmap(QPixmap('watches/xiaomi-redmi-watch-2-lite-.png'))
                img.move(0,0)
                img.resize(350,300) 

            btn = QPushButton('Digikala',self)
            btn.move(20,345)
            btn.clicked.connect(self.Digikala)

            btn = QPushButton('Divar',self)
            btn.move(120,345)
            btn.clicked.connect(self.Divar)

            btn = QPushButton('Third Website',self)
            btn.move(220,345)
            btn.clicked.connect(self.third_website)

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

            if self.productName == 'APPLE MACBOOK PRO 14 2021 M1 PRO':
                img = QLabel(self)
                img.setPixmap(QPixmap('laptops/macbook-pro-14-inch.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'ASUS VIVOBOOK R565EP':
                img = QLabel(self)
                img.setPixmap(QPixmap('laptops/asus-vivobook-r565ep-.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'MICROSOFT SURFACE LAPTOP GO':
                img = QLabel(self)
                img.setPixmap(QPixmap('laptops/microsoft-surface-laptop-go-.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'ASUS VIVOBOOK X515EP':
                img = QLabel(self)
                img.setPixmap(QPixmap('laptops/asus-x515ep-laptop-.png'))
                img.move(0,0)
                img.resize(350,300)

            if self.productName == 'ASUS ROG STRIX G15 G513RC':
                img = QLabel(self)
                img.setPixmap(QPixmap('laptops/asus-g513rm-.png'))
                img.move(0,0)
                img.resize(350,300)

            btn = QPushButton('Digikala',self)
            btn.move(20,345)
            btn.clicked.connect(self.Digikala)

            btn = QPushButton('Divar',self)
            btn.move(120,345)
            btn.clicked.connect(self.Divar)

            btn = QPushButton('Third Website',self)
            btn.move(220,345)
            btn.clicked.connect(self.third_website)

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
            tex9 = QLabel(self.resolution,self)
            tex9.move(80,520)
            text10 = QLabel('Digikala:',self)
            text10.move(20,535)
            tex10 = QLabel(self.price1,self)
            tex10.move(70,535)
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

        if productId == 'Mobile':
            query=("SELECT * FROM mobile WHERE product_name=?")
            product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,)
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


    def widgets(self):
        #################Top layouts wigdets#########
        self.product_Img=QLabel(self)
        self.product_Img.setPixmap(QPixmap('a.png'))
        self.product_Img.move(100,100)
        self.product_Img.resize(300,300)
        self.titleText=QLabel("Update Product")
        self.addFavoritebtn=QPushButton("add to favorite")
        self.addFavoritebtn.clicked.connect(self.favoriteProduct)

    def layouts(self):
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout=QFormLayout()
        self.topFrame=QFrame()
        self.bottomFrame=QFrame()
        self.bottomFrame.setStyleSheet(style.productBottomFrame())
        ###############add widgets###########
        self.topFrame.setLayout(self.topLayout)    
        self.bottomLayout.addRow(QLabel(""),self.addFavoritebtn)
        self.bottomFrame.setLayout(self.bottomLayout)
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)


        self.setLayout(self.mainLayout)


    def favoriteProduct(self):
        global favoriteProductsName
        
        favoriteProductsName = self.productName
        query = cur.execute('SELECT product_manufacturer FROM mobile WHERE product_name = ?',(favoriteProductsName,)).fetchone()
 
        try:
            query = cur.execute('SELECT product_manufacturer FROM mobile WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            if query != None:
                if query[0] == 'Mobile':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(user_name,)).fetchone()
            query = cur.execute('SELECT product_manufacturer FROM Tablet WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            if query != None:
                if query[0] == 'Tablet':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(user_name,)).fetchone()
            query = cur.execute('SELECT product_manufacturer FROM Airpod WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            if query != None:
                if query[0] == 'Airpod':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(user_name,)).fetchone()

            query = cur.execute('SELECT product_manufacturer FROM Clock WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            if query != None:
                if query[0] == 'Clock':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(user_name,)).fetchone()

            query = cur.execute('SELECT product_manufacturer FROM Laptop WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            if query != None:
                if query[0] == 'Laptop':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(user_name,)).fetchone()

            if a[0] == None:
                favoriteProductsName = self.productName
            else:
                favoriteProductsName = a[0] + ','+ self.productName
            cur.execute(f'UPDATE member SET favorite= ? WHERE user_name = ?',(favoriteProductsName,user_name))
            con.commit()
        except:
            QMessageBox.information(self, "Info", "log in to your panel first")

        
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

        self.productsTable.setHorizontalHeaderItem(0,QTableWidgetItem("Product Name"))
        self.productsTable.setHorizontalHeaderItem(1,QTableWidgetItem("Manufacturer"))
        self.productsTable.setHorizontalHeaderItem(2,QTableWidgetItem("Digikala"))
        self.productsTable.setHorizontalHeaderItem(3,QTableWidgetItem("Divar"))
        self.productsTable.setHorizontalHeaderItem(4,QTableWidgetItem("Third Website"))


        self.productsTable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.productsTable.doubleClicked.connect(self.selectedProduct)
    
    def layouts(self):

        self.mainLayout=QHBoxLayout(self)
        
        self.mainLayout.addWidget(self.productsTable)

    def displayProducts(self):

        self.productsTable.setFont(QFont("Times", 12))

        try:
            query = cur.execute('SELECT favorite FROM member WHERE user_name=?',(user_name,)).fetchone()
            lis = query[0].split(',')
            lis = set(lis)
            lis = list(lis)
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

        self.display = DisplayProduct()

        self.display.show()

def main():
    App=QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()

    