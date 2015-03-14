from django.contrib.sitemaps import Sitemap
from keithvaluation.models import Entry

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['main', 'about', 'license']

    def location(self, item):
        return reverse(item)
