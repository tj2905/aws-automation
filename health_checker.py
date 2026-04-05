import requests
from datetime import datetime
def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            status = "UP"
            emoji = "✅"
        else:
            status = f"ISSUE ({response.status_code})"
            emoji = "⚠️"

        time_taken = round(response.elapsed.total_seconds(), 2)

        return {
            'url': url,
            'status': status,
            'emoji': emoji,
            'response_time': time_taken
 }

    except requests.exceptions.ConnectionError:
        return {
            'url': url,
            'status': 'DOWN',
            'emoji': '❌',
            'response_time': None
        }
    except requests.exceptions.Timeout:
        return {
            'url': url,
            'status': 'TIMEOUT',
            'emoji': '⏱️',
            'response_time': None
        }
def run_health_check():
    websites = [
        'https://google.com',
        'https://github.com',
        'https://dev.to',
        'https://hub.docker.com',
        'https://this-site-does-not-exist-xyz.com'
    ]

    print("=" * 50)
    print(f"Website Health Check")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    results = []
    for url in websites:
        result = check_website(url)
        results.append(result)

        if result['response_time']:
            print(f"{result['emoji']} {result['url']}")
            print(f" Status: {result['status']}")
            print(f" Response Time: {result['response_time']}s")
        else:
            print(f"{result['emoji']} {result['url']}")
            print(f" Status: {result['status']}")

    print("\nSummary:")
    up = sum(1 for r in results if r['status'] == 'UP')
    down = sum(1 for r in results if r['status'] in ['DOWN', 'TIMEOUT'])
    print(f" UP: {up}")
    print(f" DOWN/TIMEOUT: {down}")
    print("=" * 50)
run_health_check()
