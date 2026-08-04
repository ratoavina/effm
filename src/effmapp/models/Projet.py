from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# from . import Partenaire
# from . import User

class Projet(models.Model):
    # nom
    nom = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # description
    description = models.CharField(
        null = True,
        blank = True
    )
    # # responsable (user)
    # responsable = models.ManyToManyField(
    #     User,
    #     null = True,
    #     blank = True
    # )
    # budget
    budget = models.IntegerField(
        null = True,
        blank = True
    )
    # date_debut
    date_i = models.DateField(
        null = True,
        blank = True
    )
    # date_fin
    date_f = models.DateField(
        null = True,
        blank = True
    )
    # pays ajanona charfield aloha sao misy tanana vao2 tsy ao anaty BDD
    pays = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # region ajanona charfield aloha sao misy tanana vao2 tsy ao anaty BDD
    region = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # district ajanona charfield aloha sao misy tanana vao2 tsy ao anaty BDD
    district = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # commune ajanona charfield aloha sao misy tanana vao2 tsy ao anaty BDD
    commune = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # statut
    statut = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # donateur_principal
    donateur = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # photo
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        retour = self.nom
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_patient')# mbola amboarina

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom) + slugify(self.responsable)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Projet"