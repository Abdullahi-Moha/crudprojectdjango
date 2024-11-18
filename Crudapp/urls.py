from django.urls import path

from crudproject.urls import urlpatterns
from . import views

urlpatterns=[
    path('', views.create_item, name='item_list'),
]