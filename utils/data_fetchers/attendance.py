from zeep import Client

from models.models import DeputySession, DeputyAttendance
from utils.data_fetchers.constants import METHODS
from utils.data_fetchers.utils import get_client


def __add_attendance_for_session(
        session: DeputySession,
        client: Client,
        delete_all_previous=False
):
    method = METHODS['attendance_by_session']
    if delete_all_previous:
        session.attendances.delete()
    deputys = set(session.attendances.values_list(
        'deputy_id', flat=True
    ))
    new_attendances = []
    data = {
        'prmSesionId': session.pk
    }
    attendances_detail = getattr(client.service, method)(**data)
    for attendance in attendances_detail.ListadoAsistencia.Asistencia:
        deputy_id = int(attendance.Diputado.Id)
        if deputy_id in deputys:
            continue
        attend = attendance.TipoAsistencia.Valor
        new_attendances.append(DeputyAttendance(
            deputy_id=deputy_id,
            attend=attend,
            session_id=session.pk
        ))
    DeputyAttendance.objects.bulk_create(new_attendances)


def fill_attendances(session_filter: None):
    if session_filter is None:
        session_filter = {}
    sessions = DeputySession.objects.filter(**session_filter)
    client = get_client('sessions')
    if client.is_err():
        return
    client = client.ok()
    for session in sessions:
        __add_attendance_for_session(session, client)

