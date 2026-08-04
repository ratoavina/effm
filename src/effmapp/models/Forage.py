from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# from . import Projet

class Forage(models.Model):
    # projet
    # projet = models.ManyToManyField(
    #     Projet,
    #     null = True,
    #     blank = True
    # )
    # nom
    nom = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # village
    village = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # lien_maps
    lien_maps = models.CharField(
        null = True,
        blank = True
    )
    # latitude

    # longitude

    # profondeur
    profondeur = models.IntegerField(
        null = True,
        blank = True
    )
    # debit
    debit = models.IntegerField(
        null = True,
        blank = True
    )
    # date_realisation
    date_real = models.DateField(
        null = True,
        blank = True
    )
    # cout
    cout = models.IntegerField(
        null = True,
        blank = True
    )
    # responsable
    responsable = models.CharField(
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
    slug = models.SlugField(
        null=True,
        blank=True
    )

    def __str__(self):
        retour = self.nom
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_patient')# mbola amboarina

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom) + slugify(self.lien_maps)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Forage"