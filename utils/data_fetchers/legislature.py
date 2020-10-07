from typing import List

from models.models import DeputyLegislature
from utils.data_fetchers.constants import METHODS
from utils.data_fetchers.utils import get_client


def __add_legislatures_to_database(legislatures: List):
    for legislature in legislatures:
        __add_legislature(legislature)


def __add_legislature(legislature):
    defaults = {
        'init_date': legislature.FechaInicio.date(),
        'end_date': legislature.FechaTermino.date(),
        'kind': legislature.Tipo.Valor,
    }
    DeputyLegislature.objects.get_or_create(
        defaults=defaults,
        id=legislature.Id,
    )


def fill_legislatures():
    method = METHODS['legislatures']
    client = get_client('legislatures')
    if client.is_err():
        return
    client = client.ok()
    legislatures = getattr(client.service, method)()
    __add_legislatures_to_database(legislatures)
