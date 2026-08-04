from django.shortcuts import render

from effmapp.models import *
from django.views import View

from datetime import *

# from effmapp.models import Consultation


class Index(View):
    var = "index"
    hello = ""

    def get(self, request):
        # date_now = datetime.now().date()
        # month_now = str(datetime.now().date().year) + "-" + str(datetime.now().date().month)
        # year_now = datetime.now().date().year

        # consult_total = Consultation.objects.all()
        # count_patient_jour = 0
        # count_patient_mois = 0
        # count_patient_annee = 0
        # count_total = 0

        # for i in consult_total:
        #     count_total = count_total + 1

        # for x in consult_total:
        #     date_base = str(x.date_consultation)
        #     split_date_base = date_base.split("-")
        #     mois_base = split_date_base[0] + "-" + split_date_base[1]
        #     year_base = split_date_base[0]
        #     if x.date_consultation == date_now:
        #         count_patient_jour = count_patient_jour + 1
        #     if mois_base == month_now:
        #         count_patient_mois = count_patient_mois + 1
        #     if year_base == str(year_now):
        #         count_patient_annee = count_patient_annee + 1

        # count_j = count_patient_jour
        # count_m = count_patient_mois
        # count_y = count_patient_annee

        return render(request, "effmapp/index.html", context={
                                                                    # "patient_jour": count_j,
                                                                    # "patient_mois": count_m,
                                                                    # "patient_annee": count_y,
                                                                    # "patient_total": count_total
                                                                })
