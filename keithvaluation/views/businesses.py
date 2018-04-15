from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from keithvaluation.models import BusinessListing


class BusinessListings(ListView):
    page_title = 'Businesses for Sale'
    template_name = 'list-pages/business-listings.html'
    model = BusinessListing


class BusinessListingDetail(DetailView):
    template_name = 'business-listing.html'
    model = BusinessListing

    @property
    def page_title(self):
        return self.object.business_name

