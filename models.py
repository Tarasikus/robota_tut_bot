from typing import TypedDict

class Vacancy(TypedDict):
    id: int
    title: str
    description: str
    salary: str
    contact: str
    lat: float
    lng: float
    is_active: bool
    type: str
