import requests
# Simple GET request
response = requests.get('https://google.com')
print(f"Status Code: {response.status_code}")
print(f"Response Time: {response.elapsed.total_seconds()}s")
# Status codes samjho
if response.status_code == 200:
    print("Website UP hai")
elif response.status_code == 404:
    print("Page nahi mila")
elif response.status_code == 500:
    print("Server error")
