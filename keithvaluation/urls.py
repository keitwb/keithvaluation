from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

from keithvaluation import views

from .decorators import cache_page
from .sitemap import KVSitemap

cacher = cache_page(60 * 60 * 2)

pages = [
    {"template": "aboutus.html", "name": "aboutus", "title": "About Us"},
    {"template": "become-appraiser.html", "name": "become-appraiser", "title": "How to Become an Appraiser"},
    {"template": "bv-services.html", "name": "bv-services", "title": "Business Valuation Services"},
    {"template": "contact.html", "name": "contact", "title": "Contact Us"},
    {"template": "employment.html", "name": "employment", "title": "Employment Information"},
    {"template": "re-services.html", "name": "re-services", "title": "Real Estate Services"},
    {"template": "salary.html", "name": "salary", "title": "Salary Information"},
    {"template": "why-bv.html", "name": "why-bv", "title": "Why Business Valuation?"},
    {"template": "resmenu.html", "name": "resmenu", "title": "Research Menu"},
]


urlpatterns = [
    re_path(r"^$", cacher(TemplateView.as_view(template_name="index.html")), name="home"),
    re_path(r"^news/$", cacher(views.CompanyNewsView.as_view()), name="news"),
    re_path(r"^staff/$", cacher(views.StaffView.as_view()), name="staff"),
    re_path(r"^links/$", cacher(views.ExternalLinksView.as_view()), name="links"),
    re_path(r"^re-research/$", cacher(views.RealEstateResearchView.as_view()), name="re-research"),
    re_path(r"^bv-research/$", cacher(views.BusinessValuationResearchView.as_view()), name="bv-research"),
    re_path(r"^court-cases/$", cacher(views.CourtCasesView.as_view()), name="court-cases"),
    re_path(r"^economic-trends/$", cacher(views.EconomicTrendsView.as_view()), name="economic-trends"),
    re_path(r"^newsletters/$", cacher(views.NewslettersView.as_view()), name="newsletters"),
    re_path(r"^whitepapers/$", cacher(views.WhitePapersView.as_view()), name="whitepapers"),
    re_path(r"^expert-testimony/$", cacher(views.TestimonyView.as_view()), name="expert-testimony"),
    re_path(r"^business-listings/$", cacher(views.BusinessListings.as_view()), name="business-listings"),
    re_path(
        r"^business-listing/(?P<slug>[-\w]+)/$",
        cacher(views.BusinessListingDetail.as_view()),
        name="business-listing-detail",
    ),
    re_path(r"^hunting-land/$", cacher(views.HuntingLand.as_view()), name="hunting-land"),
    re_path(
        r"^hunting-land/(?P<slug>[-\w]+)/$",
        cacher(views.HuntingLandDetail.as_view()),
        name="hunting-land-detail",
    ),
    re_path(r"^property-listings/$", cacher(views.PropertyListings.as_view()), name="property-listings"),
    re_path(
        r"^property-listings/(?P<slug>[-\w]+)/$",
        cacher(views.PropertyListingDetail.as_view()),
        name="property-listing-detail",
    ),
    re_path(
        r"^sitemap\.xml$",
        sitemap,
        {"sitemaps": {"static": KVSitemap()}},
        name="django.contrib.sitemaps.views.sitemap",
    ),
] + static('content/media/', document_root=settings.MEDIA_ROOT) \
  + static('content/static/', document_root=settings.STATIC_ROOT)

urlpatterns += [
    re_path(
        r"^%s/$" % (p["name"],),
        cacher(views.KVView.as_view(template_name=p["template"], page_title=p["title"])),
        name=p["name"],
    )
    for p in pages
]

