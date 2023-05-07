from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RadioButton:
    def __init__(self, driver: WebDriver, name: str):
        self.driver = driver
        self.locator = '//label[.="{}"]//ancestor::div[contains(@class, "radio")]'.format(name)
        self.input_ = '/input'
        self.label = '/label'
        self.get_locator = '//span[text()="{}"]'.format(name)

    def is_selected(self) -> bool:
        element = self.driver.find_element(By.XPATH, f'{self.locator}{self.input_}')
        return element.is_selected()

    def get_selected_element_field(self) -> str:
        return self.driver.find_element(By.XPATH, f'{self.get_locator}').text

    def select(self) -> None:
        self.driver.find_element(By.XPATH, f'{self.locator}{self.label}').click()
