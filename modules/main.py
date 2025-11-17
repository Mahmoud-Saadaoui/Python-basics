import requests
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))

print(r.status_code) # 200
print("*" * 100)
print(r.headers['content-type']) # application/json
print("*" * 100)
print(r.json()) # {'authenticated': True, 'user': 'user'}
print("-" * 100)


# ---------------------------------------------------------
response = requests.get("https://api.github.com")
print(response.status_code)
print("-" * 100)
print(response.json())