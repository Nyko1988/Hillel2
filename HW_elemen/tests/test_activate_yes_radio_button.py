import pytest

from HW_elemen.src.widgets.radio_button import RadioButton


@pytest.mark.usefixtures('chrome')
class TestRadioButtonSelect:
    def test_widget(self):
        self.driver.get('https://demoqa.com/radio-button')
        button = 'Yes'

        radio_button_yes = RadioButton(driver=self.driver, name=button)
        radio_button_yes.select()
        a = radio_button_yes.is_selected()
        b = radio_button_yes.get_selected_element_field()
        assert a
        assert button in b