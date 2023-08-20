from django.shortcuts import render
from .animation import typewriter_effect

# Create your views here.
def index(request):
    return render(request, 'index.html')
     