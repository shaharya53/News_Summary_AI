from django.shortcuts import render
from .models import NewsArticle
from .news_scraper import scrape_and_store_news

def news_list(request):
   # scrape_and_store_news()

    selected_category = request.GET.get("category", "")
    selected_country = request.GET.get("country", "")
    selected_date = request.GET.get("date", "")

    articles = NewsArticle.objects.all()

    if selected_category:
        articles = articles.filter(category=selected_category)

    if selected_country and selected_country != "None":
        articles = articles.filter(country=selected_country)

    if selected_date:
        articles = articles.filter(date=selected_date)

    articles = articles.order_by('-date')
    categories = NewsArticle.objects.values_list("category", flat=True).distinct()
    countries = NewsArticle.objects.values_list("country", flat=True).distinct()
    dates = NewsArticle.objects.values_list("date", flat=True).distinct().order_by('-date')

    return render(request, "news_list.html", {
        "news": articles,
        "categories": categories,
        "countries": countries,
        "dates": dates,
        "selected_category": selected_category,
        "selected_country": selected_country,
        "selected_date": selected_date,
    })
