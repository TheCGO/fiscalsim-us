# Rick's notes for PR

## Name mappings
* "master" to "main"
* "policyengine-us" to "fiscalsim-us"

## Question name mappings
* "OpenFisca"

## Files in PolicyEngine excluded from this PR
* `.github/update_api.py`: This file updates the PolicyEngine-US package version used by the PolicyEngine-API repository. This file is only referenced in the deleted `.github/update_api.py`.
* In `.github/workflows/push.yaml`, I leave out `Deploy Documentation`, `Publish`, and `Deploy` actions.
