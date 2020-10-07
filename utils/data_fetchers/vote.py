from zeep import Client

from models.models import DeputyVotation, DeputyVote
from utils.data_fetchers.constants import METHODS
from utils.data_fetchers.utils import get_client


def __add_votes_for_votation(
        votation: DeputyVotation,
        client: Client,
        delete_all_previous=False
):
    method = METHODS['votation_detail']
    if delete_all_previous:
        votation.votes.delete()
    voted_deputys = set(votation.votes.values_list('deputy_id', flat=True))
    new_votes = []
    data = {
        'prmVotacionId': votation.pk
    }
    votation_detail = getattr(client.service, method)(**data)
    for vote in votation_detail.Votos.Voto:
        deputy_id = int(vote.Diputado.Id)
        if deputy_id in voted_deputys:
            continue
        resolution = vote.OpcionVoto.Valor
        new_votes.append(DeputyVote(
            deputy_id=deputy_id,
            resolution=resolution,
            votation_id=votation.pk
        ))
    DeputyVote.objects.bulk_create(new_votes)


def fill_votes(votations_filter: None):
    if votations_filter is None:
        votations_filter = {}
    votations = DeputyVotation.objects.filter(**votations_filter)
    client = get_client('legislatures')
    if client.is_err():
        return
    client = client.ok()
    for votation in votations:
        try:
            __add_votes_for_votation(votation, client)
        except AttributeError:
            print(votation.id)
