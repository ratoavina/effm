from django.shortcuts import render

from django.views.generic import UpdateView

from effmapp.models.Produit import *
from effmapp.models.Produit import Produit
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from datetime import date, timedelta
from django.contrib.auth.forms import UserCreationForm

from django.template.defaultfilters import slugify

from datetime import *
# Create your views here.

class UpdateProduit(UpdateView):
   model = Produit
   context_object_name = "produit"
   template_name = "application/produit_edit.html"
   fields = [
      'desination',
   ]
