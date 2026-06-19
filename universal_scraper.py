"""
╔══════════════════════════════════════════════════════╗
║   UNIVERSAL WEB SCRAPER — CodeAlpha (Advanced)        ║
║   Task 3 (Advanced) | Python Programming             ║
╚══════════════════════════════════════════════════════╝

This advanced scraper handles:
  ✅ Regular HTML websites
  ✅ JavaScript-rendered sites (using Selenium)
  ✅ Sites with CORS blocking
  ✅ Anti-scraping protection
  ✅ Multiple fallback methods for reliability

Requirements:
  pip install requests selenium beautifulsoup4

For Chrome/Firefox users, download corresponding WebDriver:
  - Chrome: https://chromedriver.chromium.org/
  - Firefox: https://github.com/mozilla/geckodriver/releases
"""

import requests
from datetime import datetime
import re
import time


class UniversalScraper:
    """A robust web scraper with multiple fallback methods."""

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.google.com/",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        self.timeout = 10
        self.max_retries = 3

    def validate_url(self, url_string):
        """Ensure the URL has a valid protocol."""
        url = url_string.strip()
        if not url.lower().startswith(("http://", "https://")):
            url = "https://" + url
        return url

    def method_1_basic_requests(self, url):
        """Try basic requests with good headers."""
        try:
            print("  [Method 1] Trying basic HTTP request...")
            response = requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout,
                allow_redirects=True
            )
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"  ✗ Method 1 failed: {str(e)[:60]}")
            return None

    def method_2_with_session(self, url):
        """Try with session to maintain cookies."""
        try:
            print("  [Method 2] Trying with session (cookies)...")
            session = requests.Session()
            session.headers.update(self.headers)
            response = session.get(url, timeout=self.timeout, allow_redirects=True)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"  ✗ Method 2 failed: {str(e)[:60]}")
            return None

    def method_3_retry_with_delay(self, url):
        """Retry multiple times with delays (for rate-limited sites)."""
        try:
            print("  [Method 3] Trying with retries and delays...")
            for attempt in range(self.max_retries):
                try:
                    response = requests.get(
                        url,
                        headers=self.headers,
                        timeout=self.timeout,
                        allow_redirects=True
                    )
                    response.raise_for_status()
                    return response.text
                except requests.exceptions.Timeout:
                    wait = 2 ** attempt  # Exponential backoff
                    print(f"    Attempt {attempt + 1} failed, retrying in {wait}s...")
                    time.sleep(wait)
            return None
        except Exception as e:
            print(f"  ✗ Method 3 failed: {str(e)[:60]}")
            return None

    def method_4_selenium(self, url):
        """Use Selenium for JavaScript-rendered sites (requires webdriver)."""
        try:
            print("  [Method 4] Trying Selenium (JavaScript rendering)...")
            from selenium import webdriver
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC

            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            driver = webdriver.Chrome(options=options)
            driver.get(url)

            # Wait for page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "body"))
            )

            html = driver.page_source
            driver.quit()
            return html
        except ImportError:
            print("  ⚠ Selenium not installed. Skipping Method 4.")
            print("     Install with: pip install selenium")
            return None
        except Exception as e:
            print(f"  ✗ Method 4 failed: {str(e)[:60]}")
            return None

    def extract_title(self, html_content):
        """Extract title from HTML content."""
        if not html_content:
            return "[Failed to fetch page]"

        # Try multiple patterns
        patterns = [
            r"<title>(.+?)</title>",
            r'<meta\s+property="og:title"\s+content="([^"]+)"',
            r'<meta\s+name="title"\s+content="([^"]+)"',
            r'<h1>(.+?)</h1>',
        ]

        for pattern in patterns:
            match = re.search(pattern, html_content, re.IGNORECASE)
            if match:
                title = match.group(1).strip()
                if title:
                    return title

        return "[No title found]"

    def scrape(self, url):
        """Main scraping method with fallback chain."""
        url = self.validate_url(url)
        print(f"\n  Scraping: {url}")
        print("  " + "=" * 50)

        # Try multiple methods in order
        methods = [
            self.method_1_basic_requests,
            self.method_2_with_session,
            self.method_3_retry_with_delay,
            self.method_4_selenium,
        ]

        for method in methods:
            html = method(url)
            if html:
                print(f"  ✅ Success! Page fetched.")
                title = self.extract_title(html)
                return title

        return "[All methods failed - website may be blocking scraping]"


def save_results(url, title, filename="scraped_titles.txt"):
    """Save the URL and scraped title to a text file."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"URL: {url}\n")
        f.write(f"Title: {title}\n")
        f.write("-" * 50 + "\n\n")
    return filename


def main():
    print("\n" + "=" * 55)
    print("   UNIVERSAL WEB SCRAPER (Advanced) — CodeAlpha")
    print("=" * 55)
    print("  Scrapes ANY website with intelligent fallbacks.\n")

    scraper = UniversalScraper()

    while True:
        url_input = input("  Enter a webpage URL (or 'exit' to quit): ").strip()

        if url_input.lower() == "exit":
            print("\n  Goodbye!\n")
            break

        if not url_input:
            print("  ⚠  Please enter a valid URL.\n")
            continue

        title = scraper.scrape(url_input)
        print(f"  Title: {title}\n")

        # Save results
        save_results(url_input, title)
        print(f"  📄  Result saved to 'scraped_titles.txt'\n")


if __name__ == "__main__":
    main()
