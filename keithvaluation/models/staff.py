
from django.db import models


class Staff(models.Model):
    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Staff'

    name = models.CharField(max_length=128)
    email = models.EmailField()
    description = models.TextField()
    image = models.ImageField(upload_to='headshots')
    resume = models.FileField(upload_to='resumes')
    order = models.PositiveIntegerField(
        help_text='Relative ordering of this staff member (lowest is higher up '
                  'on the page)')

    def __unicode__(self):
        return u'Staff: %s' % self.name
