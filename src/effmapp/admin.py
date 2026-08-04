from django.contrib import admin
from .models import Actualite, Beneficiaire, Bourse, CampagneKurban, CampagneRamadan, DistributionKurban, DistributionRamadan
from .models import Document, Don, Donateur, Forage, Galerie, Materiel, Partenaire, Pays, Produit, Projet, Region,User, Volontaire
from .models import Commune, District, Fokotany

admin.site.register(Actualite)
admin.site.register(Beneficiaire)
admin.site.register(Bourse)
admin.site.register(CampagneKurban)
admin.site.register(CampagneRamadan)
admin.site.register(DistributionKurban)
admin.site.register(DistributionRamadan)
admin.site.register(Document)
admin.site.register(Don)
admin.site.register(Donateur)
admin.site.register(Forage)
admin.site.register(Galerie)
admin.site.register(Pays)
admin.site.register(Produit)
admin.site.register(Materiel)
admin.site.register(Partenaire)
admin.site.register(Projet)
admin.site.register(Region)
admin.site.register(User)
admin.site.register(Volontaire)
admin.site.register(Commune)
admin.site.register(District)
admin.site.register(Fokotany)

