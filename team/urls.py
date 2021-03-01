from django.urls import path
from .views import tournamentView, groupView

app_name = "team"
urlpatterns = [
    # path("", tournamentView, name="tournamentView"),
    path("", groupView, name="groupView"),
]
