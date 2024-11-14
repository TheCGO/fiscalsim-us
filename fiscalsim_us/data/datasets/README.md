# Updating microdata

If you are updating the microdata (e.g., modifying code in `cps.py`), you will need to regenerate the processed microdata file locally and add it as a new data release.

Steps:
1. Clear old microdata with `rm fiscalsim_us/data/storage/*.h5`
2. Generate new microdata in Python with a command like this: `python -c "from fiscalsim_us.data import CPS_2023; CPS_2023().generate()"`
3. Make a copy of the new microdata file with a name that includes the _bumped_ version number. For example, if FiscalSim-US is currently version 0.2.9 and you are updating the 2023 CPS in a minor-bump PR, run `cp fiscalsim_us/data/storage/cps_2023.h5 fiscalsim_us/data/storage/cps_2023_v0_263_5.h5`.
4. Upload this new file to [github.com/TheCGO/fiscalsim-us/releases](https://github.com/TheCGO/fiscalsim-us/releases), both overwriting the existing unversioned file (delete the old one) and adding the versioned file as a new release.
5. Update the `CPS_2023` class in `fiscalsim_us/data/cps.py` to point to the new versioned file, e.g. `new_url="release://TheCGO/fiscalsim-us/v0.2.9/cps_2023_v0_2_9.h5",`.
6. Verify that this works by downloading it, e.g. `python -c "from fiscalsim_us.data import CPS_2023; CPS_2023().download()"`.
