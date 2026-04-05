import requests
username = 'your-github-username'
response = requests.get(f'https://api.github.com/users/{username}')
data = response.json()
print(f"Name: {data.get('name', 'N/A')}")
print(f"Public Repos: {data.get('public_repos', 0)}")
print(f"Followers: {data.get('followers', 0)}")
