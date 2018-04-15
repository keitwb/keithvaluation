from django.db import models


def flier_path(instance, filename):
    return 'business-fliers/%s' % (filename)


class BusinessListing(models.Model):
    class Meta:
        ordering = ['-updated_date']

    business_name = models.CharField(max_length=512)
    slug = models.SlugField()
    subtitle = models.CharField(max_length=1024)
    description = models.TextField()
    flier = models.FileField(upload_to=flier_path)
    updated_date = models.DateField(auto_now=True)
