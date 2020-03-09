from django.db import models

# Create your models here.
class Post(models.Model):
    TEXT_COLOUR_CHOICES = [
        ('ffffff', 'White'),
        ('ffff00', 'Yellow'),
    ]
    BG_COLOUR_CHOICES = [
        ('000000', 'Black'),
        ('000080', 'Dark blue'),
    ]

    text = models.TextField()
    text_colour = models.CharField(
        max_length=6,
        choices=TEXT_COLOUR_CHOICES,
        default='ffffff'
    )
    bg_colour = models.CharField(
        max_length=6,
        choices=BG_COLOUR_CHOICES,
        default='000000'
    )

    def __str__(self):
        return "id={} TEXT: '{}'".format(self.pk, self.text)
