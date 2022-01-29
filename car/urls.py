from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CarCreate, CarView, CarUpdate, CarDelete, CarView

urlpatterns = [
    path('api/create', CarCreate.as_view()),
    path('api', CarView.as_view()),
    path('api/<int:pk>', CarUpdate.as_view()),
    path('api/<int:pk>/delete',CarDelete.as_view()),
    path('api-auth/', obtain_auth_token, name='api_token_auth'),
]