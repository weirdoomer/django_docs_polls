from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello from pools app index page!")
