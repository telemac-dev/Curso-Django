from django.urls import path
from contato.views import index

urlpatterns = [
    path('', index, name='index'),
]
