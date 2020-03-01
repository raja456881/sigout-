from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.home , name='home' ),
    path('res/', views.res , name='res'),
    path('login/', views.login, name='login'),
    path('logout/' , views.logout , name='logout'),
    path('image/', views.image , name='image'),
    path('excel/', views.excel , name='excel'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)