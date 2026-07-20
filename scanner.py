import requests
from config import DEXSCREENER_URL

def get_pairs():
    try:
        r = requests.get(DEXSCREENER_URL, timeout=10)
        r.raise_for_status()

        return r.json()["pairs"]

    except Exception as e:
        print(e)
        return []
