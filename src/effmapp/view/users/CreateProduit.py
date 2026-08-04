from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

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

def createProduit(request):
   msg1 = ""
   msg2 = ""
   if request.method == "POST":
      if request.POST.get("desination"):
         design = request.POST.get("desination")
         prix = request.POST.get("prix_u")
         r_entre = request.POST.get("entre")
         r_stock = request.POST.get("stock")
         r_sortie = request.POST.get("sortie")
         if not r_stock:
            r_stock = 0
         if not r_sortie:
            r_sortie = 0
         if not r_entre:
            r_entre = 0
         date_entre = request.POST.get("date_entree")
         date_perempt = request.POST.get("date_peremption") 

         try:
            Produit.objects.create( desination = design,
                                    prix_u = int(prix),
                                    entre = int(r_entre),
                                    stock = int(r_stock),
                                    sortie = int(r_sortie),
                                    date_entree = date_entre,
                                    date_peremption = date_perempt
                                 )
            msg1 = " Le produit est bien ajoute"
         except:
            msg2 = "Il y a une erreur, merci de verifier les informations"
      else:
         msg2 = "Veuillez remplir le formulair s'il vous plait"
   return render(request, "effmapp/produit_create.html",   {
                                                                  "message1": msg1,
                                                                  "message2": msg2
                                                               })