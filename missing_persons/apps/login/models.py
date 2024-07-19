import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords

from .managers import CustomUserManager


# Create your models here.
class UserAccount(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = PhoneNumberField(null=True, blank=True)
    bio = models.TextField(verbose_name=_("Bio"), blank=True, null=True)
    history = HistoricalRecords()
    email = models.EmailField(_("Email address"), unique=True)
    username = None
    
    USERNAME_FIELD = "email"
    

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    objects = CustomUserManager()



    class Meta:
        verbose_name = _("User Account")
        verbose_name_plural = _("User Accounts")
        ordering = ("-date_joined",)

    def __str__(self) -> str:
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse("dashboard:login:staff_details", kwargs={"pk": self.pk})
