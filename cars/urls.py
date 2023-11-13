from django.urls import path, include
from cars.views import *
from django.contrib.auth import views as as_view


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('addcar/', CreateCarView.as_view(), name='addcar'),
    path('create-user/', CreateUserView.as_view(), name='createuser'),
    path('login/', as_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', as_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('car-detail/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('update_car/<int:pk>/', UpdateCarView.as_view(), name='update_cars'),
    path('delete_car/<int:pk>/', DeleteCarView.as_view(), name='delete_car')
]
