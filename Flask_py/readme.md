## Smart Portfolio Rebalancer - Best-in-Class Hackathon Edition

Production-inspired Flask MVP for multi-asset portfolios (Mutual Fund, ETF, Stocks, Commodity, FX, Crypto) with institutional controls, AI forecasting, and multi-agent orchestration.

## What is now industry-standard in this version
- **AI Copilot Briefing** endpoint with explainable top-priority actions and risk flags for PM/IC workflows.
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


### Multi-Agent Tandem Demo (How agents work together)

### UI Architecture View + Tandem Demo Preview
The dashboard now includes:
- **Asset drilldown interactions**: click an asset class row to view exact holdings, per-holding predictions, and rebalancing action details.
- visual multi-agent architecture cards (all agents + roles)
- orchestration flow banner
- tandem handoff timeline cards (step-by-step)
- raw tandem JSON preview for auditability
- scenario demo cards for one-click showcase runs

This makes demos immediately understandable for non-technical stakeholders while preserving technical detail for engineers.

The new tandem simulation endpoint demonstrates all agents in sequence on the same payload:
1. **Market Data Agent** ingests and validates assets.
2. **Forecast Agent** generates forecast + confidence snapshot.
3. **Risk Agent** computes risk metrics and risk flags.
4. **Rebalance Optimizer Agent** produces constrained trade plan.
5. **Execution Agent** builds staged execution queue.
6. **Supervisor Agent** approves/escalates with final narrative.

This gives a transparent, step-by-step handoff trace for demos and architecture reviews.

Governance standards included:
- model versioning / challengers / backtesting
- pre-trade risk controls
- post-trade TCA surveillance
- audit trail requirements


## Why this is a winning hackathon idea
1. **Real pain, real buyers:** Portfolio drift and risk-limit breaches are daily institutional problems.
2. **Decision speed:** Converts market movement to executable buy/sell guidance in seconds.
3. **Differentiated AI:** Combines forecasting, explainability, and a multi-agent orchestration model.
4. **Trust layer:** Risk analytics + execution cost + tandem timeline create auditability, not black-box outputs.
5. **Demo power:** Interactive architecture, scenario cards, and holding-level drilldown make judges instantly understand value.
6. **Production path:** Deployable on Docker/GitHub/GitLab with minimal friction.

## Local Run
```bash
cd Flask_py
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Host & Deploy (Production-Style)

### Option A: Docker (recommended)
```bash
cd Flask_py
docker build -t smart-portfolio-rebalancer .
docker run -p 8000:8000 -e PORT=8000 -e HOST=0.0.0.0 smart-portfolio-rebalancer
```
Open http://localhost:8000

### Option B: Docker Compose
```bash
cd Flask_py
docker compose up --build
```

### Option C: PaaS (Render / Railway / Fly.io / Heroku-like)
- App entrypoint is production-ready via `Procfile` + `wsgi.py`.
- Start command:
```bash
gunicorn --workers 2 --threads 4 --timeout 120 --bind 0.0.0.0:$PORT wsgi:app
```
- Ensure environment variables:
  - `PORT` (provided by platform)
  - `HOST=0.0.0.0`


### Option D: GitHub Actions Preview Deploy (auto preview per branch)
This repo includes GitHub workflows for CI and preview deployment:
- `.github/workflows/ci.yml` for tests and compile checks.
- `.github/workflows/deploy-preview.yml` for building/pushing image to GHCR and deploying preview branch environments.

Required GitHub Secrets:
- `PREVIEW_HOST` - VM/server hostname running Docker + Traefik.
- `PREVIEW_USER` - SSH user for deploy host.
- `PREVIEW_SSH_KEY` - private key for deployment host.
- `PREVIEW_BASE_URL` - base domain for previews (example: `preview.yourdomain.com`).

Generated preview URL pattern:
```text
https://<branch-slug>.<PREVIEW_BASE_URL>
```
Example:
```text
https://feature-rebalancer.preview.yourdomain.com
```

Troubleshooting (no live preview deployment):
- Verify all required GitHub secrets are set.
- Ensure preview host has Docker + Traefik and can pull images from GHCR.
- CI still runs via `ci.yml` even if deploy secrets are not present.


### Option E: GitLab CI Preview Deploy (also supported)
GitLab support is also included via root `.gitlab-ci.yml`.

Required GitLab CI variables:
- `PREVIEW_HOST`
- `PREVIEW_USER`
- `PREVIEW_SSH_KEY`
- `PREVIEW_BASE_URL`

Preview URL pattern:
```text
https://<CI_ENVIRONMENT_SLUG>.<PREVIEW_BASE_URL>
```

Notes:
- `review_status` always registers deployment records so GitLab does not show “No deployments”.
- `review_app` deploys live preview when secrets are configured.

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

### `GET /api/preview-scenarios`
Returns curated market scenarios for one-click dashboard preview/demo mode.

### `POST /api/ai-copilot/insights`
Returns an executive-ready AI copilot brief with top actions, risk flags, execution playbook, and cutting-edge model stack recommendations.

### `POST /api/multi-agent/tandem-demo`
Returns a full timeline showing how each agent works in tandem and what output each handoff produces.

### `GET /api/multi-agent-blueprint`
Returns deployable multi-agent orchestration + governance template.

### `asset_drilldown` response block
`POST /api/rebalance` now returns `asset_drilldown` keyed by asset class with:
- holdings list
- per-holding predicted return
- implied units/notional
- trade action and cost summary

## Tests
```bash
cd Flask_py
python -m unittest test_rebalancer.py
python -m py_compile app.py test_rebalancer.py wsgi.py
```
