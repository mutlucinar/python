from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
time.sleep(5)
#variables
bos_koltuk_olan_tren_sayisi=0
t =0
trains_ids = []
secim=0

"""
name = input("Ad : ")
surname = input("Soyad : ")
tarife = input("Tarife seçiniz (tam vs) : ")
dt = input("Doğum Tarihi (gg.aa.yyyy) : ")
tckn = input("Tc Kimlik No : ")
gsm = input("Cep_Tel : ")
email =  input("E Posta (eposta@ornek.com) : ")
cinsiyet=input("Cinsiyet Seçimi e,k ? \n")
"""
# Default values for testing
name = "Mutlu"
surname = "Çınar    "
tarife = "tam"
cinsiyet="e"
dt = "12.09.1994"
tckn = "47470214414"
gsm = "05444444444"
email =  "ornekmail@ornekmail.com"
kart_sahibi = "Mutlu Çınar"
kart_numarası = "1111111111111111"
kart_son_kullanma_ay = 3
kart_son_kullanma_yıl = 24
kart_güvenlik_kodu = 777

nereden = "1609" #pendik
nereye = "9092" # eryaman
gidis_tarihi = "05-01-2024"
koltuk_secimi_yapilmak_isteniyormu = "h" #e yapılırsa koltuk seçiminde onay istenir


# Tarayıcı sürücüsünü başlat
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5) # element vs. herhangi birşey bulunamazsa burda yazılan saniye kadar sonra hataya düşer

# Sayfaya git.
driver.get("https://bilet.tcdd.gov.tr/")
print("Sayfa acildi.")


go_from = driver.find_element(By.XPATH,'//*[@id="fromTrainInput"]')
go_from.click()
select_from_station = driver.find_element(By.XPATH, '//*[@id="gidis-'+str(nereden)+'"]/div/div')
select_from_station.click()

go_to = driver.find_element(By.XPATH, '//*[@id="buyTicket"]/div[2]/div[2]/div')
go_to.click()
select_to_station = driver.find_element(By.XPATH, '//*[@id="donus-'+str(nereye)+'"]/div/div')
select_to_station.click()
driver.find_element(By.XPATH, '//*[@id="buyTicket"]/div[3]/div/div[2]/div/div/div[1]/div').click()
select_time = driver.find_element(By.XPATH, '//*[@id="buyTicket"]//*[@id="'+str(gidis_tarihi)+'"]').click()

#sefer_ara
driver.find_element(By.XPATH, '//*[@id="buyTicket"]/div[5]/div/button').click()


ff= driver.find_elements(By.XPATH, '//div[@class="card-header"]')
len_of_trains = len(ff)
#print ("Tren sayisi " + str(len_of_trains))
#train_ids = ff.get_dom_attribute('id')

for seeked_id in ff:
    trains_ids.append(seeked_id.get_attribute("id"))
#print(trains_ids)
    
#sırasıyla her bir tren için boş koltuk kontrolü yap

for index in range(len_of_trains):
  
    try:
        #print(index)
        ts = driver.find_element(By.XPATH, '//*[@id="gidis'+ str(index) +'btn"]/div/div[2]/div/div[2]/div[2]/span[1]')
        tren_saati = ts.text
        #print(ts.screenshot('./ts.png'))
        bos_koltuk = driver.find_element(By.XPATH, '//*[@id="gidis'+ str(index) +'btn"]/div/div[3]/div/div/span[2]')
        #print(bos_koltuk.text)
        if len(bos_koltuk.text) == 5:
            bos_koltuk_sayisi = int(bos_koltuk.text[1:4])
        elif len(bos_koltuk.text) == 4:
            bos_koltuk_sayisi = int(bos_koltuk.text[1:3])
        elif len(bos_koltuk.text) == 3:
            bos_koltuk_sayisi = int(bos_koltuk.text[1:2])
        print("Tren "+ str(index)+"  Saat "+ str(tren_saati) +"'daki trende bulunan boş koltuk sayisi: "+ str(bos_koltuk_sayisi))
    except:
        print("Tren "+ str(index)+"  Saat "+ str(tren_saati) +"'daki tren tamamen dolu")
   
    if bos_koltuk_sayisi > 2:
        bos_koltuk_olan_tren_sayisi = bos_koltuk_olan_tren_sayisi + 1
        #print(bos_koltuk_olan_tren_sayisi)

secilen_tren = int(input("Toplam " + str(bos_koltuk_olan_tren_sayisi) + " adet trende müsaitlik var birini seçiniz."))
#print(type(secilen_tren))
print("Secilen tren "+ str(secilen_tren))

selected_train_id = str(trains_ids[secilen_tren])[5:16]
#print("Secilen tren id")
#print(selected_train_id)
#print(type(selected_train_id))

time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="gidis'+ str(secilen_tren) +'btn"]/div/div[2]/div/div[2]/div[2]/span[1]').click() #seçilen trenin div'ine tıkla
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="collapseBodygidis'+ str(secilen_tren) +'"]/div/div[3]/div/div[2]/div/div/div/div[2]').click() #seçilen trenin seçin butonuna tıkla 
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="seferListScroll"]/div[3]/div/div[2]/button[2]').click() #seçilen trenin seçin butonuna tıkla 
driver.implicitly_wait(0) #koltuk seçimlerinin hızlı yapılması için azaltıldı.
time.sleep(2)

def find_available_seat():
    try:
        
        for x in range(1,10):             
            vagon_element = driver.find_element(By.XPATH, '//*[@id="connectedTab'+str(selected_train_id)+'"]/section[1]/div['+str(x)+']/div/button/div/span')
            vagon_seat = int(vagon_element.text)
            if vagon_seat > 1:
                
                driver.find_element(By.XPATH, '//*[@id="connectedTab'+str(selected_train_id)+'"]/section[1]/div['+str(x)+']/div/button/div/span').click()
                time.sleep(2)
            else:
                continue    
            if ((vagon_element) and (vagon_seat > 0)):
                
                print(str(vagon_seat)+" adet koltuk bulunan "+str(x)+" nolu vagonda arama yapılıyor.")   
                            
                for char_index in "abcd":
                    for number_index in range(1,21):
                        try:
                            element = driver.find_element(By.XPATH, '//*[@id="passengerForImageSingle'+str(selected_train_id)+ str(number_index)+ str(char_index)+'"]')
                            print(str(number_index) +str(char_index) +" is available")
                            if element:
                                #print(driver.find_element(By.XPATH, '//*[@id="passengerForImageSingle'+str(selected_train_id)+ str(number_index)+ str(char_index)+'"]'))
                                time.sleep(1)
                                driver.find_elements(By.XPATH, '//*[@id="passengerForImageSingle'+str(selected_train_id)+ str(number_index)+str(char_index)+'"]')[1].click()
                                if koltuk_secimi_yapilmak_isteniyormu == "h":
                                    secim="e"
                                elif koltuk_secimi_yapilmak_isteniyormu == "e":
                                    ecim= input(str(number_index)+ str(char_index) +" ile devam edilsin mi? e, h?")
                                    print(secim)
                                
                                if secim=="e":
                                    secim_yapildi=True
                                    if cinsiyet == "e":
                                        driver.find_element(By.XPATH, '//button[@selenium-test="male"]').click()
                                        return
                                    elif cinsiyet == "k":
                                        driver.find_element(By.XPATH, '//button[@selenium-test="female"]').click()
                                        return
                                    else:
                                        print("Hatalı seçim")
                                        
                                        
                        except KeyboardInterrupt:
                            exit()       
                        except Exception as err: 
                            #print("1. Except")
                            #print(err)                    
                            print(str(number_index) + str(char_index)+" is NOT available")
                    if (secim_yapildi):  
                        break
            if (secim_yapildi):  
                break                   
    except KeyboardInterrupt:
        exit()                   
    except:
        print("2. except")     
        print(str(x)+"Tren Bitmiştir. Başka bir Tren incelemek için restart edin.")
  
find_available_seat()


time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="Scroll"]/div[2]/div/button').location_once_scrolled_into_view
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="Scroll"]/div[2]/div/button').click()
driver.find_element(By.XPATH, '//*[@id="passengerInformationScroll"]/section/div[1]/div/div[1]/div/div[3]/div/div[1]/div/input').send_keys(name)
driver.find_element(By.XPATH, '//*[@id="passengerInformationScroll"]/section/div[1]/div/div[1]/div/div[3]/div/div[2]/div/input').send_keys(surname)
driver.find_element(By.XPATH, '//*[@id="passengerInformationScroll"]/section/div[1]/div/div[1]/div/div[3]/div/div[3]/div/div/div[1]/input').click()
driver.find_element(By.XPATH, '//button[@selenium-test="tarife-0-TAM (ADULT)"]').click() # diğer seçimler için if else yapılabilir
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="passengerInformationScroll"]/section/div[1]/div/div[1]/div/div[3]/div/div[4]/div/input').send_keys(dt)
driver.find_element(By.XPATH, '//*[@id="passengerInformationScroll"]/section/div[1]/div/div[1]/div/div[3]/div/div[6]/div/input').send_keys(tckn)
driver.find_element(By.XPATH, '//*[@id="passengerInformationScroll"]/section/div[1]/div/div[1]/div/div[3]/div/div[9]/div/input').send_keys(gsm)
driver.find_element(By.XPATH, '//*[@id="emailPassenger0"]').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="seferListScroll"]/section[2]/div/div[2]/div/div/div/div/div[2]/button').click()
time.sleep(3)

#Kredi Kartı ile Ödeme Sayfası
driver.find_element(By.XPATH, '//*[@id="seferListScroll"]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/form/div/div[1]/div/input').send_keys(kart_sahibi)
driver.find_element(By.XPATH, '//*[@id="seferListScroll"]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/form/div/div[3]/div/input').send_keys(kart_numarası)
driver.find_element(By.XPATH, '//button[@title="Ay"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//span[text()="'+str(kart_son_kullanma_ay-1).zfill(2)+'"]').click()
driver.find_element(By.XPATH, '//button[@title="Yıl"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//span[text()="'+str(kart_son_kullanma_yıl)+'"]').click()
driver.find_element(By.XPATH, '//*[@id="seferListScroll"]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/form/div/div[4]/div/div[1]/div/input').send_keys(kart_güvenlik_kodu)
driver.find_element(By.XPATH, '//*[@id="seferListScroll"]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/label/span[2]').click()

#wait for input
satin_alma_onayı  = input("SATIN ALINSIN MI?(e,h)")
if satin_alma_onayı =="e":
    driver.find_element(By.XPATH, '//*[@id="seferListScroll"]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/button')
else:
    driver.quit()

time.sleep(20)
driver.quit()
