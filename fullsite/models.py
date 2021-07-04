from django.db import models

# Create your models here.
class Country(models.Model):
    c_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    populations=models.IntegerField()
    def __str__(self):
        return f"{self.name}--{self.c_id}"