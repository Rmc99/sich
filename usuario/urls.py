from django.urls import path
from .views import registrar

app_name = 'usuario'
urlpatterns = [
    path('registrar/', registrar, name='registrar'),
]