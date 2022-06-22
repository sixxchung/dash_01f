from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    id: int
    name: str
    birthdate: date
    admin: bool = False


user1 = User(id=1, name="Steve Jobs", birthdate=date(1955, 2, 24))
