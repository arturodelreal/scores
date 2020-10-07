from datetime import datetime
from typing import List

from models.models import DeputyVotation
from utils.data_fetchers.constants import METHODS
from utils.data_fetchers.utils import get_client


MINIMUM_DATE = datetime(2018, 3, 11)


def __add_votations_to_database(votations: List):
    for votation in votations:
        __add_votation(votation)


def __add_votation(votation):
    if votation.Fecha < MINIMUM_DATE:
        return
    result = votation.Resultado
    defaults = {
        'description': votation.Descripcion,
        'date': votation.Fecha,
        'quorum': votation.Quorum.Valor,
        'kind': votation.Tipo.Valor,
        'result': result.Valor if result is not None else 9,
    }
    DeputyVotation.objects.update_or_create(
        defaults=defaults,
        id=votation.Id,
    )


def fill_votations(years: List[int]):
    method = METHODS['votations_by_year']
    client = get_client('legislatures')
    if client.is_err():
        return
    client = client.ok()
    for year in years:
        data = {
            'prmAnno': year,
        }
        votations = getattr(client.service, method)(**data)
        __add_votations_to_database(votations)
