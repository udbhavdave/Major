from django.db import models

# Create your models here.


class Image(models.Model):
    image_name = models.ImageField(upload_to="uploads/images")
    text = models.CharField(max_length=5000, blank=True, default="image text")

    def __str__(self):
        return f"{self.pk} {self.image_name}"

    class Meta:
        db_table = "image"


class Audio(models.Model):
    audio_name = models.FileField(upload_to="uploads/audio")
    text = models.CharField(max_length=5000, blank=True, default="audio text")

    def __str__(self):
        return f"{self.pk} {self.audio_name}"

    class Meta:
        db_table = "audio"
