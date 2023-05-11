import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('/Users/an.tikhomirov/PycharmProjects/pythonProject//pythonProject//resource/chromedriver')

    driver = webdriver.Chrome(options=options, service=g)

    print("Start test")

    login = Login_page(driver)
    login.authorization()   # Methods

    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(3)

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)      # cp = cart_page
    cp.product_confirmation()   # Methods

    p = Payment_page(driver)
    p.payment()

    print("Finish Test")
    driver.quit()