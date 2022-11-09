import json
import yaml
import argparse

TAXCALC_PARAM_FILE = (
    "/home/nikhil/pslmodels/Tax-Calculator/taxcalc/policy_current_law.json"
)

MARS_map = {
    "single": "SINGLE",
    "mjoint": "JOINT",
    "mseparate": "SEPARATE",
    "headhh": "HEAD_OF_HOUSEHOLD",
    "widow": "WIDOW",
}


def year_to_date(year: int) -> str:
    return f"{year}-01-01"


def convert_param(param: dict) -> dict:
    result = dict(description=param["title"], values={})
    for value in param["value"]:
        date = year_to_date(value["year"])
        val = float(value["value"])
        if "MARS" not in value:
            result["values"][date] = val
        else:
            mars = MARS_map[value["MARS"]]
            if mars not in result:
                result[mars] = dict(values={date: val})
            else:
                result[mars]["values"][date] = val
    result["metadata"] = dict(
        unit=USD,
    )
    if result["values"] == {}:
        del result["values"]
    return yaml.dump(result, sort_keys=False).replace("'", "")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Utility to convert tax-calculator parameters to FiscalSim parameters."
    )
    parser.add_argument(
        "--tc-params",
        default=TAXCALC_PARAM_FILE,
        help="Path to the tax-calculator policy_current_law.json file.",
    )
    parser.add_argument(
        "parameter", help="The name of the parameter to convert"
    )
    args = parser.parse_args()

    with open(args.tc_params, "r") as f:
        tc = json.load(f)

    print(convert_param(tc[args.parameter]))
