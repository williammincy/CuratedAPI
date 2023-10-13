
import unittest
from curatedapi_wm import CuratedApi

class TestCuratedApi(unittest.TestCase):
    
    def setUp(self):
        self.api = CuratedApi(api_key="sample_api_key")
    
    def test_init(self):
        self.assertEqual(self.api.api_key, "sample_api_key")
    
    def test_str(self):
        expected_output = "API Key: sample_api_key"
        self.assertEqual(str(self.api), expected_output)
    
    def test_from_json(self):
        json_data = '{"api_key": "sample_api_key"}'
        api_from_json = CuratedApi.from_json(json_data)
        self.assertEqual(api_from_json.api_key, "sample_api_key")
    
    def test_to_json(self):
        expected_json = '{"api_key": "sample_api_key"}'
        self.assertEqual(self.api.to_json(), expected_json)
    
if __name__ == "__main__":
    unittest.main()
