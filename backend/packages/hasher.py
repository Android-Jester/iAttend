import bcrypt

def hash_password(password: str):
    password = bytes(password,'utf-8')
    password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
    return password_hash