from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_ctg_nasos = "//*[@id='section_1897']"  # выбираем категорию насосы
    select_drenage = "//a[@id='section_7294']"  # подкатегория дренажные насосы
    select_brand = "//*[@id='ff-catalog']/div[2]/ul/li[3]/div[2]/p/span"  # выбираем бренд в выпадающем списке
    select_checkbox_zubr = "//li[@data-val='11663']"  # бренд Зубр
    select_checkbox_apply = "//p[@class='btnOk btnOkActive']"  # подтверждаем выбор в чекбоксе
    select_product_1 = "//*[@id='main_block']/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[1]/a"  # выбираем продукт
    cart = "//*[@id='e_258764']/div/div/a[1]"  # добавляем товар в корзину
    cart_in = "//span[@class='layout-header-down__text']"  # переходим в корзину

    # Getters

    def get_select_ctg_nasos(self):
        return self.driver.find_element(by=By.XPATH, value="//*[@id='section_1897']")

    def get_select_drenage(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_drenage)))

    def get_select_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_brand)))

    def get_select_checkbox_zubr(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_checkbox_zubr)))

    def get_select_checkbox_apply(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_checkbox_apply)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_cart_in(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_in)))

    # Actions

    def click_select_ctg_nasos(self):
        self.get_select_ctg_nasos().click()
        print("Click select category nasos")

    def click_select_drenage(self):
        self.get_select_drenage().click()
        print("Click select drenage")

    def click_select_brand(self):
        self.get_select_brand().click()
        print("Click select select brend")

    def click_select_checkbox_zubr(self):
        self.get_select_checkbox_zubr().click()
        print("Click select checkbox zubr")

    def click_select_checkbox_apply(self):
        self.get_select_checkbox_apply().click()
        print("Click select checkbox apply")

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click Select Product 1")

    def click_cart(self):
        self.get_cart().click()
        print("Click Cart")

    def click_cart_in(self):
        self.get_cart_in().click()
        print("Click Cart in")

    # Methods

    def select_products_1(self):
        self.get_current_url()
        self.click_select_ctg_nasos()
        self.click_select_drenage()
        self.click_select_brand()
        self.click_select_checkbox_zubr()
        self.click_select_checkbox_apply()
        self.click_select_product_1()
        self.click_cart()
        self.click_cart_in()
