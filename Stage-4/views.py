from django.contrib import admin
from django.urls import path

from home.views import AboutView, home, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', AboutView.as_view()),
    path('contact/', contact),
]