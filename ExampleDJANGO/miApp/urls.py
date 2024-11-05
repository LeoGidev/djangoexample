from django.urls import path
from .views import login_view, dashboard, logout_view
from .views import dash2

urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('pagina2/', dash2, name='dashboard2'),
]


