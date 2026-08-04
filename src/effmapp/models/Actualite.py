from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Actualite(models.Model):
    titre = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    resume = models.CharField(
        null = True,
        blank = True
    )
    contenu = models.CharField(
        null = True,
        blank = True
    )
    auteur = models.CharField(
        max_length = 50,  
        null = True,
        blank = True
    )
    # dt_pub = models.DateField(
    #     null = True,
    #     blank = True
    # )
    slug = models.SlugField(
        null=True,
        blank=True
    )
    # visible
    # image

    def __str__(self):
        retour = self.titre
        return str(retour)

    def get_absolute_url(self):
        return reverse('apply:liste_patient')# mbola amboarina

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre) + slugify(self.resume) + slugify(self.auteur)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Actualite"