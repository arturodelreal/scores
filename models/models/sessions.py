from django.db import models

from models.models import DeputyLegislature
from models.models.constants import SESSION_KIND, SESSION_STATUS


class DeputySession(models.Model):
    number = models.IntegerField()
    init_date = models.DateTimeField()
    end_date = models.DateTimeField()
    kind = models.IntegerField(
        choices=SESSION_KIND,
    )
    status = models.IntegerField(
        choices=SESSION_STATUS,
    )
    legislature = models.ForeignKey(
        DeputyLegislature,
        models.CASCADE,
    )
