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
