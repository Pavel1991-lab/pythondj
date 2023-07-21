from django.urls import path

from progect5.catalog.views import index

urlpatterns = [
    path('', index)
]