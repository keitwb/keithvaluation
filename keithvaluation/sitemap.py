from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class KVSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return [
            'home',
            'news',
            'staff',
            'links',
            're-research',
            'bv-research',
            'court-cases',
            'economic-trends',
            'newsletters',
            'whitepapers',
            'aboutus',
            'become-appraiser',
            'bv-services',
            'contact',
            'employment',
            're-services',
            'salary',
            'why-bv',
            'resmenu',
        ]

    def location(self, item):
        return reverse(item)
