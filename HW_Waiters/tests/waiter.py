import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from HW_Waiters.src.widgets.waiter import ButtonWaiter


@pytest.mark.usefixtures('chrome')
class TestButtonVisible:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = ButtonWaiter(driver=self.driver)
        self.page.open()

    def test_button_not_visible_at_once(self):
        assert not self.page.visible_button_at_once()

    def test_button_visible_in_5_seconds(self):
        assert self.page.visible_button_in_time(time=10)

    def test_not_clicable_at_once(self):
        assert not self.page.button_clicable_at_once()

    def test_clicable_in_time(self):
        assert self.page.button_clicable_in_time()

    def test_button_collor_at_once(self):
        assert self.page.button_color_at_once() == "mt-4 btn btn-primary"

    def test_button_collor_in_time(self):
        assert self.page.button_color_in_time()
