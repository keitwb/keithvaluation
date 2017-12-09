from django.db import models

class FeatureFlag(models.Model):
    name = models.CharField(max_length=512)
    enabled = models.BooleanField(default=False)

    @classmethod
    def has_flag(cls, name):
        return cls.objects.filter(name=name, enabled=True).count() > 0
