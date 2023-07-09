from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import arabic_reshaper
from bidi.algorithm import get_display
import sqlite3

conn = sqlite3.connect('costumer.db')
c = conn.cursor()

def persian_to_english(persian_currency):
    
    if persian_currency == "ناموجود":
        return persian_currency
    else:
        persian_number = re.sub("[٬,]", "", persian_currency)
        persian_number = persian_number.replace("تومان", "").strip()
        
        
        reshaped_text = arabic_reshaper.reshape(persian_number)
        bidi_text = get_display(reshaped_text)
        english_number = bidi_text.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
        
        english_number = "{:,}".format(int(english_number))
        
        return english_number


driver = webdriver.Chrome()

######################################
"""   AIRPODS       """

"""   QCY T19 """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/qcy-t19/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
Type_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[1]/td[2]")
acostic_type_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[2]/td[2]")
connection_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[3]/td[2]")
airpodtype_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[4]/td[2]")
noisecancelling_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
blutooth_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[14]/tr[3]/td[2]")
color_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[1]/td[2]")
# Extract the text
name = name_element.text
Type = Type_element.text
acostic = acostic_type_element.text
connection = connection_element.text
airpodtype = airpodtype_element.text
noisecancelling = noisecancelling_element.text
blutooth = blutooth_element.text
color = color_element.text


driver.get("https://www.digikala.com/product/dkp-9349961/%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D8%A8%DB%8C-%D8%B3%DB%8C%D9%85-%DA%A9%DB%8C%D9%88-%D8%B3%DB%8C-%D9%88%D8%A7%DB%8C-%D9%85%D8%AF%D9%84-rak-new-bt-item-t19-2022/")
time.sleep(3)
try:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
    Digikala = Digikala_price_element.text
except:
    Digikala = "ناموجود"

driver.get("https://www.technolife.ir/product-5829/%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D8%A8%DB%8C-%D8%B3%DB%8C%D9%85-%DA%A9%DB%8C%D9%88-%D8%B3%DB%8C-%D9%88%D8%A7%DB%8C-%D9%85%D8%AF%D9%84-t19-")
time.sleep(3)

try:
    Technolife_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(2) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
except:
    Technolife_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
Technolife = Technolife_price_element.text

driver.get("https://divar.ir/s/tehran/mobile-tablet-accessories?q=t%2019")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text
# print(Divar)
# time.sleep(40)
# Write the data to a text file
c.execute(f'UPDATE Airpod SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(Technolife),name))
conn.commit()

"""   QCY T13 """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/qcy-t13/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
Type_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[1]/td[2]")
acostic_type_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[2]/td[2]")
connection_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[3]/td[2]")
airpodtype_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[4]/td[2]")
noisecancelling_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
blutooth_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[14]/tr[3]/td[2]")
color_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[2]/td[2]")
# Extract the text
name = name_element.text
Type = Type_element.text
acostic = acostic_type_element.text
connection = connection_element.text
airpodtype = airpodtype_element.text
noisecancelling = noisecancelling_element.text
blutooth = blutooth_element.text
color = color_element.text


driver.get("https://www.digikala.com/product/dkp-5856710/%D9%87%D8%AF%D9%81%D9%88%D9%86-%D8%A8%D9%84%D9%88%D8%AA%D9%88%D8%AB%DB%8C-%DA%A9%DB%8C%D9%88-%D8%B3%DB%8C-%D9%88%D8%A7%DB%8C-%D9%85%D8%AF%D9%84-t13-tws/")
time.sleep(3)
                                                            
try:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
    Digikala = Digikala_price_element.text
except:
    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3 > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
        Digikala = Digikala_price_element.text
    except:
        try:
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
            Digikala = Digikala_price_element.text

        except:
            Digikala = "ناموجود"


driver.get("https://www.technolife.ir/product-3163/%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D8%A8%DB%8C-%D8%B3%DB%8C%D9%85-%DA%A9%DB%8C%D9%88-%D8%B3%DB%8C-%D9%88%D8%A7%DB%8C-%D9%85%D8%AF%D9%84-t13-")
time.sleep(3)

Technolife_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
Technolife = Technolife_price_element.text

driver.get("https://divar.ir/s/tehran/mobile-tablet-accessories?goods-business-type=all&q=t13%20tws")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


# Write the data to a text file
c.execute(f'UPDATE Airpod SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(Technolife),name))
conn.commit()

"""   Buds 2 PRO """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/samsung-galaxy-buds2-pro/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
Type_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[2]/tr[1]/td[2]")
acostic_type_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[2]/tr[2]/td[2]")
connection_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[2]/tr[3]/td[2]")                     
airpodtype_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[2]/tr[4]/td[2]")
noisecancelling_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[4]/tr[2]/td[2]")
blutooth_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[14]/tr[3]/td[2]")
color_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[12]/tr[3]/td[2]")
# Extract the text
name = name_element.text
Type = Type_element.text
acostic = acostic_type_element.text
connection = connection_element.text
airpodtype = airpodtype_element.text
noisecancelling = noisecancelling_element.text
blutooth = blutooth_element.text
color = color_element.text


driver.get("https://www.digikala.com/product/dkp-9188766/%D9%87%D8%AF%D9%81%D9%88%D9%86-%D8%A8%D9%84%D9%88%D8%AA%D9%88%D8%AB%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-buds2-pro/")
time.sleep(3)
try:
    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
    except:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")

except:

    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3 > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
                                                                  
Digikala = Digikala_price_element.text

driver.get("https://www.technolife.ir/product-7383/-%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D8%A8%DB%8C-%D8%B3%DB%8C%D9%85-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-buds-2-pro")
time.sleep(3)

Technolife_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(2) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
Technolife = Technolife_price_element.text

driver.get("https://divar.ir/s/tehran/mobile-tablet-accessories?goods-business-type=all&q=buds2%20pro")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


# Write the data to a text file
c.execute(f'UPDATE Airpod SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(Technolife),name))
conn.commit()


"""   XIAOMI REDMI BUDS 3 PRO """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/xiaomi-redmi-airdots-3-pro/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
Type_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[2]/td[2]")
acostic_type_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[3]/td[2]")
connection_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[4]/td[2]")
airpodtype_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[5]/td[2]")
noisecancelling_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[3]/td[2]")
blutooth_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[14]/tr[3]/td[2]")
color_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[3]/td[2]")
# Extract the text
name = name_element.text
Type = Type_element.text
acostic = acostic_type_element.text
connection = connection_element.text
airpodtype = airpodtype_element.text
noisecancelling = noisecancelling_element.text
blutooth = blutooth_element.text
color = color_element.text


driver.get("https://www.digikala.com/product/dkp-9555069/%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D8%A8%D9%84%D9%88%D8%AA%D9%88%D8%AB%DB%8C-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-thi-global-earbuds-redmi-buds-3-pro-reduction/")
time.sleep(3)
try:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
    Digikala = Digikala_price_element.text
except:
    Digikala = "ناموجود"
driver.get("https://hamechionline.ir/xiaomi-redmi-airdots-3-pro")
time.sleep(3)

hamechionline_price_element = driver.find_element(By.CSS_SELECTOR,"body > main.product-container.ng-scope:nth-child(5) > div.container > div.product-context:nth-child(1) > div.banners.border-amp.bg-white-amp.p-25.p-sm-30.p-md-40:nth-child(2) > div.row:nth-child(1) > div.col-md-8:nth-child(2) > div.product-left-container.pr-lg-20 > div.row:nth-child(2) > div.col-12.card-shadow.border-amp.bg-white-amp.p-30 > form.product-info.ng-scope.ng-valid-min.ng-valid-max.ng-dirty.ng-valid-parse.ng-valid.ng-valid-required:nth-child(1) > div.product-buttons.d-flex.align-items-center.flex-column.flex-sm-row.justify-content-between.w-100:nth-child(8) > div.product-price-container:nth-child(4) > h5.product-price > span.ng-binding:nth-child(3)")
hamechionline = hamechionline_price_element.text

driver.get("https://divar.ir/s/tehran?q=BUDS%203%20PRO")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


# Write the data to a text file
c.execute(f'UPDATE Airpod SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(hamechionline),name))
conn.commit()


"""   AIRPODS 3     """

"""    """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/apple-airpods-3nd-generation/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
Type_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[2]/td[2]")
acostic_type_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[3]/td[2]")
connection_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[4]/td[2]")
airpodtype_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[5]/td[2]")
noisecancelling_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[1]/td[2]")
blutooth_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[14]/tr[3]/td[2]")
color_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[3]/td[2]")
# Extract the text
name = name_element.text
Type = Type_element.text
acostic = acostic_type_element.text
connection = connection_element.text
airpodtype = airpodtype_element.text
noisecancelling = noisecancelling_element.text
blutooth = blutooth_element.text
color = color_element.text


driver.get("https://www.digikala.com/product/dkp-6801162/%D9%87%D8%AF%D9%81%D9%88%D9%86-%D8%A8%DB%8C-%D8%B3%DB%8C%D9%85-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-airpods-3-%D9%87%D9%85%D8%B1%D8%A7%D9%87-%D8%A8%D8%A7-%D9%85%D8%AD%D9%81%D8%B8%D9%87-%D8%B4%D8%A7%D8%B1%DA%98/")
time.sleep(3)
try:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
    Digikala = Digikala_price_element.text
except:
    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3 > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
        Digikala = Digikala_price_element.text
    except:
        Digikala = "ناموجود"


driver.get("https://www.technolife.ir/product-3544/%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D8%A8%DB%8C-%D8%B3%DB%8C%D9%85-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-airpods-3")
time.sleep(3)

Technolife_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(2) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
Technolife = Technolife_price_element.text

driver.get("https://divar.ir/s/tehran/mobile-tablet-accessories?goods-business-type=all&q=airpods%203")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


# Write the data to a text file
c.execute(f'UPDATE Airpod SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(Technolife),name))
conn.commit()


######################################
"""   LAPTOPS     """

"""  APPLE MACBOOK PRO 14 2021 M1 PRO  """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/apple-macbook-pro-14-2021-m1-pro-16gb-512gb/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[1]/td[2]")
weight_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[2]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[1]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[2]/td[2]")
battery_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[14]/tr[1]/td[2]")
screensize_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[1]/td[2]")
processor_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr/td[2]")
resolotion_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
# Extract the text
name = name_element.text
size = size_element.text
weight = weight_element.text
RAM = RAM_element.text
memory = memory_element.text
battery = battery_element.text
screensize = screensize_element.text
processor = processor_element.text
resolotion = resolotion_element.text


driver.get("https://www.digikala.com/product/dkp-8687163/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-142-%D8%A7%DB%8C%D9%86%DA%86-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-macbook-mkgp3-m1-pro-2021/")
time.sleep(3)

Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
Digikala = Digikala_price_element.text

driver.get("https://amitis-group.com/product/%d8%a7%d9%be%d9%84-%d9%85%d8%af%d9%84-%d9%85%da%a9-%d8%a8%d9%88%da%a9-%d9%be%d8%b1%d9%88-mkgr3-1%db%b4-inch/")
time.sleep(3)

amitis_price_element = driver.find_element(By.CSS_SELECTOR,"body > div.website-wrapper:nth-child(10) > div.main-page-wrapper:nth-child(2) > div.container-fluid > div.row.content-layout-wrapper.align-items-start > div.site-content.shop-content-area.col-12.breadcrumbs-location-summary.wd-builder-off > div#product-249572.single-product-page.single-product-content.product-design-default.tabs-location-standard.tabs-type-tabs.meta-location-add_to_cart.reviews-location-separate.product-summary-shadow.product-no-bg.product.type-product.post-249572.status-publish.first.instock.product_cat-hot.product_cat-15774.product_cat-product.product_cat-macbook-pro.product_cat-14-inch-macbook-pro.product_cat-m1-m1pro-m1max.has-post-thumbnail.shipping-taxable.purchasable.product-type-variable.has-default-attributes:nth-child(2) > div.container:nth-child(1) > div.row.product-image-summary-wrap:nth-child(2) > div.product-image-summary.col-lg-12.col-12.col-md-12 > div.row.product-image-summary-inner > div.col-lg-6.col-12.col-md-6.text-right.summary.entry-summary:nth-child(2) > div.summary-inner > p.price:nth-child(3) > span.woocommerce-Price-amount.amount > bdi")
amitis = amitis_price_element.text

driver.get("https://divar.ir/s/tehran?q=macbook%20m1%20pro%202021")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


c.execute(f'UPDATE Laptop SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(amitis),name))
conn.commit()

"""  ASUS VIVOBOOK R565EP  """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/asus-vivobook-r565ep-core-i7-1135g7-mx330-8gb-512gb/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[1]/td[2]")
weight_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[2]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[1]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[3]/td[2]")
battery_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[14]/tr[1]/td[2]")
screensize_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[1]/td[2]")
processor_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr/td[2]")
resolotion_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
# Extract the text
name = name_element.text
size = size_element.text
weight = weight_element.text
RAM = RAM_element.text
memory = memory_element.text
battery = battery_element.text
screensize = screensize_element.text
processor = processor_element.text
resolotion = resolotion_element.text


driver.get("https://www.digikala.com/product/dkp-11152888/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-156-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-%D9%85%D8%AF%D9%84-vivobook-r565ep-ej615-i5-16gb-512ssd-mx330-%DA%A9%D8%A7%D8%B3%D8%AA%D9%88%D9%85-%D8%B4%D8%AF%D9%87-clone-1-of-11050158/")
time.sleep(3)

Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
Digikala = Digikala_price_element.text

driver.get("https://www.technolife.ir/product-10637/%D9%84%D9%BE%E2%80%8C-%D8%AA%D8%A7%D9%BE-15.6-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-%D9%85%D8%AF%D9%84-vivobook-r565ep-ej615")
time.sleep(3)

techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(2) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
techno = techno_price_element.text

driver.get("https://divar.ir/s/tehran?q=ASUS%20VIVOBOOK%20R565EP")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


c.execute(f'UPDATE Laptop SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()



"""  MICROSOFT SURFACE LAPTOP GO  """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/microsoft-surface-laptop-go-core-i5-1035g1-uhd-8gb-256gb/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[1]/td[2]")
weight_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[2]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[1]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[3]/td[2]")
battery_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[14]/tr[1]/td[2]")
screensize_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[1]/td[2]")
processor_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr/td[2]")
resolotion_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
# Extract the text
name = name_element.text
size = size_element.text
weight = weight_element.text
RAM = RAM_element.text
memory = memory_element.text
battery = battery_element.text
screensize = screensize_element.text
processor = processor_element.text
resolotion = resolotion_element.text


driver.get("https://www.digikala.com/product/dkp-5341288/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-124-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA-%D9%85%D8%AF%D9%84-surface-laptop-go-b/")
time.sleep(3)

Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
Digikala = Digikala_price_element.text

driver.get("https://adak.shop/product/laptop-microsoft-surface-laptop-go/")
time.sleep(3)

adak_price_element = driver.find_element(By.CSS_SELECTOR,"body > section#product-wrap:nth-child(8) > div.container.product_inwrap > div.row > div.col-md-12 > div#product-71649.post-71649.product.type-product.status-publish.has-post-thumbnail.product_cat-laptop-and-accessories.product_cat-laptop.product_cat-microsoft-laptops.first.instock.shipping-taxable.purchasable.product-type-variable.has-default-attributes:nth-child(2) > div.product-image-description:nth-child(1) > div.row > div.col-lg-6:nth-child(1) > div.summary.entry-summary > form.variations_form.cart:nth-child(4) > div.single_variation_wrap:nth-child(3) > div.woocommerce-variation.single_variation:nth-child(1) > div.woocommerce-variation-price:nth-child(2) > span.price > span.woocommerce-Price-amount.amount:nth-child(2) > bdi")
adak = adak_price_element.text

driver.get("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&q=surface%20laptop%20go")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[1]/div/div/div/div[4]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


# Write the data to a text file
c.execute(f'UPDATE Laptop SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(adak),name))
conn.commit()
"""  ASUS VIVOBOOK X515EP  """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/asus-vivobook-x515ep-core-i5-1135g7-mx330-16gb-512gb/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[1]/td[2]")
weight_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[2]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[1]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[3]/td[2]")
battery_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[14]/tr[1]/td[2]")
screensize_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[1]/td[2]")
processor_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr/td[2]")
resolotion_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
# Extract the text
name = name_element.text
size = size_element.text
weight = weight_element.text
RAM = RAM_element.text
memory = memory_element.text
battery = battery_element.text
screensize = screensize_element.text
processor = processor_element.text
resolotion = resolotion_element.text


driver.get("https://www.digikala.com/product/dkp-9723829/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-156-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-%D9%85%D8%AF%D9%84-vivobook-x515ep-ej338-i5-16gb-1ssd-mx330-%DA%A9%D8%A7%D8%B3%D8%AA%D9%88%D9%85-%D8%B4%D8%AF%D9%87/")
time.sleep(3)

Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
Digikala = Digikala_price_element.text

driver.get("https://www.technolife.ir/product-11556/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-15.6-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D9%85%D8%AF%D9%84-vivobook-x515ep-ej338")
time.sleep(3)

techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(2) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
techno = techno_price_element.text

driver.get("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&q=VIVOBOOK%20X515EP")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[1]/div/div/div/div[4]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


# Write the data to a text file
c.execute(f'UPDATE Laptop SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()


"""  ASUS ROG STRIX G15 G513RC  """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/asus-rog-strix-g15-g513rc-ryzen-7-6800h-rtx-3050-16gb-1tb/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[1]/td[2]")
weight_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[2]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[1]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[3]/td[2]")
battery_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[14]/tr[1]/td[2]")
screensize_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[1]/td[2]")
processor_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr/td[2]")
resolotion_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
# Extract the text
name = name_element.text
size = size_element.text
weight = weight_element.text
RAM = RAM_element.text
memory = memory_element.text
battery = battery_element.text
screensize = screensize_element.text
processor = processor_element.text
resolotion = resolotion_element.text


driver.get("https://www.digikala.com/product/dkp-9734995/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-156-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-%D9%85%D8%AF%D9%84-rog-strix-g513rc-hn136/")
time.sleep(3)

Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
Digikala = Digikala_price_element.text

driver.get("https://www.technolife.ir/product-7794/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-15.6-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-%D9%85%D8%AF%D9%84-rog-strix-g15-g513rc-hn101-")
time.sleep(3)

techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
techno = techno_price_element.text

driver.get("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&q=G513RC")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[1]/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


# Write the data to a text file
c.execute(f'UPDATE Laptop SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()


def persian_to_english(persian_currency):
    
    if persian_currency == "ناموجود":
        return persian_currency
    else:
        persian_number = re.sub("[٬,]", "", persian_currency)
        persian_number = persian_number.replace("تومان", "").strip()
        
        
        reshaped_text = arabic_reshaper.reshape(persian_number)
        bidi_text = get_display(reshaped_text)
        english_number = bidi_text.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
        
        english_number = "{:,}".format(int(english_number))
        
        return english_number
    



#####################################
"""   MOBILE       """

"""   S22Ultra 256 12   """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/samsung-galaxy-s22-ultra/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
battery_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[16]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
cores_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[3]/td[2]")
operatingsystem_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[8]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[3]/td[2]")
weight_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
camera_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[2]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[6]/td[2]")
# Extract the text
name = name_element.text
battery = battery_element.text
screen_size = screen_size_element.text
cores = cores_element.text
operatingsystem = operatingsystem_element.text
RAM = RAM_element.text
memory = memory_element.text
weight = weight_element.text
camera = camera_element.text
color = color__element.text

driver.get("https://www.digikala.com/product/dkp-10261550/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-s22-ultra-5g-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-12-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%86%D8%B3%D8%AE%D9%87-%D8%A7%D8%B3%D9%86%D9%BE%D8%AF%D8%B1%D8%A7%DA%AF%D9%88%D9%86-%D9%88%DB%8C%D8%AA%D9%86%D8%A7%D9%85/")
time.sleep(5)

try:                                                          
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
except:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
Digikala = Digikala_price_element.text

driver.get("https://www.technolife.ir/product-10032/-%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-%DA%AF%D9%84%DA%A9%D8%B3%DB%8C-s22-ultra-5g-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D8%B1%D9%85-12-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D9%88%DB%8C%D8%AA%D9%86%D8%A7%D9%85")
time.sleep(3)

try:
    try:
        techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
        techno = techno_price_element.text
    except:
        techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(2) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
        techno = techno_price_element.text
except:
    techno  = "ناموجود"



driver.get("https://divar.ir/goods/mobile/prices?q=s22")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/p[2]")
Divar = Divar_element.text
# Write the data to a text file
c.execute(f'UPDATE mobile SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()
 
# Quit the WebDriver

"""   F13 64 4    """

driver.get("https://www.zoomit.ir/product/samsung-galaxy-f13/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
battery_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[16]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
cores_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[3]/td[2]")
operatingsystem_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[8]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[3]/td[2]")
weight_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
camera_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[2]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[6]/td[2]")
# Extract the text
name = name_element.text
battery = battery_element.text
screen_size = screen_size_element.text
cores = cores_element.text
operatingsystem = operatingsystem_element.text
RAM = RAM_element.text
memory = memory_element.text
weight = weight_element.text
camera = camera_element.text
color = color__element.text

driver.get("https://www.digikala.com/product/dkp-9666954/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-f13-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%87%D9%86%D8%AF/")
time.sleep(5)      
                                                       
try:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
except:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")

Digikala = Digikala_price_element.text

driver.get("https://divar.ir/goods/mobile/prices?q=F13")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/p[2]")
Divar = Divar_element.text

driver.get("https://www.technolife.ir/product-7658/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-f13-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA?utm_source=ZoomitDB&utm_medium=PriceList")
time.sleep(3)

techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
techno = techno_price_element.text

c.execute(f'UPDATE mobile SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()




"""   poco x4 pro 5G 256 8    """ 

driver.get("https://www.zoomit.ir/product/xiaomi-poco-x4-pro-5g/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
battery_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[16]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
cores_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[3]/td[2]")
operatingsystem_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[5]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[3]/td[2]")
weight_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
camera_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[2]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[6]/td[2]")
# Extract the text
name = name_element.text
battery = battery_element.text
screen_size = screen_size_element.text
cores = cores_element.text
operatingsystem = operatingsystem_element.text
RAM = RAM_element.text
memory = memory_element.text
weight = weight_element.text
camera = camera_element.text
color = color__element.text

driver.get("https://www.digikala.com/product/dkp-8123707/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-poco-x4-pro-5g-2201116pg-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/")
time.sleep(3)
                                                                 


try:  
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3 > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
    Digikala = Digikala_price_element.text
except:
    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3 > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
        Digikala = Digikala_price_element.text

    except:
        Digikala = "ناموجود"



driver.get("https://www.technolife.ir/product-5165/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-poco-x4-pro-5g-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA")
time.sleep(3)

try:
    techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
    techno = techno_price_element.text

except:
    techno = "ناموجود"

driver.get("https://divar.ir/goods/mobile/prices?q=poco%20x4")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/p[2]")
Divar = Divar_element.text

c.execute(f'UPDATE mobile SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()



"""   A53 5G 256 8   """ 

driver.get("https://www.zoomit.ir/product/samsung-galaxy-a53-5g/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
battery_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[16]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
cores_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[3]/td[2]")
operatingsystem_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[7]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[3]/td[2]")
weight_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
camera_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[2]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[5]/td[2]")
# Extract the text
name = name_element.text
battery = battery_element.text
screen_size = screen_size_element.text
cores = cores_element.text
operatingsystem = operatingsystem_element.text
RAM = RAM_element.text
memory = memory_element.text
weight = weight_element.text
camera = camera_element.text
color = color__element.text

driver.get("https://www.digikala.com/product/dkp-8119459/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-a53-5g-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D8%A7%DA%A9%D8%AA%DB%8C%D9%88/")
time.sleep(3)

try:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3 > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
except:
    Digikala = "ناموجود"

        


driver.get("https://divar.ir/goods/mobile/prices?q=A53")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/p[2]")
Divar = Divar_element.text

driver.get("https://www.technolife.ir/product-3704/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-%DA%AF%D9%84%DA%A9%D8%B3%DB%8C-a53-5g-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA")
time.sleep(3)

try:
    techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(2) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
except:
    techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")

techno = techno_price_element.text

c.execute(f'UPDATE mobile SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()


"""   S21 FE 5G 256 8   """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/samsung-galaxy-s21-fe-5g/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
battery_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[16]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
cores_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[3]/td[2]")
operatingsystem_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[2]/tr[8]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
weight_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
camera_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[2]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[6]/td[2]")
# Extract the text
name = name_element.text
battery = battery_element.text
screen_size = screen_size_element.text
cores = cores_element.text
operatingsystem = operatingsystem_element.text
RAM = RAM_element.text
memory = memory_element.text
weight = weight_element.text
camera = camera_element.text
color = color__element.text


driver.get("https://www.digikala.com/product/dkp-7475119/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-s21-fe-5g-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/")
time.sleep(3)

try:
    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
    except:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
except:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3 > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")

Digikala = Digikala_price_element.text

driver.get("https://divar.ir/goods/mobile/prices?q=S21")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/p[2]")
Divar = Divar_element.text

driver.get("https://www.technolife.ir/product-4107/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-s21-fe-5g-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA")
time.sleep(3)

techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
techno = techno_price_element.text


# Write the data to a text file
c.execute(f'UPDATE mobile SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()


######################################
"""   TABLET       """

"""   Samsung Galaxy Tab S8   """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/samsung-galaxy-tab-s8/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
battery_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[16]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
cores_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[3]/td[2]")
material_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[3]/td[2]")
tarashe_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[1]/td[2]")
camera_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[2]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[5]/td[2]")
# Extract the text
name = name_element.text
battery = battery_element.text
screen_size = screen_size_element.text
cores = cores_element.text
material = material_element.text
RAM = RAM_element.text
memory = memory_element.text
tarashe = tarashe_element.text
camera = camera_element.text
color = color__element.text


driver.get("https://www.digikala.com/product/dkp-8417820/%D8%AA%D8%A8%D9%84%D8%AA-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-tab-s8-5g-sm-x706b-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-128-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/")
time.sleep(3)
try:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
    Digikala = Digikala_price_element.text
except:
    Digikala = "ناموجود"
driver.get("https://divar.ir/s/tehran/tablet?goods-business-type=all&q=Samsung%20Galaxy%20Tab%20S8")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[1]/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text

driver.get("https://darsoo.com/product/%D8%AA%D8%A8%D9%84%D8%AA-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-Samsung-Galaxy-Tab-S8-%D8%A8%D8%A7128-%DA%AF%DB%8C%DA%AF-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-%D8%AF%D8%A7%D8%AE%D9%84%DB%8C-%D9%88-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/")
time.sleep(3)
                                                                                                                         
try:
    darsoo_price_element = driver.find_element(By.CSS_SELECTOR,"body > div.wrapper.default:nth-child(3) > main.single-product.default:nth-child(8) > div.container:nth-child(1) > div.row:nth-child(3) > div.col-lg-8.col-md-12.col-sm-12.mr-4.mr-lg-0:nth-child(1) > article > div.row > div.col-lg-6.col-md-6.col-sm-12:nth-child(2) > form#addToBasketForm:nth-child(4) > div#showAttrBaseG1:nth-child(12) > div#basketV1:nth-child(5) > div#basketBase > div.mt-4.mb-2.p-4.widthBask > div#priceSection.price-product.defualta:nth-child(2) > div.row:nth-child(2) > div.col-6.px-3.py-2.text-center:nth-child(1) > span#priceshow:nth-child(1)")
except:
    darsoo_price_element = driver.find_element(By.CSS_SELECTOR,"body > div.wrapper.default:nth-child(3) > main.single-product.default:nth-child(8) > div.container:nth-child(1) > div.row:nth-child(3) > div.col-lg-8.col-md-12.col-sm-12.mr-4.mr-lg-0:nth-child(1) > article > div.row > div.col-lg-6.col-md-6.col-sm-12:nth-child(2) > form#addToBasketForm:nth-child(4) > div#showAttrBaseG1:nth-child(12) > div.row.col-sm-12:nth-child(4) > div#basketV1:nth-child(2) > div#basketBase > div.mt-4.mb-2.p-4.widthBask > div#priceSection.price-product.defualta:nth-child(2) > div.row:nth-child(2) > div.col-6.px-3.py-2.text-center:nth-child(1) > span#priceshow:nth-child(1)")
darsoo = darsoo_price_element.text


# Write the data to a text file
c.execute(f'UPDATE Tablet SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(darsoo),name))
conn.commit()

"""   Apple iPad Pro 11 2022   """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/apple-ipad-pro-11-2022/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
battery_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[16]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
cores_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[2]/td[2]")
material_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[3]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[3]/td[2]")
tarashe_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[1]/td[2]")
camera_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[2]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[6]/td[2]")
# Extract the text
name = name_element.text
battery = battery_element.text
screen_size = screen_size_element.text
cores = cores_element.text
material = material_element.text
RAM = RAM_element.text
memory = memory_element.text
tarashe = tarashe_element.text
camera = camera_element.text
color = color__element.text


driver.get("https://www.digikala.com/product/dkp-9834648/%D8%AA%D8%A8%D9%84%D8%AA-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-ipad-pro-11-2022-wifi-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-128-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/")
time.sleep(3)
                                                              

try:

    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
        Digikala = Digikala_price_element.text

    except:

        try:
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
            Digikala = Digikala_price_element.text

        except:
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3 > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
            Digikala = Digikala_price_element.text



except:

    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
        Digikala = Digikala_price_element.text

    except:

        try:                                                            
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
            Digikala = Digikala_price_element.text

        except:
            
            try:
                Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
                Digikala = Digikala_price_element.text

            except:
                Digikala = "ناموجود"

driver.get("https://divar.ir/s/tehran/tablet?goods-business-type=all&q=Apple%20iPad%20Pro%2011%202022")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[1]/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text

driver.get("https://darsoo.com/product/ipad-pro-10-9-inches-2022-wifi-128GB-8Ram/")
time.sleep(3)

darsoo_price_element = driver.find_element(By.CSS_SELECTOR,"body > div.wrapper.default:nth-child(3) > main.single-product.default:nth-child(8) > div.container:nth-child(1) > div.row:nth-child(3) > div.col-lg-8.col-md-12.col-sm-12.mr-4.mr-lg-0:nth-child(1) > article > div.row > div.col-lg-6.col-md-6.col-sm-12:nth-child(2) > form#addToBasketForm:nth-child(4) > div#basketV1:nth-child(15) > div#basketBase > div.mt-4.mb-2.p-4.widthBask > div#priceSection.price-product.defualta:nth-child(2) > div.row:nth-child(2) > div.col-6.px-3.py-2.text-center:nth-child(1) > span#priceshow:nth-child(1)")
darsoo = darsoo_price_element.text


# Write the data to a text file
c.execute(f'UPDATE Tablet SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(darsoo),name))
conn.commit()

"""   Samsung Galaxy Tab S6 Lite 2022   """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/samsung-galaxy-tab-s6-lite-2022/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
battery_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[16]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
cores_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[3]/td[2]")
material_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[3]/td[2]")
tarashe_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[1]/td[2]")
camera_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[2]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[5]/td[2]")
# Extract the text
name = name_element.text
battery = battery_element.text
screen_size = screen_size_element.text
cores = cores_element.text
material = material_element.text
RAM = RAM_element.text
memory = memory_element.text
tarashe = tarashe_element.text
camera = camera_element.text
color = color__element.text


driver.get("https://www.digikala.com/product/dkp-9936864/%D8%AA%D8%A8%D9%84%D8%AA-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-tab-s6-lite-2022-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-%DA%86%D9%87%D8%A7%D8%B1-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/")
time.sleep(3)
try:

    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
        Digikala = Digikala_price_element.text

    except:

        try:
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
            Digikala = Digikala_price_element.text

        except:
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3 > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
            Digikala = Digikala_price_element.text



except:

    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
        Digikala = Digikala_price_element.text

    except:

        try:                                                            
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
            Digikala = Digikala_price_element.text

        except:
            
            try:
                Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"div[class='pos-relative w-full w-auto-lg px-4-lg pb-4-lg'] div[class='w-full w-auto-lg z-3 bg-000 shadow-fab-button shadow-none-lg styles_BuyBoxFooter__actionWrapper__Hl4e7'] div span[class='text-h4 ml-1 color-800']")
                Digikala = Digikala_price_element.text

            except:
                Digikala = "ناموجود"




driver.get("https://divar.ir/s/tehran/tablet?goods-business-type=all&q=Samsung%20Galaxy%20Tab%20S6%20Lite")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[1]/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text

driver.get("https://darsoo.com/product/Samsung-Galaxy-Tab-S6-Lite-(2022-P619)-64-ram-4/")
time.sleep(3)
try:
    darsoo_price_element = driver.find_element(By.CSS_SELECTOR,"body > div.wrapper.default:nth-child(3) > main.single-product.default:nth-child(8) > div.container:nth-child(1) > div.row:nth-child(3) > div.col-lg-8.col-md-12.col-sm-12.mr-4.mr-lg-0:nth-child(1) > article > div.row > div.col-lg-6.col-md-6.col-sm-12:nth-child(2) > form#addToBasketForm:nth-child(4) > div#showAttrBaseG1:nth-child(12) > div.row.col-sm-12:nth-child(4) > div#basketV1:nth-child(2) > div#basketBase > div.mt-4.mb-2.p-4.widthBask > div#priceSection.price-product.defualta:nth-child(2) > div.row:nth-child(2) > div.col-6.px-3.py-2.text-center:nth-child(1) > span#priceshow:nth-child(1)")
    darsoo = darsoo_price_element.text
except:
    try:
        darsoo_price_element = driver.find_element(By.CSS_SELECTOR,"body > div.wrapper.default:nth-child(3) > main.single-product.default:nth-child(8) > div.container:nth-child(1) > div.row:nth-child(3) > div.col-lg-8.col-md-12.col-sm-12.mr-4.mr-lg-0:nth-child(1) > article > div.row > div.col-lg-6.col-md-6.col-sm-12:nth-child(2) > form#addToBasketForm:nth-child(4) > div#showAttrBaseG1:nth-child(12) > div.row.col-sm-12:nth-child(4) > div#basketV1:nth-child(2) > div#basketBase > div.mt-4.mb-2.p-4.widthBask > div#priceSection.price-product.defualta:nth-child(2) > div.row:nth-child(2) > div.col-6.px-3.py-2.text-center:nth-child(1) > span#priceshow:nth-child(1)")
        darsoo = darsoo_price_element.text
    except:
        darsoo = "ناموجود"


# Write the data to a text file
c.execute(f'UPDATE Tablet SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(darsoo),name))
conn.commit()
"""   Xiaomi redmi Pad    """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/xiaomi-redmi-pad/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
battery_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[16]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
cores_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[3]/td[2]")
material_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[4]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[3]/td[2]")
tarashe_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[1]/td[2]")
camera_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[2]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[3]/td[2]")
# Extract the text
name = name_element.text
battery = battery_element.text
screen_size = screen_size_element.text
cores = cores_element.text
material = material_element.text
RAM = RAM_element.text
memory = memory_element.text
tarashe = tarashe_element.text
camera = camera_element.text
color = color__element.text


driver.get("https://www.digikala.com/product/dkp-11511750/%D8%AA%D8%A8%D9%84%D8%AA-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-redmi-pad-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-128-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-6-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D8%A8%D9%87-%D9%87%D9%85%D8%B1%D8%A7%D9%87-%D9%87%D9%86%D8%AF%D8%B2%D9%81%D8%B1%DB%8C-%D9%88-%DA%A9%DB%8C%D9%81-%D9%88-%D9%85%D8%AD%D8%A7%D9%81%D8%B8-%D8%B5%D9%81%D8%AD%D9%87-%D9%86%D9%85%D8%A7%DB%8C%D8%B4/")
time.sleep(3)

try:

    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
        Digikala = Digikala_price_element.text

    except:

        try:
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
            Digikala = Digikala_price_element.text

        except:
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3 > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
            Digikala = Digikala_price_element.text



except:

    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
        Digikala = Digikala_price_element.text

    except:

        try:                                                            
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
            Digikala = Digikala_price_element.text

        except:
            
            try:
                Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
                Digikala = Digikala_price_element.text

            except:
                Digikala = "ناموجود"


driver.get("https://divar.ir/s/tehran?q=redmi%20pad")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text

driver.get("https://darsoo.com/product/xiaomi-redmi-pad-128g-6g/")
time.sleep(3)

darsoo_price_element = driver.find_element(By.CSS_SELECTOR,"body > div.wrapper.default:nth-child(3) > main.single-product.default:nth-child(8) > div.container:nth-child(1) > div.row:nth-child(3) > div.col-lg-8.col-md-12.col-sm-12.mr-4.mr-lg-0:nth-child(1) > article > div.row > div.col-lg-6.col-md-6.col-sm-12:nth-child(2) > form#addToBasketForm:nth-child(4) > div#showAttrBaseG1:nth-child(12) > div.row.col-sm-12:nth-child(2) > div#basketV1:nth-child(2) > div#basketBase > div.mt-4.mb-2.p-4.widthBask > div#priceSection.price-product.defualta:nth-child(2) > div.row:nth-child(2) > div.col-6.px-3.py-2.text-center:nth-child(1) > span#priceshow:nth-child(1)")
darsoo = darsoo_price_element.text


# Write the data to a text file
c.execute(f'UPDATE Tablet SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(darsoo),name))
conn.commit()

"""   Samsung Galaxy Tab A7 Lite   """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/samsung-galaxy-tab-a7-lite/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
battery_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[16]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
cores_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[3]/td[2]")
material_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
RAM_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[2]/td[2]")
memory_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[10]/tr[3]/td[2]")
tarashe_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[8]/tr[1]/td[2]")
camera_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[2]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[5]/td[2]")

# Extract the text
name = name_element.text
battery = battery_element.text
screen_size = screen_size_element.text
cores = cores_element.text
material = material_element.text
RAM = RAM_element.text
memory = memory_element.text
tarashe = tarashe_element.text
camera = camera_element.text
color = color__element.text


driver.get("https://www.digikala.com/product/dkp-5549287/%D8%AA%D8%A8%D9%84%D8%AA-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-tab-a7-lite-t225-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-32-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/")
time.sleep(3)
try:

    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
        Digikala = Digikala_price_element.text

    except:

        try:
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
            Digikala = Digikala_price_element.text

        except:
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3 > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
            Digikala = Digikala_price_element.text



except:

    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
        Digikala = Digikala_price_element.text

    except:

        try:                                                            
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
            Digikala = Digikala_price_element.text

        except:
            
            try:
                Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"div[class='pos-relative w-full w-auto-lg px-4-lg pb-4-lg'] div[class='w-full w-auto-lg z-3 bg-000 shadow-fab-button shadow-none-lg styles_BuyBoxFooter__actionWrapper__Hl4e7'] div span[class='text-h4 ml-1 color-800']")
                Digikala = Digikala_price_element.text

            except:
                Digikala = "ناموجود"


driver.get("https://divar.ir/s/tehran?q=Samsung%20Galaxy%20Tab%20A7%20Lite")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text

driver.get("https://www.technolife.ir/product-2900/-%D8%AA%D8%A8%D9%84%D8%AA-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-tab-a7-lite-sm-t225-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-32-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D8%B1%D9%85-3-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-")
time.sleep(3)
try:
    techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(2) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
except:
    techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
techno = techno_price_element.text


# Write the data to a text file
c.execute(f'UPDATE Tablet SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()


######################################
"""   WATCH       """

"""   SAMSUNG GALAXY WATCH 5 40MM   """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/samsung-galaxy-watch-5/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
screentype_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[2]/td[2]")
Resolotion_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[3]/td[2]")
weight_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
battery_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[14]/tr[1]/td[2]")
dimension_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[1]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[22]/tr[1]/td[2]")
# Extract the text
name = name_element.text
screentype = screentype_element.text
screen_size = screen_size_element.text
Resolotion = Resolotion_element.text
weight = weight_element.text
battery = battery_element.text
dimension = dimension_element.text
color = color__element.text


driver.get("https://www.digikala.com/product/dkp-9270334/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-watch-5-40mm/")
time.sleep(5)
                                                              
try:
    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
        Digikala = Digikala_price_element.text
    except:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3 > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
        Digikala = Digikala_price_element.text

except:
    Digikala = "ناموجود"



driver.get("https://www.technolife.ir/product-7219/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-watch5-40mm")
time.sleep(3)

try:
    techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
except:
    techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(2) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
techno = techno_price_element.text

driver.get("https://divar.ir/s/tehran?q=SAMSUNG%20GALAXY%20WATCH%205")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


# Write the data to a text file
c.execute(f'UPDATE Clock SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()

"""   XIAOMI MI BAND 7 PRO  """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/xiaomi-mi-band-7-pro/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
screentype_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[2]/td[2]")
Resolotion_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[3]/td[2]")
weight_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
battery_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[1]/td[2]")
dimension_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[1]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[20]/tr[1]/td[2]")
# Extract the text
name = name_element.text
screentype = screentype_element.text
screen_size = screen_size_element.text
Resolotion = Resolotion_element.text
weight = weight_element.text
battery = battery_element.text
dimension = dimension_element.text
color = color__element.text


driver.get("https://www.digikala.com/product/dkp-9962415/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-mi-band-7-pro/")
time.sleep(3)

Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
Digikala = Digikala_price_element.text

driver.get("https://www.technolife.ir/product-8315/-%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-band-7-pro")
time.sleep(3)
try:
    techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
    techno = techno_price_element.text
except:
    try:
        techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(2) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
        techno = techno_price_element.text

    except:
        techno = "ناموجود"

driver.get("https://divar.ir/s/tehran?q=MI%20BAND%207%20PRO")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


# Write the data to a text file
c.execute(f'UPDATE Clock SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()



"""   XIAOMI MIBRO LITE  """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/xiaomi-mibro-lite/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
                                                    
screentype_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[6]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[6]/tr[2]/td[2]")
Resolotion_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[6]/tr[3]/td[2]")
weight_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[4]/tr[2]/td[2]")
battery_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[12]/tr[1]/td[2]")
dimension_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[4]/tr[1]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div[1]/div/table/tbody[20]/tr/td[2]")
# Extract the text
name = name_element.text
screentype = screentype_element.text
screen_size = screen_size_element.text
Resolotion = Resolotion_element.text
weight = weight_element.text
battery = battery_element.text
dimension = dimension_element.text
color = color__element.text


driver.get("https://www.digikala.com/product/dkp-7199868/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D9%85%DB%8C%D8%A8%D8%B1%D9%88-%D9%85%D8%AF%D9%84-lite-smartwatch/")
time.sleep(3)

Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
Digikala = Digikala_price_element.text


driver.get("https://www.technolife.ir/product-3946/-%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-mibro-lite-")
time.sleep(3)

techno_price_element = driver.find_element(By.XPATH,"/html/body/div[1]/main/div[2]/div[3]/section[1]/div[3]/div[3]/div[2]/h6/span[1]")
techno = techno_price_element.text

driver.get("https://divar.ir/s/tehran?q=MIBRO%20LITE")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


# Write the data to a text file
c.execute(f'UPDATE Clock SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()


"""   XIAOMI WATCH S1 ACTIVE  """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/xiaomi-watch-s1-active/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
screentype_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[2]/td[2]")
Resolotion_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[3]/td[2]")
weight_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
battery_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[1]/td[2]")
dimension_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[1]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[20]/tr[1]/td[2]")
# Extract the text
name = name_element.text
screentype = screentype_element.text
screen_size = screen_size_element.text
Resolotion = Resolotion_element.text
weight = weight_element.text
battery = battery_element.text
dimension = dimension_element.text
color = color__element.text


driver.get("https://www.digikala.com/product/dkp-8738616/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-s1-active-%D8%A8%D9%86%D8%AF-%D8%B3%D9%84%DB%8C%DA%A9%D9%88%D9%86%DB%8C/")
time.sleep(5)

Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
Digikala = Digikala_price_element.text

driver.get("https://www.technolife.ir/product-6648/-%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-s1-active")
time.sleep(3)

techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(2) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
techno = techno_price_element.text

driver.get("https://divar.ir/s/tehran?q=s1%20active")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


# Write the data to a text file
c.execute(f'UPDATE Clock SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()


"""   XIAOMI REDMI WATCH 2 LITE  """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/xiaomi-redmi-watch-2-lite/")
time.sleep(3)
#_element = driver.find_element(By.XPATH,"")
# Find the price element
name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[1]/div/div/div")
screentype_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[1]/td[2]")
screen_size_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[2]/td[2]")
Resolotion_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[6]/tr[3]/td[2]")
weight_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[2]/td[2]")
battery_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[12]/tr[1]/td[2]")
dimension_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[4]/tr[1]/td[2]")
color__element = driver.find_element(By.XPATH,"/html/body/div[2]/div[8]/div/div[1]/div/div[2]/div/div[3]/table/tbody[20]/tr[1]/td[2]")
# Extract the text
name = name_element.text
screentype = screentype_element.text
screen_size = screen_size_element.text
Resolotion = Resolotion_element.text
weight = weight_element.text
battery = battery_element.text
dimension = dimension_element.text
color = color__element.text


driver.get("https://www.digikala.com/product/dkp-7380557/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-redmi-watch-2-lite-%D8%A8%D9%86%D8%AF-%D8%B3%D9%84%DB%8C%DA%A9%D9%88%D9%86%DB%8C/")
time.sleep(3)

try:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
    Digikala = Digikala_price_element.text
except:
    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
        Digikala = Digikala_price_element.text
    except:
        try:
            Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"div[class='pos-relative w-full w-auto-lg px-4-lg pb-4-lg'] div[class='w-full w-auto-lg z-3 bg-000 shadow-fab-button shadow-none-lg styles_BuyBoxFooter__actionWrapper__Hl4e7'] div span[class='text-h4 ml-1 color-800']")
            Digikala = Digikala_price_element.text
        except:
            Digikala = "ناموجود"
driver.get("https://www.technolife.ir/product-5029/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-redmi-watch-2-lite")
time.sleep(3)
try:
    techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
    techno = techno_price_element.text
except:
    try:
        techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(2) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
        techno = techno_price_element.text

    except:
        techno = "ناموجود"
driver.get("https://divar.ir/s/tehran?q=REDMI%20WATCH%202%20LITE")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


# Write the data to a text file
c.execute(f'UPDATE Clock SET price1= ?,price2=?,price3=? WHERE product_name = ?',(persian_to_english(Digikala),persian_to_english(Divar),persian_to_english(techno),name))
conn.commit()


driver.quit()




