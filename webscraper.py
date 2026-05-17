import requests
from bs4 import BeautifulSoup
import csv
import time
from requests.exceptions import RequestException

def scrape_books():
    # Base URL for 5 pages of books
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    total_pages = 5
    output_file = "scraped_books_full.csv"

    # CSV Headers
    headers = [
        "Book_ID",
        "Book_Title",
        "Price",
        "Availability",
        "Star_Rating",
        "Book_URL"
    ]

    # Write to CSV
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        book_id = 1

        # Loop through pages
        for page_num in range(1, total_pages + 1):
            url = base_url.format(page_num)
            print(f"\n======================================")
            print(f"Scraping Page {page_num} of {total_pages}")
            print(f"URL: {url}")
            print("======================================")

            try:
                response = requests.get(url, timeout=15)
                response.raise_for_status()

            except RequestException as e:
                print(f"❌ ERROR: Failed to load page {page_num}")
                print(f"Details: {str(e)}")
                continue

            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            books = soup.find_all('article', class_='product_pod')

            if not books:
                print("⚠️ No books found on this page.")
                continue

            # Extract each book
            for book in books:
                try:
                    # Title
                    title = book.h3.a['title'].strip()

                    # Price
                    price = book.find('p', class_='price_color').get_text(strip=True)

                    # Stock
                    stock = book.find('p', class_='instock availability').get_text(strip=True)

                    # Star rating
                    rating_class = book.find('p', class_='star-rating')['class']
                    rating = rating_class[1] if len(rating_class) > 1 else "Zero"

                    # Book link
                    book_url = "https://books.toscrape.com/catalogue/" + book.h3.a['href']

                    # Write row
                    writer.writerow({
                        "Book_ID": book_id,
                        "Book_Title": title,
                        "Price": price,
                        "Availability": stock,
                        "Star_Rating": rating,
                        "Book_URL": book_url
                    })

                    print(f"✅ Book {book_id}: {title[:40]}...")
                    book_id += 1

                except Exception as e:
                    print(f"⚠️ Skipped a book (error: {str(e)})")
                    continue

            time.sleep(2)  # Respect server

    print("\n🎉 SCRAPING COMPLETED SUCCESSFULLY!")
    print(f"📄 Data saved to: {output_file}")
    print(f"📚 Total books scraped: {book_id - 1}")

if __name__ == "__main__":
    print("======================================")
    print("  ADVANCED WEB SCRAPER ")
    print("======================================")
    scrape_books()
