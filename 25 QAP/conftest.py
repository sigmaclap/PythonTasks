import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()

    driver.implicitly_wait(5)
    # Переходим на страницу авторизации
    driver.get('http://petfriends.skillfactory.ru/login')
    # Вводим email
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'email'))).send_keys('motherland@mail.ru')
    # Вводим пароль
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'pass'))).send_keys('123123')
    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
    # Нажимаем на кнопку "Мои питомцы"
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы'))).click()
    yield driver
    driver.quit()
