from dataclasses import dataclass

@dataclass
class LoginUser():
    reference: str
    username: str
    role: str
    status: str
    password: str  

   