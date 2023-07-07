from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import arabic_reshaper
from bidi.algorithm import get_display
import sqlite3 , os

con=sqlite3.connect("dynamicproduct.db")
cur=con.cursor()

def search(link):
    def colour(input_string):
        if input_string != "ناموجود":
            input_string = input_string.replace(":", "")
            input_string = input_string.replace("رنگ", "")
            input_string = input_string.strip()
            return input_string

        else:
            return "ناموجود"


    def getting_model(title):


        match = re.search(r"مدل([a-zA-Z0-9\s\-.,]+)", title)
        characters_after_model = match.group(1).strip()

        return characters_after_model


    def persian_to_english(persian_currency):
        
        if persian_currency == "ناموجود":
            return persian_currency

        elif "در" in persian_currency:
            return "ناموجود"

        else:
            persian_number = re.sub("[٬٫,]", "", persian_currency)
            persian_number = persian_number.replace("تومان", "").strip()
            
            
            reshaped_text = arabic_reshaper.reshape(persian_number)
            bidi_text = get_display(reshaped_text)
            english_number = bidi_text.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
            
            english_number = "{:,}".format(int(english_number))
            
            return english_number



    driver = webdriver.Chrome()
    # link = "https://www.digikala.com/product/dkp-3035899/%D8%A7%D8%AC%D8%A7%D9%82-%DA%AF%D8%A7%D8%B2-%D8%B5%D9%81%D8%AD%D9%87-%D8%A7%DB%8C-%D8%AF%D9%86%D9%BE%D8%A7%D8%B3%D8%B1-%D9%85%D8%AF%D9%84-bt1/"

    driver.get(link)
    time.sleep(3)

    name_element = driver.find_element(By.CSS_SELECTOR,".text-h4.color-900.mb-2.disable-events")
    name = name_element.text


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


    ####color#####


    try:
        color_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.pb-3.w-min-0.mx-5.mx-0-lg.pb-3-lg.styles_InfoSection__wrapper__e2TLb.styles_InfoSection__variantInfo__PVSw4:nth-child(1) > div.border-t.border-none-lg.mt-3.mt-0-lg:nth-child(4) > div.break-words.py-3:nth-child(1) > div.d-flex.ai-center.grow-1 > p.grow-1.text-h5.color-900:nth-child(1)")
        color = color_element.text

    except:

        try:

            color_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.pb-3.w-min-0.mx-5.mx-0-lg.pb-3-lg.styles_InfoSection__wrapper__e2TLb.styles_InfoSection__variantInfo__PVSw4:nth-child(1) > div.border-t.border-none-lg.mt-3.mt-0-lg:nth-child(3) > div.break-words.py-3:nth-child(1) > div.d-flex.ai-center.grow-1 > p.grow-1.text-h5.color-900:nth-child(1)")
            color = color_element.text

        except:

            color = "ناموجود"


    time.sleep(3)

    try:
        try: 

            try:                                                 
                options_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.w-full:nth-child(7) > div.grow-1.w-min-0:nth-child(1) > section#specification.mt-4-lg.px-5.px-0-lg.pb-5.styles_PdpProductContent__sectionBorder__39zAX:nth-child(1) > div.mt-4.grow-1:nth-child(2) > div.d-flex.flex-column.flex-row-lg.pb-6.py-4-lg.styles_SpecificationBox__main__JKiKI")
                options = options_element.text
            except:
                options_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.w-full:nth-child(10) > div.grow-1.w-min-0:nth-child(1) > section#specification.mt-4-lg.px-5.px-0-lg.pb-5.styles_PdpProductContent__sectionBorder__39zAX:nth-child(2) > div.mt-4.grow-1:nth-child(2) > div.d-flex.flex-column.flex-row-lg.pb-6.py-4-lg.styles_SpecificationBox__main__JKiKI")
                options = options_element.text



        except:
                                                        
            try:
                options_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.w-full:nth-child(9) > div.grow-1.w-min-0:nth-child(1) > section#specification.mt-4-lg.px-5.px-0-lg.pb-5.styles_PdpProductContent__sectionBorder__39zAX:nth-child(1) > div.mt-4.grow-1:nth-child(2) > div.d-flex.flex-column.flex-row-lg.pb-6.py-4-lg.styles_SpecificationBox__main__JKiKI")
                options = options_element.text
            except:
                options_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.w-full:nth-child(7) > div.grow-1.w-min-0:nth-child(1) > section#specification.mt-4-lg.px-5.px-0-lg.pb-5.styles_PdpProductContent__sectionBorder__39zAX:nth-child(2) > div.mt-4.grow-1:nth-child(2) > div.d-flex.flex-column.flex-row-lg.pb-6.py-4-lg.styles_SpecificationBox__main__JKiKI")
                options = options_element.text

    except:
        try:                                                      
            options_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.w-full:nth-child(7) > div.grow-1.w-min-0:nth-child(1) > section#specification.mt-4-lg.px-5.px-0-lg.pb-5.styles_PdpProductContent__sectionBorder__39zAX:nth-child(3) > div.mt-4.grow-1:nth-child(2) > div.d-flex.flex-column.flex-row-lg.pb-6.py-4-lg.styles_SpecificationBox__main__JKiKI")
            options = options_element.text
                                                                
        except:

            try:
                options_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.w-full:nth-child(8) > div.grow-1.w-min-0:nth-child(1) > section#specification.mt-4-lg.px-5.px-0-lg.pb-5.styles_PdpProductContent__sectionBorder__39zAX:nth-child(2) > div.mt-4.grow-1:nth-child(2) > div.d-flex.flex-column.flex-row-lg.pb-6.py-4-lg.styles_SpecificationBox__main__JKiKI")
                options = options_element.text
                                                                    
            except:

                try:
                    options_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.w-full:nth-child(8) > div.grow-1.w-min-0:nth-child(1) > section#specification.mt-4-lg.px-5.px-0-lg.pb-5.styles_PdpProductContent__sectionBorder__39zAX:nth-child(1) > div.mt-4.grow-1:nth-child(2) > div.d-flex.flex-column.flex-row-lg.pb-6.py-4-lg.styles_SpecificationBox__main__JKiKI")
                    options = options_element.text

                except:
                    try:
                        options_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.w-full:nth-child(8) > div.grow-1.w-min-0:nth-child(1) > section#specification.mt-4-lg.px-5.px-0-lg.pb-5.styles_PdpProductContent__sectionBorder__39zAX:nth-child(3) > div.mt-4.grow-1:nth-child(2) > div.d-flex.flex-column.flex-row-lg.pb-6.py-4-lg.styles_SpecificationBox__main__JKiKI")
                        options = options_element.text

                    except:
                        
                        try:

                            try:
                                options_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.w-full:nth-child(9) > div.grow-1.w-min-0:nth-child(1) > section#specification.mt-4-lg.px-5.px-0-lg.pb-5.styles_PdpProductContent__sectionBorder__39zAX:nth-child(3) > div.mt-4.grow-1:nth-child(2) > div.d-flex.flex-column.flex-row-lg.pb-6.py-4-lg.styles_SpecificationBox__main__JKiKI")
                                options = options_element.text

                            except:
                                options_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.w-full:nth-child(6) > div.grow-1.w-min-0:nth-child(1) > section#specification.mt-4-lg.px-5.px-0-lg.pb-5.styles_PdpProductContent__sectionBorder__39zAX:nth-child(3) > div.mt-4.grow-1:nth-child(2) > div.d-flex.flex-column.flex-row-lg.pb-6.py-4-lg.styles_SpecificationBox__main__JKiKI")
                                options = options_element.text



                        except:
                            try:
                                options_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.w-full:nth-child(10) > div.grow-1.w-min-0:nth-child(1) > section#specification.mt-4-lg.px-5.px-0-lg.pb-5.styles_PdpProductContent__sectionBorder__39zAX:nth-child(3) > div.mt-4.grow-1:nth-child(2) > div.d-flex.flex-column.flex-row-lg.pb-6.py-4-lg.styles_SpecificationBox__main__JKiKI")
                                options = options_element.text
                            
                            except:
                                options = "ناموجود"

                                                                        
    image_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.ml-4-lg.shrink-0.styles_InfoSection__rightSection__PiYpa:nth-child(1) > div.d-flex.flex-column.ai-center.max-w-92-lg.max-w-145-xl.d-block-lg.mb-2:nth-child(2) > div.d-flex:nth-child(1) > div.pos-relative.d-flex.ai-center:nth-child(2) > div:nth-child(1)")


    image_element.screenshot('image.jpg')           

            



    driver.get("https://divar.ir/s/tehran")
    time.sleep(3)

    search_box = driver.find_element(By.CSS_SELECTOR,"#app > header > nav > div > div.nav-bar__search-container > div > div > div.kt-nav-text-field__field > form > input")

    # Enter text into the search box



    try:
        search_box.send_keys(f'{name}')
        search_box.send_keys(Keys.ENTER)

        time.sleep(3)

        Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
        Divar = Divar_element.text 
        Divar_link = driver.current_url


    except:

        try:
        
            driver.get("https://divar.ir/s/tehran")
            time.sleep(3)

            search_box = driver.find_element(By.CSS_SELECTOR,"#app > header > nav > div > div.nav-bar__search-container > div > div > div.kt-nav-text-field__field > form > input")
            search_box.send_keys(f'{getting_model(name)}')
            search_box.send_keys(Keys.ENTER)
            time.sleep(3)
        
            Divar_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div/div[1]/a/article/div/div[1]/div[2]")
            Divar = Divar_element.text
            Divar_link = driver.current_url

        except:

            Divar = "ناموجود"
            Divar_link = "ناموجود"

    driver.get("https://torob.com/")
    time.sleep(3)


    search_box = driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div/form/input")

    time.sleep(3)

    search_box.send_keys(name)
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)
                                                            
                                                

    time.sleep(3)
                                                
    product_element = driver.find_element(By.CSS_SELECTOR,"#layout-wrapp > div.jsx-6e2eb7b36d5f1b6c.content.false > div > div > div.jsx-149d835e1ecfb944.left-container > div.jsx-149d835e1ecfb944.cards-wrapper > div > div > div:nth-child(1) > a").get_attribute("href")

    driver.get(f"{product_element}")

    try:
        third_price_element = driver.find_element(By.CSS_SELECTOR,"#layout-wrapp > div.jsx-6e2eb7b36d5f1b6c.content.false > div > div.jsx-ec6258a0ede3ee2d.jsx-260973103.grid-container.grid-container-with-seller > div.jsx-ec6258a0ede3ee2d.jsx-260973103.showcase > div > div > div.jsx-63b317fab2efbae.main-info > div.jsx-63b317fab2efbae.buy_box > a > div > div.jsx-63b317fab2efbae.ellipsis > div:nth-child(2)")
        third_price = third_price_element.text     

    except:
        try:
            third_price_element = driver.find_element(By.CSS_SELECTOR,"#layout-wrapp > div.jsx-6e2eb7b36d5f1b6c.content.false > div > div.jsx-ec6258a0ede3ee2d.jsx-198346415.grid-container.grid-container-with-seller > div.jsx-ec6258a0ede3ee2d.jsx-198346415.showcase > div > div > div.jsx-63b317fab2efbae.main-info > div.jsx-63b317fab2efbae.buy_box > a > div > div.jsx-63b317fab2efbae.ellipsis > div:nth-child(2)")
            third_price = third_price_element.text  

        except:
            third_price = "ناموجود"                                             

    
    try:                                                         
        third_site_element = driver.find_element(By.CSS_SELECTOR,"#layout-wrapp > div.jsx-6e2eb7b36d5f1b6c.content.false > div > div.jsx-ec6258a0ede3ee2d.jsx-260973103.grid-container.grid-container-with-seller > div.jsx-ec6258a0ede3ee2d.jsx-260973103.showcase > div > div > div.jsx-63b317fab2efbae.main-info > div.jsx-63b317fab2efbae.buy_box > a").get_attribute("href")
        third_site_link = third_site_element 

    except:
        try:
            third_site_element = driver.find_element(By.CSS_SELECTOR,"#layout-wrapp > div.jsx-6e2eb7b36d5f1b6c.content.false > div > div.jsx-ec6258a0ede3ee2d.jsx-198346415.grid-container.grid-container-with-seller > div.jsx-ec6258a0ede3ee2d.jsx-198346415.showcase > div > div > div.jsx-63b317fab2efbae.main-info > div.jsx-63b317fab2efbae.buy_box > a").get_attribute("href")
            third_site_link = third_site_element 

        except:
            third_site_link = "ناموجود"
                                                            
    #driver.get(f"{third_site_link}")






    Digikala_link = link



    with open('image.jpg', 'rb') as file:
        image_data = file.read()

    cur.execute('INSERT INTO products VALUES (?,?,?,?,?,?,?,?,?,?)',(name,persian_to_english(Divar),persian_to_english(Digikala),persian_to_english(third_price),colour(color),options,sqlite3.Binary(image_data),Divar_link,Digikala_link,third_site_link))

    con.commit()
    os.remove('image.jpg')


