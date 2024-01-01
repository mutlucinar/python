from typing import Self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service 
#from selenium.webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import time

from seleniumbase import SB



# Tarayıcı sürücüsünü başlat
options = webdriver.ChromeOptions()
 
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options) 
driver.implicitly_wait(5) # element vs. herhangi birşey bulunamazsa burda yazılan saniye kadar sonra hataya düşer
driver.maximize_window()
driver.get("https://www.idata.com.tr/ita/tr/p/randevu-islemleri-ita")





"""
def verify_success(sb):
    sb.assert_element('img[alt="Logo Assembly"]', timeout=8)
    sb.sleep(4)

with SB(uc_cdp=True, guest_mode=True) as sb:
    sb.open("https://www.idata.com.tr/ita/tr/p/randevu-islemleri-ita")
    if sb.is_element_visible('//*[@id="challenge-stage"]/div/label/span[2]'):
        sb.click('//*[@id="challenge-stage"]/div/label/span[2]')
"""

time.sleep(10)


input("ASD")
driver.quit()