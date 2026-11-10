from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=150)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "brand"
