from django.db import models
from brand.models import Brand
from category.models import Category
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
# pip install Pillow
class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="products")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="images/")
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "product"

# variable length keyword arguments
@receiver(post_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)