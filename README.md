<!-- README.md for amazon_scrapper2 -->

# 🛍️ Amazon Scraper 2 — Local Web Application 💻

[![Run with Streamlit](https://static.streamlit.io/badges/ai.svg)](https://streamlit.io)  
_Built with a modern Python stack to scrape Amazon product data with built‑in proxy handling & AI enrichment._

---

## 🚀 What It Does

- Scrapes Amazon product pages via Search or ASIN input  
- Uses **ScrapeOps Proxy** (automatic proxy rotation + server logs) to avoid blocks  
- Sends data to **Groq API** for richer AI-powered post‑processing  
- Presents results instantly with **Streamlit** in an interactive UI  
- Logs operations, stores records in **pandas** DataFrames  
- Custom‑built parsers powered by **BeautifulSoup** + **requests**

---

## 🧰 Tech Stack

| Logo | Library / Tool | Version | Why It’s Used |
|------|----------------|---------|----------------|
| <img src="https://www.crummy.com/software/BeautifulSoup/bs4/doc/logo.svg" alt="BeautifulSoup" height="30" /> | **BeautifulSoup** | 4.x | HTML parsing & DOM traversal |
| <img src="https://requests.readthedocs.io/en/latest/_static/requests-blue.svg" alt="requests" height="30" /> | **requests** | 2.x | HTTP client (with `User-Agent`, timeouts, etc.) |
| <img src="https://pandas.pydata.org/static/img/pandas_white.svg" alt="pandas" height="30" /> | **pandas** | 2.x | Tabular data storage & export (CSV/JSON) |
| <img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" alt="Streamlit" height="30" /> | **Streamlit** | 1.x | Interactive local web UI |
| <img src="https://scrapeops.io/static/img/logo.svg" alt="ScrapeOps" height="30" /> | **ScrapeOps Proxy** | — | Avoid CAPTCHAs & IP rate limits |
| <img src="https://aicovery.com/groq-cloud-logo.png" alt="Groq API" height="30" /> | **Groq API** | Free Tier | Light LLM inference, partially OpenAI‑compatible |

> Logos are sourced from official or public assets; only minimal resizing applied.

---

## ⚙️ Setup Locally – in &lt; 5 minutes 📦

Follow these steps to spin it up on your machine:

```bash
git clone https://github.com/techStack11/amazon_scrapper2.git
cd amazon_scrapper2
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp example.env .env
