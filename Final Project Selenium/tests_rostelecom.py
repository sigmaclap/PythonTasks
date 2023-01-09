from time import sleep

from selenium.webdriver.common.by import By

import values
from conftest import AuthPage
from conftest import RegPage


# Test case - #1:
# Проверка авторизации через valid_email
def test_correct_email(selenium):
    page = AuthPage(selenium)
    page.enter_username(values.EMAIL)
    page.enter_password(values.PASSWORD)
    page.btn_click()

    assert page.get_base_url() == '/account_b2c/page'


# Test case - #2: (Negative)
# Проверка авторизации через invalid_email
def test_correct_email_invalid(selenium):
    page = AuthPage(selenium)
    page.enter_username(values.INVALID_VALUES_LOGIN[0])
    page.enter_password(values.INVALID_VALUES_PASSWORD[1])
    page.btn_click()

    assert page.get_base_url() != '/account_b2c/page'
    assert page.find_element('id', 'form-error-message').text == 'Неверный логин или пароль'


# Test case - #3:
# Проверка авторизации через valid_phone
def test_correct_phone_positive(selenium):
    page = AuthPage(selenium)
    page.enter_username(values.PHONE)
    page.enter_password(values.PASSWORD)
    page.btn_click()

    assert page.get_base_url() == '/account_b2c/page'


# Test case - #4: (Negative)
# Проверка авторизации через invalid_phone
def test_correct_phone_invalid(selenium):
    page = AuthPage(selenium)
    page.enter_username(values.INVALID_VALUES_LOGIN[1])
    page.enter_password(values.INVALID_VALUES_PASSWORD[1])
    page.btn_click()

    assert page.get_base_url() != '/account_b2c/page'
    assert page.find_element('id', 'form-error-message').text == 'Неверный логин или пароль'


# Test case #5:
# Проверка авторизации через valid_login
def test_correct_login_valid(selenium):
    page = AuthPage(selenium)
    page.enter_username(values.LOGIN)
    page.enter_password(values.PASSWORD)
    page.btn_click()

    assert page.get_base_url() == '/account_b2c/page'


# Test case #6: (Negative)
# Проверка авторизации через invalid_login
def test_correct_login_invalid(selenium):
    page = AuthPage(selenium)
    page.enter_username(values.INVALID_VALUES_LOGIN[2])
    page.enter_password(values.INVALID_VALUES_PASSWORD[2])
    page.btn_click()

    assert page.get_base_url() == '/account_b2c/page'


# Test case - #7:
# Проверка авторизации через valid_ID
def test_correct_ID_valid(selenium):
    page = AuthPage(selenium)
    page.place_ID.click()
    page.enter_username(values.PERSONAL_DATA)
    page.enter_password(values.PASSWORD)
    page.btn_click()

    assert page.get_base_url() == '/account_b2c/page'


# Test case - #8: (Negative)
# Проверка авторизации через invalid_ID
def test_correct_ID_invalid(selenium):
    page = AuthPage(selenium)
    page.place_ID.click()
    page.enter_username(values.INVALID_VALUES_LOGIN[3])
    page.enter_password(values.INVALID_VALUES_PASSWORD[2])
    page.btn_click()

    assert page.get_base_url() != '/account_b2c/page'
    assert page.find_element('id', 'form-error-message').text == 'Неверный логин или пароль'


# Test case #9:
# Проверка регистрации пользователя - "Зарегистрироваться"
def test_registration(selenium):
    page = AuthPage(selenium)
    page.register.click()

    assert page.find_element(By.XPATH, "//h1[contains(text(),'Регистрация')]").text == 'Регистрация'


# Test case #10:
# Проверка формы для пользователя - "Забыл пароль"
def test_forgot_password(selenium):
    page = AuthPage(selenium)
    page.forgot_password.click()

    assert page.find_element(By.XPATH, "//h1[contains(text(),'Восстановление пароля')]").text == 'Восстановление пароля'


# Test case #11:
# Вход по неправильному паролю в форме "Авторизация", надпись "Забыл пароль" перекрашивается в оранжевый цвет
def test_authorization_with_orange_btn(selenium):
    page = AuthPage(selenium)
    page.enter_username(values.PHONE)
    page.enter_password(values.INVALID_VALUES_PASSWORD[1])
    page.auth_btn.click()
    sleep(10)

    assert page.find_element('id',
                             'form-error-message').text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'
    assert "rt-link--orange" in page.find_element(By.XPATH, "//a[@id='forgot_password']").get_attribute('class')


# Test case #12:
# Проверка работоспособности кнопки авторизации через VK
def test_auth_VK(selenium):
    page = AuthPage(selenium)
    page.vk_btn.click()

    assert page.get_base_url() == 'oauth.vk.com'


# Test case #13:
# Проверка работоспособности кнопки авторизации через Одноклассники
def test_auth_OK(selenium):
    page = AuthPage(selenium)
    page.ok_btn.click()

    assert page.get_base_url() == 'connect.ok.ru'


# Test case #14:
# Проверка работоспособности кнопки авторизации через Мой Мир
def test_auth_MyMir(selenium):
    page = AuthPage(selenium)
    page.mailru_btn.click()

    assert page.get_base_url() == 'connect.mail.ru'


# Test case - #15:
# Проверка работоспособности кнопки авторизации через Google
def test_auth_Google(selenium):
    page = AuthPage(selenium)
    page.find_element(By.ID, 'oidc_google').click()

    assert page.get_base_url() == 'accounts.google.com'


# Test case - #16:
# Проверка работоспособности кнопки авторизации через Yandex
def test_auth_Yandex(selenium):
    page = AuthPage(selenium)
    page.ya_btn.click()

    assert page.get_base_url() == 'passport.yandex.ru'


# Test case - #17:
# Авторизация пользователя с использованием недопустимых символов в поле Имя и Фамилия
def test_correct_valid_data_in_registration(selenium):
    pages = AuthPage(selenium)
    pages.register.click()
    page = RegPage(selenium, pages.get_current_url())
    page.name.send_keys(values.INVALID_CHARACTERS_IN_LOGIN[0])
    page.subname.send_keys(values.INVALID_CHARACTERS_IN_LOGIN[0])
    page.whiteplace.click()

    assert page.find_element('xpath', "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]") \
               .text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    assert page.find_element('xpath', "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div["
                                      "1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]").text == 'Необходимо заполнить ' \
                                                                                                'поле кириллицей. От ' \
                                                                                                '2 до 30 символов.'

