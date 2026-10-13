import requests

from src.utils.logger import logger


def build_report_message(source, findings):
    lines = [
        "🚨 *K4L1NUX DarkWeb Alert* 🚨",
        "",
        f"🔗 *Fuente:* `{source}`",
        f"📌 *Hallazgos:* {len(findings)}",
        "",
    ]
    for f in findings:
        lines.append(f"• `[{f.severity}] {f.type}` `{f.value}`")
    lines += ["", "🕵️ *K4L1NUX DarkWeb Monitor*"]
    return "\n".join(lines)


def send_telegram_alert(message, config):
    telegram_cfg = config.get("telegram", {})
    token = telegram_cfg.get("token")
    chat_id = telegram_cfg.get("chat_id")

    if not token or not chat_id:
        logger.error("Telegram token o chat_id no configurado")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    # Sin parse_mode: el contenido deriva de fuentes no confiables (evita inyección Markdown)
    payload = {"chat_id": chat_id, "text": message}

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=15,
            proxies={"http": None, "https": None},
        )
        response.raise_for_status()
        logger.info("Alerta enviada por Telegram")
    except Exception as e:
        logger.error(f"Error enviando alerta Telegram: {e}")
