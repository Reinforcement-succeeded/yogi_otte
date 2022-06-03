from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        db_table = "custom_user"

