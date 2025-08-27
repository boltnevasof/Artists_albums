from django.contrib import admin

# Register your models here.
from .models import Song, Artist, Album, AlbumTrack

admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(AlbumTrack)