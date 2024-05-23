import requests
def get_text_from_page(url:str) -> str:

    try:
        try:
            response = requests.get(url, timeout=15)
        except requests.exceptions.Timeout:
            print(f"La solicitud a {url} tardó demasiado tiempo.")
            return None
        if response.ok:
            response_text = response.text
            return response_text
    except requests.exceptions.ConnectionError as exc:
        print("Request coneect error in get text_from_page, details :", exc)
        return None