from django.db import models
from django.contrib.auth.models import User
from . constants import GENDERTYPE, ACCOUNTTYPE
from django.utils.crypto import get_random_string
# Create your models here.


class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name = 'account', on_delete = models.CASCADE)
    account_type = models.CharField(max_length = 40, choices =ACCOUNTTYPE)
    def __str__(self):
        return str(self.user.username)
    
