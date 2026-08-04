from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# from . import Projet

class Document(models.Model):
    # nom
    nom = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # # projet
    # projet = models.ManyToManyField(
    #     Projet,
    #     null = True,
    #     blank = True
    # )
    # # type
    # type = models.CharField(
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    # # fichier
    # fichier = models.CharField(
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    # auteur
    auteur = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # date
    date = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        retour = self.nom
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_patient')# mbola amboarina

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom) + slugify(self.projet) + slugify(self.auteur) + slugify(self.date)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Document"