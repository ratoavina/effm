from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# from . import Projet

class Galerie(models.Model):
    # # Projet
    # projet = models.ManyToManyField(
    #     Projet,
    #     null = True,
    #     blank = True
    # )
    # photo
    # titre
    titre = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # description
    description = models.CharField(
        null = True,
        blank = True
    )
    # date
    date = models.DateField(
        max_length = 100,
        null = True,
        blank = True
    )
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        retour = self.projet
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_patient')# mbola amboarina

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.projet) + slugify(self.titre)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Galerie"