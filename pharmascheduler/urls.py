from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='accounts/login/')),   

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    path('upload/', include('upload.urls')),

    path('schedule/', include('schedule.urls')),
]