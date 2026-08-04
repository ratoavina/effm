from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Materiel(models.Model):
    # nom
    nom = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # categorie
    categorire = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # numero_serie
    sn = models.IntegerField(
        null = True,
        blank = True
    )
    # marque
    marque = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # modele
    modele = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # etat
    etat = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    # date_achat
    date_achat = models.DateField(
        null = True,
        blank = True
    )
    # valeur
    valeur = models.IntegerField(
        null = True,
        blank = True
    )
    # localisation
    localisation = models.CharField(
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
    # observation
    observation = models.CharField(
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
            self.slug = slugify(self.nom) + slugify(self.sn) + slugify(self.etat) + slugify(self.marque) + slugify(self.modele)
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['nom']
        verbose_name = "Materiel"