import requests
from src.utils.logger import logger

class TelegramAlert:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{token}/sendMessage"

    def send(self, message):
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }

        try:
            r = requests.post(self.api_url, json=payload, timeout=10)
            if r.status_code == 200:
                logger.info("Alerta enviada por Telegram")
            else:
                logger.error("Error enviando alerta Telegram")
        except Exception as e:
            logger.error(f"Telegram error: {e}")






