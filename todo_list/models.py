from django.db import models

# Create your models here.
class List(models.Model):
    # the item or task that needs to be finished
    item = models.CharField(max_length=255)
    # wether the item/task is completed or not!
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item