from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.urls import reverse

class std(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    date_posted=models.DateTimeField(default=timezone.now)
    image=models.ImageField()
    country=CountryField(blank=True)

    def get_absolute_url(self):
        return reverse('home')