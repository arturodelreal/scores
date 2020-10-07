from typing import List

from models.models import DeputySession
from utils.data_fetchers.constants import METHODS
from utils.data_fetchers.utils import get_client


def __add_sessions_to_database(sessions: List, legislature_id):
    for session in sessions:
        __add_session(session, legislature_id)


def __add_session(session, legislature_id: int):
    defaults = {
        'init_date': session.FechaInicio,
        'number': session.Numero,
        'end_date': session.FechaTermino,
        'kind': session.Tipo.Valor,
        'status': session.Estado.Valor,
        'legislature_id': legislature_id,
    }
    DeputySession.objects.update_or_create(
        defaults=defaults,
        id=session.Id,
    )


def fill_sessions(legislatures: List[int]):
    method = METHODS['sessions_by_legislature']
    client = get_client('sessions')
    if client.is_err():
        return
    client = client.ok()
    for legislature in legislatures:
        data = {
            'prmLegislaturaId': legislature,
        }
        sessions = getattr(client.service, method)(**data)
        __add_sessions_to_database(sessions, legislature)
