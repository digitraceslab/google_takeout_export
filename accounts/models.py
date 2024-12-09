import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    consent = models.BooleanField('Consented to study', default=False)
    privacy = models.BooleanField('Agreed to privacy notice', default=False)

    