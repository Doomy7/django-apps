from django.shortcuts import render

# Create your views here.
#render main page
def index(request):
    return render(request, 'pages/index.html')