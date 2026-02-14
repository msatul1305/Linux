## Smart Portfolio Rebalancer (Flask MVP)

### Features
- Input portfolio target/current weights and market returns across asset classes (Mutual Fund, ETF, Stocks, Commodity, FX, Crypto, etc.).
- Calculates allocation drift from target weights.
- Suggests buy/sell/hold actions using configurable drift thresholds.
- Computes portfolio risk metrics: volatility, Sharpe ratio, and max drawdown.
- Includes a simple UI dashboard with a field editor for assets.

### Run
```bash
cd Flask_py
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000.

### API
`POST /api/rebalance`

Sample request body:
```json
{
  "portfolio_value": 100000,
  "drift_threshold": 0.02,
  "assets": [
    {"asset": "ETF", "target_weight": 0.2, "current_weight": 0.24, "market_return": 0.022}
  ]
}
```

### Tests
```bash
cd Flask_py
python -m unittest test_rebalancer.py
```
