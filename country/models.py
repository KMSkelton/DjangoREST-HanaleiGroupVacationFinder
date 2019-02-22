from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=40, unique=True, blank=True)
    code = models.CharField(max_length=2, blank=True)  # not unique as there are duplicates (IT)

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ('name',)

    def __str__(self):
        return '%s' % (self.name or self.code)
