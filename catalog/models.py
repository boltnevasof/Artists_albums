from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'


class Artist(models.Model):
    name = models.CharField('Исполнитель', max_length=255)

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField('Альбом', max_length=255)
    release_year = models.PositiveIntegerField('Год выпуска')
    songs = models.ManyToManyField(Song, through='AlbumTrack')


class AlbumTrack(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='tracks')
    track_number = models.PositiveIntegerField('Номер песни')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['album', 'song'], name='uniq_album_song'),
            models.UniqueConstraint(fields=['album', 'track_number'], name='uniq_album_track'),
        ]

    def __str__(self):

        return f"{self.album.title} — {self.track_number}. {self.song.name}"
