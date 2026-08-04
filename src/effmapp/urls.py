from django.urls import path, include
from . import views
from .view.index.Index import Index
from .view.billetage.bill import billetage
from .view.produit.CreateProduit import createProduit
from .view.produit.DeleteProduit import DeleteProduit
from .view.produit.DetailProduit import DetailProduit
from .view.produit.ListeProduit import listProduit
from .view.produit.UpdateProduit import UpdateProduit
from .view.materiel.CreateMateriel import createMateriel
from .view.materiel.DeleteMateriel import DeleteMateriel
from .view.materiel.DetailMateriel import DetailMateriel
from .view.materiel.ListeMateriel import listMateriel
from .view.materiel.UpdateMateriel import UpdateMateriel

app_name = 'apply'

urlpatterns = [
    path('', Index.as_view(), name="accueil"),
    path('inscription/', views.inscription, name="inscription"),
    path('compte/', include('django.contrib.auth.urls')),

    path('create_produit/', createProduit, name='create_produit'),
    path('liste_produit/', listProduit, name="liste_produit"),
    path('edit_produit/<str:slug>/', UpdateProduit.as_view(), name="edit_produit"),
    path('detail_produit/<str:slug>/', DetailProduit.as_view(), name="detail_produit"),
    path('delete_produit/<str:slug>/', DeleteProduit.as_view(), name="delete_produit"),

    path('create_materiel/', createMateriel, name='create_materiel'),
    path('liste_materiel/', listMateriel, name="liste_materiel"),
    path('edit_materiel/<str:slug>/', UpdateMateriel.as_view(), name="edit_materiel"),
    path('detail_materiel/<str:slug>/', DetailMateriel.as_view(), name="detail_materiel"),
    path('delete_materiel/<str:slug>/', DeleteMateriel.as_view(), name="delete_materiel"),
]
