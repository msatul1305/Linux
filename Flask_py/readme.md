## Smart Portfolio Rebalancer - Best-in-Class Hackathon Edition

Production-inspired Flask MVP for multi-asset portfolios (Mutual Fund, ETF, Stocks, Commodity, FX, Crypto) with institutional controls, AI forecasting, and multi-agent orchestration.

## What is now industry-standard in this version
- **Strict API validation** with deterministic 400 error responses for bad payloads.
- **Governance-aware outputs**: metadata timestamps/versioning and model-governance blueprint.
- **Execution realism**: turnover limits, trade units, and estimated transaction cost (bps).
- **Advanced risk analytics**: Volatility, Sharpe, Max Drawdown, VaR95, CVaR95, Expected Annual Return, Tracking Error.
- **Stress testing**: Monte Carlo loss probability and downside percentile terminal value.
- **Operational endpoint**: `/api/health` for deployment monitoring.

## Core Features
### Rebalancing Engine
- Input portfolio weights + market returns.
- Drift calculation from target allocation.
- Buy/Sell/Hold recommendations with threshold + turnover constraints.
- AI-assisted optimized targets using a confidence-weighted ensemble.

### Risk Engine
- Volatility (annualized)
- Sharpe ratio
- Max drawdown
- VaR (95%)
- CVaR (95%)
- Expected annual return
- Tracking error
- Monte Carlo probability of loss

### ML Layer (MVP + Scalable upgrade path)
Current dependency-light ensemble:
1. Momentum (short window mean)
2. Mean-reversion (long/short relation)
3. EWMA signal
4. Confidence scoring via return dispersion

Recommended production upgrades:
- **XGBoost/LightGBM** alpha models + SHAP explainability
- **Temporal Fusion Transformer** for multi-horizon forecasts
- **Regime classifier** (HMM or deep sequence model)
- **RL allocator** (PPO/SAC) with transaction-cost-aware reward design

### Multi-Agent Design
- Market Data Agent
- Forecast Agent
- Risk Agent
- Rebalance Optimizer Agent
- Execution Agent
- Supervisor Agent

Flow: `Supervisor -> Data -> Forecast -> Risk -> Optimizer -> Execution -> Supervisor Approval`

Governance standards included:
- model versioning / challengers / backtesting
- pre-trade risk controls
- post-trade TCA surveillance
- audit trail requirements

## Run
```bash
cd Flask_py
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## API
### `POST /api/rebalance`
```json
{
  "portfolio_value": 100000,
  "drift_threshold": 0.02,
  "turnover_limit": 0.2,
  "transaction_cost_bps": 10,
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

### `GET /api/health`
Basic health/status endpoint with metadata.

### `GET /api/multi-agent-blueprint`
Returns deployable multi-agent orchestration + governance template.

## Tests
```bash
cd Flask_py
python -m unittest test_rebalancer.py
```
