from django.urls import path
from .views import PiecesBySinger,BandSubs

urlpatterns = [
    path("bandsByLetter/",BandSubs.as_view(),name="bandsbyletter"),
    path("<str:name>/", PiecesBySinger.as_view(), name="pieces-by-singer"),
]