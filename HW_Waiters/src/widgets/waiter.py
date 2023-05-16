from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class ButtonWaiter:
    _instance = None
    URL = 'https://demoqa.com/dynamic-properties'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.button_enabled_in_5_seconds = '#enableAfter'
        self.button_color_after = '//*[contains(@class, "mt-4 text-danger btn btn-primary")]'
        self.button_color_change = '#colorChange'
        self.button_visible_in_5_seconds = '#visibleAfter'

    def open(self) -> 'ButtonWaiter':
        self.driver.get(self.URL)
        return self

    def visible_button_at_once(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, self.button_visible_in_5_seconds)
        except NoSuchElementException:
            return None

    def visible_button_in_time(self, time):
        try:
            return WebDriverWait(self.driver, time).until(
                lambda x: x.find_element(By.CSS_SELECTOR, self.button_visible_in_5_seconds))
        except NoSuchElementException:
            return None

    def button_clicable_at_once(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.button_enabled_in_5_seconds).is_enabled()

    def button_clicable_in_time(self):
        return WebDriverWait(self.driver, 8).until(
            lambda x: x.find_element(By.CSS_SELECTOR, self.button_enabled_in_5_seconds).is_enabled())

    def button_color_at_once(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.button_color_change).get_attribute(name='class')

    def button_color_in_time(self):
        return WebDriverWait(self.driver, 8).until(
            lambda x: x.find_element(By.XPATH, self.button_color_after))
