from bs4 import BeautifulSoup


class Parser:
    def to_text(self, html: str) -> str:
        return BeautifulSoup(html, "html.parser").get_text(" ")
