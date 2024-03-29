from django.contrib.sites.models import Site
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save)
def clear_cache(sender, **kwargs):
    """
    Clear the memcached cache every time anything is updated in the database
    """
    cache.clear()
