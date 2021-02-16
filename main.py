from pathlib import Path
from fastapi import FastAPI
import json
import os
from dotenv import load_dotenv
from binance.exceptions import BinanceAPIException

from line_notify import notify
from binance_api import get_ticker

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_quote/")
async def get_quote(symbol: str = "BTCUSDT"):
    try:
        ticker = get_ticker(symbol)
        notify(os.getenv("LINE_SECRET"),
               {"message": json.dumps(ticker)})
        return {"message": "success"}
    except BinanceAPIException as e:
        print(e)
        return {"message": e.message}
