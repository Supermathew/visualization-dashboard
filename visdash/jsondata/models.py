from django.db import models

# Create your models here.




class JSONData(models.Model):
    json_file = models.FileField(upload_to='json_files/')


class EnergyInsight(models.Model):
    end_year = models.CharField(max_length=255, null=True, blank=True)
    intensity = models.IntegerField(null=True, blank=True)
    sector = models.CharField(max_length=255, null=True, blank=True)
    topic = models.CharField(max_length=255, null=True, blank=True)
    insight = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    start_year = models.CharField(max_length=255, null=True, blank=True)
    impact = models.CharField(max_length=255, null=True, blank=True)
    added = models.DateTimeField(null=True, blank=True)
    published = models.DateTimeField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    relevance = models.IntegerField(null=True, blank=True)
    pestle = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    likelihood = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

