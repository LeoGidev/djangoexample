from django.urls import path
from .views import login_view, dashboard, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]

from .views import crear_usuario
urlpatterns += [
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
]
