import zeep
from requests import RequestException
from result import Result, Ok, Err

from utils.data_fetchers.constants import RESOURCE_URL


def get_client(source: str) -> Result[zeep.Client, str]:
    try:
        return Ok(zeep.Client(RESOURCE_URL[source]))
    except RequestException as error:
        return Err(str(error))
