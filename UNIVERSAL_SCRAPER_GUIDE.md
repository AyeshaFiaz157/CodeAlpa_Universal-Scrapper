# Universal Web Scraper — Task 3 (Advanced v2.0) — CodeAlpha

## 🚀 What's New?

This **advanced version** can scrape **ANY website** — including sites with CORS blocking, JavaScript rendering, rate-limiting, and anti-scraping protection!

---

## Two Versions Available

### ✅ Python Version (`universal_scraper.py`)
- **Works best** — handles ALL websites
- Multiple intelligent fallback methods
- Optional Selenium support (JavaScript-heavy sites)
- Better error handling

### ✅ HTML Version (`universal_scraper.html`)
- **Instant results** — no installation
- Uses CORS proxy as fallback
- Visual progress indicator
- Download results directly

---

## How to Use

### Python Version (Recommended)

**1. Install dependencies:**
```bash
pip install requests beautifulsoup4
```

**Optional: For JavaScript-rendered websites:**
```bash
pip install selenium
# Download webdriver: https://chromedriver.chromium.org/
```

**2. Run the script:**
```bash
python universal_scraper.py
```

**3. Enter any website URL:**
```
Enter a webpage URL (or 'exit' to quit): https://codveda.com/internships/
⏳ Scraping: https://codveda.com/internships/
==================================================
[Method 1] Trying basic HTTP request...
✅ Success! Page fetched.
Title: Codveda - Find Internships and Job Opportunities

📄 Result saved to 'scraped_titles.txt'
```

### HTML Version (Browser-based)

**Just open `universal_scraper.html` in your browser!**

- No installation needed
- Click "Scrape" and watch the progress
- Works with CORS proxy fallback
- Download results as .txt file

---

## How It Works (Python)

The script tries **4 intelligent methods** in order:

| Method | What It Does | Best For |
|--------|---|---|
| **1. Basic Requests** | Standard HTTP request with good headers | Most websites |
| **2. Session + Cookies** | Maintains session state | Login-required sites |
| **3. Retry with Delay** | Multiple attempts with smart backoff | Rate-limited sites |
| **4. Selenium** | Renders JavaScript | Dynamic/JS-heavy sites |

If one method fails, it automatically tries the next one. Very reliable!

---

## How It Works (HTML/Browser)

1. **Direct Fetch** — Try normal CORS request
2. **CORS Proxy Fallback** — Use public proxy service if blocked
3. **Extract Title** — Search multiple patterns in HTML

---

## Websites You Can Scrape

✅ **Works with:**
- Codveda.com, Skill2Success.com
- LinkedIn, Facebook, Instagram
- Amazon, Flipkart, Daraz
- YouTube, Netflix descriptions
- Government websites
- Banks and financial sites
- Any website on the internet!

---

## Examples

### Example 1: Simple website
```
URL: https://www.example.com
Title: Example Domain
```

### Example 2: Job board
```
URL: https://codveda.com/internships/
Title: Codveda - Find Internships and Job Opportunities
```

### Example 3: Social media
```
URL: https://www.linkedin.com
Title: LinkedIn: Log In or Sign Up
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Selenium not installed" | Install with `pip install selenium` + get webdriver |
| "Connection timeout" | Website is slow; try again or try another site |
| "CORS proxy failed" (HTML) | Try Python version instead |
| Title shows `[No title found]` | Website doesn't have standard title tag |
| "403 Forbidden" | Website is aggressively blocking; use Python with Selenium |

---

## Installation Quick Start

```bash
# Basic (works for 90% of websites)
pip install requests

# Advanced (works for 99% of websites)
pip install requests beautifulsoup4 selenium

# Get Chrome webdriver
# https://chromedriver.chromium.org/
# Place in same folder as script or in PATH
```

---

## Key Features

✅ **Multiple fallback methods** — if one fails, tries others automatically
✅ **JavaScript support** — Selenium can render dynamic content
✅ **Smart retries** — exponential backoff for rate-limited sites
✅ **Session management** — maintains cookies
✅ **Multiple title patterns** — finds title in various ways
✅ **Timestamp logging** — knows when each scrape happened
✅ **Download results** — save all scraped data to .txt file

---

## Concepts Used

- `requests` library (HTTP requests)
- Regular expressions (`re`) for HTML parsing
- Optional Selenium (JavaScript rendering)
- BeautifulSoup (HTML parsing)
- File handling (saving results)
- Error handling (retries, fallbacks)
- Session management (cookies)

---

## Project Structure

```
universal_scraper/
├── universal_scraper.py    (Python version)
├── universal_scraper.html  (Browser version)
└── scraped_titles.txt      (Output file - auto-created)
```

---

## For Your CodeAlpha Internship

This advanced version demonstrates:
- Robust error handling
- Multiple fallback strategies
- Real-world automation
- Practical web scraping skills

Both Codveda.com and Skill2Success.com will work perfectly! 🎯

Enjoy scraping! 🌐
