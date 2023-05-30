import requests


class GetInformationBank:
    URl = 'https://bank.gov.ua/NBU_BankInfo/get_data_branch?json'  # 'https://www.api-football.com/'
    FILE = 'D:\XPI\Python\HW_GET.txt'

    def __init__(self, url: str = URl, file: str = FILE):
        self.url = url
        self.file = file

    def get_current_date(self):
        element = requests.get(self.url).headers
        return element.get('Date')

    def write_response_from_server(self):
        date_of_element = requests.get(self.url).json()
        with open(file=self.file, mode='a', encoding='utf-8') as e:
            e.write('Response at {} is {}\n'.format(self.get_current_date(), requests.get(self.url).status_code))
            for i in date_of_element:
                e.write('Банк {} за адресою {}, {} в стані {}\n'.format(i.get('N_GOL'), i.get('N_OBL'), i.get('ADRESS'),
                                                                        i.get('NSTAN_GOL')))




class PostGoogleTranslate:
    URL = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    Headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "ecf6a7a9efmshb913b886ad569cap1ddeaajsna775ba334a29",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    def __init__(self, url: str = URL, sentence: str = '', target: str = 'uk', source: str = 'en', headers=None):
        if headers is None:
            headers = self.Headers
        self.url = url
        self.sentence = sentence
        self.target = target
        self.source = source
        self.payload = {"q": sentence, "target": target, "source": source}
        self.headers = headers

    def get_translation(self):
        response = requests.post(self.url, data=self.payload, headers=self.headers)
        return response.json()
