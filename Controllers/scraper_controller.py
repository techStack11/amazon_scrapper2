import requests
import logging
from bs4 import BeautifulSoup # pyright: ignore[reportMissingModuleSource]
from Products.product import ScrapedProduct
from Helpers.utils import get_scrapeops_url


logger = logging.getLogger(__name__)

def search_products(product_name: str, page_number: int=1, location:str="in", retries: int=2, data_pipeline=None):
    scraped_products = []
    attempts = 0
    success = False

    while attempts < retries and not success and len(scraped_products) < 10:
        try: 
            search_url = get_scrapeops_url(f"https://www.amazon.in/s?k={product_name}&page={page_number}", location)
            logger.info(f"Fetching: {search_url}")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            }
            response = requests.get(search_url, headers=headers, timeout=10)

            if response.status_code != 200:
                raise Exception(f"Status code: {response.status_code}")
            
            logger.info("Successfully fetched page")
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Remove ads
            for ad_div in soup.find_all("div", class_="AdHolder"):
                ad_div.decompose()
            
            product_divs = soup.find_all("div", class_="s-result-item")
            for product_div in product_divs:
                if len(scraped_products) >= 10:
                    break
                    
                h2 = product_div.find("h2")
                if not h2 or not h2.text.strip():
                    continue
                    
                product_title = h2.text.strip()
               
                
                
                name = product_div.get("data-asin")
                if not name: 
                    continue
                product_url = f"https://www.amazon.in/dp/{name}"

                price_currency = product_div.find("span", class_="a-price-symbol")
                currency = price_currency.text if price_currency else ""
                
                # Skip if not Indian currency
                if currency != "₹":
                    continue
                
                prices = product_div.find_all("span", class_="a-offscreen")
                try: 
                    current_price = float(prices[0].text.replace(currency, "").replace(",","").strip()) if prices else 0.0
                except:
                    continue

                rating_tag = product_div.find("span", class_="a-icon-alt")
                try:
                    rating = float(rating_tag.text[0:3]) if rating_tag else 0.0
                except: 
                    rating = 0.0
                
                product = ScrapedProduct(
                    name=name, 
                    product_title=product_title,
                    product_url=product_url,
                    current_price=current_price,
                    currency=currency,
                    rating=rating
                )
                scraped_products.append(product)
                if data_pipeline:
                    data_pipeline.add_data(product)
            
            success = len(scraped_products) >= 10

        except Exception as e: 
            logger.warning(f"Attempt {attempts + 1} failed: {e}")
            attempts += 1
    
    if not success and len(scraped_products) < 10:
        logger.error("Failed to scrape at least 10 products")
    
    return scraped_products