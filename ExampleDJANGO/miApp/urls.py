from django.urls import path
from .views import login_view, dashboard, logout_view
from .views import crear_usuario

urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
]


