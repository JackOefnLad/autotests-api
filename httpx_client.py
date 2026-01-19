import httpx 
import httpx
import os

os.environ["NO_PROXY"] = "*"  # отключение прокси

login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response.status_code)
print(login_response_data)

# -----------------------------------------------------------
client = httpx.Client(
    base_url = "http://localhost:8000",
    timeout=2,
    headers = {"Authentication":f"Bearer {login_response_data['token']['accessToken']}"}
    )

get_user_me_response = client.get("/api/v1/users/me")

print(get_user_me_response.status_code)
# print(get_user_me_response.text)
print(get_user_me_response.json())