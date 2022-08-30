from django.urls import path
from . import views


app_name = 'cms'

urlpatterns = [
    path('', views.sessite, name='ses_site'),
    path('origin/', views.originsite, name='origin_site'),
]