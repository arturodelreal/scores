from django.db import models

from models.models.constants import RESOLUTIONS
from models.models.deputy import Deputy
from models.models.votation import DeputyVotation


class DeputyVote(models.Model):

    deputy = models.ForeignKey(
        Deputy,
        models.CASCADE,
        related_name='votes',
    )

    votation = models.ForeignKey(
        DeputyVotation,
        models.CASCADE,
        related_name='votes',
    )

    resolution = models.IntegerField(
        choices=RESOLUTIONS,
        null=True,
    )
