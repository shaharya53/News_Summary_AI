# 📰 News Summary AI

A Django-based project that automatically collects, summarizes, and categorizes the latest news articles.  
The system uses web scraping (RSS feeds) and AI-based classification to deliver organized and easy-to-read news.

---

## 📌 Problem Statement
People today consume news from multiple sources, which makes it time-consuming and overwhelming.  
Our project solves this problem by automatically fetching news, summarizing it, and classifying it into categories like Politics, Technology, Health, Sports, etc.

---

## 🎯 Objectives
- Collect live news articles automatically.
- Summarize long articles into short and readable text.
- Categorize news using AI for better organization.
- Provide a simple web interface and API to access the news.

---

## ⚙️ Tech Stack
- **Backend**: Django, Django REST Framework  
- **Database**: PostgreSQL / SQLite  
- **Scraping**: Feedparser (RSS parsing)  
- **AI Tools**: Gemini API (categorization)  
- **Frontend**: HTML, CSS, Bootstrap  
- **Others**: Celery / Cron jobs (for scheduling news updates)

---

## 🚀 Key Features
- Automatic news fetching from RSS feeds.  
- AI-powered summarization of articles.  
- Categorization into Politics, Technology, Sports, Health, etc.  
- REST API for accessing summarized news.  
- User-friendly interface with search and filter options.  

---

## 🔄 Example Flow
1. System fetches latest news from RSS feeds.  
2. Each news article is summarized into a short version.  
3. AI assigns a category to the article.  
4. News is stored in the database.  
5. Users can view, search, and filter news through the web app or API.  

---

## 🔮 Future Scope
- Add support for regional/local language news.  
- Implement personalized recommendations for users.  
- Add sentiment analysis for each news article.  
- Mobile app integration.  
- Advanced analytics dashboard for trending topics.  

---

## 📂 Project Structure
