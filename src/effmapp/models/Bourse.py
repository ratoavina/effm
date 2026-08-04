from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# from . import Region, Projet

class Bourse(models.Model):
    # etudiant
    etudiant = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # ecole
    ecole = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # # region/ville
    # region = models.ManyToManyField(
    #     Region,
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    # destination
    destination = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # # projet
    # projet = models.ManyToManyField(
    #     Projet,
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    # filiere
    filiere = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # debut
    debut = models.DateField(
        null = True,
        blank = True
    )
    # fin
    fin = models.DateField(
        null = True,
        blank = True
    )
    # parrain
    parrain = models.CharField(
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
    # obsevation
    observation = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    slug = models.SlugField(
        null=True,
        blank=True
    )

    def __str__(self):
        retour = self.etudiant
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_patient')# mbola amboarina

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.etudiant) + slugify(self.ecole) + slugify(self.region)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Bourse"