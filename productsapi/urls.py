from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup_api'),
    path('login/', views.login, name='login_api'),
    path('logout/', views.logout, name='logout_api'),
    path('create-product/', views.create_product, name='createproductapi'),
    path('list-products/', views.list_products, name='listproductapi'),
    path('<int:pk>/update-product/', views.update_product, name='updateproductapi'),
    path('<int:pk>/delete-product/', views.delete_product, name='deleteproductapi'),
    path('search/', views.search_product, name='searchproductapi',)
]