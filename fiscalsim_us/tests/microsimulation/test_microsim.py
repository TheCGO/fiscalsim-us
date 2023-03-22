def test_microsim_runs_cps():
    from fiscalsim_us import Microsimulation

    sim = Microsimulation()
    print(sim.calc("spm_unit_net_income"))
