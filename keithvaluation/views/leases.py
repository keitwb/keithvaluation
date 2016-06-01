from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from keithvaluation.models import HuntingLease


class HuntingLeases(ListView):
    page_title = 'Hunting Leases'
    template_name = 'list-pages/hunting-leases.html'
    model = HuntingLease


class HuntingLeaseDetail(DetailView):
    template_name = 'hunting-lease-detail.html'
    model = HuntingLease

    @property
    def page_title(self):
        return self.object.property_name

