import requests

def ticker_lookup(name):
    """
    https://www.worldtradingdata.com/api/v1/stock?symbol=AAPL,MSFT,HSBA.L&api_token=demo
    """
    wtd_key = "eCK0L4fxRNlDXtZYTrn7m7lr7Ps1oLc3JJ8uMxhcRls8XZOS0VFZcWtnFeK3"

    addr = "https://www.worldtradingdata.com/api/v1/stock"

    params = {
        "symbol":name,
        "api_token":wtd_key
    }

    r = requests.get(addr,params=params)

    return r.json()["data"][0]["name"]
