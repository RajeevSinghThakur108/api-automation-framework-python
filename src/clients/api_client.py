import requests as r
class APIClient:
    def get(self , url):
        return r.get(url)