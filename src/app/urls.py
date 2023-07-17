from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),
    
    #Includes de la App 'eventos'
    path('eventos/', include('eventos.urls')),

    #Includes de la App 'eventos'
    path('usuarios/', include('usuarios.urls')),

    #Includes de la App 'recursos'
    path('recursos/', include('recursos.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
