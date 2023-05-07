from selenium.webdriver.remote.webdriver import WebDriver


class TextBoxPage:
    def __init__(self, driver: WebDriver):
        self.url = 'https://demoqa.com/radio-button/text-box'
        self.driver = driver

    def open(self):
        self.driver.get(self.url)