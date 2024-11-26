from django.urls import path
from .views import dash2
from .views import login_view, dashboard, logout_view, dash2, agregar_dato


urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('pagina2/', dash2, name='dashboard2'),
    path('agregar-dato/', agregar_dato, name='agregar_dato'),  # Ruta para agregar_dato
    path('profile/', views.perfil_usuario, name='perfil_usuario'),
]



