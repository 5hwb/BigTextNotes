from django.db import models

# Create your models here.
class Post(models.Model):
    TEXT_COLOUR_CHOICES = [
        ('ffffff', 'White'),
        ('ffb45e', 'Light orange'),
        ('ffffa0', 'Light yellow'),
        ('a0ffa0', 'Light green'),
        ('88c2ff', 'Light blue'),
        
    ]
    BG_COLOUR_CHOICES = [
        ('000000', 'Black'),
        ('500000', 'Dark red'),
        ('502800', 'Brown'),
        ('005000', 'Dark green'),
        ('000050', 'Dark blue'),
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
