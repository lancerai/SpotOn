from django.urls import path
from .views import search_places, ask_question

urlpatterns = [
    path('', search_places, name='search_places'),
    path('ask-question/', ask_question, name='ask_question'),
]
