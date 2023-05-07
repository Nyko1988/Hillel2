from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RadioButton:
    def __init__(self, driver: WebDriver, name: str):
        self.driver = driver
        self.locator = '//label[.="{}"]//ancestor::div[contains(@class, "radio")]'.format(name)
        self.input_ = '/input'
        self.label = '/label'
        self.get_locator = '//span[text()="{}"]'.format(name)
        self.get_all_locator = 'input[type="radio"]'
        self.get_all_locator2 = '//label'

    def is_selected(self) -> bool:
        element = self.driver.find_element(By.XPATH, f'{self.locator}{self.input_}')
        return element.is_selected()

    def get_selected_element_field(self) -> str:
        return self.driver.find_element(By.XPATH, f'{self.get_locator}').text

    def select(self) -> None:
        self.driver.find_element(By.XPATH, f'{self.locator}{self.label}').click()

    def get_dict_radio_buttons(self):
        radio_buttons_name = self.driver.find_elements(By.XPATH, self.get_all_locator2)
        radio_buttons_attributes = self.driver.find_elements(By.CSS_SELECTOR, self.get_all_locator)
        radio_buttons_dict = {}

        for button, elem in zip(radio_buttons_name, radio_buttons_attributes):
            name = button.text
            radio_buttons_dict[name] = {'name': name}
            is_selected = elem.is_selected()
            is_enabled = elem.is_enabled()

            radio_buttons_dict[name] = {'is_selected': is_selected,
                                        'is_enabled': is_enabled}
        return radio_buttons_dict
