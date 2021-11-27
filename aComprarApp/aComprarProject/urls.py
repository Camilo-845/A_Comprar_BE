from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from aComprarApp.views.userCreateView import UserCreateView
from aComprarApp.views.userDetailView import UserDetailView
from aComprarApp.views.compraCreateView import compraCreateView
from aComprarApp.views.Catalogo import Catalogo
from aComprarApp.views.Catalogo import CatalogoUpdate

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', UserCreateView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('catalogo/',Catalogo.as_view()),
    path('catalogo/<id>/',CatalogoUpdate.as_view()),
    path('compra/',compraCreateView.as_view())
]
