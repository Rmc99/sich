from django.urls import path
from .views import ficha_inscricao

app_name = 'inscricao'
urlpatterns = [
    path('ficha_inscricao/', ficha_inscricao, name='ficha_inscricao'),
]