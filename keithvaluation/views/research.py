from django.views.generic.list import ListView

from keithvaluation import models


class RealEstateResearchView(ListView):
    page_title = 'Real Estate Research'
    template_name = 'list-pages/real-estate.html'
    model = models.REResearch


class BusinessValuationResearchView(ListView):
    page_title = 'Business Valuation Research'
    template_name = 'list-pages/business-valuation.html'
    model = models.BVResearch


class CourtCasesView(ListView):
    page_title = 'Court Cases'
    template_name = 'list-pages/court-cases.html'
    model = models.CourtCase


class EconomicTrendsView(ListView):
    page_title = 'Economic Trends'
    template_name = 'list-pages/economic-trends.html'
    model = models.EconomicTrend


class NewslettersView(ListView):
    page_title = 'Newsletters'
    template_name = 'list-pages/newsletters.html'
    model = models.Newsletter


class ExpertTestimonyView(ListView):
    page_title = 'Expert Testimony'
    template_name = 'list-pages/expert-testimony.html'
    model = models.ExpertTestimony


class WhitePapersView(ListView):
    page_title = 'White Papers'
    template_name = 'list-pages/white-papers.html'
    model = models.WhitePaper
