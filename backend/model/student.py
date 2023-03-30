from dataclasses import dataclass

@dataclass
class Student():
    student_reference: str
    student_index: str
    student_firstname: str
    student_lastname: str
    student_nationality: str
    student_gender: str
    student_disability: str
    card_issued_date: str
    card_expiry_date: str