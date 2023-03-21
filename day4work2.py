from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class loginTestleri:
    
    def test_1_kullanici_sifre_bos_test(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult= errorMessage.text=="Epic sadface: Username is required"
        print(f"Test 1: {testResult}")

    def test_2_kullanici_dolu_sifre_bos(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        userBox=driver.find_element(By.ID,"user-name")
        userBox.send_keys("user")
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult= errorMessage.text=="Epic sadface: Password is required"
        print(f"Test 2: {testResult}")

    def test_3_kilitli_kullanici(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        userBox=driver.find_element(By.ID,"user-name")
        userBox.send_keys("locked_out_user")
        passwordBox=driver.find_element(By.ID,"password")
        passwordBox.send_keys("secret_sauce")
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult= errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"Test 3: {testResult}")

    def test_4_ikon_kontrol(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        ikonOnce=driver.find_elements(By.CSS_SELECTOR,"div.form_group svg ")   
        if(len(ikonOnce)==2):
            mesajKapat=driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button > svg")
            mesajKapat.click()
            ikonSonra=driver.find_elements(By.CSS_SELECTOR,"div.form_group svg")
            testResult= len(ikonSonra)==0
            print(f"Test 4: {testResult}")

    def test_5_basarili_giris(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        userBox=driver.find_element(By.ID,"user-name")
        userBox.send_keys("standard_user")
        passwordBox=driver.find_element(By.ID,"password")
        passwordBox.send_keys("secret_sauce")
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        testResult= driver.current_url=="https://www.saucedemo.com/inventory.html"
        print(f"Test 5: {testResult}")

    def test_6_urun_sayisi_6(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        userBox=driver.find_element(By.ID,"user-name")
        userBox.send_keys("standard_user")
        passwordBox=driver.find_element(By.ID,"password")
        passwordBox.send_keys("secret_sauce")
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        urunAdet=driver.find_elements(By.CSS_SELECTOR,".inventory_item")
        testResult= len(urunAdet)==6
        print(f"Test 6: {testResult}")

test=loginTestleri()
test.test_1_kullanici_sifre_bos_test()
test.test_2_kullanici_dolu_sifre_bos()
test.test_3_kilitli_kullanici()
test.test_4_ikon_kontrol()
test.test_5_basarili_giris()
test.test_6_urun_sayisi_6()

