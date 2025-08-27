from rest_framework import serializers
from .models import Song, Artist, AlbumTrack, Album


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name']


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'release_year']


class AlbumTrackSerializer(serializers.ModelSerializer):
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())
    song = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all())

    class Meta:
        model = AlbumTrack
        fields = ['id', 'album', 'song', 'track_number']
