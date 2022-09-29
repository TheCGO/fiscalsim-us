from openfisca_tools.data import openfisca_data_cli
from fiscalsim_us.data.datasets import DATASETS


def cli():
    openfisca_data_cli(DATASETS)
