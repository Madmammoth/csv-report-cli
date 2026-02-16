from collections import defaultdict

from reports.loader import register


@register("average-gdp")
def average_gdp(rows: list[dict]) -> list[dict]:
    totals = defaultdict(lambda: {"sum_gdp": 0, "count": 0})
    for row in rows:
        country = row["country"]
        gdp = int(row["gdp"])
        totals[country]["sum_gdp"] += gdp
        totals[country]["count"] += 1
    result = [
        {"country": c, "gdp": v["sum_gdp"] / v["count"]}
        for c, v in totals.items()
    ]
    return sorted(result, key=lambda x: x["gdp"], reverse=True)
