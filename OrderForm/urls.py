from django.urls import path
from .views import order_view
from . import views

urlpatterns = [
    path('', order_view, name='order_view'),  # Make sure the path is correctly associated with the view
    path('', order_view, name='order'),
    path('', views.order_view, name='index'),
]
