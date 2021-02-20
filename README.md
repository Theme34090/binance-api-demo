# Binance API Demo for Robowelth Internship

## Usage

### Setup

1. Register for Binance API
2. Register LINE Notify API
3. Add secrets to .env

```
LINE_SECRET=YOUR_LINE_SECRET
BINANCE_API_KEY=YOUR_BINANCE_API_KEY
BINANCE_API_SECRET=YOUR_BINANCE_API_SECRET
```

```bash
uvicorn main:app
```

### Endpoint

GET: /get_quote/?symbol=ETHBTC
will send ticker to your LINE Notify

## Model

LSTM with 30 timestep look back (30 days) and predict price of next 10 days
best acc around 0.3 but didn't save that model
trained with data from 2016 to 2021 scale with log10
something must be wrong as model acc, loss didn't improve

## Backtest

use backtrader package
test with sma 20 days cross price and sma crossover of 20 and 100 days
