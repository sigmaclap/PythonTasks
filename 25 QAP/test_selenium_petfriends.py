from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



def test_all_pets_are_present(driver):
   '''Проверяем что на странице со списком моих питомцев присутствуют все питомцы'''
   WebDriverWait(driver, 5).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
   # Сохраняем в переменную statistic элементы статистики
   statistic = driver.find_elements(By.CSS_SELECTOR,".\\.col-sm-4.left")
   WebDriverWait(driver, 5).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pets элементы карточек питомцев
   pets = driver.find_elements(By.CSS_SELECTOR,'.table.table-hover tbody tr')
   # Получаем количество питомцев из данных статистики
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])
   # Получаем количество карточек питомцев
   number_of_pets = len(pets)
   # Проверяем что количество питомцев из статистики совпадает с количеством карточек питомцев
   assert number == number_of_pets


def test_photo_availability(driver):
    ''' Проверяем что у половины моих питомцев присутствует фото '''
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//th[@scope='row']/img")))
    # Сохраняем в переменную images все карточки питомцев
    images = driver.find_elements(By.XPATH, "//th[@scope='row']/img")
    # Сохраняем в переменную num_photos карточки питомцев, в которых присутствует фото
    num_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            num_photos += 1
    # Сохраняем в переменную ststistic элементы статистики
    statistic = driver.find_elements(By.XPATH, "//div[@class='.col-sm-4 left']")
    # Получаем количество питомцев из данных статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])
    # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
    assert num_photos >= number // 2


def test_name_breed_age(driver):
    ''' Проверяем что у всех питомцев есть имя, порода и возраст'''
    # Устанавливаем явное ожидание
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td")))
    # Сохраняем в переменную descriptions элементы с данными о питомцах
    descriptions = driver.find_elements(By.XPATH,"//td[@class='smart_cell']/preceding-sibling::td")
    # Перебираем данные из descriptions и сравниваем их с ожидаемым результатом
    for i in range(len(descriptions)):
        assert descriptions[i].text != ''


def test_unique_names(driver):
    ''' Проверяем что у всех питомцев разные имена '''
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td[3]")))
    # Сохраняем в переменную names информацию с именами питомцев
    names = driver.find_elements(By.XPATH,"//td[@class='smart_cell']/preceding-sibling::td[3]")
    # Перебираем имена и добавляем их в список names
    pets_name = []
    for i in range(len(names)):
        pets_name.append(names[i].text)
    # преобразуем список с именами в множество и сравниваем его длину с длиной списка pets_name
    assert len(set(pets_name)) == len(pets_name)


def test_duplicate_pets(driver):
    ''' Проверяем что в списке нет повторяющихся питомцев '''
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td[3]")))
    # Сохраняем в переменную descriptions_name информацию с именами питомцев
    descriptions_name = driver.find_elements(By.XPATH,"//td[@class='smart_cell']/preceding-sibling::td[3]")
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td[2]")))
    # Сохраняем в переменную descriptions_breed информацию с породами питомцев
    descriptions_breed = driver.find_elements(By.XPATH,"//td[@class='smart_cell']/preceding-sibling::td[2]")
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td[1]")))
    # Сохраняем в переменную descriptions_age информацию с возрастом питомцев
    descriptions_age = driver.find_elements(By.XPATH,"//td[@class='smart_cell']/preceding-sibling::td[1]")
    # Перебираем имена и добавляем их в список names
    pets_name = []
    for i in range(len(descriptions_name)):
        pets_name.append(descriptions_name[i].text)
    # Перебираем породы и добавляем их в список pets_breed
    pets_breed = []
    for i in range(len(descriptions_breed)):
        pets_breed.append(descriptions_breed[i].text)
    # Перебираем возраст и добавляем их в список pets_age
    pets_age = []
    for i in range(len(descriptions_age)):
        pets_age.append(descriptions_age[i].text)
    # Перебираем имена, породы и возраст, склеиваем и добавляем их в список pets_data
    pets_data = []
    for (x, y, z) in zip(pets_name, pets_breed, pets_age):
        pets_data.append(x + y + z)
    # преобразуем список с именами в множество и сравниваем его длину с длиной списка pets_name
    assert len(set(pets_data)) == len(pets_data)
