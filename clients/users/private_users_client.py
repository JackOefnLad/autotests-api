from clients.api_client import APIClient
from clients.private_http_builder import get_authentication_client, AuthenticationDict
from httpx import Response
from typing import TypedDict
    
class UpdateDict(TypedDict):
    email:      str | None 
    lastnmae:   str | None 
    firstName:  str | None 
    middleName: str | None 

class PrivateUsersClient(APIClient):
    def get_user_me_api(self) -> Response:
        return self.get("/api/v1/users/me")
    
    def get_user_api(
            self,
            user_id: str
            ) -> Response:
        return self.get(f"/api/v1/users/{user_id}")
    
    def update_user_api(
            self, 
            user_id: str, 
            request: UpdateDict
            ) -> Response:
        return self.patch(f"/api/v1/users/{user_id}", json = request)
        
    def delete_user_api(
            self, 
            user_id: str
            ) -> Response:
        return self.delete(f"/api/v1/users/{user_id}")
    
def get_private_users_client(user: AuthenticationDict) -> PrivateUsersClient:
        return PrivateUsersClient(client=get_private_users_client())