
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Login_page(Base):
    url = "https://www.afonya-spb.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    windows = "//*[@id='af-grandsale-warning']/div[1]/a"                 # всплывающее окно рекламы
    icon_entrance = "/html/body/header/div[2]/div/ul/details/summary"    # иконка входа
    new_account = "//*[@id='content']/div/div/div/div/form/div[5]/div[2]/a"
    user_name = "//input[@name='REGISTER[NAME]']"
    user_email = "//input[@name='REGISTER[EMAIL]']"
    user_password = "//input[@name='REGISTER[PASSWORD]']"
    user_password_confirm = "//input[@name='REGISTER[CONFIRM_PASSWORD]']"
    checkbox_agree = "//input[@name='permission']"
    button_registration = "//input[@name='register_submit_button']"
    main_word = "/html/body/header/div[2]/div/ul/details/summary/span[1]"
    select_city = "//button[@class='af-button af-button__blue JSLocationSet']"  # окно выбора города

    # Getters

    def get_windows(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.windows)))

    def get_icon_entrance(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.icon_entrance)))

    def get_new_account(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_account)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_user_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_email)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_user_password_confirm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password_confirm)))

    def get_checkbox_agree(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_agree)))

    def get_button_registration(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.button_registration)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.main_word)))

    def get_select_city(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.select_city)))

    # Actions

    def click_windows(self):
        self.get_windows().click()
        print("Click windows")

    def click_icon_entrance(self):
        self.get_icon_entrance().click()
        print("Click icon entrance")

    def click_new_account(self):
        self.get_new_account().click()
        print("Click new account")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user number")

    def input_user_email(self, user_email):
        self.get_user_email().send_keys(user_email)
        print("Input user email")

    def input_user_password(self, user_password):
        self.get_user_password().send_keys(user_password)
        print("Input password")

    def input_user_password_confirm(self):
        self.get_user_password_confirm().send_keys("12345qW12345")
        print("Input password confirm")

    def click_checkbox_agree(self):
        self.get_checkbox_agree().click()
        print("Click checkbox agree")

    def click_button_registration(self):
        self.get_button_registration().click()
        print("Click button registration")

    def click_select_city(self):
        self.get_select_city().click()
        print("Click select city")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_select_city()
        # self.click_windows()
        self.click_icon_entrance()
        self.click_new_account()
        self.input_user_name("Иван Петрович")
        self.input_user_email("t006_mail@mail.ru")
        self.input_user_password("12345qW12345")
        self.input_user_password_confirm()
        self.click_checkbox_agree()
        self.click_button_registration()
        self.assert_word(self.get_main_word(), "Иван")
