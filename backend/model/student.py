from dataclasses import dataclass

@dataclass
class Student():
    reference: int
    index_: int
    firstname: str
    lastname: str
    college: str
    program: str
    nationality: str
    start_date: str
    end_date: str