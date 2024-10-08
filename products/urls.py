from django.urls import path
from django.contrib import admin
from products import views


urlpatterns = [
    
    path('', views.product_list, name="product_list"),
    path('<int:id>/', views.product_detail, name="product_detail"),
    path('categories/', views.category_list, name='category-list'),  # הוספת נתיב לקטגוריות
    path('categories/<int:id>/', views.category_detail, name='category-detail'),  # נתיב לקטגוריה בודדת

]