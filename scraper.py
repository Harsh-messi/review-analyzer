import requests
from bs4 import BeautifulSoup

def scrape_reviews(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        reviews = []

        # Flipkart review block
        for review in soup.find_all("div", {"class": "_16PBlm"}):
            text = review.get_text(strip=True)
            if text:
                reviews.append(text)

        if not reviews:
            print("⚠️ No reviews found. Try another URL.")
        
        return reviews

    except Exception as e:
        print("❌ Scraping error:", e)
        return []