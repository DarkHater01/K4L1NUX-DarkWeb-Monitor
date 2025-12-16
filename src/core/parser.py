from bs4 import BeautifulSoup

class Parser:
    def search_keywords(self, html, keywords):
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text().lower()

        found = []
        for k in keywords:
            if k.lower() in text:
                found.append(k)

        return found
