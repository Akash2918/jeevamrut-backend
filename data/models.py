from django.db import models

# Create your models here.


class Data(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    reason = models.TextField(max_length=500)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)


        