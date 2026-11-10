from django.urls import path
from users.views import LoginUserView, RegistrationUserView, EditUserView


urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('registration/', RegistrationUserView.as_view(), name='registration'),
    path('edit/<str:username>/', EditUserView.as_view(), name='edit')
]