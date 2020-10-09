from django.db import models

from models.models.constants import ATTENDANCE_KIND
from models.models.deputy import Deputy
from models.models.sessions import DeputySession


class DeputyAttendance(models.Model):

    deputy = models.ForeignKey(
        Deputy,
        models.CASCADE,
        related_name='attendances',
    )

    session = models.ForeignKey(
        DeputySession,
        models.CASCADE,
        related_name='attendances',
    )

    attend = models.IntegerField(
        choices=ATTENDANCE_KIND,
        null=True,
    )
