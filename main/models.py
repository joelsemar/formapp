from django.db import models

# Create your models here.
class TestModel(models.Model):
    field_1 = models.BooleanField(default=True)
    field_2 = models.BooleanField(default=True)
    field_3 = models.BooleanField(default=True)
    