from django.urls import path
from .views import maps, index

urlpatterns = [
    path('', view=maps, name='maps'),
    path('list', view=index, name='index')
]
