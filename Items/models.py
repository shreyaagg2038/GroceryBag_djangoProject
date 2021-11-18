from django.db import models

from django.contrib.auth.models import User

status = (('PENDING','PENDING'),('BOUGHT','BOUGHT'),('NOT AVAILABLE','NOT AVAILABLE'))

class item(models.Model):
    item_name = models.TextField()
    item_quantity = models.TextField()
    item_user = models.ForeignKey(User, on_delete= models.CASCADE)
    item_date = models.DateField( null = True)
    item_status = models.CharField(max_length=100, choices=status, default='PENDING')

