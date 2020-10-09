RESOURCE_URL = {
    'deputies': 'http://opendata.camara.cl/camaradiputados/WServices/'
                'WSDiputado.asmx?WSDL',
    'legislatures': 'http://opendata.camara.cl/camaradiputados/'
                    'WServices/WSLegislativo.asmx?WSDL',
    'sessions': 'http://opendata.camara.cl/camaradiputados/'
                'WServices/WSSala.asmx?WSDL',
}

METHODS = {
    'current_deputies': 'retornarDiputadosPeriodoActual',
    'legislatures': 'retornarLegislaturas',
    'sessions_by_legislature': 'retornarSesionesXLegislatura',
    'votations_by_year': 'retornarVotacionesXAnno',
    'votation_detail': 'retornarVotacionDetalle',
    'attendance_by_session': 'retornarSesionAsistencia',
}
