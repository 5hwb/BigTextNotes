from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return "id={} TEXT: '{}'".format(self.pk, self.text)
