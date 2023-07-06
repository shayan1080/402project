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


driver = webdriver.Edge()


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

Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
Digikala = Digikala_price_element.text

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




c.execute(f'''INSERT INTO Tablet VALUES ('{name}' , 'Tablet' , '{battery}' , '{screen_size}' , '{cores}' , '{memory}' , '{RAM}' , '{tarashe}' , '{camera}','{material}' , '{color}' ,'{persian_to_english(Digikala)}','{persian_to_english(Divar)}','{darsoo}')''')
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
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
except:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
Digikala = Digikala_price_element.text

driver.get("https://divar.ir/s/tehran/tablet?goods-business-type=all&q=Apple%20iPad%20Pro%2011%202022")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[1]/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text

driver.get("https://darsoo.com/product/ipad-pro-10-9-inches-2022-wifi-128GB-8Ram/")
time.sleep(3)

darsoo_price_element = driver.find_element(By.CSS_SELECTOR,"body > div.wrapper.default:nth-child(3) > main.single-product.default:nth-child(8) > div.container:nth-child(1) > div.row:nth-child(3) > div.col-lg-8.col-md-12.col-sm-12.mr-4.mr-lg-0:nth-child(1) > article > div.row > div.col-lg-6.col-md-6.col-sm-12:nth-child(2) > form#addToBasketForm:nth-child(4) > div#basketV1:nth-child(15) > div#basketBase > div.mt-4.mb-2.p-4.widthBask > div#priceSection.price-product.defualta:nth-child(2) > div.row:nth-child(2) > div.col-6.px-3.py-2.text-center:nth-child(1) > span#priceshow:nth-child(1)")
darsoo = darsoo_price_element.text

c.execute(f'''INSERT INTO Tablet VALUES ('{name}' , 'Tablet' , '{battery}' , '{screen_size}' , '{cores}' , '{memory}' , '{RAM}' , '{tarashe}' , '{camera}','{material}' , '{color}' ,'{persian_to_english(Digikala)}','{persian_to_english(Divar)}','{darsoo}')''')
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

Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
Digikala = Digikala_price_element.text

driver.get("https://divar.ir/s/tehran/tablet?goods-business-type=all&q=Samsung%20Galaxy%20Tab%20S6%20Lite")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[1]/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text

driver.get("https://darsoo.com/product/Samsung-Galaxy-Tab-S6-Lite-(2022-P619)-64-ram-4/")
time.sleep(3)

darsoo_price_element = driver.find_element(By.CSS_SELECTOR,"body > div.wrapper.default:nth-child(3) > main.single-product.default:nth-child(8) > div.container:nth-child(1) > div.row:nth-child(3) > div.col-lg-8.col-md-12.col-sm-12.mr-4.mr-lg-0:nth-child(1) > article > div.row > div.col-lg-6.col-md-6.col-sm-12:nth-child(2) > form#addToBasketForm:nth-child(4) > div#showAttrBaseG1:nth-child(12) > div.row.col-sm-12:nth-child(4) > div#basketV1:nth-child(2) > div#basketBase > div.mt-4.mb-2.p-4.widthBask > div#priceSection.price-product.defualta:nth-child(2) > div.row:nth-child(2) > div.col-6.px-3.py-2.text-center:nth-child(1) > span#priceshow:nth-child(1)")
darsoo = darsoo_price_element.text

c.execute(f'''INSERT INTO Tablet VALUES ('{name}' , 'Tablet' , '{battery}' , '{screen_size}' , '{cores}' , '{memory}' , '{RAM}' , '{tarashe}' , '{camera}','{material}' , '{color}' ,'{persian_to_english(Digikala)}','{persian_to_english(Divar)}','{darsoo}')''')
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
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
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


c.execute(f'''INSERT INTO Tablet VALUES ('{name}' , 'Tablet' , '{battery}' , '{screen_size}' , '{cores}' , '{memory}' , '{RAM}' , '{tarashe}' , '{camera}','{material}' , '{color}' ,'{persian_to_english(Digikala)}','{persian_to_english(Divar)}','{darsoo}')''')
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

Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(4) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
Digikala = Digikala_price_element.text

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


c.execute(f'''INSERT INTO Tablet VALUES ('{name}' , 'Tablet' , '{battery}' , '{screen_size}' , '{cores}' , '{memory}' , '{RAM}' , '{tarashe}' , '{camera}','{material}' , '{color}' ,'{persian_to_english(Digikala)}','{persian_to_english(Divar)}','{techno}')''')
conn.commit()

driver.quit()