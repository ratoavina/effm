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

from django.core.paginator import Paginator

def listProduit(request):
   date_now = datetime.now().date()
   split_date_now = str(date_now).split("-")
   
   # model = Produit.objects.filter(date_entre=date_now)
   model = Produit.objects.all()
   message = ""

   # ___ Recherche ___
   get = ""
   if request.method == "POST":
      get = request.POST.get("search")
      produit_filter = Produit.objects.filter(desination__icontains=get)
      if produit_filter:
         model = produit_filter
      else:
         try:
            produit_filter1 = Produit.objects.filter(a_peremption__icontains=get)
         except:
            produit_filter1 = None
         if produit_filter1:
            model = produit_filter1
         else:
            try:
               produit_filter2 = Produit.objects.filter(prix_u__icontains=get)
            except:
               produit_filter2 = None
            if produit_filter2:
               model = produit_filter2
            else:
               try:
                  produit_filter3 = Produit.objects.filter(entre__icontains=get)
               except:
                  produit_filter3 = None
               if produit_filter3:
                  model = produit_filter3
               else:
                  try:
                     produit_filter4 = Produit.objects.filter(stock__icontains=get)
                  except:
                     produit_filter4 = None
                  if produit_filter4:
                     model = produit_filter4
                  else:
                     try:
                        produit_filter5 = Produit.objects.filter(sortie__icontains=get)
                     except:
                        produit_filter5 = None
                     if produit_filter5:
                        model = produit_filter5
                     else:
                        try:
                           produit_filter6 = Produit.objects.filter(recette__icontains=get)
                        except:
                           produit_filter6 = None
                        if produit_filter6:
                           model = produit_filter6
                        else:
                           try:
                              produit_filter7 = Produit.objects.filter(stock_31__icontains=get)
                           except:
                              produit_filter7 = None
                           if produit_filter7:
                              model = produit_filter7
                           else:
                              try:
                                 produit_filter8 = Produit.objects.filter(montant_physique__icontains=get)
                              except:
                                 produit_filter8 = None
                              if produit_filter8:
                                 model = produit_filter8
                              else:
                                 try:
                                    produit_filter9 = Produit.objects.filter(a_entree__icontains=get)
                                 except:
                                    produit_filter9 = None
                                 if produit_filter9:
                                    model = produit_filter9
                                 else:
                                    message = "Desole, " + " '" + get + "'" + " n'existe pas"
   # ___ end Recherche ___

   # ___ Paginator ___
   paginator = Paginator(model, 8)
   page = request.GET.get("page")
   model = paginator.get_page(page)
   # ___ end Paginator ___ 

   return render(request, "application/produit_liste.html", context={
                                                                        "produit": model,
                                                                        "msg": message,
                                                                        "date_now": date_now,
                                                                     })