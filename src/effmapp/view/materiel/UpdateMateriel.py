from django.shortcuts import render

from django.views.generic import UpdateView

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

class UpdateMateriel(UpdateView):
   model = Materiel
   context_object_name = "materiel"
   template_name = "effmapp/materiel_edit.html"
   fields = [
      'desination',
   ]
