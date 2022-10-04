from fiscalsim_us.data import CPS
import pytest
from fiscalsim_us import Microsimulation

CPS_YEARS = [2020]


@pytest.mark.dependency(name="cps")
@pytest.mark.parametrize("year", CPS_YEARS)
def test_cps_dataset_generates(year):
    CPS.generate(year)


@pytest.mark.dependency(depends=["cps"])
@pytest.mark.parametrize("year", CPS_YEARS)
def test_cps_fiscalsim_us_compatible(year):
    Microsimulation(dataset=CPS, year=year).calc("employment_income")
