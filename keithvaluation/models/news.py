from django.db import models


class NewsItem(models.Model):
    class Meta:
        ordering = ['-date']

    title = models.CharField(max_length=128)
    content = models.TextField()
    date = models.DateField()
