from django.db import models

# Create your models here.
class Hobby(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.summary

