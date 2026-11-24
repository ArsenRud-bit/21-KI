import requests


def demo_requests():
    try:
        response = requests.get("https://api.github.com", timeout=5)
        print("Статус відповіді:", response.status_code)
    except requests.RequestException as e:
        print("Не вдалося зробити запит:", e)