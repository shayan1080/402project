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


c.execute(f'''INSERT INTO Laptop VALUES ('{name}' , 'Laptop' , '{size}' , '{weight}' , '{RAM}' , '{memory}' , '{battery}' , '{screensize}' , '{processor}','{resolotion}','{persian_to_english(Digikala)}' , '{persian_to_english(Divar)}' ,'{persian_to_english(amitis)}')''')
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


c.execute(f'''INSERT INTO Laptop VALUES ('{name}' , 'Laptop' , '{size}' , '{weight}' , '{RAM}' , '{memory}' , '{battery}' , '{screensize}' , '{processor}','{resolotion}','{persian_to_english(Digikala)}' , '{persian_to_english(Divar)}' ,'{techno}')''')
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
c.execute(f'''INSERT INTO Laptop VALUES ('{name}' , 'Laptop' , '{size}' , '{weight}' , '{RAM}' , '{memory}' , '{battery}' , '{screensize}' , '{processor}','{resolotion}','{persian_to_english(Digikala)}' , '{persian_to_english(Divar)}' ,'{persian_to_english(adak)}')''')
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
c.execute(f'''INSERT INTO Laptop VALUES ('{name}' , 'Laptop' , '{size}' , '{weight}' , '{RAM}' , '{memory}' , '{battery}' , '{screensize}' , '{processor}','{resolotion}','{persian_to_english(Digikala)}' , '{persian_to_english(Divar)}' ,'{techno}')''')
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
c.execute(f'''INSERT INTO Laptop VALUES ('{name}' , 'Laptop' , '{size}' , '{weight}' , '{RAM}' , '{memory}' , '{battery}' , '{screensize}' , '{processor}','{resolotion}','{persian_to_english(Digikala)}' , '{persian_to_english(Divar)}' ,'{techno}')''')
conn.commit()

driver.quit()

