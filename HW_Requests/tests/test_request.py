import requests
import pytest


@pytest.mark.parametrize("url, method, data", [
    ("https://bank.gov.ua/NBU_BankInfo/get_data_branch?json", "GET", None),
    (
    "https://bank.gov.ua/NBU_Exchange/exchange_site?start=yyyymmdd&end=%20yyyymmdd&valcode=usd&sort=exchangedate&order=desc&json",
    "GET", None),
    ("https://bank.gov.ua/NBU_BankInfo/get_data_branch?json", "GET", None)])
def test_api_get(url, method, data):
    response = requests.request(method=method, url=url, json=data)
    assert response.status_code == 200
