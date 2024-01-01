1.  elementi sayfanın görünür yerine getirmek/ortalamak için

driver.find_element(By.XPATH, '//*[@id="Scroll"]/div[2]/div/button').location_once_scrolled_into_view

2. Herhangi bir attribute'ı seçmek için

driver.find_element(By.XPATH, '//button[@selenium-test="tarife-0-TAM (ADULT)"]')

3. element içerisindeki text'e göre seçmek için

driver.find_element(By.CSS_SELECTOR, '//span[text()="'+str(kart_son_kullanma_ay-1).zfill(2)+'"]')
