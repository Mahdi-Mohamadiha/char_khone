from django.db import models

# Create your models here.
class House(models.Model):
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=4, decimal_places=2)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='house_images/')
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HouseDetail(models.Model):
    house = models.OneToOneField(House, on_delete=models.CASCADE)
    feature = models.CharField(max_length=100)
    year_built = models.IntegerField()
    lot_size = models.DecimalField(max_digits=10, decimal_places=2)
    garage_size = models.DecimalField(max_digits=10, decimal_places=2)
    heating_type = models.CharField(max_length=100)
    cooling_type = models.CharField(max_length=100)
    other_details = models.TextField()

class HouseImage(models.Model):
    house = models.ForeignKey(House, related_name='images', on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to='house_images/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
