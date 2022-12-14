# [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&width=800&lines=%D0%98%D1%82%D0%BE%D0%B3%D0%BE%D0%B2%D1%8B%D0%B9+%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82+%D0%BF%D0%BE+%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8+%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F+-+Selenium)](https://git.io/typing-svg) #

### Задачи стояли следующие: 
---
1. Протестировать требования. 
[Объект тестирования.](https://b2c.passport.rt.ru)
2. Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
3. Провести автоматизированное тестирование продукта (не менее 15 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.
4. Оформить описание обнаруженных дефектов.
---
### В своей работе применял такие техники тест-дизайна:
---
1. Эквивалентное разделение - с помощью которой тестировал валидные и не валидные варианта ввода.  
2. Граничные значения - с помощью которой проверял требования к длине вводимых символов в качестве логина или пароля.   
3. Угадывание ошибок - с помощью которой согласно своему опыту, получилось обнаружить один баг, который был внесен в реестр.  
4. Позитивное и негативное тестирование.   
---
### Выполненные автотесты:
---
* Test case - #1:
Проверка авторизации через valid_email
* Test case - #2: (Negative)
Проверка авторизации через invalid_email
* Test case - #3:
 Проверка авторизации через valid_phone
* Test case - #4: (Negative)
 Проверка авторизации через invalid_phone
* Test case - #5:
 Проверка авторизации через valid_login
* Test case - #6: (Negative)
 Проверка авторизации через invalid_login
* Test case - #7:
 Проверка авторизации через valid_ID
* Test case - #8: (Negative)
 Проверка авторизации через invalid_ID
* Test case - #9:
 Проверка регистрации пользователя - "Зарегистрироваться"
* Test case - #10:
 Проверка формы для пользователя - "Забыл пароль"
* Test case - #11:
 Вход по неправильному паролю в форме "Авторизация", надпись "Забыл пароль" перекрашивается в оранжевый цвет
* Test case - #12:
 Проверка работоспособности кнопки авторизации через VK
* Test case - #13:
 Проверка работоспособности кнопки авторизации через Одноклассники
* Test case - #14:
 Проверка работоспособности кнопки авторизации через Мой Мир
* Test case - #15:
 Проверка работоспособности кнопки авторизации через Google
* Test case - #16:
 Проверка работоспособности кнопки авторизации через Yandex
* Test case - #17:
 Авторизация пользователя с использованием недопустимых символов в поле Имя и Фамилия
---
### Preconditions
---
1. Скачать [Chrome WebDriver](https://chromedriver.chromium.org/downloads) (выбрать версию согласно Вашей ОС)
2. Запуск:
```html
pytest -v --driver Chrome --driver-path  <Путь до вебдрайвера>\chromedriver.exe tests_rostelecom.py 
```
---
