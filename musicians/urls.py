from django.urls import path
from .views import MusicianView, MusicianRetriveView

urlpatterns = [
    path('musicians/', MusicianView.as_view()),
    path('musicians/<int:musician_id>/', MusicianRetriveView.as_view())
]