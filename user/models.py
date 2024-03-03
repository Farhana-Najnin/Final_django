from django.db import models
from django.contrib.auth.models import User
from . constants import GENDERTYPE, ACCOUNTTYPE
from django.utils.crypto import get_random_string
# Create your models here.


class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name = 'account', on_delete = models.CASCADE)
    account_type = models.CharField(max_length = 40, choices =ACCOUNTTYPE)
    # account_no = models.IntegerField()
    birth_date = models.DateField(null=True, blank = True)
    gender = models.CharField(max_length=13, choices=GENDERTYPE)
    # initial_deposite_date = models.DateField(auto_now_add = True)
    # balance = models.DecimalField(default=0, max_digits=12, decimal_places = 2)

    def __str__(self):
        return str(self.account_no)
    
    def save(self, *args, **kwargs):
        if not self.account_no:
            self.account_no = get_random_string(length=10)  # Generate a random account number
        super().save(*args, **kwargs)
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name = 'address', on_delete = models.CASCADE)
    street_address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.user.email)