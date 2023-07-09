import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import style
import webbrowser
import sqlite3


con=sqlite3.connect("dynamicproduct.db")
cur=con.cursor()


class SearchByLink(QWidget):
    def __init__(self):
        ##########make main window######
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
        ##########make coloumns of main window###########
        self.productsTable = QTableWidget(self)
        self.productsTable.setColumnCount(4)

        self.productsTable.setHorizontalHeaderItem(0,QTableWidgetItem("Product Name"))
        self.productsTable.setHorizontalHeaderItem(1,QTableWidgetItem("Digikala"))
        self.productsTable.setHorizontalHeaderItem(2,QTableWidgetItem("Divar"))
        self.productsTable.setHorizontalHeaderItem(3,QTableWidgetItem("Third website"))

        self.productsTable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.productsTable.doubleClicked.connect(self.selectedProduct)
    
    def layouts(self):
        #############add products table to main window#####
        self.mainLayout=QHBoxLayout(self)
        
        self.mainLayout.addWidget(self.productsTable)
        self.mainLayout = QVBoxLayout(self)

    def displayProducts(self):

        self.productsTable.setFont(QFont("Times", 12))
        for i in reversed(range(self.productsTable.rowCount())):
            self.productsTable.removeRow(i)

        ############add the products of dynamic search to products table ########
        query = cur.execute("SELECT product_name,price1,price2,price3 FROM products")
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        
    def selectedProduct(self):
        global productId
        global product_name
        
        ##########get value of products from products table(Not db) for using in double click show options###########
        listProduct=[]
        for i in range(0,3):
            listProduct.append(self.productsTable.item(self.productsTable.currentRow(),i).text())

        productId=listProduct[1]
        product_name = listProduct[0]

        self.a = DisplayProduct()
        self.a.show()

class DisplayProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Details")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,400,700)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
      self.productDetails()
      self.widgets()
      self.layouts()


    def productDetails(self):
        global productId
        ##########get products value from db##########
        query=("SELECT product_name,price1,price2,price3,color,description,Divar,Digikala,Third_website FROM products WHERE product_name=?")
        product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,)

        self.productName=product[0]
        self.productprice1=product[1]
        self.productPrice2=product[2]
        self.productprice3 = product[3]
        self.productcolor=product[4]
        self.productoption=product[5]
        self.divarLink = product[6]
        self.digikalaLink = product[7]
        self.thirdWebsiteLink = product[8]
        query=("SELECT image FROM products WHERE product_name=?")
        product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,) 
        image_data = product[0]
        #########get image of product from db###########
        with open('image.jpg', 'wb') as file:
            file.write(image_data)

    def widgets(self):
        #################Top layouts wigdets#########
        self.product_Img=QLabel()
        self.img=QPixmap('image.jpg')
        os.remove('image.jpg')

        self.product_Img.setPixmap(self.img)
        self.product_Img.setAlignment(Qt.AlignCenter)

        #############make QtextEdit for showing the extracted informatin from db#########
        self.nameEntry=QTextEdit()
        self.nameEntry.setReadOnly(True)
        self.nameEntry.setFixedHeight(30)
        self.nameEntry.setText(self.productName)
 
        self.manufacturerEntry=QTextEdit()
        self.manufacturerEntry.setFixedHeight(20)
        self.manufacturerEntry.setReadOnly(True)
        self.manufacturerEntry.setText(self.productprice1)
        self.priceEntry=QTextEdit()
        self.priceEntry.setReadOnly(True)
        self.priceEntry.setFixedHeight(20)
        self.priceEntry.setText(str(self.productPrice2))

        self.price3=QTextEdit()
        self.price3.setFixedHeight(20)
        self.price3.setReadOnly(True)
        self.price3.setText(str(self.productprice3))

        self.qoutaEntry=QTextEdit()
        self.qoutaEntry.setFixedHeight(30)
        self.qoutaEntry.setReadOnly(True)
        self.qoutaEntry.setText(str(self.productcolor))
        self.option=QTextEdit()
        self.qoutaEntry.setReadOnly(True)
        self.option.setText(str(self.productoption))

        ########make Qpush buttom for showing the website of product #########
        self.btn = QPushButton('Divar')
        self.btn.clicked.connect(self.Divar)
        self.btn2 = QPushButton('Digikala')
        self.btn2.clicked.connect(self.Digikala)
        self.btn3 = QPushButton('Third Website')
        self.btn3.clicked.connect(self.thirdWebsite)

    ###### these three wbsite show the website of product with webbrowser
    def Divar(self):
        webbrowser.open(self.divarLink)

    def Digikala(self):
        webbrowser.open(self.digikalaLink)
    
    def thirdWebsite(self):
        webbrowser.open(self.thirdWebsiteLink)

    def layouts(self):
        #########make section of top , main , buttom ###########
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout=QFormLayout()
        self.topFrame=QFrame()
        self.bottomFrame=QFrame()
        self.bottomFrame.setStyleSheet(style.productBottomFrame())
        ###############add widgets###########
        ########### make the label of products############
        self.topLayout.addWidget(self.product_Img)
        self.topFrame.setLayout(self.topLayout)
        self.bottomLayout.addRow(QLabel("Name: "),self.nameEntry)
        self.bottomLayout.addRow(QLabel("Digikala: "),self.manufacturerEntry)
        self.bottomLayout.addRow(QLabel("Divar: "),self.priceEntry)
        self.bottomLayout.addRow(QLabel("Third Website: "),self.price3)
        self.bottomLayout.addRow(QLabel("colors: "),self.qoutaEntry)
        self.bottomLayout.addRow(QLabel("option: "),self.option)

        self.bottomFrame.setLayout(self.bottomLayout)
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        ########make the buttons of three website###########
        self.bottomLayout.addRow(QLabel(""),self.btn)
        self.bottomLayout.addRow(QLabel(""),self.btn2)
        self.bottomLayout.addRow(QLabel(""),self.btn3)

        self.setLayout(self.mainLayout)
