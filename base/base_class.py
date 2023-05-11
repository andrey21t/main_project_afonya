import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Method Get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word ")

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%H.%M. %d.%m.%Y")
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('/Users/an.tikhomirov/PycharmProjects/main_project_afonya/screen/' + name_screenshot)
