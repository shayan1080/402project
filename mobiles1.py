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

# Set up the WebDriver (replace "path_to_webdriver" with the actual path to the WebDriver executable)
driver = webdriver.Edge()


######################################
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
c.execute(f'''INSERT INTO mobile VALUES ('{name}' , 'Mobile' , '{battery}' , '{screen_size}' , '{cores}' , '{memory}' , '{RAM}' , '{weight}' , '{camera}','{operatingsystem}' , '{color}' ,'{persian_to_english(Digikala)}','{persian_to_english(Divar)}','{techno}')''')
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

c.execute(f'''INSERT INTO mobile VALUES ('{name}' , 'Mobile' , '{battery}' , '{screen_size}' , '{cores}' , '{memory}' , '{RAM}' , '{weight}' , '{camera}','{operatingsystem}' , '{color}' ,'{persian_to_english(Digikala)}','{persian_to_english(Divar)}','{techno}')''')
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

Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3 > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
Digikala = Digikala_price_element.text

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

c.execute(f'''INSERT INTO mobile VALUES ('{name}' , 'Mobile' , '{battery}' , '{screen_size}' , '{cores}' , '{memory}' , '{RAM}' , '{weight}' , '{camera}','{operatingsystem}' , '{color}' ,'{persian_to_english(Digikala)}','{persian_to_english(Divar)}','{techno}')''')
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
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3 > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
Digikala = Digikala_price_element.text


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

c.execute(f'''INSERT INTO mobile VALUES ('{name}' , 'Mobile' , '{battery}' , '{screen_size}' , '{cores}' , '{memory}' , '{RAM}' , '{weight}' , '{camera}','{operatingsystem}' , '{color}' ,'{persian_to_english(Digikala)}','{persian_to_english(Divar)}','{techno}')''')
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
c.execute(f'''INSERT INTO mobile VALUES ('{name}' , 'Mobile' , '{battery}' , '{screen_size}' , '{cores}' , '{memory}' , '{RAM}' , '{weight}' , '{camera}','{operatingsystem}' , '{color}' ,'{persian_to_english(Digikala)}','{persian_to_english(Divar)}','{techno}')''')
conn.commit()

driver.quit()