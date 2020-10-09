from django.utils.translation import gettext as _

# this is binary because the data given is binary, please don't judge me
SEX_OPTIONS = (
    ('M', _('Hombre')),
    ('F', _('Mujer')),
)

COLORS = (
    ('red', 'red'),
)

RESOLUTIONS = (
    (0, _('En Contra')),
    (1, _('Afirmativo')),
    (2, _('Abstención')),
    (3, _('Dispensado')),
    (4, _('No Vota')),
)

LEGISLATURE_KIND = (
    (1, _('Ordinaria')),
    (2, _('Extraordinaria')),
    (3, '-'),
)

SESSION_KIND = (
    (1, _('Ordinaria')),
    (2, _('Especial')),
    (3, _('Congreso Pleno')),
    (4, _('De Instalación')),
    (5, _('Pedida')),
)

SESSION_STATUS = (
    (0, _('Citada')),
    (1, _('Celebrada')),
    (2, _('Fracasada')),
)

VOTATION_KIND = (
    (1, _('Proyecto de Ley')),
    (2, _('Proyecto de Resolución')),
    (3, _('Proyecto de Acuerdo')),
    (4, _('Otros')),
)

VOTATION_QUORUM = (
    (1, _('Quorum Simple')),
    (2, _('Quorum Calificado')),
    (3, _('Reforma Constitucional 2/3')),
    (4, _('Reforma Constitucional 3/5')),
    (5, _('Ley Orgánica Constitucional')),
    (6, _('Ley Interpretativa')),
    (7, _('3/5')),
    (8, _('2/5')),
    (9, _('1/3')),
    (10, _('2/3')),
)

VOTATION_RESULT = (
    (0, _('Rechazado')),
    (1, _('Aprobado')),
    (2, _('Unánime')),
    (3, _('Empate')),
    (4, _('Sin Quorum')),
    (9, _('Sin Resultado')),
)

ATTENDANCE_KIND = (
    (0, _('No Asiste')),
    (1, _('Asiste')),
    (2, _('Justificado')),
)
