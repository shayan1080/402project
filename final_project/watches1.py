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
with open("watches.txt", "w", encoding="utf-8") as file:
    file.write("name: " + name + "\n")  
    file.write("screentype: " + screentype + "\n")
    file.write("screen size: " + screen_size + "\n")
    file.write("Resolotion: " + Resolotion + "\n")
    file.write("weight: " + weight + "\n")
    file.write("battery: " + battery + "\n")    
    file.write("dimension: " + dimension + "\n")
    file.write("colors: " + color + "\n")
    file.write("Digikala: " + persian_to_english(Digikala) + "\n")
    file.write("Divar: " + persian_to_english(Divar) + "\n")
    file.write("techno: " + techno + "\n")
    file.write("\n")
    file.write("\n") 

c.execute(f'''INSERT INTO Clock VALUES ('{name}' , 'Clock' , '{screentype}' , '{screen_size}' , '{Resolotion}' , '{weight}' , '{battery}' , '{dimension}' , '{color}','{persian_to_english(Digikala)}' , '{persian_to_english(Divar)}' ,'{techno}')''')
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

techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
techno = techno_price_element.text

driver.get("https://divar.ir/s/tehran?q=MI%20BAND%207%20PRO")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text

c.execute(f'''INSERT INTO Clock VALUES ('{name}' , 'Clock' , '{screentype}' , '{screen_size}' , '{Resolotion}' , '{weight}' , '{battery}' , '{dimension}' , '{color}','{persian_to_english(Digikala)}' , '{persian_to_english(Divar)}' ,'{techno}')''')
conn.commit()


"""   XIAOMI MIBRO LITE  """
# Navigate to the website
driver.get("https://www.zoomit.ir/product/xiaomi-mibro-lite/")
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


c.execute(f'''INSERT INTO Clock VALUES ('{name}' , 'Clock' , '{screentype}' , '{screen_size}' , '{Resolotion}' , '{weight}' , '{battery}' , '{dimension}' , '{color}','{persian_to_english(Digikala)}' , '{persian_to_english(Divar)}' ,'{techno}')''')
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


c.execute(f'''INSERT INTO Clock VALUES ('{name}' , 'Clock' , '{screentype}' , '{screen_size}' , '{Resolotion}' , '{weight}' , '{battery}' , '{dimension}' , '{color}','{persian_to_english(Digikala)}' , '{persian_to_english(Divar)}' ,'{techno}')''')
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
except:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")

Digikala = Digikala_price_element.text

driver.get("https://www.technolife.ir/product-5029/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-redmi-watch-2-lite")
time.sleep(3)

techno_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > main.main.main2:nth-child(2) > div.leftside > div._content:nth-child(4) > section#productP1.product_productInfo__59k47:nth-child(2) > div.product_productInfoLeftSide__pyD3F:nth-child(4) > div.product_productPrice__1z46Z:nth-child(4) > div:nth-child(1) > h6 > span.product_sameTransition__ZxNeN:nth-child(1)")
techno = techno_price_element.text

driver.get("https://divar.ir/s/tehran?q=REDMI%20WATCH%202%20LITE")
time.sleep(3)

Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
Divar = Divar_element.text


c.execute(f'''INSERT INTO Clock VALUES ('{name}' , 'Clock' , '{screentype}' , '{screen_size}' , '{Resolotion}' , '{weight}' , '{battery}' , '{dimension}' , '{color}','{persian_to_english(Digikala)}' , '{persian_to_english(Divar)}' ,'{techno}')''')
conn.commit()

driver.quit()
