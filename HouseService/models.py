from django.db import models
from django.utils import timezone

# Create your models here.
class House(models.Model):
    STATUS_CHOICES = (
    ('s', 'فروش'),
    ('r', 'اجاره'),
    )
    
    TYPE_CHOICES = (
    ('v', 'ویلایی'),
    ('a', 'آپارتمان'),    
    )
    
    name = models.CharField(max_length= 100, verbose_name = "نام ساختمان")
    title = models.CharField(max_length= 200, verbose_name = "عنوان")
    address = models.CharField(max_length=255, verbose_name = "آدرس")
    #location_x = models.DecimalField(max_digits=10, decimal_places=2, verbose_name= "طول جغرافیایی")
    #location_y =  models.DecimalField(max_digits=10, decimal_places=2, verbose_name= "عرض جغرافیایی")
    price = models.TextField(verbose_name= "قیمت")
    bedrooms = models.IntegerField(verbose_name= "تعداد اتاق‌ها")
    bathrooms = models.DecimalField(max_digits=4, decimal_places=2, verbose_name= "سرویس بهداشتی")
    parking_lot = models.BooleanField(verbose_name= "پارکینگ")
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name= "مساحت")
    description = models.TextField(verbose_name= "محتوا")
    image = models.ImageField(upload_to='house_images/', verbose_name= "تصویر")
    status = models.CharField (max_length = 1, choices = STATUS_CHOICES, verbose_name = "وضعیت")
    type = models.CharField (max_length = 1, choices = TYPE_CHOICES, verbose_name = "نوع")
    publish = models.DateTimeField (default = timezone.now, verbose_name = "زمان انتشار")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "زمان ساخت")
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField (max_length = 100, unique=True, verbose_name = "آدرس مقاله")
    
    class Meta(object):
        verbose_name = "خانه"
        verbose_name_plural = "خانه ها"

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
