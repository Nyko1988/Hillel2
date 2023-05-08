from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckBox:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def change_folder_expand_state(self, name: str, driver: WebDriver, expanded: bool = True) -> None:
        element = driver.find_element(By.XPATH,
                                      f'//label[contains(@for, "tree-node-{name}")]//ancestor::span/button')
        if expanded:
            x = element.find_element(By.XPATH, '//*[contains(@class, "expand-open")]')
        else:
            x = element.find_element(By.XPATH, '//*[contains(@class, "expand-close")]')
        x.click()

    def expand_folder(self, name):
        self.change_folder_expand_state(name, expanded=False, driver=self.driver)

    def collapse_folder(self, name):
        self.change_folder_expand_state(name, expanded=True, driver=self.driver)

    def change_folder_selection_state(self, driver: WebDriver, name, enabled=False):
        element = driver.find_element(By.XPATH, f'//label[contains(@for, "tree-node-{name}")]')
        element_input = driver.find_element(By.XPATH, f'//label[contains(@for, "tree-node-{name}")]/input')
        if enabled:
            if not element_input.is_selected():
                element.click()
        else:
            if element_input.is_selected():
                element.click()

    def mark_folder(self, name):
        self.change_folder_selection_state(name=name, enabled=True, driver=self.driver)

    def unmark_folder(self, name):
        self.change_folder_selection_state(name=name, enabled=False, driver=self.driver)
