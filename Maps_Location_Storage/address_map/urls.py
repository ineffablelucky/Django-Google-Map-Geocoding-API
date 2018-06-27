from django.urls import path
from .views import maps, index, create

urlpatterns = [
    path('', view=maps, name='maps'),
    path('list/', view=index, name='index'),
    path('create/', view=create, name='create')

]
