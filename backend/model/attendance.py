
from dataclasses import dataclass

@dataclass
class Attendance():
    student_reference: str
    student_college: str
    student_faculty: str
    student_program: str
    student_category: str
    student_nationality: str
    student_gender: str
    student_disability: str
    date_stamp: str
    time_in: str
    time_out: str
    duration: str