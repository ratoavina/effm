from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
from datetime import *

from . import MyUserManager


class User(AbstractBaseUser):
	name = models.CharField(max_length = 100)
	email = models.EmailField(
		unique = True,
		max_length = 255,
		blank = False
	)
	is_active = models.BooleanField(default=True)#is connected
	is_staff = models.BooleanField(default=False)#acces admin GI or no
	is_admin = models.BooleanField(default=False)#a les droits d'admin ou non
	slug = models.SlugField(null=True, blank=True)
	prenom = models.CharField(
		max_length = 100,
		null = True,
		blank = True
	)
	sexe = models.CharField(
		max_length = 5,
		null = True,
		blank = True
	)
	dtn = models.DateField(
		null=True,
		blank=True
	)
	phone = models.IntegerField(
		null = True,
		blank = True
	)
	adresse = models.CharField(
		max_length = 100,
		null = True,
		blank = True
	)
	ville = models.CharField(
		max_length = 100,
		null = True,
		blank = True
	)
	pays = models.CharField(
		max_length = 20,
		default = "Madagascar"
	)
	region = models.CharField(
		max_length = 50,
		null = True,
		blank = True
	)
	profession = models.CharField(
		max_length = 50,
		null = True,
		blank = True
	)
	date_embauche = models.DateField(
		null = True,
		blank = True
	)
	# derniere_connexion
	# Photo

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ['name']

	objects = MyUserManager()

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True
	
	# def __str__(self):
    #     retour = self.name
    #     return str(retour)

    # def get_absolute_url(self):
    #     return reverse('apply:liste_patient')# mbola amboarina

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name) + slugify(self.prenom) + slugify(self.phone)
    #     super().save(*args, **kwargs)

    # class Meta:
    #     # ordering = ['nom']
    #     verbose_name = "User"

