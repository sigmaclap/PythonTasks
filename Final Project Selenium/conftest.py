from urllib.parse import urlparse

from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_base_url(self):
        url = urlparse(self.driver.current_url)
        return url.hostname

    def get_current_url(self):
        return self.driver.current_url


class AuthPage(BasePage):

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c' \
              '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid& '

        driver.get(url)

        self.username = driver.find_element(By.ID, "username")
        self.password = driver.find_element(By.ID, "password")
        self.auth_btn = driver.find_element(By.ID, "kc-login")
        self.place_ID = driver.find_element(By.ID, "t-btn-tab-ls")
        self.forgot_password = driver.find_element(By.ID, "forgot_password")
        self.register = driver.find_element(By.ID, 'kc-register')
        self.placeholder = driver.find_element(By.XPATH,
                                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
        self.vk_btn = driver.find_element(By.ID, "oidc_vk")
        self.ok_btn = driver.find_element(By.ID, 'oidc_ok')
        self.mailru_btn = driver.find_element(By.ID, 'oidc_mail')
        self.google_btn = driver.find_element(By.ID, 'oidc_google')
        self.ya_btn = driver.find_element(By.ID, 'oidc_ya')

    def find_element(self, by, location):
        return self.driver.find_element(by, location)

    def btn_click(self):
        self.auth_btn.click()

    def refresh_page(self):
        self.driver.refresh()

    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)


class RegPage(BasePage):

    def __init__(self, driver, url, timeout=10):
        super().__init__(driver, url, timeout)

        url1 = url

        driver.get(url1)

        self.name = driver.find_element(By.XPATH,
                                        "//body/div[@id='app']/main[@id='app-container']/section["
                                        "@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]")
        self.subname = driver.find_element(By.XPATH,
                                           "//body/div[@id='app']/main[@id='app-container']/section["
                                           "@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div["
                                           "1]/input[1]")
        self.whiteplace = driver.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section["
                                                        "@id='page-right']/div[1]")

    def find_element(self, by, location):
        return self.driver.find_element(by, location)
