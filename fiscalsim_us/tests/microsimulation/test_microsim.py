import numpy as np
from fiscalsim_us import Microsimulation
from policyengine_core.reforms import Reform
from policyengine_core.periods import instant
import pytest


"""
In US nationwide simulations, use reported state income tax liabilities
"""


def use_reported_state_income_tax(parameters):
    parameters.simulation.reported_state_income_tax.update(
        start=instant("2024-01-01"), stop=instant("2100-12-31"), value=True
    )
    return parameters


class baseline_reform(Reform):
    def apply(self):
        self.modify_parameters(use_reported_state_income_tax)


@pytest.mark.skipif(True, reason="This test temporarily suspended.")
def test_microsim_runs_cps():
    sim = Microsimulation(reform=baseline_reform)
    hnet = sim.calc("household_net_income", period=2024, map_to="person")
    assert not hnet.isna().any(), "Some households have NaN net income."
    hidecile = sim.calc(
        "household_income_decile", period=2024, map_to="person"
    )
    assert np.all(hidecile >= 1) and np.all(hidecile <= 10)
    sidecile = sim.calc("spm_unit_income_decile", period=2024, map_to="person")
    assert np.all(sidecile >= 1) and np.all(sidecile <= 10)
    idecile = sim.calc("income_decile", period=2024, map_to="person")
    assert np.all(idecile >= 1) and np.all(idecile <= 10)
