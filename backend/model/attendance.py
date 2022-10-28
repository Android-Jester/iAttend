
from dataclasses import dataclass

@dataclass
class Attendance():
    st_reference:str
    program:str
    date:str
    time_in:str
    time_out:str
    duration:str