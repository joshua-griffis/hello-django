from django.contrib import admin
from django.urls import path

from app.views import hello_view, roll_die_view, random_between_view

urlpatterns = [
    path('hello-django/', hello_view),
    path('admin/', admin.site.urls),
]
