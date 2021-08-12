from django.urls import path
from .views import login_view


app_name = 'registration'

urlpatterns = [
    path('users/login/', login_view, name="login"),
]
