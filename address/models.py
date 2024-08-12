from django.db import models
from user.models import User


# Create your models here.
class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    addr = models.CharField(max_length=200)

    def __str__(self):
        return self.addr
