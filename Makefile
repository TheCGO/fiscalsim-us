all: build
format:
	autopep8 -r .
	black . -l 79
	linecheck . --fix
install:
	pip install -e .[dev]
	pip install --upgrade jupyter-book
test-policy:
	fiscalsim-us test fiscalsim_us/tests/policy/baseline
	fiscalsim-us test fiscalsim_us/tests/policy/contrib
test-variables:
	fiscalsim-us test fiscalsim_us/tests/test_variables.py
test:
	pytest fiscalsim_us/tests/ --maxfail=0
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/baseline/calcfunctions
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/baseline/contrib
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/baseline/demographic
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/baseline/expense
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/baseline/gov/doe
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/baseline/gov/fcc
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/baseline/gov/hhs
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/baseline/gov/hud
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/baseline/gov/irs
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/baseline/gov/ssa
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/baseline/gov/states
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/baseline/gov/usda
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/baseline/income
	coverage run -a --branch -m fiscalsim_us.tools.cli test fiscalsim_us/tests/policy/contrib

	coverage xml -i
documentation:
	jb build docs
build:
	rm fiscalsim_us/data/storage/*.h5 | true
	python setup.py sdist bdist_wheel
changelog:
	build-changelog changelog.yaml --output changelog.yaml --update-last-date --start-from 0.0.1 --append-file changelog_entry.yaml
	build-changelog changelog.yaml --org TheCGO --repo fiscalsim-us --output CHANGELOG.md --template .github/changelog_template.md
	bump-version changelog.yaml setup.py
	rm changelog_entry.yaml || true
	touch changelog_entry.yaml
