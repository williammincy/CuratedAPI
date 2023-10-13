
import unittest
from curatedapi_wm import CuratedLink

class TestCuratedLink(unittest.TestCase):
    
    def setUp(self):
        self.link = CuratedLink(url="https://example.com", title="Example", description="This is an example link", image="https://example.com/image.jpg", category="General", id="12345")
    
    def test_init(self):
        self.assertEqual(self.link.url, "https://example.com")
        self.assertEqual(self.link.title, "Example")
        self.assertEqual(self.link.description, "This is an example link")
        self.assertEqual(self.link.image, "https://example.com/image.jpg")
        self.assertEqual(self.link.category, "General")
        self.assertEqual(self.link.id, "12345")
    
    def test_str(self):
        expected_output = "Title: Example\nURL: https://example.com\nDescription: This is an example link\nCategory: General\nImage: https://example.com/image.jpg"
        self.assertEqual(str(self.link), expected_output)
    
if __name__ == "__main__":
    unittest.main()
