## Smart Portfolio Rebalancer - Hackathon Edition

A full-stack Flask MVP for mutual funds / ETF / stocks / commodity / FX / crypto portfolios that:
- monitors drift from target allocation,
- recommends trades under turnover constraints,
- calculates advanced risk metrics,
- and includes an AI + multi-agent architecture blueprint.

## Features

### Core Portfolio Engine
- Input: target weights, current weights, market returns, prices.
- Drift calculator and buy/sell/hold recommendation.
- Turnover-aware trade sizing and trade units.
- Optimized AI target weights based on model confidence.

### Risk Engine
- Volatility (annualized)
- Sharpe ratio
- Max drawdown
- VaR (95%)
- CVaR (95%)
- Expected annual return
- Monte Carlo probability of loss (30-day horizon)

### ML Layer (MVP + Proposed Upgrade Path)
Current MVP uses a dependency-light ensemble:
1. Momentum model (recent rolling mean)
2. Mean-reversion model
3. EWMA signal
4. Confidence score from return dispersion

Recommended hackathon extensions:
- **XGBoost / LightGBM** for cross-asset return forecasting with features (macro, vol, momentum, valuation).
- **Temporal Fusion Transformer (TFT)** for multi-horizon forecasting.
- **Regime-switching HMM** to detect bull/bear/sideways states.
- **RL allocator (PPO/SAC)** for dynamic rebalancing with transaction costs.

### Multi-Agent Solution
The app ships with a practical orchestrated agent design:
1. Market Data Agent
2. Forecast Agent
3. Risk Agent
4. Rebalance Optimizer Agent
5. Execution Agent
6. Supervisor Agent

Flow: `Supervisor -> Data -> Forecast -> Risk -> Optimizer -> Execution -> Supervisor Approval`

## Run
```bash
cd Flask_py
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## API
### POST `/api/rebalance`
```json
{
  "portfolio_value": 100000,
  "drift_threshold": 0.02,
  "turnover_limit": 0.2,
  "assets": [
    {
      "asset": "ETF",
      "target_weight": 0.2,
      "current_weight": 0.24,
      "market_return": 0.022,
      "price": 95,
      "historical_returns": [0.01, 0.012, 0.008, 0.011, 0.022]
    }
  ]
}
```

### GET `/api/multi-agent-blueprint`
Returns a production-ready multi-agent orchestration template.

## Tests
```bash
cd Flask_py
python -m unittest test_rebalancer.py
```
