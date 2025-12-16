import argparse
from core.scraper import Scraper
from utils.logger import logger

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

    keywords = load_keywords(args.keywords)
    scraper = Scraper(args.url)

    matches = scraper.run(keywords)
    logger.info(f"Coincidencias encontradas: {matches}")

if __name__ == "__main__":
    main()
