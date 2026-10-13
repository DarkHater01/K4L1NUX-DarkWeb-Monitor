import requests

MAX_BYTES = 5 * 1024 * 1024


class TorClient:
    def __init__(self, proxy="socks5h://127.0.0.1:9050"):
        self.session = requests.Session()
        self.session.proxies = {
            "http": proxy,
            "https": proxy,
        }

    def get(self, url):
        try:
            with self.session.get(url, timeout=30, stream=True) as response:
                response.raise_for_status()
                raw = response.raw.read(MAX_BYTES, decode_content=True)
                return raw.decode("utf-8", "replace")
        except Exception:
            return None
