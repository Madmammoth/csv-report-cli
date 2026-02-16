import pkgutil

import reports
from reports.average_gdp import average_gdp
from reports.loader import REPORTS


def test_average_gdp_basic():
    rows = [
        {"country": "A", "year": "2023", "gdp": "10"},
        {"country": "A", "year": "2022", "gdp": "20"},
        {"country": "B", "year": "2023", "gdp": "20"},
        {"country": "B", "year": "2022", "gdp": "20"},
        {"country": "C", "year": "2023", "gdp": "10"},
        {"country": "C", "year": "2022", "gdp": "30"},
    ]

    result = average_gdp(rows)

    assert result == [
        {"country": "B", "gdp": 20.0},
        {"country": "C", "gdp": 20.0},
        {"country": "A", "gdp": 15.0},
    ]


def test_all_modules_registered():
    module_names = {
        m.name.replace("_", "-")
        for m in pkgutil.iter_modules(reports.__path__)
        if m.name != "loader"
    }
    assert module_names.issubset(REPORTS.keys())
