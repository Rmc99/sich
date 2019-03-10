from django.urls import path
from .views import efetua_inscricao

app_name = 'inscricao'
urlpatterns = [
    path('efetua_inscricao/', efetua_inscricao, name='efetua_inscricao'),
]