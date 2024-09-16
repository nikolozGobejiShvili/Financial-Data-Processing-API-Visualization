# Financial Data Processing API

This project provides a backend API for processing financial market data and a frontend for visualizing the data as a K-Line chart. The service computes and returns important technical indicators like **MACD** and **RSI**, allowing real-time analysis of market data.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```bash
    cd financial-data-api
    ```

3. Install the dependencies:
    ```bash
    pip install fastapi uvicorn pandas
    ```

4. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

5. Open the `index.html` file in your browser to view the K-Line chart visualization.

## API Endpoints

- **`/kline`**: Retrieves 1-minute K-Line data.
    - **Response Example**:
      ```json
      [
        {"timestamp": "2024-09-01T10:00:00", "open": 100, "high": 103, "low": 99, "close": 102, "volume": 1000},
        {"timestamp": "2024-09-01T10:01:00", "open": 102, "high": 106, "low": 101, "close": 105, "volume": 1200},
        {"timestamp": "2024-09-01T10:02:00", "open": 105, "high": 107, "low": 104, "close": 106, "volume": 1500}
      ]
      ```

- **`/indicators/macd`**: Calculates and returns the **MACD** (Moving Average Convergence Divergence) indicator.
    - **Response Example**:
      ```json
      [
        {"timestamp": "2024-09-01T10:00:00", "macd": 0.5, "signal": 0.3},
        {"timestamp": "2024-09-01T10:01:00", "macd": 0.8, "signal": 0.5}
      ]
      ```

- **`/indicators/rsi`**: Calculates and returns the **RSI** (Relative Strength Index) indicator.
    - **Response Example**:
      ```json
      [
        {"timestamp": "2024-09-01T10:00:00", "rsi": 55},
        {"timestamp": "2024-09-01T10:01:00", "rsi": 60}
      ]
      ```

## Performance Considerations

- **Bulk Insert** for fast data ingestion.
- **Indexing** on timestamp column to optimize querying.
- **Caching** with Redis to optimize frequent data access.
