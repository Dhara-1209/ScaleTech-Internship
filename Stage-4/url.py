from django.contrib import admin
from django.urls import path
from home.views import home, AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', AboutView.as_view()),
]