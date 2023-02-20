from unicodedata import category
from django.db import models
import uuid


class Property(models.Model):
    """Properties Model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    no_of_beds = models.IntegerField(blank=True, null=True)
    no_of_baths = models.IntegerField(blank=True, null=True)
    no_of_garages = models.IntegerField(blank=True, null=True)
    area = models.name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('PropertyCategories', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class PropertyCategories(models.Model):
    """Property Categories Model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Property Category'
        verbose_name_plural = 'Property Categories'

