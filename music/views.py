from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Yoo first music homepage</h1>")