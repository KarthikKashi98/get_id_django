from django.db import models


# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True),
    given_id = models.IntegerField(default=1, blank=False, null=False)


    def __str__(self):
        return str(self.given_id)
