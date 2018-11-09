from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from keithvaluation.models import Property


class HuntingLand(ListView):
    page_title = "Hunting Land"
    template_name = "list-pages/hunting-land.html"
    model = Property
    queryset = Property.objects.filter(available_to_hunt=True)


class HuntingLandDetail(DetailView):
    template_name = "hunting-land-detail.html"
    model = Property

    @property
    def page_title(self):
        return self.object.property_name


class PropertyListings(ListView):
    page_title = "Property for Sale"
    template_name = "list-pages/property-listings.html"
    model = Property
    queryset = Property.objects.filter(Q(available_for_sale=True) | Q(available_for_lease=True))


class PropertyListingDetail(DetailView):
    template_name = "property-listing-detail.html"
    model = Property

    @property
    def page_title(self):
        return self.object.property_name
