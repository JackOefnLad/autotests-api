import httpx

login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response.status_code)
print(login_response_data)

headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(response.status_code)
print(response.json())