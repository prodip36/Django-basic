from django.http import HttpResponse


def home(request):
    return HttpResponse(
        'Welcome home! Django server is running')


def home_sample(request):
    return HttpResponse(
        'I need to build up my knowledge')
