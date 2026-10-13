from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255, unique=True)
    summary = models.TextField()
    date = models.DateField()
    link = models.URLField()
    image_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50)
    country = models.CharField(max_length=50, blank=True, null=True)  # 🆕 New field

    def __str__(self):
        return self.title
