from django.urls import path
from .views import home, ficha_inscricao, comprovante_inscricao

app_name = 'inscricao'
urlpatterns = [
    path('ficha_inscricao/', ficha_inscricao, name='ficha_inscricao'),
    path('comprovante_inscricao/', comprovante_inscricao, name='comprovante_inscricao'),
    path('', home, name='home'),
]