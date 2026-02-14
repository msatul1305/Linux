import unittest

from app import app, calculate_risk_metrics, generate_rebalance_plan, multi_agent_blueprint


class RebalancerTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def _sample_payload(self):
        return {
            "portfolio_value": 100000,
            "drift_threshold": 0.02,
            "turnover_limit": 0.2,
            "transaction_cost_bps": 12,
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

    def test_generate_rebalance_plan_industry_fields(self):
        plan = generate_rebalance_plan(self._sample_payload())
        self.assertIn("optimized_target_weight", plan["weights"][0])
        self.assertIn("estimated_cost", plan["trades"][0])
        self.assertIn("estimated_total_transaction_cost", plan)
        self.assertIn("metadata", plan)

    def test_risk_metrics_extended(self):
        metrics = calculate_risk_metrics([0.01, -0.02, 0.015, -0.005], 0.02)
        for key in ["volatility", "sharpe", "max_drawdown", "var_95", "cvar_95", "expected_annual_return", "tracking_error"]:
            self.assertIn(key, metrics)

    def test_api_rebalance_and_blueprint(self):
        response = self.client.post("/api/rebalance", json=self._sample_payload())
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("house_view", data)
        self.assertIn("multi_agent_blueprint", data)

    def test_validation_error(self):
        response = self.client.post(
            "/api/rebalance",
            json={"portfolio_value": -10, "assets": []},
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_health_endpoint(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "ok")

    def test_multi_agent_blueprint_shape(self):
        blueprint = multi_agent_blueprint()
        self.assertGreaterEqual(len(blueprint["agents"]), 5)
        self.assertIn("governance_standards", blueprint)


if __name__ == "__main__":
    unittest.main()
