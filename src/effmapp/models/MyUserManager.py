from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
from datetime import *


class MyUserManager(BaseUserManager):
	def create_user(self, email, name, password=None, **extra_fields):
		if not email:
			raise ValueError("Vous devez entrer un email")
		if not name:
			raise ValueError("Vous devez entrer un nom")

		user = self.model(
			email=self.normalize_email(email),
			name=name,
            **extra_fields # Manquant avant
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, name=None, password=None, **extra_fields):
		extra_fields.setdefault("is_admin", True)
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_active", True)

		user = self.create_user(
			email=email,
			password=password,
			name=name,
            **extra_fields
			)
		# user.is_admin = True
		# user.is_staff = True
		# user.save()
		return user
