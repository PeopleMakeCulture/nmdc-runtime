"""
Translating an export of the JGI GOLD [1] database of SQL tables to the NMDC database JSON schema.

[1] Genomes OnLine Database (GOLD) <https://gold.jgi.doe.gov/>.
"""

from dagster import pipeline

from nmdc_runtime.solids.core import local_file_to_api_object
from nmdc_runtime.solids.gold_translation import build_merged_db, run_etl

from nmdc_runtime.pipelines.core import (
    mode_normal,
    preset_normal_env,
)


@pipeline(mode_defs=[mode_normal], preset_defs=[preset_normal_env])
def gold_translation():
    local_file_to_api_object(run_etl(build_merged_db()))


@pipeline(mode_defs=[mode_normal], preset_defs=[preset_normal_env])
def gold_translation_curation():
    # TODO
    #   solid that
    #   - finds (claimed job) op for this site with workflow.id "gold-translation-1.0.0"
    #   - gets /objects id for gold_etl_latest from config
    #   - passes this id to next solid
    #   solid that
    #   - loads /objects/{id}
    #   - does stuff!
    pass
