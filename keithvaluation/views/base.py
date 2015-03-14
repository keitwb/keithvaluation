from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from keithvaluation import models


class KVView(TemplateView):
    page_title = None


class CompanyNewsView(ListView):
    page_title = 'Company News'
    template_name = 'news.html'
    model = models.NewsItem
