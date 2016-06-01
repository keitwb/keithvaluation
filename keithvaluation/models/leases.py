from django.db import models


class County(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class HuntingLease(models.Model):
    property_name = models.CharField(max_length=256,
                                     help_text="A short name for the property")
    description = models.TextField(
        help_text="A longer description of the tract (e.g. types of game, land condition, etc.")

    acreage = models.DecimalField(decimal_places=1, max_digits=8)
    county = models.ForeignKey(County)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    leased_to = models.CharField(max_length=1024,
                                 help_text="Who the property is leased to",
                                 null=True, blank=True)
    scanned_lease = models.FileField(help_text="Scanned PDF of the lease",
                                     null=True, blank=True)
    lease_start_date = models.DateField(help_text="The start date of the lease", null=True, blank=True)
    lease_end_date = models.DateField(help_text="The end date of the lease",
                                      null=True, blank=True)

