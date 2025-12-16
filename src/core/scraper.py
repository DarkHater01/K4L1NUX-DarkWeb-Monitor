from src.core.tor_client import TorClient
from src.core.parser import Parser
from src.utils.logger import logger


class Scraper:
    def __init__(self, url):
        self.url = url
        self.client = TorClient()
        self.parser = Parser()

    def run(self, keywords):
        logger.info(f"Scrapeando {self.url}")
        html = self.client.get(self.url)

        if not html:
            logger.error("No se pudo obtener contenido")
            return []

        return self.parser.search_keywords(html, keywords)
