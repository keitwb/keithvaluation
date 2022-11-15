from django.db import models


class CondemnationCase(models.Model):
    class Meta:
        ordering = ['-date']

    owner = models.CharField(max_length=256)
    property_type = models.CharField(max_length=256)
    attorney = models.CharField(max_length=128)
    appraiser = models.CharField(max_length=128)
    condemnor_offer = models.PositiveIntegerField()
    appraisers_estimate = models.PositiveIntegerField()
    settlement = models.PositiveIntegerField()
    is_jury_trial = models.BooleanField(default=False)
    date = models.DateField()

    @property
    def gain_above_offer(self):
        return self.settlement - self.condemnor_offer

    @property
    def percent_increase_over_offer(self):
        return float(self.gain_above_offer / self.condemnor_offer) * 100

class JudicialHearing(models.Model):
    class Meta:
        ordering = ['-date']

    case_number = models.CharField(max_length=128)
    expert_witness = models.CharField(max_length=128)
    jurisdiction = models.CharField(max_length=256)
    appraiser_testimony = models.CharField(max_length=512)
    agreed = models.BooleanField(default=True)
    date = models.DateField()
