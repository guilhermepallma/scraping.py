import os
import log
import skus
import pandas as pd
from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
options = Options()
options.add_argument('windows-size=1366,768')
browser = webdriver.Chrome(options=options)

browser.get('https://portal.americanasmarketplace.com.br/v3/produtos')

sleep(3)

input_email = browser.find_element('xpath', '//*[@id="main"]/app-login/main/section/div/div[1]/form/div[1]/input')
input_pass = browser.find_element('xpath', '//*[@id="main"]/app-login/main/section/div/div[1]/form/div[2]/input')
button_enter = browser.find_element('xpath', '//*[@id="main"]/app-login/main/section/div/div[1]/form/p/button')

input_email.send_keys(os.getenv('EMAIL'))
input_pass.send_keys(os.getenv('PASSWORD'))

sleep(3)

button_enter.click()

sleep(10)

data = []

for sku in skus.all_skus:
    try:
        url = f'https://portal.americanasmarketplace.com.br/v3/produtos/detalhes?sku={sku}'
        browser.get(url)
        sleep(3)
        page_content = browser.page_source
        site = BeautifulSoup(page_content, 'html.parser')
        product_name = site.find('h1', class_='mt-0 title-product bold').text.strip()
        
        ids_01 = ['variation-0-input-store-0-stock-qty', 'input-store-0-stock-qty']
        
        element_01 = None
        
        for id_element in ids_01:
            try:
                element_01 = browser.find_element(By.ID, id_element)
                if element_01:
                    stock_01 = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, id_element)))
                break
            except NoSuchElementException:
                pass 
        
        
        ids_02 = ['variation-0-input-store-1-stock-qty', 'input-store-1-stock-qty']
        
        element_02 = None
        
        for id_element in ids_02:
            try:
                element_02 = browser.find_element(By.ID, id_element)
                if element_02:
                    stock_02 = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, id_element)))
                break
            except NoSuchElementException:
                pass
                            
        input_01 = stock_01.get_attribute('value')
        input_02 = stock_02.get_attribute('value')
        
        data.append({'MODELO': product_name, 'ESTOQUE 01': input_01, 'ESTOQUE 02': input_02})
        sleep(3)
    
    except NoSuchElementException:
        erro_01 = f"Elemento para o SKU {sku} não encontrado. Continuando..."
        log.logging.warning(erro_01)
    except Exception as e:
        erro_02 = f"Ocorreu um erro ao processar o SKU {sku}: {e}"
        log.logging.error(erro_02)


df = pd.DataFrame(data)
df['ESTOQUE 01'] = pd.to_numeric(df['ESTOQUE 01'], errors='coerce')
df['ESTOQUE 02'] = pd.to_numeric(df['ESTOQUE 02'], errors='coerce')

current_date = datetime.now().strftime("%d-%m-%Y")
df.to_excel(f'estoque_b2w_{current_date}.xlsx', index=False)