from django.urls import path
from . import views

urlpatterns = [
    path('order', views.place_order),
    path('<str:name>', views.get_pizza )
    
]
