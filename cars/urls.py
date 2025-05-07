from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list, name='car_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('careers/', views.careers, name='careers'),
    path('terms/', views.terms, name='terms'),

    path('car/<int:car_id>/purchase/', views.purchase_car, name='purchase_car'),
    path('order/<int:order_id>/confirmation/', views.order_confirmation, name='order_confirmation'),
   
]
