from selenium import webdriver
from time import sleep as sl
import fake_useragent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as web
from selenium_stealth import stealth



# executable_path="chromedriver-win64/chromedriver.exe"
service = Service(executable_path="/usr/bin/chromedriver")
fake = fake_useragent.UserAgent()
user = fake.random
user = str(user) # str : user | str(user)
headers = f"user-agent={user}"

options = Options()
options.add_argument(headers)
options.add_argument("--no-snadbox")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.page_load_strategy='eager'
options.add_argument("--headless=new")

url1 = "https://sunlight.net/profile/login/?next_encoded=Lw=="
url2 = "https://lk.plusofon.ru/registration"
url3 = "https://www.parfum-lider.ru/"
url4 = "https://www.dns-shop.ru/"

driver = webdriver.Chrome(service=service,
                          options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source' : '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;


'''
})


stealth(driver=driver,
        languages=['en-US', 'en'],
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

num = '9064887738'
waits = web(driver, 5)

def finish_driver():
    try:
        driver.quit()
        driver.close()
    except:
        pass

def sunlight_call(number):
    try:
        driver.get(url=url1)
        waits.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div[6]/div/div/div/div/form/div[3]/input')))
        auth_button_one = driver.find_element(By.XPATH,'//*[@id="wrapper"]/div[6]/div/div/div/div/form/div[3]/input').send_keys(number)
        waits.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div[6]/div/div/div/div/form/button')))
        auth_button_two = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[6]/div/div/div/div/form/button').click()
        sl(1.5)
    except Exception as ex:
        pass




def parfum_call(number):
    try:
        driver.get(url=url3)
        waits.until(ec.element_to_be_clickable((By.XPATH, '/html/body/header/div/div[2]/div[4]/div[4]/div')))
        auth_button_one = driver.find_element(By.XPATH, '/html/body/header/div/div[2]/div[4]/div[4]/div').click()
        waits.until(ec.element_to_be_clickable((By.XPATH, '/html/body/header/div/div[2]/div[4]/div[4]/div/nav/ul/li[2]/a')))
        auth_button_one2 = driver.find_element(By.XPATH, '/html/body/header/div/div[2]/div[4]/div[4]/div/nav/ul/li[2]/a').click()
        waits.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="signInByCallPopup"]/form/div[3]/input')))
        auth_button_two = driver.find_element(By.XPATH, '//*[@id="signInByCallPopup"]/form/div[3]/input').send_keys(number)
        waits.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="signInByCallPopup"]/form/div[5]/button')))
        auth_button_three = driver.find_element(By.XPATH, '//*[@id="signInByCallPopup"]/form/div[5]/button').click()
        sl(1.5)

    except Exception as ex:
        pass
    
def dns_call(number):    
    try:
        driver.get(url=url4)
        waits.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="header-search"]/div/div[3]/div[2]/div/div/div[2]')))
        auth_button_one = driver.find_element(By.XPATH,'//*[@id="header-search"]/div/div[3]/div[2]/div/div/div[2]').click()
        waits.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="header-search"]/div/div[3]/div[2]/div/div/div[3]/div/div[2]/div[1]/button')))
        auth_button_two = driver.find_element(By.XPATH,'//*[@id="header-search"]/div/div[3]/div[2]/div/div/div[3]/div/div[2]/div[1]/button').click()
        waits.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/div/div/div[2]/div/input')))
        auth_button_three = driver.find_element(By.XPATH,'/html/body/div[1]/header/div[2]/div/div/div/div/div/div[2]/div/input').send_keys(number)
        waits.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="modals"]/div/div/div/div/div/div[3]/div/button')))
        auth_button_four = driver.find_element(By.XPATH,'//*[@id="modals"]/div/div/div/div/div/div[3]/div/button').click()
        sl(1)
        
    except Exception as ex:
        pass




   
