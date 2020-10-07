from typing import List, Optional

from models.models import PoliticalGroup, Deputy
from utils.data_fetchers.constants import METHODS
from utils.data_fetchers.utils import get_client


def __add_deputies_to_database(deputies: List, fields: Optional[List]):
    for deputy in deputies:
        __add_deputy_with_political_group(deputy, fields)


def __add_deputy_with_political_group(deputy, fields):
    political_group = __get_political_group_by_deputy(deputy)
    defaults = {
        'name': deputy.Diputado.Nombre,
        'last_name': deputy.Diputado.ApellidoPaterno,
        'second_last_name': deputy.Diputado.ApellidoMaterno,
        'birth_date': deputy.Diputado.FechaNacimiento.date(),
        'sex': 'M' if deputy.Diputado.Sexo.Valor == 1 else 'F',
        'political_group': political_group
    }
    if fields is not None:
        defaults = {
            key: value for key, value in defaults.items()
            if key in fields
        }
    Deputy.objects.get_or_create(
        defaults=defaults,
        id=deputy.Diputado.Id,
    )


def __get_political_group_by_deputy(deputy) -> Optional[PoliticalGroup]:
    try:
        political_group_data = sorted(
            deputy.Diputado.Militancias.Militancia,
            key=lambda x: x.FechaInicio
        )[-1].Partido
    except AttributeError:
        political_group_data = None
    if political_group_data is not None:
        try:
            code = political_group_data['Id']
            name = political_group_data['Nombre']
            return PoliticalGroup.objects.get_or_create(
                defaults={'name': name},
                code=code,
            )[0]
        except KeyError:
            return None
    else:
        return None


def fill_current_deputy_data(fields=None):
    if fields is None:
        fields = []
    method = METHODS['current_deputies']
    client = get_client('deputies')
    if client.is_err():
        return
    client = client.ok()
    deputies = getattr(client.service, method)()
    __add_deputies_to_database(deputies, fields)
