from django.shortcuts import render
from datetime import *


def billetage(request):
    return render(request, 'effmapp/billetage.html',{})