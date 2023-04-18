import requests
from parsers.uf_parser import UFParser

class UFService:
    BASE_URL = "https://www.sii.cl/valores_y_fechas/uf"

    def fetch_uf(self, year):
        url = f"{self.BASE_URL}/uf{year}.htm"
        response = requests.get(url)

        if response.status_code != 200:
            return None

        return response.text

    def get_uf_value(self, date):
        html = self.fetch_uf(date.year)

        if html is None:
            return None
    
        uf_parser = UFParser()
        uf_value = uf_parser.parse_uf(html, date)

        return uf_value