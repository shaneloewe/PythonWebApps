from django.db import models


class Hero(models.Model):
    heroName = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk}. {self.heroName} - from {self.origin}'
