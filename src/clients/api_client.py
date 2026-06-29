import requests as r
from src.config.config import BASE_URL , DEFAULT_TIMEOUT
from src.utils.logger import get_logger

class APIClient:

    def __init__(self):
        self.session = r.session()
        self.base_url = BASE_URL 
        self.logger = get_logger()

        self.session.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json"
        })


    def _request(self, method, endpoint, **kwargs):
        url = self.base_url + endpoint
        self.logger.info(f"{method} Request: {url}")
        try:
            response = self.session.request(
            method = method, 
            url = url, 
            timeout=DEFAULT_TIMEOUT,
            **kwargs
            )
            self.logger.info(f"Response Status: {response.status_code}")
            return response 
        except r.exceptions.RequestException as e:
            self.logger.error(f"Request Failed: {e}")
            raise
        

    def get(self , endpoint , **kwargs):
        return self._request("GET", endpoint , **kwargs)
        
        
    # def post(self, endpoint, **kwargs):
    #     url = self.base_url + endpoint
    #     self.logger.info(f"POST Request: {url}")
    #     response = self.session.post(url, **kwargs)
    #     self.logger.info(f"Response Status: {response.status_code}")
    #     return response

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint , **kwargs)
    
    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)
    
    def patch(self, endpoint, **kwargs):
        return self._request("PATCH", endpoint, **kwargs)
    
    def delete(self, endpoint, **kwargs):
         return self._request("DELETE", endpoint, **kwargs)

   


    

    
    