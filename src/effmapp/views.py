from django.shortcuts import render
from . import *
from datetime import *

# Create your views here.
def accueil(request):
    return render(request, 'effmapp/index.html')

def inscription(request):
    return render(request, "effmapp/inscription.html", {})

