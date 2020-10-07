from django.db import models

from models.models.constants import SEX_OPTIONS
from models.models.political_group import PoliticalGroup


class Deputy(models.Model):

    name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    second_last_name = models.CharField(max_length=255, default='')

    birth_date = models.DateField(null=True)

    sex = models.CharField(
        max_length=1,
        choices=SEX_OPTIONS,
        default='M'
    )

    political_group = models.ForeignKey(
        PoliticalGroup,
        models.CASCADE,
        null=True,
    )

    image = models.ImageField(null=True)
