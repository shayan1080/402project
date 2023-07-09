import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QEvent
import sqlite3
import addproduct,addmember,style
import dynamicsearch
import options

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
        ####################showing of search results################
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
        ################make suggestion part##################
        self.suggestionText = QLabel("Suggestions:")
        self.suggestionEntry = QLineEdit()
        self.suggestionEntry.setPlaceholderText("Enter a price1-price2-category(e.g:4000000-5000000-mobile)")
        self.suggestionButton = QPushButton("Suggest")
        self.suggestionButton.clicked.connect(self.suggest)
        self.suggestionButton.setStyleSheet(style.suggestionBtnStyle())
        #################make search by link part#############
        self.search = QLabel("Search Online:")
        self.searchOnlineEntry = QLineEdit()
        self.searchOnlineEntry.setPlaceholderText("give a link")
        self.searchOnlineBtn = QPushButton("Find link")
        self.searchOnlineBtn.clicked.connect(self.searchlink)
        self.searchOnlineBtn.setStyleSheet(style.suggestionBtnStyle())
        self.searchButton.setStyleSheet(style.searchButtonStyle())
        ##########################Right middle layout widgets###########
        ###############make category of products###################
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
        #################make the tab of showing members##########
        self.membersTable=QTableWidget()
        self.membersTable.setColumnCount(1)
        self.membersTable.setHorizontalHeaderItem(0,QTableWidgetItem("Member user_id"))
        self.updatebtn = QPushButton("update")
        self.updatebtn.clicked.connect(self.displayMembers)
        self.membersTable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.membersTable.doubleClicked.connect(self.selectedMember)

    def layouts(self):
        ######################Tab1 layouts##############
        ############ make two parts for main window to showing products table and search,category,suggestion part #################
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
        ##################Right main leyout###############
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
        
        self.rightTopLayout.addWidget(self.searchText)
        self.rightTopLayout.addWidget(self.searchEntry)
        self.rightTopLayout.addWidget(self.searchButton)
        self.topGroupBox.setLayout(self.rightTopLayout)
        ##############Category of products###################
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
        dynamicsearch.search(x)

    def suggest(self):
        ################extract price information of products from db to find that the considered price#############
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
        ##############extract data from db and save in the products table##########
        self.productsTable.setFont(QFont("Times", 12))
        for i in reversed(range(self.productsTable.rowCount())):
            self.productsTable.removeRow(i)

        ############mobile##################
        query = cur.execute("SELECT product_name,product_manufacturer,price1,price2,price3 FROM mobile")
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)


        #############Tablet###################
        query = cur.execute("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Tablet")
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        ##########Airpod################
        query = cur.execute("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Airpod")
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)


        #########Clock#############
        query = cur.execute("SELECT product_name,product_manufacturer,price1,price2,price3 FROM Clock")
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
    
        ########Laptop###################
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

        ##############Extract data of members from member table in db###########
        members=cur.execute("SELECT * FROM member")
        
        for row_data in members:
            row_number = self.membersTable.rowCount()
            self.membersTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.membersTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))

        self.membersTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    ############make this list to show multiple windows of products information###########
    display_window = []
    def selectedProduct(self):
        global productId
        global product_name
        global user_name
        listProduct=[]
        ###############Extract data from products table###########
        for i in range(0,4):
            listProduct.append(self.productsTable.item(self.productsTable.currentRow(),i).text())

        ###########using productId and product_name in showing of product's information##########3
        productId=listProduct[1]
        product_name = listProduct[0]
        try:
            display = options.DisplayProduct(product_name,productId,user_name,'1')
            Main.display_window.append(display)  # Add the instance to the list
            display.show()
        except:
            QMessageBox.information(self, "Info", "log in to your panel first")

    ###########Rasing of entering password window################
    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonDblClick and obj == self.widget:
            self.widget.handle_input()
        return super().eventFilter(obj, event)

    ################send password of member entry for authenticating##########
    def selectedMember(self):        
        self.widget = CustomWidget(self.handle_password)
        self.widget.show()

    #########quantify of user_name to showing in the main window############
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

            ############show the results in the products table 
            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)
            for row_data in results:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(row_number,column_number,QTableWidgetItem(str(data))) 

    ##############Sort the products by their category##############
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
        #########make coloumns of Favorite window######
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
        ##########show the products information in the product table#########
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
        ##########Send the data for options module to show products information###############
        self.display = options.DisplayProduct(product_name,productId,user_name,'2')

        self.display.show()

def main():
    App=QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()

    