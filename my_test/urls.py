from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_test_all, name="my_test_all"),
    path('test/<int:pk>', views.my_test_single, name="my_test_single"),
]