from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "store category"

    name = models.CharField(max_length=256)


class Store(models.Model):
    class Meta:
        db_table = "store"

    name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
