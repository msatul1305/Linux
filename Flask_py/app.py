from __future__ import annotations

import os
import random
from datetime import datetime, timezone
from math import sqrt
from statistics import mean, stdev
from typing import Any

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

TRADING_DAYS = 252


class ValidationError(ValueError):
    """Raised when incoming payload violates contract."""


def risk_mitigation(inputs):
    results = []
    for input_data in inputs:
        n, _ = map(int, input_data[0].split())
        a_values = list(map(int, input_data[1].split()))
        results.append(calculate(n, a_values))
    return results


def calculate(strategies, input_values):
    n = len(input_values)
    max_diff_array = [0] * n

    for i in range(n - 1, 0, -1):
        max_diff = 0
        for j in range(i - 1, -1, -1):
            max_diff = max(max_diff, input_values[i] - input_values[j])
        max_diff_array[i] = max_diff

    max_diff_array.sort(reverse=True)
    return sum(max_diff_array[:strategies])


def _safe_float(value: Any, fallback: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return fallback


def _normalize_weights(raw_weights: list[float]) -> list[float]:
    total = sum(raw_weights)
    if total <= 0:
        return [0.0 for _ in raw_weights]
    return [w / total for w in raw_weights]


def _validate_payload(payload: dict[str, Any]) -> None:
    assets = payload.get("assets")
    if not isinstance(assets, list) or not assets:
        raise ValidationError("'assets' must be a non-empty array.")

    drift_threshold = _safe_float(payload.get("drift_threshold", 0.02), 0.02)
    turnover_limit = _safe_float(payload.get("turnover_limit", 0.2), 0.2)
    portfolio_value = _safe_float(payload.get("portfolio_value", 0.0), 0.0)

    if not (0 <= drift_threshold <= 0.5):
        raise ValidationError("'drift_threshold' must be between 0 and 0.5.")
    if not (0 < turnover_limit <= 1.0):
        raise ValidationError("'turnover_limit' must be between 0 (exclusive) and 1.")
    if portfolio_value <= 0:
        raise ValidationError("'portfolio_value' must be greater than 0.")

    for idx, asset in enumerate(assets):
        if not isinstance(asset, dict):
            raise ValidationError(f"assets[{idx}] must be an object.")
        name = str(asset.get("asset", "")).strip()
        if not name:
            raise ValidationError(f"assets[{idx}].asset is required.")

        for field in ("target_weight", "current_weight"):
            val = _safe_float(asset.get(field), -1.0)
            if val < 0:
                raise ValidationError(f"assets[{idx}].{field} must be >= 0.")

        price = _safe_float(asset.get("price", 100.0), 100.0)
        if price <= 0:
            raise ValidationError(f"assets[{idx}].price must be > 0.")


def _default_holdings_for_asset(asset_name: str, price: float) -> list[dict[str, Any]]:
    presets = {
        "Mutual Fund": [("Bluechip Basket", 0.45), ("Midcap Growth", 0.35), ("Defensive Value", 0.20)],
        "ETF": [("S&P 500 ETF", 0.50), ("Nasdaq ETF", 0.30), ("Quality ETF", 0.20)],
        "Stocks": [("AAPL", 0.35), ("MSFT", 0.33), ("NVDA", 0.32)],
        "Commodity": [("Gold", 0.55), ("Silver", 0.25), ("Energy Basket", 0.20)],
        "FX": [("USDINR", 0.40), ("EURUSD", 0.35), ("GBPUSD", 0.25)],
        "Crypto": [("BTC", 0.60), ("ETH", 0.30), ("SOL", 0.10)],
    }
    rows = presets.get(asset_name, [(f"{asset_name} Core", 0.50), (f"{asset_name} Growth", 0.30), (f"{asset_name} Tactical", 0.20)])
    return [
        {
            "holding": h,
            "holding_weight": round(w, 4),
            "last_price": round(price * (0.85 + idx * 0.08), 4),
        }
        for idx, (h, w) in enumerate(rows)
    ]


def _build_asset_drilldown(asset: dict[str, Any], weight: dict[str, Any], trade: dict[str, Any], portfolio_value: float) -> dict[str, Any]:
    name = weight.get("asset", "Unknown")
    price = max(0.01, _safe_float(asset.get("price", 100.0), 100.0))
    holdings = asset.get("holdings")
    if not isinstance(holdings, list) or not holdings:
        holdings = _default_holdings_for_asset(name, price)

    enriched_holdings = []
    for row in holdings:
        holding_name = row.get("holding", "Unknown Holding")
        holding_weight = _safe_float(row.get("holding_weight", 0.0), 0.0)
        last_price = max(0.01, _safe_float(row.get("last_price", price), price))
        implied_notional = portfolio_value * max(0.0, weight.get("current_weight", 0.0)) * max(0.0, holding_weight)
        implied_units = implied_notional / last_price
        enriched_holdings.append(
            {
                "holding": holding_name,
                "holding_weight": round(holding_weight, 4),
                "last_price": round(last_price, 4),
                "implied_notional": round(implied_notional, 2),
                "implied_units": round(implied_units, 4),
                "predicted_return": round(weight.get("forecast_return", 0.0) * (0.8 + holding_weight), 4),
                "rebalance_action": trade.get("action", "Hold"),
            }
        )

    return {
        "asset": name,
        "summary": {
            "current_weight": weight.get("current_weight", 0.0),
            "target_weight": weight.get("target_weight", 0.0),
            "optimized_target_weight": weight.get("optimized_target_weight", 0.0),
            "forecast_return": weight.get("forecast_return", 0.0),
            "forecast_confidence": weight.get("forecast_confidence", 0.0),
            "drift": weight.get("drift", 0.0),
            "trade_action": trade.get("action", "Hold"),
            "trade_value": trade.get("trade_value", 0.0),
            "trade_units": trade.get("trade_units", 0.0),
            "estimated_cost": trade.get("estimated_cost", 0.0),
        },
        "holdings": enriched_holdings,
    }


def calculate_risk_metrics(portfolio_returns: list[float], risk_free_rate: float = 0.0) -> dict[str, float]:
    if not portfolio_returns:
        return {
            "volatility": 0.0,
            "sharpe": 0.0,
            "max_drawdown": 0.0,
            "var_95": 0.0,
            "cvar_95": 0.0,
            "expected_annual_return": 0.0,
            "tracking_error": 0.0,
        }

    volatility = stdev(portfolio_returns) * sqrt(TRADING_DAYS) if len(portfolio_returns) > 1 else 0.0
    avg_return = mean(portfolio_returns)
    sharpe = ((avg_return * TRADING_DAYS) - risk_free_rate) / volatility if volatility > 0 else 0.0

    cumulative = 1.0
    peak = 1.0
    max_drawdown = 0.0
    for ret in portfolio_returns:
        cumulative *= 1 + ret
        peak = max(peak, cumulative)
        drawdown = (cumulative - peak) / peak
        max_drawdown = min(max_drawdown, drawdown)

    sorted_returns = sorted(portfolio_returns)
    var_index = max(0, int(0.05 * (len(sorted_returns) - 1)))
    var_95 = sorted_returns[var_index]
    tail = [ret for ret in sorted_returns if ret <= var_95]
    cvar_95 = mean(tail) if tail else var_95

    benchmark = mean(portfolio_returns)
    active = [r - benchmark for r in portfolio_returns]
    tracking_error = stdev(active) * sqrt(TRADING_DAYS) if len(active) > 1 else 0.0

    return {
        "volatility": round(volatility, 4),
        "sharpe": round(sharpe, 4),
        "max_drawdown": round(abs(max_drawdown), 4),
        "var_95": round(abs(var_95), 4),
        "cvar_95": round(abs(cvar_95), 4),
        "expected_annual_return": round(avg_return * TRADING_DAYS, 4),
        "tracking_error": round(tracking_error, 4),
    }


def _model_forecast(asset: dict[str, Any]) -> dict[str, float]:
    historical = asset.get("historical_returns", [])
    hist = [_safe_float(v) for v in historical if isinstance(v, (int, float, str))]
    if not hist:
        baseline = _safe_float(asset.get("market_return", 0.0))
        return {
            "momentum": baseline,
            "mean_reversion": baseline,
            "ewma": baseline,
            "ensemble": baseline,
            "confidence": 0.35,
        }

    short = hist[-min(5, len(hist)):]
    long = hist[-min(20, len(hist)):]
    short_mean = mean(short)
    long_mean = mean(long)

    momentum = short_mean
    mean_reversion = long_mean - 0.5 * (short_mean - long_mean)
    ewma = 0.0
    alpha = 0.35
    for value in hist:
        ewma = alpha * value + (1 - alpha) * ewma

    ensemble = 0.5 * momentum + 0.25 * mean_reversion + 0.25 * ewma
    dispersion = stdev(hist) if len(hist) > 1 else abs(ensemble)
    confidence = max(0.1, min(0.95, 1 - (dispersion * 8)))

    return {
        "momentum": round(momentum, 5),
        "mean_reversion": round(mean_reversion, 5),
        "ewma": round(ewma, 5),
        "ensemble": round(ensemble, 5),
        "confidence": round(confidence, 3),
    }


def _generate_house_view(assets: list[dict[str, Any]]) -> dict[str, Any]:
    model_outputs = []
    for asset in assets:
        forecast = _model_forecast(asset)
        model_outputs.append({"asset": asset.get("asset", "Unknown"), **forecast})

    winners = sorted(model_outputs, key=lambda a: a["ensemble"], reverse=True)[:3]
    laggards = sorted(model_outputs, key=lambda a: a["ensemble"])[:3]
    return {
        "asset_forecasts": model_outputs,
        "top_conviction_buys": [w["asset"] for w in winners],
        "risk_reduction_candidates": [l["asset"] for l in laggards],
        "proposed_models": [
            "Time-series ensemble (Momentum + Mean Reversion + EWMA)",
            "Regime classifier (bull / bear / sideways) using volatility + trend features",
            "Transaction-cost-aware optimizer with reinforcement learning for execution",
            "Production upgrade: XGBoost/LightGBM alpha model with SHAP explainability and model monitoring",
        ],
    }


def _run_monte_carlo(portfolio_return: float, volatility: float, n_sims: int = 1000, horizon_days: int = 30) -> dict[str, float]:
    rng = random.Random(42)
    end_values = []
    for _ in range(n_sims):
        value = 1.0
        for _ in range(horizon_days):
            shock = rng.gauss(portfolio_return / TRADING_DAYS, volatility / sqrt(TRADING_DAYS))
            value *= max(0.01, 1 + shock)
        end_values.append(value)

    downside = [v for v in end_values if v < 1.0]
    probability_of_loss = len(downside) / len(end_values)
    expected_terminal = mean(end_values)
    worst_5pct = sorted(end_values)[max(0, int(0.05 * (len(end_values) - 1)))]

    return {
        "expected_terminal_value": round(expected_terminal, 4),
        "probability_of_loss": round(probability_of_loss, 4),
        "worst_5pct_terminal_value": round(worst_5pct, 4),
    }


def _response_metadata() -> dict[str, Any]:
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "version": "v2-industry-standard",
    }


def generate_rebalance_plan(payload: dict[str, Any]) -> dict[str, Any]:
    _validate_payload(payload)

    assets = payload.get("assets", [])
    portfolio_value = _safe_float(payload.get("portfolio_value", 100000), 100000)
    threshold = _safe_float(payload.get("drift_threshold", 0.02), 0.02)
    risk_free_rate = _safe_float(payload.get("risk_free_rate", 0.02), 0.02)
    turnover_limit = _safe_float(payload.get("turnover_limit", 0.2), 0.2)
    transaction_cost_bps = _safe_float(payload.get("transaction_cost_bps", 10), 10)

    target_weights = _normalize_weights([_safe_float(a.get("target_weight")) for a in assets])
    current_weights = _normalize_weights([_safe_float(a.get("current_weight")) for a in assets])

    house_view = _generate_house_view(assets)
    forecast_map = {item["asset"]: item for item in house_view["asset_forecasts"]}

    weights, trades, market_returns = [], [], []
    drilldown = {}
    gross_turnover = 0.0
    total_cost = 0.0

    for i, asset in enumerate(assets):
        name = asset.get("asset", f"Asset {i + 1}")
        drift = current_weights[i] - target_weights[i]
        model_forecast = forecast_map.get(name, {"ensemble": 0.0, "confidence": 0.3})

        tilt = model_forecast["ensemble"] * model_forecast["confidence"] * 0.5
        optimized_target = max(0.0, min(1.0, target_weights[i] + tilt))

        desired_trade_weight = optimized_target - current_weights[i]
        max_trade_weight = turnover_limit / len(assets)
        capped_trade_weight = max(-max_trade_weight, min(max_trade_weight, desired_trade_weight))
        gross_turnover += abs(capped_trade_weight)

        if abs(capped_trade_weight) <= threshold:
            direction = "Hold"
        else:
            direction = "Buy" if capped_trade_weight > 0 else "Sell"

        price = _safe_float(asset.get("price", 100.0), 100.0)
        trade_value = capped_trade_weight * portfolio_value
        trade_units = trade_value / price

        execution_cost = abs(trade_value) * (transaction_cost_bps / 10000)
        total_cost += execution_cost

        weights.append(
            {
                "asset": name,
                "target_weight": round(target_weights[i], 4),
                "optimized_target_weight": round(optimized_target, 4),
                "current_weight": round(current_weights[i], 4),
                "drift": round(drift, 4),
                "forecast_return": round(model_forecast.get("ensemble", 0.0), 4),
                "forecast_confidence": round(model_forecast.get("confidence", 0.0), 3),
            }
        )

        trades.append(
            {
                "asset": name,
                "action": direction,
                "trade_value": round(abs(trade_value), 2),
                "signed_trade_value": round(trade_value, 2),
                "trade_units": round(trade_units, 4),
                "estimated_cost": round(execution_cost, 2),
            }
        )

        drilldown[name] = _build_asset_drilldown(asset, weights[-1], trades[-1], portfolio_value)
        market_returns.append(_safe_float(asset.get("market_return", 0.0), 0.0))

    portfolio_return = sum(w * r for w, r in zip(current_weights, market_returns))
    return_samples = [portfolio_return * (1 + (i - 10) / 50) for i in range(20)]
    risk_metrics = calculate_risk_metrics(return_samples, risk_free_rate=risk_free_rate)
    monte_carlo = _run_monte_carlo(portfolio_return, risk_metrics["volatility"])

    return {
        "portfolio_value": portfolio_value,
        "drift_threshold": threshold,
        "turnover_used": round(gross_turnover, 4),
        "estimated_total_transaction_cost": round(total_cost, 2),
        "weights": weights,
        "trades": trades,
        "risk_metrics": risk_metrics,
        "house_view": house_view,
        "monte_carlo": monte_carlo,
        "multi_agent_blueprint": multi_agent_blueprint(),
        "asset_drilldown": drilldown,
        "metadata": _response_metadata(),
    }


def preview_scenarios() -> dict[str, Any]:
    return {
        "scenarios": [
            {
                "name": "Risk-Off Shock",
                "description": "Equities and crypto pull back while bonds/FX cushion portfolio.",
                "portfolio_value": 100000,
                "drift_threshold": 0.02,
                "turnover_limit": 0.15,
                "transaction_cost_bps": 12,
                "assets": [
                    {"asset": "Mutual Fund", "target_weight": 0.25, "current_weight": 0.23, "market_return": -0.012, "price": 42},
                    {"asset": "ETF", "target_weight": 0.20, "current_weight": 0.24, "market_return": -0.024, "price": 95},
                    {"asset": "Stocks", "target_weight": 0.20, "current_weight": 0.22, "market_return": -0.031, "price": 130},
                    {"asset": "Commodity", "target_weight": 0.10, "current_weight": 0.11, "market_return": 0.007, "price": 77},
                    {"asset": "FX", "target_weight": 0.10, "current_weight": 0.08, "market_return": 0.004, "price": 1.2},
                    {"asset": "Crypto", "target_weight": 0.15, "current_weight": 0.12, "market_return": -0.055, "price": 26000},
                ],
            },
            {
                "name": "Risk-On Rally",
                "description": "Growth assets outperform and optimizer reduces concentration risk.",
                "portfolio_value": 100000,
                "drift_threshold": 0.02,
                "turnover_limit": 0.25,
                "transaction_cost_bps": 10,
                "assets": [
                    {"asset": "Mutual Fund", "target_weight": 0.25, "current_weight": 0.21, "market_return": 0.010, "price": 42},
                    {"asset": "ETF", "target_weight": 0.20, "current_weight": 0.19, "market_return": 0.018, "price": 95},
                    {"asset": "Stocks", "target_weight": 0.20, "current_weight": 0.23, "market_return": 0.026, "price": 130},
                    {"asset": "Commodity", "target_weight": 0.10, "current_weight": 0.09, "market_return": 0.011, "price": 77},
                    {"asset": "FX", "target_weight": 0.10, "current_weight": 0.08, "market_return": 0.003, "price": 1.2},
                    {"asset": "Crypto", "target_weight": 0.15, "current_weight": 0.20, "market_return": 0.061, "price": 26000},
                ],
            },
        ]
    }


def _asset_priority_signal(weight_entry: dict[str, Any], trade_entry: dict[str, Any]) -> float:
    return abs(weight_entry.get("drift", 0.0)) * 0.45 + abs(weight_entry.get("forecast_return", 0.0)) * 0.35 + abs(weight_entry.get("forecast_confidence", 0.0)) * 0.20


def generate_ai_copilot_insights(payload: dict[str, Any]) -> dict[str, Any]:
    plan = generate_rebalance_plan(payload)

    ranked = []
    for weight, trade in zip(plan.get("weights", []), plan.get("trades", [])):
        ranked.append({
            "asset": weight["asset"],
            "priority_score": round(_asset_priority_signal(weight, trade), 4),
            "action": trade.get("action", "Hold"),
            "reason": f"Drift {weight.get('drift', 0.0):.2%}, forecast {weight.get('forecast_return', 0.0):.2%}, confidence {weight.get('forecast_confidence', 0.0):.2f}",
        })

    ranked.sort(key=lambda x: x["priority_score"], reverse=True)
    top_actions = ranked[:3]

    risk = plan.get("risk_metrics", {})
    risk_flags = []
    if risk.get("var_95", 0) > 0.03:
        risk_flags.append("VaR95 elevated above 3%")
    if risk.get("max_drawdown", 0) > 0.08:
        risk_flags.append("Max drawdown above 8%")
    if plan.get("turnover_used", 0) > 0.18:
        risk_flags.append("Turnover approaching governance cap")
    if not risk_flags:
        risk_flags.append("Risk posture within configured guardrails")

    narrative = (
        "AI Copilot Summary: Rebalance favors assets with highest drift and strongest confidence-weighted return signal. "
        f"Top focus assets: {', '.join([x['asset'] for x in top_actions]) if top_actions else 'None'}. "
        f"Portfolio estimated transaction cost is ${plan.get('estimated_total_transaction_cost', 0):,.2f}."
    )

    return {
        "narrative": narrative,
        "top_actions": top_actions,
        "risk_flags": risk_flags,
        "execution_playbook": [
            "Stage 1: Execute high-liquidity ETF/FX legs first for rapid risk normalization",
            "Stage 2: Execute equity/commodity slices using TWAP scheduling",
            "Stage 3: Execute crypto rebalance in smaller child orders with slippage guard",
        ],
        "cutting_edge_model_stack": [
            "Temporal Fusion Transformer (multi-horizon forecasts)",
            "N-BEATS/N-HiTS (time-series specialists)",
            "Graph Neural Networks for cross-asset dependency modeling",
            "RL (PPO/SAC) for transaction-cost-aware dynamic allocation",
            "LLM Copilot layer for natural-language portfolio intelligence",
        ],
        "metadata": _response_metadata(),
    }


def simulate_multi_agent_tandem(payload: dict[str, Any]) -> dict[str, Any]:
    plan = generate_rebalance_plan(payload)
    copilot = generate_ai_copilot_insights(payload)

    ingest_assets = [w.get("asset") for w in plan.get("weights", [])]
    forecast_snapshot = [{
        "asset": w.get("asset"),
        "forecast_return": w.get("forecast_return"),
        "confidence": w.get("forecast_confidence"),
    } for w in plan.get("weights", [])]

    prioritized = sorted(plan.get("trades", []), key=lambda t: t.get("trade_value", 0), reverse=True)[:3]
    execution_queue = [
        {
            "asset": t.get("asset"),
            "action": t.get("action"),
            "notional": t.get("trade_value"),
            "estimated_cost": t.get("estimated_cost"),
        }
        for t in prioritized
    ]

    timeline = [
        {
            "step": 1,
            "agent": "Market Data Agent",
            "objective": "Ingest portfolio state, normalize schema, validate feeds",
            "output": {"assets_loaded": len(ingest_assets), "asset_list": ingest_assets},
        },
        {
            "step": 2,
            "agent": "Forecast Agent",
            "objective": "Generate confidence-weighted alpha signals",
            "output": {"forecast_snapshot": forecast_snapshot[:5]},
        },
        {
            "step": 3,
            "agent": "Risk Agent",
            "objective": "Run risk checks and policy validation",
            "output": {"risk_metrics": plan.get("risk_metrics", {}), "risk_flags": copilot.get("risk_flags", [])},
        },
        {
            "step": 4,
            "agent": "Rebalance Optimizer Agent",
            "objective": "Construct constrained target weights and trades",
            "output": {
                "turnover_used": plan.get("turnover_used"),
                "estimated_total_transaction_cost": plan.get("estimated_total_transaction_cost"),
                "top_rebalance_actions": copilot.get("top_actions", []),
            },
        },
        {
            "step": 5,
            "agent": "Execution Agent",
            "objective": "Prepare staged execution queue",
            "output": {"execution_queue": execution_queue, "playbook": copilot.get("execution_playbook", [])},
        },
        {
            "step": 6,
            "agent": "Supervisor Agent",
            "objective": "Approve and publish coordinated decision",
            "output": {
                "final_narrative": copilot.get("narrative"),
                "decision": "APPROVED" if len(copilot.get("risk_flags", [])) <= 2 else "REVIEW_REQUIRED",
                "metadata": _response_metadata(),
            },
        },
    ]

    return {
        "orchestration": multi_agent_blueprint().get("orchestration"),
        "timeline": timeline,
    }


def multi_agent_blueprint() -> dict[str, Any]:
    return {
        "agents": [
            {"name": "Market Data Agent", "role": "Ingests prices, returns, corporate actions, macro, sentiment and validates quality."},
            {"name": "Forecast Agent", "role": "Runs ML forecasts, confidence intervals and drift monitors."},
            {"name": "Risk Agent", "role": "Computes VaR/CVaR/drawdown and validates hard limits."},
            {"name": "Rebalance Optimizer Agent", "role": "Constructs targets under turnover/cost/sector/concentration constraints."},
            {"name": "Execution Agent", "role": "Generates child orders with slippage and venue routing heuristics."},
            {"name": "Supervisor Agent", "role": "Orchestrates agents, resolves conflicts, signs-off final plan."},
        ],
        "orchestration": "Supervisor -> Data -> Forecast -> Risk -> Optimizer -> Execution -> Supervisor Approval",
        "governance_standards": [
            "Model Risk Management: versioning, challenger models, and periodic backtesting",
            "Pre-trade controls: exposure, leverage, and concentration checks",
            "Post-trade surveillance and execution quality TCA",
            "Audit trail for inputs, model outputs, and decisions",
        ],
    }


@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/api/health", methods=["GET"])
def health_endpoint():
    return jsonify({"status": "ok", "service": "smart-portfolio-rebalancer", "metadata": _response_metadata()})


@app.route("/api/rebalance", methods=["POST"])
def rebalance_endpoint():
    data = request.json or {}
    try:
        return jsonify(generate_rebalance_plan(data))
    except ValidationError as exc:
        return jsonify({"error": str(exc), "metadata": _response_metadata()}), 400


@app.route("/api/preview-scenarios", methods=["GET"])
def preview_scenarios_endpoint():
    return jsonify(preview_scenarios())


@app.route("/api/ai-copilot/insights", methods=["POST"])
def ai_copilot_insights_endpoint():
    data = request.json or {}
    try:
        return jsonify(generate_ai_copilot_insights(data))
    except ValidationError as exc:
        return jsonify({"error": str(exc), "metadata": _response_metadata()}), 400


@app.route("/api/multi-agent/tandem-demo", methods=["POST"])
def multi_agent_tandem_demo_endpoint():
    data = request.json or {}
    try:
        return jsonify(simulate_multi_agent_tandem(data))
    except ValidationError as exc:
        return jsonify({"error": str(exc), "metadata": _response_metadata()}), 400

@app.route("/api/multi-agent-blueprint", methods=["GET"])
def multi_agent_blueprint_endpoint():
    return jsonify(multi_agent_blueprint())


@app.route("/risk-mitigation", methods=["POST"])
def risk_mitigation_endpoint():
    data = request.json or {}
    inputs = data.get("inputs", [])
    return jsonify({"answer": risk_mitigation(inputs)})


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5000"))
    app.run(host=host, port=port, debug=False)
