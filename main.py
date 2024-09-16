from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify the exact domains if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Example K-Line Data
data = {
    'timestamp': ['2024-09-01 10:00', '2024-09-01 10:01', '2024-09-01 10:02'],
    'open': [100, 102, 105],
    'high': [103, 106, 107],
    'low': [99, 101, 104],
    'close': [102, 105, 106],
    'volume': [1000, 1200, 1500]
}
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# API Endpoints
@app.get("/kline")
def get_kline():
    return df.to_dict(orient="records")

@app.get("/indicators/macd")
def get_macd():
    ema12 = df['close'].ewm(span=12, adjust=False).mean()
    ema26 = df['close'].ewm(span=26, adjust=False).mean()
    macd_line = ema12 - ema26
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
    df['macd'] = macd_line
    df['signal'] = signal_line
    return df[['timestamp', 'macd', 'signal']].to_dict(orient="records")

@app.get("/indicators/rsi")
def get_rsi():
    delta = df['close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14, min_periods=1).mean()
    avg_loss = loss.rolling(window=14, min_periods=1).mean()
    rs = avg_gain / avg_loss
    df['rsi'] = 100 - (100 / (1 + rs))
    df['rsi'] = df['rsi'].fillna(50)
    return df[['timestamp', 'rsi']].to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
