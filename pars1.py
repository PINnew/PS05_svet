import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


# Инициализация браузера
driver = webdriver.Chrome()

url = 'https://www.divan.ru/izhevsk/category/svet'
driver.get(url)
time.sleep(10) # Задаём время, подгружаем сайт
# Поиск всех светильников на странице
svetils = driver.find_elements(By.CSS_SELECTOR, 'div.tXEF6')

print(svetils)

parsed_data = []

for svetil in svetils:
    try:
        # Корректируем CSS-селекторы в зависимости от структуры страницы
        title = svetil.find_element(By.CSS_SELECTOR, 'span.name').text
        price = svetil.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').get_attribute('content')
        link = svetil.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')

        parsed_data.append([title, price, link])
    except Exception as e:
        print(f'Произошла ошибка при парсинге: {e}')
        continue

# Закрытие браузера
driver.quit()

# Сохранение данных в CSV
with open('svetil.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'Цена светильника', 'Ссылка на светильник'])
    writer.writerows(parsed_data)
