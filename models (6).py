from django.db import models
class Singer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Piece(models.Model):
    track = models.CharField(max_length=200)
    artist = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='pieces')
    album_name = models.CharField(max_length=255)
    album_date = models.CharField(max_length=50)
    album_pic = models.CharField(max_length=100)
    album_tracks=models.TextField()
    genres=models.CharField(max_length=255)
    class Meta:
        ordering = ["album_date", "album_name", "track"]
    def __str__(self):
        return self.track