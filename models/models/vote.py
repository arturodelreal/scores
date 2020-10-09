from typing import Dict, List

from django.db import models

from models.models.constants import RESOLUTIONS
from models.models.deputy import Deputy
from models.models.votation import DeputyVotation


class DeputyVote(models.Model):

    RESOLUTION_CONVERSION = {
        0: 0,
        1: 100,
    }

    EMPTY_RESOLUTION = 50

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

    @classmethod
    def to_dict(cls) -> Dict:
        new_dict = {}
        for vote in cls.objects.iterator():
            if vote.deputy_id not in new_dict:
                new_dict[vote.deputy_id] = {}

            new_dict[
                vote.deputy_id
            ][vote.votation_id] = cls.RESOLUTION_CONVERSION.get(
                vote.resolution,
                cls.EMPTY_RESOLUTION,
            )
        return new_dict

    @classmethod
    def to_csv(cls) -> List[List[str]]:
        headers = [
            'deputy_id',
            *map(
                str,
                DeputyVotation.objects.order_by('id').values_list(flat=True)
            )
        ]
        new_csv = [headers]
        print()
        new_row = []
        for vote in cls.objects.order_by('deputy_id',
                                         'votation_id').iterator():
            if not new_row:
                new_row.append(str(vote.deputy_id))
            new_row.append(cls.RESOLUTION_CONVERSION.get(
                vote.resolution,
                cls.EMPTY_RESOLUTION,
            ))
            if len(new_row) == len(headers):
                new_csv.append(new_row)
                new_row = []
        return new_csv
