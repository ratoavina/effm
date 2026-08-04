from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Partenaire(models.Model):
    # nom
    nom = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # pays
    pays = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # responsable
    responsable = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # telephone
    telephone = models.IntegerField(
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
    # # logo
    # logo = models.CharField(
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    # convention
    convention = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # date_debut
    date_i = models.DateField(
        max_length = 100,
        null = True,
        blank = True
    )
    # date_fin
    date_f = models.CharField(
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
        retour = self.nom
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_patient')# mbola amboarina

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom) + slugify(self.telephone) + slugify(self.email)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Partenaire"