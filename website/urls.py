from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('ficheiro1', views.ficheiro1, name='ficheiro1'),
    path('ficheiro2', views.ficheiro2, name='ficheiro2'),
    path('ficheiro3', views.ficheiro3, name='ficheiro3'),
]