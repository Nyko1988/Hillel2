import requests
import pytest

from HW_Requests.src.lib import PostGoogleTranslate, GetInformationBank


@pytest.mark.parametrize("url, method, data", [
    ("https://bank.gov.ua/NBU_BankInfo/get_data_branch?json", "GET", None),
    (
    "https://bank.gov.ua/NBU_Exchange/exchange_site?start=yyyymmdd&end=%20yyyymmdd&valcode=usd&sort=exchangedate&order=desc&json",
    "GET", None),
    ("https://bank.gov.ua/NBU_BankInfo/get_data_branch?json", "GET", None)])
def test_api_get(url, method, data):
    response = requests.request(method=method, url=url, json=data)
    assert response.status_code == 200

def test_post_api():
    post = PostGoogleTranslate()
    post_translation = post.get_translation(payload={"q": 'welcome', "target": 'uk', "source": 'en'})
    assert post_translation.get('data').get('translations')[0].get('translatedText') == 'Ласкаво просимо'

def test_api_get_bank():
    get_inform_bang = GetInformationBank()
    assert get_inform_bang.get_status_code() == 200
    assert get_inform_bang.write_response_from_server() > 1

