import pytest

from HW_elemen.src.widgets.checkbox import CheckBox

expand_elem = ['home', 'desktop', 'documents']
mark_elem = ['commands', 'office']


@pytest.mark.usefixtures('chrome')
class TestCheckBox:
    def test_widget(self):
        self.driver.get('https://demoqa.com/checkbox')
        page = CheckBox(driver=self.driver)
        for elem in expand_elem:
            page.expand_folder(name=elem)
        for item in mark_elem:
            page.mark_folder(name=item)
