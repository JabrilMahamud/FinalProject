from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class MetaDataModel(models.Model):
    account_no = models.IntegerField()
    account_name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.account_name