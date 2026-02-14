from __future__ import annotations

from math import sqrt
from statistics import mean, stdev
from typing import Any

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


def risk_mitigation(inputs):
    results = []
    for input_data in inputs:
        n, a = map(int, input_data[0].split())
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

    result = sum(max_diff_array[:strategies])

    return result


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
        return {"volatility": 0.0, "sharpe": 0.0, "max_drawdown": 0.0}

    if len(portfolio_returns) < 2:
        volatility = 0.0
    else:
        volatility = stdev(portfolio_returns) * sqrt(252)

    avg_return = mean(portfolio_returns)
    sharpe = 0.0
    if volatility > 0:
        sharpe = ((avg_return * 252) - risk_free_rate) / volatility

    cumulative = 1.0
    peak = 1.0
    max_drawdown = 0.0
    for ret in portfolio_returns:
        cumulative *= 1 + ret
        peak = max(peak, cumulative)
        drawdown = (cumulative - peak) / peak
        max_drawdown = min(max_drawdown, drawdown)

    return {
        "volatility": round(volatility, 4),
        "sharpe": round(sharpe, 4),
        "max_drawdown": round(abs(max_drawdown), 4),
    }


def generate_rebalance_plan(payload: dict[str, Any]) -> dict[str, Any]:
    assets = payload.get("assets", [])
    portfolio_value = _safe_float(payload.get("portfolio_value", 100000), 100000)
    threshold = _safe_float(payload.get("drift_threshold", 0.02), 0.02)
    risk_free_rate = _safe_float(payload.get("risk_free_rate", 0.02), 0.02)

    if not assets:
        return {
            "portfolio_value": portfolio_value,
            "drift_threshold": threshold,
            "weights": [],
            "trades": [],
            "risk_metrics": calculate_risk_metrics([], risk_free_rate=risk_free_rate),
        }

    target_weights = _normalize_weights([_safe_float(a.get("target_weight")) for a in assets])
    current_weights = _normalize_weights([_safe_float(a.get("current_weight")) for a in assets])

    weights = []
    trades = []
    market_returns = []

    for i, asset in enumerate(assets):
        drift = current_weights[i] - target_weights[i]
        trade_value = (target_weights[i] - current_weights[i]) * portfolio_value
        direction = "Hold"
        if drift > threshold:
            direction = "Sell"
        elif drift < -threshold:
            direction = "Buy"

        weights.append(
            {
                "asset": asset.get("asset", f"Asset {i + 1}"),
                "target_weight": round(target_weights[i], 4),
                "current_weight": round(current_weights[i], 4),
                "drift": round(drift, 4),
            }
        )

        trades.append(
            {
                "asset": asset.get("asset", f"Asset {i + 1}"),
                "action": direction,
                "trade_value": round(abs(trade_value), 2),
                "signed_trade_value": round(trade_value, 2),
            }
        )

        market_returns.append(_safe_float(asset.get("market_return", 0.0), 0.0))

    portfolio_return = sum(w * r for w, r in zip(current_weights, market_returns))
    scenario_returns = [
        portfolio_return,
        portfolio_return * 0.5,
        portfolio_return * -0.75,
        portfolio_return * 1.2,
        portfolio_return * 0.8,
    ]
    risk_metrics = calculate_risk_metrics(scenario_returns, risk_free_rate=risk_free_rate)

    return {
        "portfolio_value": portfolio_value,
        "drift_threshold": threshold,
        "weights": weights,
        "trades": trades,
        "risk_metrics": risk_metrics,
    }


@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/api/rebalance", methods=["POST"])
def rebalance_endpoint():
    data = request.json or {}
    plan = generate_rebalance_plan(data)
    return jsonify(plan)


@app.route('/risk-mitigation', methods=['POST'])
def risk_mitigation_endpoint():
    data = request.json
    inputs = data.get('inputs', [])
    results = risk_mitigation(inputs)

    return jsonify({"answer": results})


if __name__ == '__main__':
    app.run(debug=True)
