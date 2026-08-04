from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# from . import Region, Commune, District, Fokotany

class Beneficiaire(models.Model):
    # nom
    nom = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # prenom
    prenom = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # sexe
    sexe = models.CharField(
        max_length = 20,
        null = True,
        blank = True
    )
    # Date de naissance
    dtn = models.DateField(
        null = True,
        blank = True
    )
    # telephone
    phone = models.IntegerField(
        null = True,
        blank = True
    )
    # cin
    cin = models.IntegerField(
        null = True,
        blank = True
    )
    # passeport
    # passeport = models.IntegerField(
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    # adresse
    adresse = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # # region
    # region = models.ManyToManyField(
    #     Region,
    #     null = True,
    #     blank = True
    # )
    # # district
    # district = models.ManyToManyField(
    #     District, 
    #     null = True,
    #     blank = True
    # )
    # # commune
    # commune = models.ManyToManyField(
    #     Commune,
    #     null = True,
    #     blank = True
    # )
    # # fokotany
    # fokotany = models.ManyToManyField(
    #     Fokotany,
    #     null = True,
    #     blank = True
    # )
    # profession
    profession = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # situation_familiale
    s_famille = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # nbr_enfants
    nbr_enfant = models.IntegerField(
        null = True,
        blank = True
    )
    # handicap
    handicap = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # # photo
    # photo = models.CharField(
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    # # latitude
    # latitude = models.CharField(
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    # # longitude
    # longitude = models.CharField(
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    # observation
    obsevation = models.CharField(
        max_length = 255,
        null = True,
        blank = True
    )
    # # actif
    # actif = models.BooleanField(
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        retour = self.nom
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_patient')# mbola amboarina

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom) + slugify(self.prenom) + slugify(self.cin)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Beneficiaire"