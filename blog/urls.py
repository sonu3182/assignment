from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('car1',views.car1,name='car1'),
    path('car2',views.car2,name='car2'),
    path('car3',views.car3,name='car3')
]
