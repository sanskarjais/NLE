from django.urls import path, include
from rest_framework import routers

from .views import add_app, Home_view, MyApp_View, complete_task,Task_View, add_new, Delete,AppViewSet,points

router = routers.SimpleRouter()
router.register(r'apps', AppViewSet)

app_name = 'android'
urlpatterns = [
    path('api/', include(router.urls)),
    path('add-app/<int:pk>', add_app, name='add_app'),
    path('complete/<int:pk>',complete_task, name = 'complete'),
    path('task/',Task_View.as_view(),name = 'task'),
    path('',Home_view,name = 'home'),
    path('myapps/',MyApp_View.as_view(),name = 'my_app'),
    path('add_new/',add_new, name = 'add_new'),
    path('delete/<int:pk>',Delete, name = 'delete'),
    path('points',points,name = 'points'),

]

