from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"]) 
 
def generate_password_hash(password: str) -> str:
    # run secret through selected algorithm, returning resulting hash.
    return password_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    # verify secret against an existing hash. 
    return password_context.verify(password, hashed_password)