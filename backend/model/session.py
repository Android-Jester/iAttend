from dataclasses import dataclass

@dataclass
class Session():
    reference: str
    username: str
    date: str
    login: str
    logout: str
    duration: str
   