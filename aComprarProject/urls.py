from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from aComprarApp import views
urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('productosList/',views.ProductosList.as_view()),
    path('productoUpdate/<int:pk>/',views.ProductoUpdate.as_view()),
    path('productoCreate/',views.ProductoCreate.as_view()),
    path('productoDetail/<int:pk>/',views.ProductoDetailView.as_view()),
    path('compraCreate/<int:user>/',views.CompraCreate.as_view()),
    path('compraList/<int:user>/',views.CompraList.as_view()),
]
