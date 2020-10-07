from django.db import models

from models.models.constants import LEGISLATURE_KIND


class DeputyLegislature(models.Model):
    init_date = models.DateField()
    end_date = models.DateField()
    kind = models.IntegerField(
        choices=LEGISLATURE_KIND
    )
