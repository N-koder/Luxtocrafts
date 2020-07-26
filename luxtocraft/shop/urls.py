from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="home"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('search/', views.search,name="search"),
    path('products/<int:yoid>',views.prodview,name="prodview"),
    path('checkout/',views.checkout,name="checkout"),
    path('thank/',views.thank,name="thank"),
]