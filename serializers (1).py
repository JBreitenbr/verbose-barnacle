from rest_framework import serializers
from .models import Piece

class PieceListSerializer(serializers.ModelSerializer):
    artist = serializers.CharField(source="artist.name")  # gibt den Namen des Sängers zurück

    class Meta:
        model = Piece
        fields = ["artist","track","album_name","album_date","album_tracks","album_pic","genres"]