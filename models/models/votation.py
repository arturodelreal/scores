from django.db import models

from models.models.constants import VOTATION_QUORUM, VOTATION_KIND, \
    VOTATION_RESULT
from models.models.sessions import DeputySession


class DeputyVotation(models.Model):

    session = models.ForeignKey(
        DeputySession,
        models.CASCADE,
        null=True,
    )

    description = models.TextField(default='')

    date = models.DateTimeField()

    quorum = models.IntegerField(
        choices=VOTATION_QUORUM
    )

    result = models.IntegerField(
        choices=VOTATION_RESULT
    )

    kind = models.IntegerField(
        choices=VOTATION_KIND
    )
