from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from api import views


router = routers.SimpleRouter()
router.register('polls', views.PollView, basename='polls')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/<slug:slug>', views.poll_detail, name='poll_detail'),
    path('polls/get_result/', views.get_result, name='get_result'),
]
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


