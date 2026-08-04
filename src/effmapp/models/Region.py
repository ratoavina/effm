from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Region(models.Model):
    # Ketreo kely ndray aloh
    designation = models.CharField(max_length=100, null=True, blank=True)
    quantite = models.IntegerField(null=True, blank=True)
    etat = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        retour = self.desination
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_patient')# mbola amboarina

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.desination) + slugify(self.quantite) + slugify(self.etat)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Region"