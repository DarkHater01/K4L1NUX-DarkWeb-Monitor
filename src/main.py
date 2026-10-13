import argparse
import json
from dataclasses import asdict
from pathlib import Path
from urllib.parse import urlparse

from src.core.scraper import Scraper
from src.core.alerts import build_report_message, send_telegram_alert
from src.modules.leak_detector import scan_text, MAX_SCAN_CHARS
from src.utils.config_loader import load_config
from src.utils.logger import logger

SAMPLE_PATH = Path(__file__).resolve().parent.parent / "examples" / "sample_leak.txt"


def load_keywords(path):
    p = Path(path)
    if not p.exists():
        return []
    lines = p.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip()]


def read_capped(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read(MAX_SCAN_CHARS)


def validate_url(url):
    parsed = urlparse(url)
    host = parsed.hostname or ""
    if parsed.scheme not in ("http", "https") or not host.endswith(".onion"):
        raise SystemExit(f"URL inválida: se espera http(s)://*.onion (recibido: {url})")


def gather_text(args):
    if args.test:
        return read_capped(SAMPLE_PATH)
    if args.file:
        return read_capped(args.file)
    validate_url(args.url)
    return Scraper(args.url).fetch()


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="K4L1NUX Dark Web Monitor (defensivo)"
    )
    parser.add_argument("--keywords", default="config/keywords.txt")
    parser.add_argument("--json", action="store_true", help="salida en JSON")
    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument(
        "--test", action="store_true",
        help="escanea el ejemplo sintético incluido (no requiere Tor)",
    )
    source_group.add_argument("--file", help="escanea un fichero de texto local")
    source_group.add_argument("--url", help="escanea una URL .onion vía Tor")

    args = parser.parse_args(argv)

    keywords = load_keywords(args.keywords)
    source = "examples/sample_leak.txt" if args.test else (args.file or args.url)
    text = gather_text(args)
    findings = scan_text(text, keywords)

    if args.json:
        print(json.dumps([asdict(f) for f in findings], indent=2, ensure_ascii=False))
    elif not findings:
        logger.info(f"Sin hallazgos en {source}")
    else:
        logger.info(f"{len(findings)} hallazgo(s) en {source}")
        for f in findings:
            logger.info(f"[{f.severity}] {f.type} {f.value}  fp={f.fingerprint[:12]}")

    config = load_config()
    if findings and config.get("telegram", {}).get("enabled"):
        send_telegram_alert(build_report_message(source, findings), config)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
