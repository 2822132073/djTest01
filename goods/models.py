from django.db import models
from user.models import User
from address.models import Address


# Create your models here.

class Goods(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    buy_time = models.DateTimeField(auto_now_add=True)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
