from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# from . import CampagneRamadan, Beneficiaire

class DistributionRamadan(models.Model):
    # # campagne
    # campagne = models.ManyToManyField(
    #     CampagneRamadan,
    #     null = True,
    #     blank = True
    # )
    # # beneficiaire
    # beneficiaire = models.ManyToManyField(
    #     Beneficiaire,
    #     null = True,
    #     blank = True
    # )
    # nbr_colis
    nbr_colis = models.IntegerField(
        null = True,
        blank = True
    )
    # poids
    poid = models.IntegerField(
        null = True,
        blank = True
    )
    # date
    date = models.DateField(
        null = True,
        blank = True
    )
    # agent
    agent = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # observation
    observation = models.CharField(
        null = True,
        blank = True
    )
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        retour = self.campagne
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_patient')# mbola amboarina

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.campagne) + slugify(self.beneficiaire) + slugify(self.date)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Distribution Ramadan"