from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from effmapp.models.Materiel import Materiel
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from datetime import date, timedelta
from django.contrib.auth.forms import UserCreationForm

from django.template.defaultfilters import slugify

from datetime import *

from django.core.paginator import Paginator

def listMateriel(request):
   date_now = datetime.now().date()
   split_date_now = str(date_now).split("-")
   
   # model = Materiel.objects.filter(date_entre=date_now)
   model = Materiel.objects.all()
   message = ""

   # ___ Recherche ___
   get = ""
   if request.method == "POST":
      get = request.POST.get("search")
      materiel_filter = Materiel.objects.filter(desination__icontains=get)
      if materiel_filter:
         model = materiel_filter
      else:
         try:
            materiel_filter1 = Materiel.objects.filter(a_peremption__icontains=get)
         except:
            materiel_filter1 = None
         if materiel_filter1:
            model = materiel_filter1
         else:
            try:
               materiel_filter2 = Materiel.objects.filter(prix_u__icontains=get)
            except:
               materiel_filter2 = None
            if materiel_filter2:
               model = materiel_filter2
            else:
               try:
                  materiel_filter3 = Materiel.objects.filter(entre__icontains=get)
               except:
                  materiel_filter3 = None
               if materiel_filter3:
                  model = materiel_filter3
               else:
                  try:
                     materiel_filter4 = Materiel.objects.filter(stock__icontains=get)
                  except:
                     materiel_filter4 = None
                  if materiel_filter4:
                     model = materiel_filter4
                  else:
                     try:
                        materiel_filter5 = Materiel.objects.filter(sortie__icontains=get)
                     except:
                        materiel_filter5 = None
                     if materiel_filter5:
                        model = materiel_filter5
                     else:
                        try:
                           materiel_filter6 = Materiel.objects.filter(recette__icontains=get)
                        except:
                           materiel_filter6 = None
                        if materiel_filter6:
                           model = materiel_filter6
                        else:
                           try:
                              materiel_filter7 = Materiel.objects.filter(stock_31__icontains=get)
                           except:
                              materiel_filter7 = None
                           if materiel_filter7:
                              model = materiel_filter7
                           else:
                              try:
                                 materiel_filter8 = Materiel.objects.filter(montant_physique__icontains=get)
                              except:
                                 materiel_filter8 = None
                              if materiel_filter8:
                                 model = materiel_filter8
                              else:
                                 try:
                                    materiel_filter9 = Materiel.objects.filter(a_entree__icontains=get)
                                 except:
                                    materiel_filter9 = None
                                 if materiel_filter9:
                                    model = materiel_filter9
                                 else:
                                    message = "Desole, " + " '" + get + "'" + " n'existe pas"
   # ___ end Recherche ___

   # ___ Paginator ___
   paginator = Paginator(model, 8)
   page = request.GET.get("page")
   model = paginator.get_page(page)
   # ___ end Paginator ___ 

   return render(request, "effmapp/materiel_liste.html", context={
                                                                        "materiel": model,
                                                                        "msg": message,
                                                                        "date_now": date_now,
                                                                     })