from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class CampagneRamadan(models.Model):
    # annee
    annee = models.IntegerField(
        null = True,
        blank = True
    )
    # nom
    nom = models.CharField(
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
    # budget
    budget = models.IntegerField(
        null = True,
        blank = True
    )
    # description
    description = models.CharField(
        null = True,
        blank = True
    )
    # responsable
    responsable = models.CharField(
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
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        retour = self.annee
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_patient')# mbola amboarina

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.annee) + slugify(self.nom) + slugify(self.debut) + slugify(self.fin)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Campagne Ramadan"