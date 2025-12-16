import requests
from datetime import datetime
from src.utils.logger import logger


def build_telegram_message(url, matches, severity):
    emoji_map = {
        "HIGH": "🔥",
        "MEDIUM": "⚠️",
        "LOW": "ℹ️",
        "NONE": "✅"
    }

    emoji = emoji_map.get(severity, "❓")
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    matches_text = "\n".join([f"• `{m}`" for m in matches])

    message = f"""
🚨 *DARK WEB ALERT* 🚨

{emoji} *Severity:* `{severity}`

🔗 *Target URL:*
`{url}`

📌 *Matches detected ({len(matches)}):*
{matches_text}

🕒 *Timestamp:*
`{timestamp}`

🕵️ *Tool:*
*K4L1NUX DarkWeb Monitor*
"""
    return message.strip()


def send_telegram_alert(message, config):
    try:
        telegram_cfg = config.get("telegram", {})

        token = telegram_cfg.get("token")
        chat_id = telegram_cfg.get("chat_id")

        if not token or not chat_id:
            logger.error("Telegram bot_token o chat_id no configurado")
            return

        url = f"https://api.telegram.org/bot{token}/sendMessage"

        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }

        response = requests.post(
            url,
            json=payload,
            timeout=15,
            proxies={"http": None, "https": None}
        )

        response.raise_for_status()
        logger.info("Alerta enviada por Telegram")

    except Exception as e:
        logger.error(f"Error enviando alerta Telegram: {e}")
