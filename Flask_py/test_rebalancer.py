import unittest

from app import app, calculate_risk_metrics, generate_rebalance_plan


class RebalancerTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_generate_rebalance_plan_actions(self):
        payload = {
            "portfolio_value": 100000,
            "drift_threshold": 0.02,
            "assets": [
                {"asset": "ETF", "target_weight": 0.5, "current_weight": 0.6, "market_return": 0.01},
                {"asset": "Bond", "target_weight": 0.5, "current_weight": 0.4, "market_return": 0.005},
            ],
        }
        plan = generate_rebalance_plan(payload)
        self.assertEqual(plan["trades"][0]["action"], "Sell")
        self.assertEqual(plan["trades"][1]["action"], "Buy")

    def test_risk_metrics_present(self):
        metrics = calculate_risk_metrics([0.01, -0.02, 0.015, -0.005], 0.02)
        self.assertIn("volatility", metrics)
        self.assertIn("sharpe", metrics)
        self.assertIn("max_drawdown", metrics)

    def test_api_rebalance(self):
        response = self.client.post(
            "/api/rebalance",
            json={
                "portfolio_value": 50000,
                "drift_threshold": 0.01,
                "assets": [
                    {"asset": "Stocks", "target_weight": 0.7, "current_weight": 0.5, "market_return": 0.02},
                    {"asset": "Gold", "target_weight": 0.3, "current_weight": 0.5, "market_return": 0.01},
                ],
            },
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data["weights"]), 2)
        self.assertEqual(len(data["trades"]), 2)


if __name__ == "__main__":
    unittest.main()
