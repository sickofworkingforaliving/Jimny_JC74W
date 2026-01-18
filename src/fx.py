import requests

def get_fx_rate():
    url = "https://api.exchangerate.host/latest?base=JPY&symbols=GBP"
    r = requests.get(url)
    data = r.json()
    return data["rates"]["GBP"]
