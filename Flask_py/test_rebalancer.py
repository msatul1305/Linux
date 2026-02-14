import unittest

from app import app, calculate_risk_metrics, generate_rebalance_plan, multi_agent_blueprint


class RebalancerTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_generate_rebalance_plan_actions_and_ai_fields(self):
        payload = {
            "portfolio_value": 100000,
            "drift_threshold": 0.02,
            "turnover_limit": 0.2,
            "assets": [
                {
                    "asset": "ETF",
                    "target_weight": 0.5,
                    "current_weight": 0.6,
                    "market_return": 0.01,
                    "price": 100,
                    "historical_returns": [0.01, 0.015, 0.005, 0.012, 0.008],
                },
                {
                    "asset": "Bond",
                    "target_weight": 0.5,
                    "current_weight": 0.4,
                    "market_return": 0.005,
                    "price": 101,
                    "historical_returns": [0.003, 0.002, 0.004, 0.001, 0.005],
                },
            ],
        }
        plan = generate_rebalance_plan(payload)
        self.assertIn("optimized_target_weight", plan["weights"][0])
        self.assertIn(plan["trades"][0]["action"], {"Sell", "Buy", "Hold"})

    def test_risk_metrics_extended(self):
        metrics = calculate_risk_metrics([0.01, -0.02, 0.015, -0.005], 0.02)
        for key in ["volatility", "sharpe", "max_drawdown", "var_95", "cvar_95", "expected_annual_return"]:
            self.assertIn(key, metrics)

    def test_api_rebalance_and_blueprint(self):
        response = self.client.post(
            "/api/rebalance",
            json={
                "portfolio_value": 50000,
                "drift_threshold": 0.01,
                "turnover_limit": 0.2,
                "assets": [
                    {"asset": "Stocks", "target_weight": 0.7, "current_weight": 0.5, "market_return": 0.02, "price": 120},
                    {"asset": "Gold", "target_weight": 0.3, "current_weight": 0.5, "market_return": 0.01, "price": 75},
                ],
            },
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("house_view", data)
        self.assertIn("multi_agent_blueprint", data)

    def test_multi_agent_blueprint_shape(self):
        blueprint = multi_agent_blueprint()
        self.assertGreaterEqual(len(blueprint["agents"]), 5)


if __name__ == "__main__":
    unittest.main()
