from django.http import HttpResponse
from django.views import View


def home(request):
    return HttpResponse("Hello! This is my Function-Based View.")


def about(request):
    return HttpResponse("This is the About page.")


class AboutView(View):

    def get(self, request):
        return HttpResponse("Hello! This is my Class-Based View.")