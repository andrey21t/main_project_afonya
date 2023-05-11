import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Payment_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    checkbox_pay_metod = "//input[@id='ID_PAY_SYSTEM_ID_1']"  # выбираем способ оплаты
    checkbox_delivery_metod = "//*[@id='order_form_content']/div/div[2]/div[1]/div[2]/div[7]/div/label/div[2]/div[1]"  # выбираем способ доставки
    address = "//label[@for='store_6']"  # адрес доставки
    address_confirmation = "//*[@id='row_6']/td/div/a"  # подтверждаем адрес доставки
    user_number = "//input[@id='ORDER_PROP_37']"  # ввод номера телефона
    user_number_confirmation = "//*[@id='sale_order_props']/div[2]/div[5]/div[1]"  # подтверждения телефона

    # Getters

    def get_checkbox_pay_metod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_pay_metod)))

    def get_checkbox_delivery_metod(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_delivery_metod)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_address_confirmation(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_confirmation)))

    def get_user_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_number)))

    def get_user_number_confirmation(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.user_number_confirmation)))

    #  Actions

    def click_checkbox_pay_metod(self):
        self.get_checkbox_pay_metod().click()
        print("Click checkbox pay metod")

    def click_checkbox_delivery_metod(self):
        self.get_checkbox_delivery_metod().click()
        print("Click checkbox delivery metod")

    def click_address(self):
        self.get_address().click()
        print("Click address")

    def click_address_confirmation(self):
        self.get_address_confirmation().click()
        print("Click address confirmation")

    def input_user_number(self):
        self.get_user_number().send_keys("9510489741")
        print("Input user number")

    def click_user_number_confirmation(self):
        self.get_user_number_confirmation().click()
        print("Input user number confirmation")

    def screenshot(self):
        self.get_screenshot()
        print("Screenshot")

    #  Methods

    def payment(self):
        self.get_current_url()
        self.click_checkbox_pay_metod()
        time.sleep(3)
        self.click_checkbox_delivery_metod()
        time.sleep(3)
        self.click_address()
        time.sleep(3)
        self.click_address_confirmation()
        time.sleep(3)
        self.input_user_number()
        time.sleep(3)
        self.click_user_number_confirmation()
        self.screenshot()
