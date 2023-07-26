import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    qtyAvailable = models.IntegerField(default=0)
    # status = models.ForeignKey(TaskStatus, related_name="repent", on_delete=models.RESTRICT, default=None)
    text = models.CharField(max_length=100)
    isSaleable = models.BooleanField(default=False)

    def __str__(self):
        return self.text
