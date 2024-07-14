import logging
import time
import re
from selenium.webdriver.common.by import By
from tqdm import tqdm
from selenium import webdriver
import csv
import logging
def open_info_csv():
    with open("links.csv", mode='r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)

data = []
open_info_csv()

for row in data:
    driver  = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
    converted_list = map(str, row)
    result = ''.join(converted_list)
    driver.get(result)
    balcony=windows=agreement=elevator=type_of_build=glow_up='NaN'
    price = driver.find_element(By.XPATH,'//span[@data-marker="item-view/item-price"]').get_attribute('content')
    area=driver.find_element(by=By.XPATH, value="//div[@itemprop='address']").text
    area=area.replace('\n','')
    date=driver.find_element(By.XPATH,'//span[@data-marker="item-view/item-date"]').text

    try:
            params_ul = driver.find_element(By.XPATH, "//ul[contains(@class, 'params-paramsList')]")

            for param_li in params_ul.find_elements(by=By.TAG_NAME, value='li'):
                text = param_li.text
                if "Количество комнат" in text:
                    count_room = param_li.text.split(": ")[1]
                elif "Общая площадь" in text:
                    S = param_li.text.split(": ")[1]
                elif 'Ремонт' in text:
                    glow_up = param_li.text.split(": ")[1]
                elif 'Этаж' in text:
                    room = param_li.text.split(": ")[1]
                elif 'Санузел' in text:
                    bathroom = param_li.text.split(": ")[1]
                elif 'Вид сделки' in text:
                    agreement = param_li.text.split(": ")[1]
                elif 'Балкон или лоджия' in text:
                    balcony = param_li.text.split(": ")[1]
                elif 'Окна' in text:
                    windows = param_li.text.split(": ")[1]
           
        
    except Exception as ex:
        logging.error(msg="Ошибка при сборе данных с объявления")
    try:
        all_li = driver.find_elements(by=By.TAG_NAME, value='li')
        for li in all_li:
            text2 = li.text
            if 'Тип дома' in text2:
                type_of_build = text2.split(": ")[1]
            elif 'Этажей в доме' in text2:
                count_of_room = text2.split(": ")[1]
            elif 'Пассажирский лифт' in text2:
                 elevator = text2.split(": ")[1]

    except Exception as ex:
        logging.error(msg="Ошибка при сборе данных с объявления")
    with open("kvar_info.csv", mode='a', newline='',encoding='utf-8') as csv_file:
             writer = csv.writer(csv_file)      
             writer.writerow((area,count_room,S,room,balcony,bathroom,windows,glow_up,agreement,type_of_build,count_of_room,elevator,date,price))
    driver.close()
    driver.quit()
