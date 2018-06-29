from django.urls import path
from .views import index, create, update

urlpatterns = [

    path('list/', view=index, name='index'),
    path('create/', view=create, name='create'),
    path('update/<int:pk>', view=update, name='update')

]
