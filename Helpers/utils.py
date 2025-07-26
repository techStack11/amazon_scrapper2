from Helpers.config import API_KEY
from urllib.parse import urlencode
import logging

logger = logging.getLogger(__name__)

def get_scrapeops_url(url, location):
    if not API_KEY or not API_KEY.strip():
        raise ValueError("API KEY is missing from environment")
    
    payload = {
        "api_key": API_KEY.strip(),
        "url": url,
        "country": location
    }
    final_url = "https://proxy.scrapeops.io/v1/?" + urlencode(payload, safe="")
    logger.info(f"ScrapeOps URL: {final_url}")
    return final_url
