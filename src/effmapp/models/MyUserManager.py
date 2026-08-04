from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
from datetime import *


class MyUserManager(BaseUserManager):
	def create_user(self, email, name, password=None):
		if not email:
			raise ValueError("Vous devez entrer un email")

		user = self.model(
			email=self.normalize_email(email),
			name=name
		)

		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, name=None, password=None):
		user = self.create_user(
			email=email,
			password=password,
			name=name
			)
		user.is_admin = True
		user.is_staff = True
		user.save()
		return user

