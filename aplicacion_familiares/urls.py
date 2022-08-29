from django.urls import path
from aplicacion_familiares.views import probar_template 

urlpatterns = [
    path('', probar_template),
]
