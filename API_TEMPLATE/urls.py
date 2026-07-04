from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('create-user', views.CreateUserView.as_view(), name='create_user'),
    path('<int:user_id>/', views.details, name='user_details'),
    path('<str:user_name>/', views.nombre, name="user_name"),
    path('', views.index, name='index'),
    path('product/<int:product_id>/', views.product, name='product'),
]