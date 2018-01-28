from datetime import date

from django.db import models


def image_path(instance, filename):
    return 'property-images/%s' % (filename)

class Property(models.Model):
    class Meta:
        verbose_name_plural = "properties"

    property_name = models.CharField(max_length=256,
                                     help_text="A short name for the property")
    slug = models.SlugField()
    description = models.TextField(
        help_text="A longer description of the property.")

    acreage = models.DecimalField(decimal_places=1, max_digits=8)
    county = models.CharField(max_length=256)
    state = models.CharField(max_length=256, choices=(("NC", "NC"),))

    available_to_hunt = models.BooleanField(default=False)
    available_for_lease = models.BooleanField(default=False)
    available_for_sale = models.BooleanField(default=False)
    available_date = models.DateField(null=True, blank=True, help_text="When the property will be available for lease")

    lease_rate = models.IntegerField(null=True, blank=True, help_text="Lease price in dollars")
    lease_rate_unit = models.CharField(choices=(('month', 'month'),
                                                ('year', 'year')),
                                       max_length=16,
                                       null=True, blank=True,
                                       help_text="Is the least rate monthly or yearly?")

    boundary_points = models.TextField(null=True, blank=True,
        help_text="List of lat, long pairs (one per line) tracing out the property")
    entry_points = models.TextField(null=True, blank=True,
        help_text="List of lat, long pairs (one per line) for entrypoint to the property")

    @property
    def available_now(self):
        return not self.available_date or self.available_date <= date.today()

    @property
    def price_per_acre(self):
        return float(self.lease_rate) / float(self.acreage)

    @property
    def boundary_point_rings(self):
        if not self.boundary_points:
            return []
        point_str = self.boundary_points.replace('\r\n', '\n').replace('\r', '\n')
        rings = point_str.split("\n\n")
        return [
            [(float(c[0].strip()), float(c[1].strip()))
                for p in r.splitlines()
                for c in [p.split(',')]]
            for r in rings]

    @property
    def center_point(self):
        lats = [p[0] for r in self.boundary_point_rings for p in r]
        longs = [p[1] for r in self.boundary_point_rings for p in r]
        if not lats or not longs:
            return None
        return (sum(lats) / len(lats), sum(longs) / len(longs))

    @property
    def extents(self):
        lats = [p[0] for r in self.boundary_point_rings for p in r]
        longs = [p[1] for r in self.boundary_point_rings for p in r]
        return {
            "north": max(lats),
            "south": min(lats),
            "east": max(longs),
            "west": min(longs),
        }

    @property
    def entry_point_list(self):
        if not self.entry_points:
            return []
        return [(float(c[0].strip()), float(c[1].strip())) for p in self.entry_points.splitlines() for c in [p.split(',')]]

    def __unicode__(self):
        return self.property_name

class Image(models.Model):
    description = models.TextField()
    file = models.FileField(upload_to=image_path)
    property = models.ForeignKey(Property, related_name="images")
