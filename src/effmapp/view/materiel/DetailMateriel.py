from django.shortcuts import render

from django.views.generic import DetailView

from effmapp.models.Materiel import Materiel
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from datetime import date, timedelta
from django.contrib.auth.forms import UserCreationForm

from django.template.defaultfilters import slugify

from datetime import *
# Create your views here.

class DetailMateriel(DetailView):
   model = Materiel
   template_name = "effmapp/materiel_detail.html"
   context_object_name = "materiel"