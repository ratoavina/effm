from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Donateur(models.Model):
    # type
    #     individu
    #     association
    #     fondation
    #     entreprise
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
    # organisation
    organisation = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # telephone
    phone = models.IntegerField(
        null = True,
        blank = True
    )
    # email
    email = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # adresse
    adresse = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # pays
    Pays = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # site_web
    site_web = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # # logo
    # logo = models.CharField(
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    # description
    description = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # # actif
    # actif = models.CharField(
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        retour = self.desination
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_patient')# mbola amboarina

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom) + slugify(self.prenom) + slugify(self.telephone)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Donateur"