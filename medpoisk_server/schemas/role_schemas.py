from enum import Enum


class Role(str, Enum):
    director = "director"
    manager = "manager"
    doctor = "doctor"
