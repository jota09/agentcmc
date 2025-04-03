import os
import requests
from dotenv import load_dotenv

# You can define your COINMARKETCAP_API_KEY value as a secret or environment variable
load_dotenv()
COINMARKETCAP_API_KEY = os.environ.get("COINMARKETCAP_API_KEY","YOUR_CMC_API_KEY")
COINMARKETCAP_URL = os.environ.get("COINMARKETCAP_URL","YOUR_CMC_API_URL")

# Validar que las variables de entorno estén configuradas
if COINMARKETCAP_API_KEY is None or COINMARKETCAP_API_KEY == "YOUR_CMC_API_KEY":
    raise ValueError(
        "You need to provide an API key"
    )

if COINMARKETCAP_URL is None or COINMARKETCAP_URL == "YOUR_CMC_API_URL":
    raise ValueError(
        "You need to provide an API url"
    )

# Send slug to cmc to return the price of asset
async def get_share_price(symbol: str):
    """Retrieves cryptocurrency price for the specific share symbol"""
    api_key = COINMARKETCAP_API_KEY
    base_url = COINMARKETCAP_URL

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": api_key,
    }
    
    querystring = {"slug":symbol,"convert":"USD"}

    response = requests.get(base_url, headers=headers, params=querystring)
    data = response.json()
    try:
        first_key = next(iter(data["data"]))
        price = round(data["data"][first_key]["quote"]["USD"]["price"],3)
        message = f"The current price of {symbol} is {price} USD"
    except:
        message = f"Failed to retrieve share price for {symbol}"
    return message
