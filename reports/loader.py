from typing import Callable

ReportFunc = Callable[[list[dict]], list[dict]]

REPORTS: dict[str, ReportFunc] = {}


def register(name: str):
    def wrapper(func: ReportFunc) -> ReportFunc:
        REPORTS[name] = func
        return func
    return wrapper