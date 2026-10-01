import requests


def fetch(url):
    return requests.get(url, timeout=10).status_code


if __name__ == "__main__":
    print(fetch("https://example.com"))
