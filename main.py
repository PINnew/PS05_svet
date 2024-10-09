import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # Назначаем в каком браузере открывать сайт

url = 'https://www.divan.ru/izhevsk/category/svet' # Задаём какой сайт обрабатываем

driver.get(url) # Открываем сайт

time.sleep(3) # Задаём время, подгружаем сайт

svetils = driver.find_elements(By.CLASS_NAME, 'div._Ud0k')

print(svetils)
parsed_data = []

for svetil in svetils:
    try:
        title = svetil.find_element(By.CSS_SELECTOR, 'span.name').text
        price = svetil.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
        link = svetil.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')
    except:
        print('Произошла ошибка при парсинге')
        continue
    parsed_data.append([title, price, link])

driver.quit()

with open('svetil.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'Цена светильника', 'Ссылка на светильник'])
    writer.writerows(parsed_data)
