from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from fastapi import Request
from .utlity import decode_access_token
from fastapi.exceptions import HTTPException
from fastapi import status

class TokenBearer(HTTPBearer):
    
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)
        
    async def __call__(self, request: Request)->HTTPAuthorizationCredentials | None:
        creds = await super().__call__(request)
        
        # print(creds.scheme) # Bearer
        # print(creds.credentials) # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c

        token = creds.credentials
        
        if not self.token_validate(token):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid or Expired Token")

        return creds
        
    
    def token_validate(self, token: str)-> bool:
        token_data = decode_access_token(token)
        
        return True if token_data is not None else False
            
        
class AccessBearerToken(TokenBearer):
    pass

class AccessBearerToken(TokenBearer):
    pass