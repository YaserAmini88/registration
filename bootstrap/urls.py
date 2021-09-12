from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'bootstrap'
urlpatterns = [
    path('user.html', views.user, name='user'),
    path('table.html', views.table, name='table'),
    path('typography.html', views.typo, name='typo'),
    path('icons.html', views.icons, name='icons'),
    path('maps.html', views.maps, name='maps'),
    path('login.html', views.login, name='login'),
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('register.html', views.Register.as_view(), name='register'),
    path('notifications.html', views.notifications, name='notifications'),
    path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)