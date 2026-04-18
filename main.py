import time
import pandas as pd
from scraper import scrape_reviews
from utils import clean_text, chunk_text
from llm import analyze_review

def main():
    url = input("🔗 Enter product URL: ")

    print("\n📥 Scraping reviews...")
    reviews = scrape_reviews(url)

    if not reviews:
        print("No reviews found. Exiting.")
        return

    final_data = []

    print(f"\n🧠 Processing {len(reviews)} reviews with LLM...\n")

    for i, review in enumerate(reviews):
        cleaned = clean_text(review)

        # Handle long reviews
        chunks = chunk_text(cleaned)
        combined_analysis = ""

        for chunk in chunks:
            result = analyze_review(chunk)
            combined_analysis += result + " "

            time.sleep(1)  # avoid rate limits

        final_data.append({
            "review": cleaned,
            "analysis": combined_analysis.strip()
        })

        print(f"✅ Processed review {i+1}")

    df = pd.DataFrame(final_data)
    df.to_csv("reviews_output.csv", index=False)

    print("\n🎉 Done! Data saved to reviews_output.csv")

if __name__ == "__main__":
    main()