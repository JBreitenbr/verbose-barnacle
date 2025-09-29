#from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Piece
from .serializers import PieceListSerializer
import json

class BandSubs(APIView):
    def get(self, request):
        with open("./scripts/bandSubs.json", "r") as f:
            bsubs_json = json.load(f)
        return Response(bsubs_json)

class PiecesBySinger(generics.ListAPIView):
    serializer_class = PieceListSerializer
    def get_queryset(self):
        singer_name = self.kwargs["name"]
        return Piece.objects.filter(artist__name=singer_name)