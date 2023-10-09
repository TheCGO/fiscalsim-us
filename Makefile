all: build
format:
	black . -l 79
	linecheck . --fix
install:
	pip install -e .[dev]
test:
	coverage run -a --branch -m policyengine_core.scripts.policyengine_command test fiscalsim_us/tests/policy/ -c fiscalsim_us
	coverage xml -i
	pytest fiscalsim_us/tests/ --maxfail=0
documentation:
	jupyter-book clean docs/book
	jupyter-book build docs/book
	python fiscalsim_us/tools/add_plotly_to_book.py docs/book/_build
build:
	rm fiscalsim_us/data/storage/*.h5 | true
	python setup.py sdist bdist_wheel
changelog:
	build-changelog changelog.yaml --output changelog.yaml --update-last-date --start-from 0.0.0 --append-file changelog_entry.yaml
	build-changelog changelog.yaml --org TheCGO --repo fiscalsim-us --output CHANGELOG.md --template .github/changelog_template.md
	bump-version changelog.yaml setup.py
	rm changelog_entry.yaml || true
	touch changelog_entry.yaml
pip-package:
	pip install wheel
	python setup.py sdist bdist_wheel
