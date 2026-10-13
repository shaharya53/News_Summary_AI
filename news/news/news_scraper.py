import requests
from bs4 import BeautifulSoup
from datetime import datetime
import google.generativeai as genai
from .models import NewsArticle

# ✅ Configure Gemini API
genai.configure(api_key="AIzaSyBGzyMHC7icw46gIuMwdokmGDCwuu8ddRQ")
model = genai.GenerativeModel("gemini-1.5-flash")

def get_news_category(summary):
    prompt = f"""Read this news summary and give a one-word category from:
    ['Politics', 'Technology', 'Health', 'Sports', 'Business', 'Entertainment', 'World', 'Other'].
    Summary: {summary}"""
    try:
        response = model.generate_content(prompt)
        category = response.text.strip().split("\n")[0]
        return category
    except Exception as e:
        print(f"Error categorizing: {e}")
        return "Unknown"

# 🆕 NEW function for detecting country
def get_news_country(summary):
    prompt = f"""Read this news summary and predict the most likely country it is related to.
    If not clear, return 'International'. Only return one country name.
    Summary: {summary}"""
    try:
        response = model.generate_content(prompt)
        country = response.text.strip().split("\n")[0]
        return country
    except Exception as e:
        print(f"Error detecting country: {e}")
        return "International"

def parse_date(date_str):
    """
    Parses the date string from Times of India into a Python date object.
    Falls back to today's date if parsing fails.
    """
    try:
        # Example format: 'Aug 12, 2025, 10:30 IST'
        date_only = date_str.split(",")[0]  # 'Aug 12'
        
        if str(datetime.today().year) not in date_str:
            date_only += f" {datetime.today().year}"
        return datetime.strptime(date_only.strip(), "%b %d %Y").date()
    except Exception as e:
        print(f"Date parsing error: {e} — using today's date")
        return datetime.today().date()

def scrape_and_store_news():
    url = "https://timesofindia.indiatimes.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    box = soup.find('div', class_='grid_wrapper')
    if not box:
        print("No news container found")
        return

    links = [a.get('href') for a in box.find_all('a') if a.get('href')]

    for link in links:
        try:
            if NewsArticle.objects.filter(link=link).exists():
                continue

            article_res = requests.get(link)
            article_soup = BeautifulSoup(article_res.content, 'html.parser')

            title_tag = article_soup.find('h1')
            title = title_tag.text.strip() if title_tag else None
            if not title or NewsArticle.objects.filter(title=title).exists():
                continue

            image_tag = article_soup.find('div', class_="vdo_embedd")
            img_src = None
            if image_tag:
                img = image_tag.find('img')
                if img:
                    img_src = img.get('src')

            date_tag = article_soup.find("div", class_="byline")
            if date_tag:
                dat = date_tag.find('span')
                date_obj = parse_date(dat.text) if dat else datetime.today().date()
            else:
                date_obj = datetime.today().date()

            summary_tag = article_soup.find('div', class_='art_synopsis')
            summary = summary_tag.get_text(strip=True) if summary_tag else None

            if not summary:
                continue

            # Get AI category
            category = get_news_category(summary)

            # Skip if category is Unknown or Other
            if category.lower() in ["unknown", "other"]:
                continue

            # 🆕 Get AI country
            country = get_news_country(summary)

            # Save news
            NewsArticle.objects.create(
                title=title,
                summary=summary,
                date=date_obj,
                link=link,
                image_url=img_src,
                category=category,
                country=country  # 🆕 added
            )

        except Exception as e:
            print(f"Error processing link {link}: {e}")
