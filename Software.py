import requests
import uuid
import time

class Software:

    def __init__(self, name, spec_version, archi):
        self.id = f'software--{uuid.uuid4()}'
        self.type = "software"
        self.spec_version = "2.1"
        self.name = name
        self.cpe = ""
        self.version = spec_version
        self.archi = archi

    def setup_attributes(self):
        self.__get_cpe()
        print(f'Scanning software: {self.__dict__}')

    def __get_cpe(self):
        url = "https://services.nvd.nist.gov/rest/json/cpes/2.0"
        headers = {
            "apiKey": "ac29abbf-7401-42aa-b1ec-57a1f0bf3a6c"    # private bszollosi
        }
        params = {
            'keywordSearch': f'{self.name}'  #&keywordExactMatch
        }
        r = requests.get(url, headers=headers, params=params)
        time.sleep(1)

        try:
            cpe_response = r.json()
            try:
                self.cpe = cpe_response["products"][0]["cpe"]["cpeName"]
            except IndexError:
                pass
        except requests.exceptions.JSONDecodeError:
            pass
