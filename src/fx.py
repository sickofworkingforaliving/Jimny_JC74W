import requests

def get_fx_rate():
    url = "https://api.exchangerate.host/latest?base=USD"
    response = requests.get(url)
    try:
        data = response.json()
        return data["rates"]["GBP"]
    except Exception as e:
        print("FX API error:", e)
        print("Response content:", response.text)
        return None
