from django.conf.urls import patterns, include, url
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

from keithvaluation import views


pages = [
    { "template": "aboutus.html", "name": "aboutus", "title": "About Us", },
    { "template": "become-appraiser.html", "name": "become-appraiser", "title": "How to Become an Appraiser", },
    { "template": "bv-services.html", "name": "bv-services", "title": "Business Valuation Services", },
    { "template": "contact.html", "name": "contact", "title": "Contact Us", },
    { "template": "employment.html", "name": "employment", "title": "Employment Information", },
    { "template": "re-services.html", "name": "re-services", "title": "Real Estate Services", },
    { "template": "salary.html", "name": "salary", "title": "Salary Information", },
    { "template": "why-bv.html", "name": "why-bv", "title": "Why Business Valuation?", },
    { "template": "resmenu.html", "name": "resmenu", "title": "Research Menu", },
]


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    #(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        #name='django.contrib.sitemaps.views.sitemap'),

    url(r'^news/$', views.CompanyNewsView.as_view(), name='news'),
    url(r'^staff/$', views.StaffView.as_view(), name='staff'),
    url(r'^links/$', views.ExternalLinksView.as_view(), name='links'),
    url(r'^re-research/$', views.RealEstateResearchView.as_view(), name='re-research'),
    url(r'^bv-research/$', views.BusinessValuationResearchView.as_view(), name='bv-research'),
    url(r'^court-cases/$', views.CourtCasesView.as_view(), name='court-cases'),
    url(r'^economic-trends/$', views.EconomicTrendsView.as_view(), name='economic-trends'),
    url(r'^newsletters/$', views.NewslettersView.as_view(), name='newsletters'),
    url(r'^whitepapers/$', views.WhitePapersView.as_view(), name='whitepapers'),
)

static_patterns = [ url(r"^%s/$" % (p['name'],),
                        views.KVView.as_view(template_name=p['template'], page_title=p['title']),
                        name=p['name'])
                    for p in pages ]

urlpatterns += patterns('', *static_patterns)
