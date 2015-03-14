
from django.db import models


class ExternalLink(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    url = models.URLField()
