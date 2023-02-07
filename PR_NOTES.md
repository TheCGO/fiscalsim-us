# Rick's notes for PR

## Name mappings
* "master" to "main"
* "policyengine-us" to "fiscalsim-us"

## Files in PolicyEngine excluded from this PR
* `.github/update_api.py`: This file updates the PolicyEngine-US package version used by the PolicyEngine-API repository.
* In `.github/workflows/push.yaml`, I leave out `Deploy Documentation`, `Publish`, and `Deploy` actions.
