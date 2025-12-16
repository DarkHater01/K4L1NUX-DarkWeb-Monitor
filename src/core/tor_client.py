import requests

class TorClient:
    def __init__(self, proxy="socks5h://127.0.0.1:9050"):
        self.session = requests.Session()
        self.session.proxies = {
            "http": proxy,
            "https": proxy
        }

    def get(self, url):
        try:
            response = self.session.get(url, timeout=30)
            return response.text
        except Exception:
            return None
