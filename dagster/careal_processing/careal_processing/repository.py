from dagster import repository
from careal_processing.pipelines.my_pipeline import my_pipeline
from careal_processing.schedules.my_hourly_schedule import my_hourly_schedule
from careal_processing.sensors.my_sensor import my_sensor


@repository
def careal_processing():
    """
    The repository definition for this careal_processing Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    pipelines = [my_pipeline]
    schedules = [my_hourly_schedule]
    sensors = [my_sensor]

    return pipelines + schedules + sensors
