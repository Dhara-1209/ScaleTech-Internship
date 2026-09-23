from django.shortcuts import render
from django.views import View


def home(request):
    return render(request, 'home/home.html')


def contact(request):
    return render(request, 'home/contact.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'home/about.html')