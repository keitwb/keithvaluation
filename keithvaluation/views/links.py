from django.views.generic.list import ListView

from keithvaluation.models import ExternalLink

class ExternalLinksView(ListView):
    page_title = 'Links'
    template_name = 'list-pages/external-links.html'
    model = ExternalLink


