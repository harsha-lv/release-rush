import unittest
from app import service_info


class TestServiceInfo(unittest.TestCase):

    def test_service_contract(self):
        result = service_info()
        self.assertEqual(result["service"], "inventory-api")

    def test_api_version(self):
        result = service_info()
        self.assertEqual(result["version"], "v2")

    def test_health_status(self):
        result = service_info()
        self.assertEqual(result["health"], "ok")


if __name__ == "__main__":
    unittest.main()
