
import unittest
from curatedapi_wm import CuratedCategory

class TestCuratedCategory(unittest.TestCase):
    
    def setUp(self):
        self.category = CuratedCategory(code="GEN", name="General", sponsored=False, limit=10)
    
    def test_init(self):
        self.assertEqual(self.category.code, "GEN")
        self.assertEqual(self.category.name, "General")
        self.assertFalse(self.category.sponsored)
        self.assertEqual(self.category.limit, 10)
    
    def test_str(self):
        expected_output = "Code: GEN\nName: General\nSponsored: False\nLimit: 10"
        self.assertEqual(str(self.category), expected_output)
    
    def test_from_json(self):
        json_data = '{"code": "GEN", "name": "General", "sponsored": false, "limit": 10}'
        category_from_json = CuratedCategory.from_json(json_data)
        self.assertEqual(category_from_json.code, "GEN")
        self.assertEqual(category_from_json.name, "General")
        self.assertFalse(category_from_json.sponsored)
        self.assertEqual(category_from_json.limit, 10)
    
    def test_to_json(self):
        expected_json = '{"code": "GEN", "name": "General", "sponsored": false, "limit": 10}'
        self.assertEqual(self.category.to_json(), expected_json)
    
if __name__ == "__main__":
    unittest.main()
