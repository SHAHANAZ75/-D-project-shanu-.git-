from django.http import HttpResponse
def index(request):
    return HttpResponse("hello world")#HttpResponse(HTML tag as an argument)
def home(request):
    return HttpResponse("<h1> welcome to homepage</h1>")