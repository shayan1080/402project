from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
import style
import webbrowser

con=sqlite3.connect("costumer.db")
cur=con.cursor()



class DisplayProduct(QWidget):
    def __init__(self,product_n , product_id,user_name,num):
        super().__init__()
        self.setWindowTitle("Product Details")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,400,700)
        self.setFixedSize(self.size())
        self.product_name = product_n
        self.productId = product_id
        self.user_name = user_name
        self.num = num
        self.setStyleSheet("""
            QTextEdit {
                background-color: #fcc324;
                border: 2px black;
                padding: 0px;
                font-size: 10px;
                font-weight: bold;
            }

            QLabel {
                color: #333;
                font-size: 12px;
                font-weight: bold;
            }
        """)
        self.UI()
        self.show()


    ##########Connect to webbrowser########
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

    ##########make QTextEdit and show data #############3
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
            btn.move(55,395)
            btn.clicked.connect(self.Digikala)

            btn = QPushButton('Divar',self)
            btn.move(155,395)
            btn.clicked.connect(self.Divar)

            btn = QPushButton('Third Website',self)
            btn.move(255,395)
            btn.clicked.connect(self.third_website)

            text1 = QLabel('name:',self)
            text1.move(20,425)
            tex1 = QTextEdit(self)
            tex1.setGeometry(60,433,200,15)
            tex1.setReadOnly(True)
            tex1.setText(self.productName)
     
            text2 = QLabel('battery:',self)
            tex2 = QTextEdit(self)
            text2.move(20,445)
            tex2.setGeometry(67,453,200,15)
            tex2.setReadOnly(True)
            tex2.setText(self.battery)
        
            text3 = QLabel('size:',self)
            text3.move(20,465)
            tex3 = QTextEdit(self)
            tex3.setGeometry(60,473,200,15)
            tex3.setReadOnly(True)
            tex3.setText(self.mobileSize)
      
            text4 = QLabel('cores:',self)
            text4.move(20,485)
            tex4 = QTextEdit(self)
            tex4.setGeometry(60,493,200,15)
            tex4.setReadOnly(True)
            tex4.setText(self.cores)  
         
            text5 = QLabel('memory:',self)
            text5.move(20,505)
            tex5 = QTextEdit(self)
            tex5.setGeometry(70,513,200,15)
            tex5.setReadOnly(True)
            tex5.setText(self.memory)  
          
            text6 = QLabel('Ram:',self)
            text6.move(20,525)
            tex6 = QTextEdit(self)
            tex6.setGeometry(60,533,200,15)
            tex6.setReadOnly(True)
            tex6.setText(self.ram) 
        
            text7 = QLabel('weight:',self)
            text7.move(20,545)
            tex7 = QTextEdit(self)
            tex7.setGeometry(65,553,200,15)
            tex7.setReadOnly(True)
            tex7.setText(self.weight) 
       
            text8 = QLabel('camera:',self)
            text8.move(20,565)
            tex8 = QTextEdit(self)
            tex8.setGeometry(70,573,200,15)
            tex8.setReadOnly(True)
            tex8.setText(self.camera) 
         
            text9 = QLabel('operating system:',self)
            text9.move(20,590)
            text9.resize(140,20)
            tex9 = QTextEdit(self)
            tex9.setGeometry(80,593,200,15)
            tex9.setReadOnly(True)
            tex9.setText(self.operating) 
   
            text10 = QLabel('colors:',self)
            text10.move(20,605)
            tex10 = QTextEdit(self)
            tex10.setGeometry(60,613,200,15)
            tex10.setReadOnly(True)
            tex10.setText(self.colors) 
 
            text11 = QLabel('Digikala:',self)
            text11.move(20,625)
            tex11 = QTextEdit(self)
            tex11.setGeometry(75,633,200,15)
            tex11.setReadOnly(True)
            tex11.setText(self.price1) 
         
            text12 = QLabel('Divar:',self)
            text12.move(20,645)
            tex12 = QTextEdit(self)
            tex12.setGeometry(60,653,200,15)
            tex12.setReadOnly(True)
            tex12.setText(self.price2) 

            text13 = QLabel('Third Website:',self)
            text13.move(20,665)
            tex13= QTextEdit(self)
            tex13.setGeometry(130,673,200,15)
            tex13.setReadOnly(True)
            tex13.setText(self.price3) 
     
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
            btn.move(55,395)
            btn.clicked.connect(self.Digikala)

            btn = QPushButton('Divar',self)
            btn.move(155,395)
            btn.clicked.connect(self.Divar)

            btn = QPushButton('Third Website',self)
            btn.move(255,395)
            btn.clicked.connect(self.third_website)

            text1 = QLabel('name:',self)
            text1.move(20,425)
            tex1 = QTextEdit(self)
            tex1.setGeometry(60,433,200,15)
            tex1.setReadOnly(True)
            tex1.setText(self.productName)
  
            text2 = QLabel('battery:',self)
            tex2 = QTextEdit(self)
            text2.move(20,445)
            tex2.setGeometry(67,453,200,15)
            tex2.setReadOnly(True)
            tex2.setText(self.battery)

            text3 = QLabel('size:',self)
            text3.move(20,465)
            tex3 = QTextEdit(self)
            tex3.setGeometry(60,473,200,15)
            tex3.setReadOnly(True)
            tex3.setText(self.mobileSize)
 
            text4 = QLabel('cores:',self)
            text4.move(20,485)
            tex4 = QTextEdit(self)
            tex4.setGeometry(60,493,200,15)
            tex4.setReadOnly(True)
            tex4.setText(self.cores)  
           
            text5 = QLabel('memory:',self)
            text5.move(20,505)
            tex5 = QTextEdit(self)
            tex5.setGeometry(70,513,200,15)
            tex5.setReadOnly(True)
            tex5.setText(self.memory)  
       
            text6 = QLabel('Ram:',self)
            text6.move(20,525)
            tex6 = QTextEdit(self)
            tex6.setGeometry(60,533,200,15)
            tex6.setReadOnly(True)
            tex6.setText(self.ram) 
       
            text7 = QLabel('chip:',self)
            text7.move(20,545)
            tex7 = QTextEdit(self)
            tex7.setGeometry(65,553,200,15)
            tex7.setReadOnly(True)
            tex7.setText(self.chip) 
      
            text8 = QLabel('camera:',self)
            text8.move(20,565)
            tex8 = QTextEdit(self)
            tex8.setGeometry(70,573,200,15)
            tex8.setReadOnly(True)
            tex8.setText(self.camera) 
          
            text9 = QLabel('material:',self)
            text9.move(20,590)
            text9.resize(140,20)
            tex9 = QTextEdit(self)
            tex9.setGeometry(80,593,200,15)
            tex9.setReadOnly(True)
            tex9.setText(self.material) 
        
            text10 = QLabel('colors:',self)
            text10.move(20,605)
            tex10 = QTextEdit(self)
            tex10.setGeometry(60,613,200,15)
            tex10.setReadOnly(True)
            tex10.setText(self.colors) 
       
            text11 = QLabel('Digikala:',self)
            text11.move(20,625)
            tex11 = QTextEdit(self)
            tex11.setGeometry(75,633,200,15)
            tex11.setReadOnly(True)
            tex11.setText(self.price1) 
    
            text12 = QLabel('Divar:',self)
            text12.move(20,645)
            tex12 = QTextEdit(self)
            tex12.setGeometry(60,653,200,15)
            tex12.setReadOnly(True)
            tex12.setText(self.price2) 
   
            text13 = QLabel('Third Website:',self)
            text13.move(20,665)
            tex13= QTextEdit(self)
            tex13.setGeometry(130,673,200,15)
            tex13.setReadOnly(True)
            tex13.setText(self.price3) 

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
            btn.move(55,395)
            btn.clicked.connect(self.Digikala)

            btn = QPushButton('Divar',self)
            btn.move(155,395)
            btn.clicked.connect(self.Divar)

            btn = QPushButton('Third Website',self)
            btn.move(255,395)
            btn.clicked.connect(self.third_website)

            text1 = QLabel('name:',self)
            text1.move(20,425)
            tex1 = QTextEdit(self)
            tex1.setGeometry(60,433,200,15)
            tex1.setReadOnly(True)
            tex1.setText(self.productName)

            text2 = QLabel('type:',self)
            tex2 = QTextEdit(self)
            text2.move(20,445)
            tex2.setGeometry(67,453,200,15)
            tex2.setReadOnly(True)
            tex2.setText(self.type)

            text3 = QLabel('acostic_type:',self)
            text3.move(20,465)
            tex3 = QTextEdit(self)
            tex3.setGeometry(60,473,200,15)
            tex3.setReadOnly(True)
            tex3.setText(self.acostic)
        
            text4 = QLabel('connection:',self)
            text4.move(20,485)
            tex4 = QTextEdit(self)
            tex4.setGeometry(100,493,100,15)
            tex4.setReadOnly(True)
            tex4.setText(self.connection)  
      
            text5 = QLabel('noise_cancelling:',self)
            text5.move(20,505)
            tex5 = QTextEdit(self)
            tex5.setGeometry(130,513,100,25)
            tex5.setReadOnly(True)
            tex5.setText(self.noiseCancelling)  

            text6 = QLabel('Blutooth:',self)
            text6.move(20,525)
            tex6 = QTextEdit(self)
            tex6.setGeometry(90,533,200,15)
            tex6.setReadOnly(True)
            tex6.setText(self.blutooth) 
 
            text7 = QLabel('color:',self)
            text7.move(20,545)
            tex7 = QTextEdit(self)
            tex7.setGeometry(65,553,200,15)
            tex7.setReadOnly(True)
            tex7.setText(self.color) 

            text11 = QLabel('Digikala:',self)
            text11.move(20,565)
            tex11 = QTextEdit(self)
            tex11.setGeometry(75,573,200,15)
            tex11.setReadOnly(True)
            tex11.setText(self.price1) 
 
            text12 = QLabel('Divar:',self)
            text12.move(20,585)
            tex12 = QTextEdit(self)
            tex12.setGeometry(60,593,200,15)
            tex12.setReadOnly(True)
            tex12.setText(self.price2) 

            text13 = QLabel('Third Website:',self)
            text13.move(20,605)
            tex13= QTextEdit(self)
            tex13.setGeometry(130,613,200,15)
            tex13.setReadOnly(True)
            tex13.setText(self.price3) 

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
            btn.move(55,395)
            btn.clicked.connect(self.Digikala)

            btn = QPushButton('Divar',self)
            btn.move(155,395)
            btn.clicked.connect(self.Divar)

            btn = QPushButton('Third Website',self)
            btn.move(255,395)
            btn.clicked.connect(self.third_website)

            text1 = QLabel('name:',self)
            text1.move(20,425)
            tex1 = QTextEdit(self)
            tex1.setGeometry(60,433,200,15)
            tex1.setReadOnly(True)
            tex1.setText(self.productName)
    
            text2 = QLabel('screen_type:',self)
            tex2 = QTextEdit(self)
            text2.move(20,445)
            tex2.setGeometry(67,453,200,15)
            tex2.setReadOnly(True)
            tex2.setText(self.screenType)
     
            text3 = QLabel('screen_size:',self)
            text3.move(20,465)
            tex3 = QTextEdit(self)
            tex3.setGeometry(60,473,200,15)
            tex3.setReadOnly(True)
            tex3.setText(self.screenSize)
    
            text4 = QLabel('resolution:',self)
            text4.move(20,485)
            tex4 = QTextEdit(self)
            tex4.setGeometry(60,493,200,15)
            tex4.setReadOnly(True)
            tex4.setText(self.resolution)  
            
            text5 = QLabel('color:',self)
            text5.move(20,505)
            tex5 = QTextEdit(self)
            tex5.setGeometry(70,513,200,15)
            tex5.setReadOnly(True)
            tex5.setText(self.color)  

            text6 = QLabel('weight:',self)
            text6.move(20,525)
            tex6 = QTextEdit(self)
            tex6.setGeometry(60,533,200,15)
            tex6.setReadOnly(True)
            tex6.setText(self.weight) 
     
            text7 = QLabel('dimension:',self)
            text7.move(20,545)
            tex7 = QTextEdit(self)
            tex7.setGeometry(65,553,200,15)
            tex7.setReadOnly(True)
            tex7.setText(self.dimension) 

            text8 = QLabel('battery:',self)
            text8.move(20,565)
            tex8 = QTextEdit(self)
            tex8.setGeometry(70,573,200,15)
            tex8.setReadOnly(True)
            tex8.setText(self.battery) 

            text11 = QLabel('Digikala:',self)
            text11.move(20,625)
            tex11 = QTextEdit(self)
            tex11.setGeometry(75,633,200,15)
            tex11.setReadOnly(True)
            tex11.setText(self.price1) 

            text12 = QLabel('Divar:',self)
            text12.move(20,645)
            tex12 = QTextEdit(self)
            tex12.setGeometry(60,653,200,15)
            tex12.setReadOnly(True)
            tex12.setText(self.price2) 

            text13 = QLabel('Third Website:',self)
            text13.move(20,665)
            tex13= QTextEdit(self)
            tex13.setGeometry(130,673,200,15)
            tex13.setReadOnly(True)
            tex13.setText(self.price3) 

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
            btn.move(55,395)
            btn.clicked.connect(self.Digikala)

            btn = QPushButton('Divar',self)
            btn.move(155,395)
            btn.clicked.connect(self.Divar)

            btn = QPushButton('Third Website',self)
            btn.move(255,395)
            btn.clicked.connect(self.third_website)

            text1 = QLabel('name:',self)
            text1.move(20,425)
            tex1 = QTextEdit(self)
            tex1.setGeometry(60,433,200,15)
            tex1.setReadOnly(True)
            tex1.setText(self.productName)

            text2 = QLabel('laptop_size:',self)
            tex2 = QTextEdit(self)
            text2.move(20,445)
            tex2.setGeometry(67,453,200,15)
            tex2.setReadOnly(True)
            tex2.setText(self.laptopSize)

            text3 = QLabel('weight:',self)
            text3.move(20,465)
            tex3 = QTextEdit(self)
            tex3.setGeometry(60,473,200,15)
            tex3.setReadOnly(True)
            tex3.setText(self.weight)

            text4 = QLabel('ram:',self)
            text4.move(20,485)
            tex4 = QTextEdit(self)
            tex4.setGeometry(60,493,200,15)
            tex4.setReadOnly(True)
            tex4.setText(self.ram)  

            text5 = QLabel('memory:',self)
            text5.move(20,505)
            tex5 = QTextEdit(self)
            tex5.setGeometry(70,513,200,15)
            tex5.setReadOnly(True)
            tex5.setText(self.memory)  

            text6 = QLabel('battery:',self)
            text6.move(20,525)
            tex6 = QTextEdit(self)
            tex6.setGeometry(60,533,200,15)
            tex6.setReadOnly(True)
            tex6.setText(self.battery) 

            text7 = QLabel('screen_size:',self)
            text7.move(20,545)
            tex7 = QTextEdit(self)
            tex7.setGeometry(65,553,200,15)
            tex7.setReadOnly(True)
            tex7.setText(self.screenSize) 

            text8 = QLabel('processor:',self)
            text8.move(20,565)
            tex8 = QTextEdit(self)
            tex8.setGeometry(70,573,200,15)
            tex8.setReadOnly(True)
            tex8.setText(self.processor) 

            text9 = QLabel('resolution:',self)
            text9.move(20,590)
            text9.resize(140,20)
            tex9 = QTextEdit(self)
            tex9.setGeometry(80,593,200,15)
            tex9.setReadOnly(True)
            tex9.setText(self.resolution) 
  
            text11 = QLabel('Digikala:',self)
            text11.move(20,625)
            tex11 = QTextEdit(self)
            tex11.setGeometry(75,633,200,15)
            tex11.setReadOnly(True)
            tex11.setText(self.price1) 
            
            text12 = QLabel('Divar:',self)
            text12.move(20,645)
            tex12 = QTextEdit(self)
            tex12.setGeometry(60,653,200,15)
            tex12.setReadOnly(True)
            tex12.setText(self.price2) 
 
            text13 = QLabel('Third Website:',self)
            text13.move(20,665)
            tex13= QTextEdit(self)
            tex13.setGeometry(130,673,200,15)
            tex13.setReadOnly(True)
            tex13.setText(self.price3) 

    def productDetails(self):
        ##############Get data of products from db###################
        if self.productId == 'Mobile':
            query=("SELECT * FROM mobile WHERE product_name=?")
            product=cur.execute(query,(self.product_name,)).fetchone()#single item tuple=(1,)
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

        if self.productId == 'Tablet':
            query=("SELECT * FROM Tablet WHERE product_name=?")
            product=cur.execute(query,(self.product_name,)).fetchone()#single item tuple=(1,)
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

        if self.productId == 'Airpod':
            query=("SELECT * FROM Airpod WHERE product_name=?")
            product=cur.execute(query,(self.product_name,)).fetchone()#single item tuple=(1,)
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

        if self.productId == 'Clock':
            query=("SELECT * FROM Clock WHERE product_name=?")
            product=cur.execute(query,(self.product_name,)).fetchone()#single item tuple=(1,)
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

        if self.productId == 'Laptop':
            query=("SELECT * FROM Laptop WHERE product_name=?")
            product=cur.execute(query,(self.product_name,)).fetchone()#single item tuple=(1,)
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
        if self.num == '1':
            self.addFavoritebtn=QPushButton("add to favorite")
            self.addFavoritebtn.clicked.connect(self.favoriteProduct)
        if self.num == '2':
            self.addFavoritebtn=QPushButton("delete from favorite")
            self.addFavoritebtn.clicked.connect(self.deleteFavoriteProduct)

    def layouts(self):
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.topLayout.setSpacing(1000)
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

    def deleteFavoriteProduct(self):
        res = ''
        query = cur.execute('SELECT favorite FROM member where user_name = ?',(self.user_name,)).fetchone()  
        x = query[0].split(',')
        x.remove(self.product_name)
        for item in x:
            res = res + item + ','
        res = res[:-1]
        cur.execute(f'UPDATE member SET favorite= ? WHERE user_name = ?',(res,self.user_name))
        con.commit()      
        query = cur.execute('SELECT favorite FROM member where user_name = ?',(self.user_name,)).fetchone()
  

    def favoriteProduct(self):
        global favoriteProductsName
        ###############Add to favorite product with checking it in db and save it in favorite coloumn of selected user_name########
        favoriteProductsName = self.productName
        query = cur.execute('SELECT product_manufacturer FROM mobile WHERE product_name = ?',(favoriteProductsName,)).fetchone()
 
        try:
            query = cur.execute('SELECT product_manufacturer FROM mobile WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            if query != None:
                if query[0] == 'Mobile':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(self.user_name,)).fetchone()
            query = cur.execute('SELECT product_manufacturer FROM Tablet WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            if query != None:
                if query[0] == 'Tablet':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(self.user_name,)).fetchone()
            query = cur.execute('SELECT product_manufacturer FROM Airpod WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            if query != None:
                if query[0] == 'Airpod':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(self.user_name,)).fetchone()

            query = cur.execute('SELECT product_manufacturer FROM Clock WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            if query != None:
                if query[0] == 'Clock':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(self.user_name,)).fetchone()

            query = cur.execute('SELECT product_manufacturer FROM Laptop WHERE product_name = ?',(favoriteProductsName,)).fetchone()
            if query != None:
                if query[0] == 'Laptop':
                    a = cur.execute('SELECT favorite FROM member WHERE user_name = ?',(self.user_name,)).fetchone()

            if a[0] == None:
                favoriteProductsName = self.productName
            else:
                favoriteProductsName = a[0] + ','+ self.productName
            cur.execute(f'UPDATE member SET favorite= ? WHERE user_name = ?',(favoriteProductsName,self.user_name))
            con.commit()
        except:
            QMessageBox.information(self, "Info", "log in to your panel first")