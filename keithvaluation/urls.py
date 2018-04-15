from django.conf.urls import patterns, include, url
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

from keithvaluation import views

from .decorators import cache_page
from .sitemap import KVSitemap

cacher = cache_page(60*60*2)

pages = [
    { "template": "aboutus.html", "name": "aboutus", "title": "About Us", },
    { "template": "become-appraiser.html", "name": "become-appraiser", "title": "How to Become an Appraiser", },
    { "template": "bv-services.html", "name": "bv-services", "title": "Business Valuation Services", },
    { "template": "contact.html", "name": "contact", "title": "Contact Us", },
    { "template": "employment.html", "name": "employment", "title": "Employment Information", },
    { "template": "expert-testimony.html", "name": "expert-testimony", "title": "Expert Testimony", },
    { "template": "re-services.html", "name": "re-services", "title": "Real Estate Services", },
    { "template": "salary.html", "name": "salary", "title": "Salary Information", },
    { "template": "why-bv.html", "name": "why-bv", "title": "Why Business Valuation?", },
    { "template": "resmenu.html", "name": "resmenu", "title": "Research Menu", },
]


urlpatterns = patterns('',
    url(r'^$', cacher(TemplateView.as_view(template_name='index.html')), name='home'),
    url(r'^news/$', cacher(views.CompanyNewsView.as_view()), name='news'),
    url(r'^staff/$', cacher(views.StaffView.as_view()), name='staff'),
    url(r'^links/$', cacher(views.ExternalLinksView.as_view()), name='links'),
    url(r'^re-research/$', cacher(views.RealEstateResearchView.as_view()), name='re-research'),
    url(r'^bv-research/$', cacher(views.BusinessValuationResearchView.as_view()), name='bv-research'),
    url(r'^court-cases/$', cacher(views.CourtCasesView.as_view()), name='court-cases'),
    url(r'^economic-trends/$', cacher(views.EconomicTrendsView.as_view()), name='economic-trends'),
    url(r'^newsletters/$', cacher(views.NewslettersView.as_view()), name='newsletters'),
    url(r'^whitepapers/$', cacher(views.WhitePapersView.as_view()), name='whitepapers'),
    url(r'^business-listings/$', cacher(views.BusinessListings.as_view()), name='business-listings'),
    url(r'^business-listing/(?P<slug>[-\w]+)/$', cacher(views.BusinessListingDetail.as_view()), name='business-listing-detail'),
    url(r'^hunting-land/$', cacher(views.HuntingLand.as_view()), name='hunting-land'),
    url(r'^hunting-land/(?P<slug>[-\w]+)/$', cacher(views.HuntingLandDetail.as_view()), name='hunting-land-detail'),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'static': KVSitemap()}},
        name='django.contrib.sitemaps.views.sitemap'),
)

static_patterns = [ url(r"^%s/$" % (p['name'],),
                        cacher(views.KVView.as_view(template_name=p['template'], page_title=p['title'])),
                        name=p['name'])
                    for p in pages ]

urlpatterns += patterns('', *static_patterns)
