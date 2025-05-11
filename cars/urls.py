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
    path('terms/', views.terms, name='terms_of_use'),

    path('car/<int:car_id>/purchase/', views.purchase_car, name='purchase_car'),
    path('order/<int:order_id>/confirmation/', views.order_confirmation, name='order_confirmation'),
    path('orders/', views.order_history, name='order_history'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:car_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('purchase/<int:car_id>/', views.purchase_car, name='purchase_car'), 
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirm-purchase/', views.confirm_purchase, name='confirm_purchase'),  

    path('admin-dashboard/order/<int:order_id>/', views.order_detail, name='order_detail'),
   
]
