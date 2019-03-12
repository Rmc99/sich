from django.urls import path
from .views import home, dashboard, ficha_inscricao, comprovante_inscricao, visualizar_cadastro

app_name = 'inscricao'
urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('ficha_inscricao/', ficha_inscricao, name='ficha_inscricao'),
    path('comprovante_inscricao/', comprovante_inscricao, name='comprovante_inscricao'),
    path('visualizar_cadastro/', visualizar_cadastro, name='visualizar_cadastro'),
]