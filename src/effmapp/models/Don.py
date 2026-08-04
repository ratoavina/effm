from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# from . import Donateur, Projet

class Don(models.Model):
    # # donateur
    # donateur = models.ManyToManyField(
    #     Donateur,
    #     null = True,
    #     blank = True
    # )
    # # projet
    # projet = models.ManyToManyField(
    #     Projet,
    #     null = True,
    #     blank = True
    # )
    # montant
    montant = models.IntegerField(
        null = True,
        blank = True
    )
    # devise
    devise = models.CharField(
        max_length = 50,
        null = True,
        blank = True
    )
    # type
    #     argent
    #     nature
    # date
    date = models.DateField(
        null = True,
        blank = True
    )
    # # recu
    # recu = models.CharField(
    #     max_length = 100,
    #     null = True,
    #     blank = True
    # )
    # observation
    obsevation = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        retour = self.desination
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_patient')# mbola amboarina

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.donateur) + slugify(self.projet) + slugify(self.date) + slugify(self.montant)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Don"