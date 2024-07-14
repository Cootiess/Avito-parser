import logging
import time
import re
from selenium.webdriver.common.by import By
from tqdm import tqdm
from selenium import webdriver
import csv
import logging

def parser(url:str,i):
    logging.info("Start")
    driver  = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
    driver.get(url)
    driver.implicitly_wait(4)
    driver.maximize_window()
   

    try:
        ads_count = driver.find_element(by=By.XPATH, value="//span[@data-marker='page-title/count']").text.replace(' ','')
        print(ads_count)
        ads_count = int(ads_count)
        if ads_count % 50 > 0:
            page_count = (ads_count // 50) + 1
        else:
            page_count = ads_count // 50
        time.sleep(30)
        for page in range(1, page_count + 1):
            driver.get(f"{url}&p={page}")    
            driver.implicitly_wait(3)    
            ads_elements = driver.find_elements(by=By.XPATH, value='//a[@data-marker="item-title"]') 
    
            for ad in ads_elements:
                i+=1
                print(i)
                link = ad.get_attribute("href")      
                with open("info.csv", mode='a', newline='',encoding='utf-8') as csv_file:
                    writer = csv.writer(csv_file)    
                    writer.writerow([link])
            print(f"Закончил сбор объявлений на странице {page}")
    except Exception as ex:
        print(ex)

if __name__=='__main__':
    i=0
    parser('https://www.avito.ru/ulan-ude/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1&context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYysVLKTczMU7KuBQQAAP__w5qblCAAAAA',i)