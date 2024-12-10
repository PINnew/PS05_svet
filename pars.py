import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация браузера
driver = webdriver.Firefox()

# URL страницы
url = 'https://www.divan.ru/category/svet'
driver.get(url)

# Явное ожидание загрузки всех элементов на странице
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div._Ud0k'))
)

# Поиск всех светильников на странице (корректируем селектор)
svetils = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

print(svetils)

parsed_data = []

for svetil in svetils:
    try:
        # Корректируем CSS-селекторы в зависимости от структуры страницы
        title = svetil.find_element(By.CSS_SELECTOR, 'span.name').text
        price = svetil.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
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
