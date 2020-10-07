from django.db import models

from models.models.constants import COLORS


class PoliticalGroup(models.Model):

    code = models.CharField(
        max_length=8,
        primary_key=True,
    )

    name = models.CharField(
        max_length=255
    )

    color = models.CharField(
        max_length=32,
        choices=COLORS,
        null=True
    )
