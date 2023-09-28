# nmdc_runtime/site/changesheets/assets.py
"""
assets.py: Provides software-defined assets for creating changesheets for NMDC database objects.
"""
from contextlib import contextmanager
from dagster import asset, ConfigurableResource, EnvVar
from nmdc_runtime.site.resources import GoldApiClient
from typing import Iterator

GOLD_NEON_SOIL_STUDY_ID = "Gs0144570"


class GoldApiResource(ConfigurableResource):
    """
    Resource for fetching GOLD biosamples
    """
    base_url: str = EnvVar("GOLD_API_BASE_URL")
    username: str = EnvVar("GOLD_API_USERNAME")
    password: str = EnvVar("GOLD_API_PASSWORD")

    @contextmanager
    def get_client(self) -> Iterator[GoldApiClient]:
        """
        Get a GOLD API client
        :return: GoldApiClient
        """
        client = GoldApiClient(
            base_url=self.base_url,
            username=self.username,
            password=self.password,
        )
        yield client


@asset
def gold_biosamples_by_study(gold_api_resource: GoldApiResource) -> None:
    """
    Biosamples for a GOLD study
    """
    with gold_api_resource.get_client() as client:
        yield client.get_biosamples_by_study(GOLD_NEON_SOIL_STUDY_ID)
