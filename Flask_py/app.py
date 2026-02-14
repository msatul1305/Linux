from __future__ import annotations

import random
from math import sqrt
from statistics import mean, stdev
from typing import Any

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

TRADING_DAYS = 252


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


def calculate_risk_metrics(portfolio_returns: list[float], risk_free_rate: float = 0.0) -> dict[str, float]:
    if not portfolio_returns:
        return {
            "volatility": 0.0,
            "sharpe": 0.0,
            "max_drawdown": 0.0,
            "var_95": 0.0,
            "cvar_95": 0.0,
            "expected_annual_return": 0.0,
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

    return {
        "volatility": round(volatility, 4),
        "sharpe": round(sharpe, 4),
        "max_drawdown": round(abs(max_drawdown), 4),
        "var_95": round(abs(var_95), 4),
        "cvar_95": round(abs(cvar_95), 4),
        "expected_annual_return": round(avg_return * TRADING_DAYS, 4),
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
        ],
    }


def _run_monte_carlo(portfolio_return: float, volatility: float, n_sims: int = 500, horizon_days: int = 30) -> dict[str, float]:
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


def generate_rebalance_plan(payload: dict[str, Any]) -> dict[str, Any]:
    assets = payload.get("assets", [])
    portfolio_value = _safe_float(payload.get("portfolio_value", 100000), 100000)
    threshold = _safe_float(payload.get("drift_threshold", 0.02), 0.02)
    risk_free_rate = _safe_float(payload.get("risk_free_rate", 0.02), 0.02)
    turnover_limit = _safe_float(payload.get("turnover_limit", 0.2), 0.2)

    if not assets:
        return {
            "portfolio_value": portfolio_value,
            "drift_threshold": threshold,
            "weights": [],
            "trades": [],
            "risk_metrics": calculate_risk_metrics([], risk_free_rate=risk_free_rate),
            "house_view": _generate_house_view([]),
            "monte_carlo": {"expected_terminal_value": 1.0, "probability_of_loss": 0.0, "worst_5pct_terminal_value": 1.0},
            "multi_agent_blueprint": multi_agent_blueprint(),
        }

    target_weights = _normalize_weights([_safe_float(a.get("target_weight")) for a in assets])
    current_weights = _normalize_weights([_safe_float(a.get("current_weight")) for a in assets])

    house_view = _generate_house_view(assets)
    forecast_map = {item["asset"]: item for item in house_view["asset_forecasts"]}

    weights, trades, market_returns = [], [], []
    gross_turnover = 0.0

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

        direction = "Hold"
        if drift > threshold:
            direction = "Sell"
        elif drift < -threshold:
            direction = "Buy"

        price = max(0.01, _safe_float(asset.get("price", 100.0), 100.0))
        trade_value = capped_trade_weight * portfolio_value
        trade_units = trade_value / price

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
            }
        )

        market_returns.append(_safe_float(asset.get("market_return", 0.0), 0.0))

    portfolio_return = sum(w * r for w, r in zip(current_weights, market_returns))
    return_samples = [portfolio_return * (1 + (i - 10) / 50) for i in range(20)]
    risk_metrics = calculate_risk_metrics(return_samples, risk_free_rate=risk_free_rate)
    monte_carlo = _run_monte_carlo(portfolio_return, risk_metrics["volatility"])

    return {
        "portfolio_value": portfolio_value,
        "drift_threshold": threshold,
        "turnover_used": round(gross_turnover, 4),
        "weights": weights,
        "trades": trades,
        "risk_metrics": risk_metrics,
        "house_view": house_view,
        "monte_carlo": monte_carlo,
        "multi_agent_blueprint": multi_agent_blueprint(),
    }


def multi_agent_blueprint() -> dict[str, Any]:
    return {
        "agents": [
            {"name": "Market Data Agent", "role": "Ingests prices, returns, macro, sentiment, and validates data quality."},
            {"name": "Forecast Agent", "role": "Runs ML forecasts (ensemble/time-series/regime)."},
            {"name": "Risk Agent", "role": "Computes VaR/CVaR/drawdown and checks policy limits."},
            {"name": "Rebalance Optimizer Agent", "role": "Builds target weights under turnover/cost/sector constraints."},
            {"name": "Execution Agent", "role": "Generates child orders and simulates slippage."},
            {"name": "Supervisor Agent", "role": "Orchestrates other agents, resolves conflicts, and approves final plan."},
        ],
        "orchestration": "Supervisor -> Data -> Forecast -> Risk -> Optimizer -> Execution -> Supervisor Approval",
    }


@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/api/rebalance", methods=["POST"])
def rebalance_endpoint():
    data = request.json or {}
    return jsonify(generate_rebalance_plan(data))


@app.route("/api/multi-agent-blueprint", methods=["GET"])
def multi_agent_blueprint_endpoint():
    return jsonify(multi_agent_blueprint())


@app.route("/risk-mitigation", methods=["POST"])
def risk_mitigation_endpoint():
    data = request.json or {}
    inputs = data.get("inputs", [])
    return jsonify({"answer": risk_mitigation(inputs)})


if __name__ == "__main__":
    app.run(debug=True)
