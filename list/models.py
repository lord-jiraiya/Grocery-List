from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint, Q



ITEM_STATUS = (
    (0,'BOUGHT'),
    (1, 'PENDING'),
    (2,'NOT AVAILABLE'),
)

class User(AbstractUser):
    pass


class ItemList(models.Model):
    itemName = models.CharField(max_length=64)
    itemQuantity = models.CharField(max_length=64)
    itemStatus = models.CharField(max_length=400,choices = ITEM_STATUS, default = 'PENDING')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def textStyle(self):
        if self.itemStatus == '0':
            return "text-success"
        elif self.itemStatus == '1':
            return "text-info"
        else:
            return "text-danger"

    def status(self):
        return ITEM_STATUS[int(self.itemStatus)][1]