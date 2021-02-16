from binance.client import Client
import os

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")
client = Client(api_key, api_secret)


def get_ticker(symbol):
    return client.get_ticker(symbol=symbol)
