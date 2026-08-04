from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Produit(models.Model):
    # nom
    nom = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # categorie
    categorie = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # unite
    unite = models.IntegerField(
        null = True,
        blank = True
    )
    # prix_achat
    prix_achat = models.IntegerField(
        null = True,
        blank = True
    )
    # prix_moyen
    prix_moyen = models.IntegerField(
        null = True,
        blank = True
    )
    # stock_minim
    stock_min = models.IntegerField(
        null = True,
        blank = True
    )
    # qte
    qte = models.IntegerField(
        null = True,
        blank = True
    )
    # description
    description = models.CharField(
        null = True,
        blank = True
    )
    # # actif
    # actif = models.CharField(
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    # akambana miaraka @ ilay ambany, fafana fotsiny izay efa ao ......................
    desination = models.CharField(max_length=100, null=True, blank=True)
    prix_u = models.IntegerField(null=True, blank=True)
    entre = models.IntegerField(null=True, blank=True)
    date_entree = models.DateField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    date_peremption = models.DateField(null=True, blank=True)
    total_stock = models.IntegerField(null=True, blank=True)
    sortie = models.IntegerField(null=True, blank=True)
    recette = models.IntegerField(null=True, blank=True)
    montant_physique = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        retour = self.desination
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_produit')

    def save(self, *args, **kwargs):
        if not self.entre:
            self.entre = 0
        if not self.prix_u:
            self.prix_u = 0
        if not self.stock:
            self.stock = 0
        if not self.sortie:
            self.sortie = 0
            self.total_stock = self.entre + self.stock
        if self.entre != 0 and self.prix_u != 0:
            self.total_stock = self.entre + self.stock
            self.recette = self.prix_u * self.sortie
            self.montant_physique = self.prix_u * self.entre
        if not self.slug:
            self.slug = slugify(self.desination)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Produit"