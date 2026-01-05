import requests
from bs4 import BeautifulSoup

class PriceTracker:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0"
            ),
            "Accept-Language": "en-US,en;q=0.9"
        }
        self.response = requests.get(self.url, headers=self.headers).text
        # Use built-in parser (no need for lxml installation)
        self.soup = BeautifulSoup(self.response, "html.parser")

    def product_title(self):
        title_tag = self.soup.find("span", attrs={"id": "productTitle"})
        return title_tag.get_text().strip() if title_tag else "Title not found"

    def product_price(self):
        # Amazon uses different IDs/classes for price depending on product type
        price_tag = (
            self.soup.find("span", attrs={"id": "priceblock_ourprice"}) or
            self.soup.find("span", attrs={"id": "priceblock_dealprice"}) or
            self.soup.find("span", attrs={"id": "priceblock_saleprice"}) or
            self.soup.find("span", attrs={"class": "a-price-whole"}) or
            self.soup.find("span", attrs={"class": "a-offscreen"})
        )
        return price_tag.get_text().strip() if price_tag else "Price not found"


# Example usage
if __name__ == "__main__":
    url = "https://www.amazon.in/Casio-Edifice-Bluetooth-Analog-Digital-ECB-2000NP-1ADF/dp/B0CZ7LHXLB/"
    device = PriceTracker(url)
    print("Product Title:", device.product_title())
    print("Product Price:", device.product_price())