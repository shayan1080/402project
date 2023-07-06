from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import arabic_reshaper
from bidi.algorithm import get_display

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
        persian_number = re.sub("[٬,]", "", persian_currency)
        persian_number = persian_number.replace("تومان", "").strip()
        
        
        reshaped_text = arabic_reshaper.reshape(persian_number)
        bidi_text = get_display(reshaped_text)
        english_number = bidi_text.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
        
        english_number = "{:,}".format(int(english_number))
        
        return english_number



driver = webdriver.Edge()
link = "https://www.digikala.com/product/dkp-8109369/%D8%AF%D8%B3%D8%AA%D9%87-%D8%A8%D8%A7%D8%B2%DB%8C-%D9%85%DB%8C%DA%86%D8%B1-%D9%85%D8%AF%D9%84-mr58-%D8%A8%D8%B3%D8%AA%D9%87-2-%D8%B9%D8%AF%D8%AF%DB%8C/"
driver.get(link)
time.sleep(3)

name_element = driver.find_element(By.CSS_SELECTOR,".text-h4.color-900.mb-2.disable-events")
name = name_element.text


try:
    Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
    Digikala = Digikala_price_element.text

except:

    try:
        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(2) > div.d-flex.jc-start.mr-auto.text-h3:nth-child(2) > div.d-flex.ai-center.jc-end.w-100:nth-child(1) > span.text-h4.ml-1.color-800")
        Digikala = Digikala_price_element.text

    except:

        Digikala_price_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.grow-1.w-min-0:nth-child(2) > div.styles_InfoSection__leftSection__0vNpX:nth-child(2) > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP:nth-child(3) > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3:nth-child(1) > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg:nth-child(8) > div.w-full.w-auto-lg.z-3.bg-000.shadow-fab-button.shadow-none-lg.styles_BuyBoxFooter__actionWrapper__Hl4e7 > div > div.d-flex.ai-center:nth-child(1) > div.d-flex.jc-start.flex-column.ai-end.mr-auto.text-h3:nth-child(2) > div.d-flex.flex-row.ai-center:nth-child(2) > span.color-800.ml-1.text-h4:nth-child(1)")
        Digikala = Digikala_price_element.text


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
                                                             
        options_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.w-full:nth-child(7) > div.grow-1.w-min-0:nth-child(1) > section#specification.mt-4-lg.px-5.px-0-lg.pb-5.styles_PdpProductContent__sectionBorder__39zAX:nth-child(1) > div.mt-4.grow-1:nth-child(2) > div.d-flex.flex-column.flex-row-lg.pb-6.py-4-lg.styles_SpecificationBox__main__JKiKI")
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
                    options_element = driver.find_element(By.CSS_SELECTOR,"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.w-full:nth-child(9) > div.grow-1.w-min-0:nth-child(1) > section#specification.mt-4-lg.px-5.px-0-lg.pb-5.styles_PdpProductContent__sectionBorder__39zAX:nth-child(3) > div.mt-4.grow-1:nth-child(2) > div.d-flex.flex-column.flex-row-lg.pb-6.py-4-lg.styles_SpecificationBox__main__JKiKI")
                    options = options_element.text
                                                                       

        



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

    except:

        Divar = "ناموجود"



print(name)

print(color)

print(options)

print(persian_to_english(Digikala))

print(persian_to_english(Divar))

"body > div#__next:nth-child(2) > div.h-100.d-flex.flex-column.bg-000.ai-center:nth-child(2) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0:nth-child(3) > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w:nth-child(3) > div.px-5-lg:nth-child(2) > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ:nth-child(2) > div.ml-4-lg.shrink-0.styles_InfoSection__rightSection__PiYpa:nth-child(1) > div.d-flex.flex-column.ai-center.max-w-92-lg.max-w-145-xl.d-block-lg.mb-2:nth-child(2) > div.d-flex:nth-child(1) > div.pos-relative.d-flex.ai-center:nth-child(2) > div:nth-child(1)"




