import argparse

from src.core.scraper import Scraper
from src.utils.logger import logger
from src.core.alerts import TelegramAlert
from src.utils.config_loader import load_config
#from src.core.alerts import send_telegram_alert

def load_keywords(path):
    with open(path, "r") as f:
        return [x.strip() for x in f if x.strip()]


def main():
    parser = argparse.ArgumentParser(
        description="K4L1NUX Dark Web Monitor"
    )
    parser.add_argument("--keywords", default="config/keywords.txt")
    parser.add_argument("--url", required=True)

    args = parser.parse_args()

    # 1️⃣ Cargar keywords
    keywords = load_keywords(args.keywords)

    # 2️⃣ Ejecutar scraper
    scraper = Scraper(args.url)
    matches = scraper.run(keywords)
    matches = ["example", "test-alert"]

    logger.info(f"Coincidencias encontradas: {matches}")

    # 3️⃣ Cargar configuración
    config = load_config()

    # 4️⃣ Enviar alerta si hay coincidencias
    if config.get("telegram", {}).get("enabled") and matches:
        alert = TelegramAlert(
            config["telegram"]["token"],
            config["telegram"]["chat_id"]
        )

        message = (
            "🚨 *K4L1NUX DarkWeb Alert*\n\n"
            f"🌐 URL: `{args.url}`\n"
            "🔍 *Keywords detectadas:*\n"
            + "\n".join(f"- `{m}`" for m in matches)
        )

        alert.send(message)


if __name__ == "__main__":
    main()
