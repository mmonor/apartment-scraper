from django.db import models
from django.contrib.auth.models import User

class Apartment(models.Model):
    # basic info
    price = models.DecimalField(max_digits=10, decimal_places=2)
    square_footage = models.IntegerField(null=True, blank=True)
    bedrooms = models.SmallIntegerField(default=1)
    bathrooms = models.SmallIntegerField(default=1)
    balcony = models.BooleanField(default=False)

    # utilities
    washing_machine = models.BooleanField(default=False)
    dishwashing = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    own_heating = models.BooleanField(default=False)
    parking_spot = models.BooleanField(default=False)

    #location
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    sector = models.IntegerField(blank=True, null=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6,null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,null=True, blank=True)

    #URL
    olx_url = models.URLField(unique=True)
    storia_url = models.URLField(unique=True)
    date_scraped = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.address} - {self.city} - €{self.price}"

    class Meta:
        ordering = ['-date_scraped']


class SavedApartment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='saved_apartments',
        on_delete=models.CASCADE
    )
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    date_saved = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'apartment')

    def __str__(self):
        return f"{self.user.username} saved {self.apartment.address}"







