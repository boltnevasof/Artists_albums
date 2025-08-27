from rest_framework import viewsets
from .models import Song, Artist, AlbumTrack, Album
from .serializers import ArtistSerializer, AlbumSerializer, AlbumTrackSerializer, SongSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.select_related('artist').all()
    serializer_class = AlbumSerializer


class AlbumTrackViewSet(viewsets.ModelViewSet):
    queryset = AlbumTrack.objects.select_related('album', 'song').all()
    serializer_class = AlbumTrackSerializer
