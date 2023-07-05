import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import addproduct,addmember,sellings,style
from PIL import Image
import threading

con=sqlite3.connect("costumer.db")
cur=con.cursor()



class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Manager")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,1350,750)
        self.setFixedSize(self.size())
        self.name = ''
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
        self.sellProduct = QAction(QIcon('icons/sell.png'),"Sell Product",self)
        self.tb.addAction(self.sellProduct)
        # self.sellProduct.triggered.connect(self.funcSellProducts)
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
        self.tabs.addTab(self.tab3,"Statistics")
        self.tabs.addTab(self.tab4,'Compare')


    def widgets(self):
        #######################Tab1 Widgets###############
        ####################Main left layout widget##########
        self.productsTable = QTableWidget()
        self.productsTable.setColumnCount(4)
        self.productsTable.setColumnHidden(0,True)
    
        self.productsTable.setHorizontalHeaderItem(1,QTableWidgetItem("Product Name"))
        self.productsTable.setHorizontalHeaderItem(2,QTableWidgetItem("Manufacturer"))
        self.productsTable.setHorizontalHeaderItem(3,QTableWidgetItem("Price"))

        self.productsTable.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.productsTable.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
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
        self.avaialableProducts=QRadioButton("Available")
        self.notAvaialableProducts=QRadioButton("Not Available")
        self.moblie=QRadioButton('mobile')
        self.listButton=QPushButton("List")
        self.listButton.clicked.connect(self.listProducts)
        self.listButton.setStyleSheet(style.listButtonStyle())
        ########################Tab2 Widgets#########################
        self.membersTable=QTableWidget()
        self.membersTable.setColumnCount(2)
        # self.membersTable.setHorizontalHeaderItem(0,QTableWidgetItem("Member ID"))
        self.membersTable.setHorizontalHeaderItem(0,QTableWidgetItem("Member Name"))
        self.membersTable.setHorizontalHeaderItem(1,QTableWidgetItem("Member Surname"))

        self.membersTable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.membersTable.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
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

        # self.lbl = QLabel('username:',self)
        # self.lbl.move(1000,20)
        # self.lbl1 = QLabel(self.name , self)
        # self.lbl1.move(1010,20) 





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
        self.rightMiddleLayout.addWidget(self.avaialableProducts)
        self.rightMiddleLayout.addWidget(self.notAvaialableProducts)
        self.rightMiddleLayout.addWidget(self.moblie)
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
        # self.memberMainLayout.addWidget(self.memberRightGroupBox,30)
        self.tab2.setLayout(self.memberMainLayout)

        #####################Tab3 layouts########################
        self.statisticsMainLayout=QVBoxLayout()
        self.statisticsLayout=QFormLayout()
        self.statisticsGroupBox=QGroupBox("Statistics")
        self.statisticsLayout.addRow("Total Products:",self.totalProductsLabel)
        self.statisticsLayout.addRow("Total Member:",self.totalMemberLabel)
        self.statisticsLayout.addRow("Sold Products:",self.soldProductsLabel)
        self.statisticsLayout.addRow("Total Amount:",self.totalAmountLabel)

        self.statisticsGroupBox.setLayout(self.statisticsLayout)
        self.statisticsGroupBox.setFont(QFont("Arial",20))
        self.statisticsMainLayout.addWidget(self.statisticsGroupBox)
        self.tab3.setLayout(self.statisticsMainLayout)
        self.tabs.blockSignals(False)

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

        query = cur.execute('''SELECT product_id, product_name, product_manufacturer, product_price FROM mobile''')
        
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)


        query = cur.execute("SELECT product_id, product_name, product_manufacturer, product_price FROM Tablet")
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        query = cur.execute("SELECT product_id, product_name, product_manufacturer, product_price FROM Airpod")
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

        productId=listProduct[2]
        product_name = listProduct[1]
        print(product_name)
        # print(productId)

        display = DisplayProduct()
        Main.display_window.append(display)  # Add the instance to the list
        display.show()


    def selectedMember(self):
        global user_name
        self.id = 0
        self.name = self.membersTable.item(self.membersTable.currentRow(),self.id).text()
        self.updateNameLabel()
        user_name = self.name


    def updateNameLabel(self):
        self.lbl1.setText(self.name)
        self.lbl1.move(1065,20)


    def searchProducts(self):

        value=self.searchEntry.text()
        if value == "":
            QMessageBox.information(self,"Warning","Search query cant be empty!!!")

        else:

            self.searchEntry.setText("")

            query=("SELECT product_id,product_name,product_manufacturer,product_price FROM mobile WHERE product_name LIKE ? or product_manufacturer LIKE ?")
            results=cur.execute(query,('%' + value + '%','%' + value + '%')).fetchall()
            query=("SELECT product_id,product_name,product_manufacturer,product_price FROM Tablet WHERE product_name LIKE ? or product_manufacturer LIKE ?")
            results.extend(cur.execute(query,('%' + value + '%','%' + value + '%')).fetchall())
            query=("SELECT product_id,product_name,product_manufacturer,product_price FROM Airpod WHERE product_name LIKE ? or product_manufacturer LIKE ?")
            results.extend(cur.execute(query,('%' + value + '%','%' + value + '%')).fetchall())

            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)
            for row_data in results:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(row_number,column_number,QTableWidgetItem(str(data))) 



    # def searchMembers(self):
    #     value = self.memberSearchEntry.text()
    #     if value == "":
    #         QMessageBox.information(self,"Warning","Search query can not be empty")

    #     else:
    #         self.memberSearchEntry.setText("")
    #         query=("SELECT * FROM members WHERE member_name LIKE ? or member_surname LIKE ? or member_phone LIKE ?")
    #         results=cur.execute(query,('%' + value + '%', '%' + value + '%', '%' + value + '%')).fetchall()
    #         if results == []:
    #             QMessageBox.information(self,"Warning","There is no such a member")
    #         else:
    #             for i in reversed(range(self.membersTable.rowCount())):
    #                 self.membersTable.removeRow(i)

    #             for row_data in results:
    #                 row_number = self.membersTable.rowCount()
    #                 self.membersTable.insertRow(row_number)
    #                 for column_number, data in enumerate(row_data):
    #                     self.membersTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))



    def listProducts(self):
        if self.allProducts.isChecked() == True:
            self.displayProducts()

        elif self.avaialableProducts.isChecked():
            query=("SELECT product_id,product_name,product_manufacturer,product_price,product_qouta,"
                   "product_availability FROM products WHERE product_availability='Available'")
            products=cur.execute(query).fetchall()
            print(products)

            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)

            for row_data in products:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        elif self.notAvaialableProducts.isChecked():
            query = ("SELECT product_id,product_name,product_manufacturer,product_price,product_qouta,"
                     "product_availability FROM products WHERE product_availability='UnAvailable'")
            products = cur.execute(query).fetchall()
            print(products)

            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)

            for row_data in products:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        elif self.moblie.isChecked():
            query = ("SELECT product_id,product_name,product_availability,product_price,product_qouta,"
                     "product_manufacturer FROM products WHERE product_manufacturer='Apple'")
            products = cur.execute(query).fetchall()
            print(products)

            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)

            for row_data in products:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))


    # def funcSellProducts(self):
    #     if self.membersTable.selectedItems():
    #         listMember = []
    #         for i in range(4):
    #             item = self.membersTable.item(self.membersTable.currentRow(), i)
    #             if item is not None:
    #                 listMember.append(item.text())
    #             else:
    #                 # Handle the case when the item is None
    #                 listMember.append("")
    #         self.sell = sellings.SellProduct(listMember)
    #         self.sell.show()
    #     else:
    #         QMessageBox.warning(self, "Warning", "Please select a member to proceed.")



    # def getStatistics(self):
    #     countProducts=cur.execute("SELECT count(product_id) FROM products").fetchall()
    #     countMembers = cur.execute("SELECT count(member_id) FROM members").fetchall()
    #     soldProducts = cur.execute("SELECT SUM(selling_quantity) FROM sellings").fetchall()
    #     totalAmount = cur.execute("SELECT SUM(selling_amount) FROM sellings").fetchall()
    #     totalAmount = totalAmount[0][0]
    #     soldProducts = soldProducts[0][0]
    #     countMembers = countMembers[0][0]
    #     countProducts = countProducts[0][0]
    #     self.totalProductsLabel.setText(str(countProducts))
    #     self.totalMemberLabel.setText(str(countMembers))
    #     self.soldProductsLabel.setText(str(soldProducts))
    #     self.totalAmountLabel.setText(str(totalAmount)+" $")

    def tabChanged(self):
        # self.getStatistics()
        self.displayProducts()
        self.displayMembers()



# class DisplayMember(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Member Details")
#         self.setWindowIcon(QIcon('icons/icon.ico'))
#         self.setGeometry(450,150,350,600)
#         self.setFixedSize(self.size())
#         self.UI()
#         self.show()

#     def UI(self):
#         self.memberDetails()
#         self.widgets()
#         self.layouts()


#     def memberDetails(self):
#         global memberId
#         query=("SELECT * FROM member WHERE member_id=?")
#         member=cur.execute(query,(memberId,)).fetchone()
#         print('MEMBERS: ',member)
#         self.memberName=member[0]
#         self.memberSurname=member[1]
#         # self.memberPhone=member[3]

#     def widgets(self):
#         ###############Widgets of top layout############
#         self.memberImg=QLabel()
#         self.img=QPixmap('icons/members.png')
#         self.memberImg.setPixmap(self.img)
#         self.memberImg.setAlignment(Qt.AlignCenter)
#         self.titleText=QLabel("Display Member")
#         self.titleText.setAlignment(Qt.AlignCenter)
#         ###################widgets of bottom layout#########
#         self.nameEntry=QLineEdit()
#         self.nameEntry.setText(self.memberName)
#         self.surnameEntry=QLineEdit()
#         self.surnameEntry.setText(self.memberSurname)
#         self.phoneEntry=QLineEdit()
#         self.phoneEntry.setText(self.memberPhone)
#         self.updateBtn=QPushButton("Update")
#         self.updateBtn.clicked.connect(self.updateMember)
#         self.deleteBtn=QPushButton("Delete")
#         self.deleteBtn.clicked.connect(self.deleteMember)



#     def layouts(self):
#         self.mainLayout=QVBoxLayout()
#         self.topLayout=QVBoxLayout()
#         self.bottomLayout=QFormLayout()
#         self.topFrame=QFrame()
#         self.topFrame.setStyleSheet(style.memberTopFrame())
#         self.bottomFrame=QFrame()
#         self.bottomFrame.setStyleSheet(style.memberBottomFrame())
#         ##############add widgets######3
#         self.topLayout.addWidget(self.titleText)
#         self.topLayout.addWidget(self.memberImg)
#         self.topFrame.setLayout(self.topLayout)

#         self.bottomLayout.addRow(QLabel("Name: "),self.nameEntry)
#         self.bottomLayout.addRow(QLabel("Surname: "),self.surnameEntry)
#         self.bottomLayout.addRow(QLabel("Phone: "),self.phoneEntry)
#         self.bottomLayout.addRow(QLabel(""),self.updateBtn)
#         self.bottomLayout.addRow(QLabel(""),self.deleteBtn)
#         self.bottomFrame.setLayout(self.bottomLayout)

#         self.mainLayout.addWidget(self.topFrame)
#         self.mainLayout.addWidget(self.bottomFrame)
#         self.setLayout(self.mainLayout)


#     def deleteMember(self):
#         global memberId
#         mbox=QMessageBox.question(self,"Warning","Are you sure to delete this member",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)

#         if mbox == QMessageBox.Yes:
#             try:
#                 query="DELETE FROM members WHERE member_id=?"
#                 cur.execute(query,(memberId,))
#                 con.commit()
#                 QMessageBox.information(self,"Info","Member has been deleted!")
#             except:
#                 QMessageBox.information(self,"Info","Member has not been deleted!")


#     def updateMember(self):
#         global memberId
#         name = self.nameEntry.text()
#         surname = self.surnameEntry.text()
#         phone = self.phoneEntry.text()

#         if (name and surname and phone !=""):
#             try:
#                 query="UPDATE members set member_name=?, member_surname=?, member_phone=? WHERE member_id=?"
#                 cur.execute(query,(name,surname,phone,memberId))
#                 con.commit()
#                 QMessageBox.information(self,"Info","Member has been updated!")

#             except:
#                 QMessageBox.information(self,"Info","Member has been updated!")

#         else:
#             QMessageBox.information(self, "Info", "Fields can not be empty!")

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
            text1.move(20,400)
            tex1 = QLabel(self.productName,self)
            tex1.move(50,400)
            text2 = QLabel('battery',self)
            text2.move(20,415)
            text3 = QLabel('size:',self)
            text3.move(20,430)
            text4 = QLabel('cores:',self)
            text4.move(20,445)
            text5 = QLabel('memory:',self)
            text5.move(20,460)
            text6 = QLabel('Ram:',self)
            text6.move(20,475)
            text7 = QLabel('weight:',self)
            text7.move(20,490)
            text8 = QLabel('camera:',self)
            text8.move(20,505)
            text9 = QLabel('operating system:',self)
            text9.move(20,525)
            text9.resize(140,20)
            text10 = QLabel('colors:',self)
            text10.move(20,535)
            text11 = QLabel('Digikala:',self)
            text11.move(20,550)
            text12 = QLabel('Divar:',self)
            text12.move(20,565)
        if self.productManufacturer == 'Tablet':
            self.productDetails()
            self.widgets()
            self.layouts()
            text1 = QLabel('name:',self)
            text1.move(20,400)

            text2 = QLabel('battery',self)
            text2.move(20,415)
            text3 = QLabel('size:',self)
            text3.move(20,430)
            text4 = QLabel('cores:',self)
            text4.move(20,445)
            text5 = QLabel('memory:',self)
            text5.move(20,460)
            text6 = QLabel('Ram:',self)
            text6.move(20,475)
            text7 = QLabel('weight:',self)
            text7.move(20,490)
            text8 = QLabel('camera:',self)
            text8.move(20,505)
            text9 = QLabel('chip:',self)
            text9.move(20,520)
            text10 = QLabel('colors:',self)
            text10.move(20,535)
            text11 = QLabel('Digikala:',self)
            text11.move(20,550)
            text12 = QLabel('Divar:',self)
            text12.move(20,565)
        
    def productDetails(self):
        global productId
        print('aaaaaaaaaaaa:',productId)
        print('productname',product_name)
        if productId == 'Mobile':
            query=("SELECT * FROM mobile WHERE product_name=?")
            product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,)

        if productId == 'Tablet':
            query=("SELECT * FROM Tablet WHERE product_name=?")
            product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,)

        if productId == 'Airpod':
            query=("SELECT * FROM Airpod WHERE product_name=?")
            product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,)


        self.productName=product[2]
        self.productManufacturer=product[1]
        self.productPrice=product[3]
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



    def uploadImg(self):
        size =(256,256)
        self.filename,ok =QFileDialog.getOpenFileName(self,'Upload Image','','Image files (*.jpg *.png)')
        if ok:
            self.productImg = os.path.basename(self.filename)
            img=Image.open(self.filename)
            img=img.resize(size)
            img.save("img/{0}".format(self.productImg))

    # def updateProduct(self):
    #     global productId
    #     name = self.nameEntry.text()
    #     manufacturer=self.manufacturerEntry.text()
    #     price=int(self.priceEntry.text())
    #     qouta=int(self.qoutaEntry.text())
    #     status=self.availabilityCombo.currentText()
    #     defaultImg=self.productImg

    #     if (name and manufacturer and price and qouta !=""):

    #         try:
    #             query="UPDATE products set product_name=?, product_manufacturer =?, product_price=?,product_qouta=?, product_img=?, product_availability=? WHERE product_id=?"
    #             cur.execute(query,(name,manufacturer,price,qouta,defaultImg,status,productId))
    #             con.commit()
    #             QMessageBox.information(self,"Info","Product has been updated!")
    #         except:
    #             QMessageBox.information(self, "Info", "Product has not been updated!")
    #     else:
    #         QMessageBox.information(self, "Info", "Fields cant be empty!")

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

class Display(QWidget):
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
            text1.move(20,400)
            tex1 = QLabel(self.productName,self)
            tex1.move(50,400)
            text2 = QLabel('battery',self)
            text2.move(20,415)
            text3 = QLabel('size:',self)
            text3.move(20,430)
            text4 = QLabel('cores:',self)
            text4.move(20,445)
            text5 = QLabel('memory:',self)
            text5.move(20,460)
            text6 = QLabel('Ram:',self)
            text6.move(20,475)
            text7 = QLabel('weight:',self)
            text7.move(20,490)
            text8 = QLabel('camera:',self)
            text8.move(20,505)
            text9 = QLabel('operating system:',self)
            text9.move(20,525)
            text9.resize(140,20)
            text10 = QLabel('colors:',self)
            text10.move(20,535)
            text11 = QLabel('Digikala:',self)
            text11.move(20,550)
            text12 = QLabel('Divar:',self)
            text12.move(20,565)
        if self.productManufacturer == 'Tablet':
            self.productDetails()
            self.widgets()
            self.layouts()
            text1 = QLabel('name:',self)
            text1.move(20,400)

            text2 = QLabel('battery',self)
            text2.move(20,415)
            text3 = QLabel('size:',self)
            text3.move(20,430)
            text4 = QLabel('cores:',self)
            text4.move(20,445)
            text5 = QLabel('memory:',self)
            text5.move(20,460)
            text6 = QLabel('Ram:',self)
            text6.move(20,475)
            text7 = QLabel('weight:',self)
            text7.move(20,490)
            text8 = QLabel('camera:',self)
            text8.move(20,505)
            text9 = QLabel('chip:',self)
            text9.move(20,520)
            text10 = QLabel('colors:',self)
            text10.move(20,535)
            text11 = QLabel('Digikala:',self)
            text11.move(20,550)
            text12 = QLabel('Divar:',self)
            text12.move(20,565)
        
    def productDetails(self):
        global productId
        print('aaaaaaaaaaaa:',productId)
        print('productname',product_name)
        if productId == 'Mobile':
            query=("SELECT * FROM mobile WHERE product_name=?")
            product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,)

        if productId == 'Tablet':
            query=("SELECT * FROM Tablet WHERE product_name=?")
            product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,)

        if productId == 'Airpod':
            query=("SELECT * FROM Airpod WHERE product_name=?")
            product=cur.execute(query,(product_name,)).fetchone()#single item tuple=(1,)


        self.productName=product[2]
        self.productManufacturer=product[1]
        self.productPrice=product[3]
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
        # self.addFavoritebtn=QPushButton("add to favorite")
        # self.addFavoritebtn.clicked.connect(self.favoriteProduct)
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
       
        # self.bottomLayout.addRow(QLabel(""),self.addFavoritebtn)
        # self.bottomLayout.addRow(QLabel(""),self.updateBtn)
        self.bottomFrame.setLayout(self.bottomLayout)
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)


        self.setLayout(self.mainLayout)



    # def uploadImg(self):
    #     size =(256,256)
    #     self.filename,ok =QFileDialog.getOpenFileName(self,'Upload Image','','Image files (*.jpg *.png)')
    #     if ok:
    #         self.productImg = os.path.basename(self.filename)
    #         img=Image.open(self.filename)
    #         img=img.resize(size)
    #         img.save("img/{0}".format(self.productImg))

    # def updateProduct(self):
    #     global productId
    #     name = self.nameEntry.text()
    #     manufacturer=self.manufacturerEntry.text()
    #     price=int(self.priceEntry.text())
    #     qouta=int(self.qoutaEntry.text())
    #     status=self.availabilityCombo.currentText()
    #     defaultImg=self.productImg

    #     if (name and manufacturer and price and qouta !=""):

    #         try:
    #             query="UPDATE products set product_name=?, product_manufacturer =?, product_price=?,product_qouta=?, product_img=?, product_availability=? WHERE product_id=?"
    #             cur.execute(query,(name,manufacturer,price,qouta,defaultImg,status,productId))
    #             con.commit()
    #             QMessageBox.information(self,"Info","Product has been updated!")
    #         except:
    #             QMessageBox.information(self, "Info", "Product has not been updated!")
    #     else:
    #         QMessageBox.information(self, "Info", "Fields cant be empty!")


        
class Favorite(QWidget):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Product Details")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(455,150,450,600)
        self.setFixedSize(self.size())
        self.UI()
        self.show()
    
    def UI(self):

        self.wigdet()
        self.layouts()
        self.displayProducts()
    

    def wigdet(self):
        self.productsTable = QTableWidget(self)
        self.productsTable.setColumnCount(4)
        self.productsTable.setColumnHidden(0,True)
    
        self.productsTable.setHorizontalHeaderItem(2,QTableWidgetItem("Product Name"))
        self.productsTable.setHorizontalHeaderItem(1,QTableWidgetItem("Manufacturer"))
        self.productsTable.setHorizontalHeaderItem(3,QTableWidgetItem("Price"))

        self.productsTable.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.productsTable.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
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
            print('lis',lis)
            for item in lis:
                query = cur.execute('SELECT product_manufacturer FROM mobile WHERE product_name = ?',(item,)).fetchone()
                if query != None:
                    if query[0] == 'Mobile':
                        query = cur.execute('SELECT * FROM mobile WHERE product_name = ?',(item,))
                        for row_data in query:
                            row_number = self.productsTable.rowCount()
                            self.productsTable.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                query = cur.execute('SELECT product_manufacturer FROM Tablet WHERE product_name = ?',(item,)).fetchone()
                if query != None:
                    if query[0] == 'Tablet':
                        query = cur.execute('SELECT * FROM Tablet WHERE product_name = ?',(item,))
                        for row_data in query:
                            row_number = self.productsTable.rowCount()
                            self.productsTable.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                query = cur.execute('SELECT product_manufacturer FROM Airpod WHERE product_name = ?',(item,)).fetchone()
                if query != None:
                    if query[0] == 'Airpod':
                        query = cur.execute('SELECT * FROM Airpod WHERE product_name = ?',(item,))
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
        product_name = listProduct[2]
        print('ssssssssS:',productId)
        print('line881:',product_name)

        self.display = Display()

        self.display.show()



def main():
    App=QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()

    