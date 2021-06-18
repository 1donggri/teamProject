from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "schedule"

urlpatterns = [
    path('write_schedule/', views.write_schedule, name='write_schedule'),
    path('view_schedule/', views.view_schedule, name='view_schedule'),
    path('delete/<int:posts_id>/', views.delete, name='delete'),
]