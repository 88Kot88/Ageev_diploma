from django.db import models
from django.urls import reverse


class Wheat(models.Model):
    weight = models.FloatField()
    date = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('wheat-create', args=[str(self.id)])

    def __str__(self):
        return f'{self.id} /{self.weight} /{self.date}'

