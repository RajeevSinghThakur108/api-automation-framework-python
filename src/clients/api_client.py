import requests as r
from src.config.config import BASE_URL
from src.utils.logger import get_logger



class APIClient:

    def __init__(self):
        self.session = r.session()
        self.base_url = BASE_URL 
        self.logger = get_logger()

    def get(self , endpoint , **kwargs):
        url = self.base_url + endpoint
        response = self.session.get(url, **kwargs)
        self.logger.info(f"Response Status: {response.status_code}")
        return response