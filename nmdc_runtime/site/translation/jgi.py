"""
Translates EMSL data into JSON conformant with the NMDC JSON schema
"""
from dagster import op, graph

from nmdc_runtime.lib.nmdc_etl_class import NMDC_ETL
from nmdc_runtime.site.translation.util import (
    load_nmdc_etl_class,
    load_mongo_collection,
    preset_prod,
    preset_test,
)


@op
def transform_jgi_data_object(_context, nmdc_etl: NMDC_ETL) -> tuple:
    return "jgi.data_object_set", nmdc_etl.transform_jgi_data_object()


@graph
def jgi():
    nmdc_etl = load_nmdc_etl_class()
    jgi_data_object = transform_jgi_data_object(nmdc_etl)
    load_mongo_collection(jgi_data_object)


jgi_job = jgi.to_job(**preset_prod)
test_jgi_job = jgi.to_job(**preset_test)
