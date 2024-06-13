from django.db import models
from musician.models import Musician


# Create your models here.
class Album(models.Model):

    class Rating(models.IntegerChoices):
        ONE = 1, "1"
        TWO = 2, "2"
        THREE = 3, "3"
        FOUR = 4, "4"
        FIVE = 5, "5"

    album_title = models.CharField(max_length=100)
    release_date = models.DateField()
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, default=1)
    rating = models.IntegerField(choices=Rating.choices, default=1)

    def __str__(self):
        return f"Album: {self.album_title}"
