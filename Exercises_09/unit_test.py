# This Python script is written by Vinay Reddy B

import unittest
import formatter

class TestFormatterVinay(unittest.TestCase):
    def test_lower_vinay(self):
        test_text = "VINAY REDDY"
        result = formatter.convert_lower(test_text)
        self.assertEqual(result, "vinay reddy")

    def test_upper_vinay(self):
        test_text = "Vinay reddy"
        result = formatter.convert_upper(test_text)
        self.assertEqual(result, "VINAY REDDY")

if __name__ == "__main__":
    unittest.main()
    
#This will test whether the convert_lower() function correctly converts to lowercase and convert_upper() function correctly converts to uppercase for the name "Vinay Reddy"
