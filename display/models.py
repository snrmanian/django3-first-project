from django.db import models

# Create your models here.
class student(models.Model):
    st_id   = models.IntegerField(primary_key=True)
    st_name = models.CharField(max_length=25)

