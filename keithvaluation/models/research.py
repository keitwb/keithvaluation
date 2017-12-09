from datetime import date
from django.db import models


def document_path(instance, filename):
    return '%s/%s' % (instance.RESEARCH_TYPE, filename)


class ResearchModel(models.Model):
    class Meta:
        abstract = True
        ordering = ['-updated_date']

    RESEARCH_TYPE = None

    title = models.CharField(max_length=512)
    description = models.TextField()
    document = models.FileField(upload_to=document_path)
    updated_date = models.DateField(auto_now=True)


class BVResearch(ResearchModel):
    class Meta(ResearchModel.Meta):
        verbose_name_plural = 'Business Valuation Research'

    RESEARCH_TYPE = 'bv-research'


class REResearch(ResearchModel):
    class Meta:
        ordering = ['subtype', '-updated_date']
        verbose_name_plural = 'Real Estate Research'

    RESEARCH_TYPE = 're-research'

    SUBTYPE_CHOICES = tuple([ (c, c) for c in [
        'Agricultural Properties',
        'Apartment',
        'Commercial',
        'Damage Studies',
        'Industrial',
        'Land Development',
        'Residential',
    ]])

    subtype = models.CharField(max_length=128, choices=SUBTYPE_CHOICES)


class EconomicTrend(ResearchModel):
    RESEARCH_TYPE = 'economic-trends'


class CourtCase(ResearchModel):
    RESEARCH_TYPE = 'courtcases'


class Newsletter(ResearchModel):
    RESEARCH_TYPE = 'newsletters'


class ExpertTestimony(ResearchModel):
    class Meta:
        verbose_name_plural = "expert testimonies"

    RESEARCH_TYPE = 'expert-tesimony'


class WhitePaper(ResearchModel):
    RESEARCH_TYPE = 'whitepapers'
