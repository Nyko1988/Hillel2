import pytest

from HW_elemen.src.widgets.radio_button import RadioButton


@pytest.mark.usefixtures('chrome')
class TestRadioButtonSelect:
    def test_widget(self):
        self.driver.get('https://demoqa.com/radio-button')

        list_radio_buttons = RadioButton(driver=self.driver, name="Yes")
        assert list_radio_buttons.get_dict_radio_buttons()