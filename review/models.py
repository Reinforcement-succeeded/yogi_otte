from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import CustomUser
from store.models import Store

# Create your models here.
class Review(models.Model):
    class Meta:
        db_table = "review"

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    star = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    calc_star = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    comment = models.CharField(max_length=300)
    create_date = models.DateTimeField(null = True) #null = True
    update_date = models.DateTimeField(auto_now=True)
