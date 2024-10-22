from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_schedule, name='upload_schedule'),
    path('view/<int:schedule_id>/', views.view_schedule, name='view_schedule'),
]
