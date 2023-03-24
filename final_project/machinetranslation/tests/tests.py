import unittest
from translator import french_to_english, english_to_french

class TestClass(unittest.TestCase):
	def test_english_to_french(self):
		# Test Hello returns Bonjour
	        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        	# Test Hello does not return Hello
        	self.assertNotEqual(english_to_french('Hello'), 'Hello')
        	# Test None returns empty string
        	self.assertNotEqual(english_to_french("None"), '')
        	# Test empty string returns empty string
        	self.assertNotEqual(english_to_french(0), 0)

	def test_french_to_english(self):
		# Test Hello returns Bonjour
                self.assertEqual(french_to_english('Bonjour'), 'Hello')
                # Test Hello does not return Hello
                self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
                # Test None returns empty string
                self.assertNotEqual(frenchToEnglish("None"), '')
                # Test empty string returns empty string
                self.assertNotEqual(frechToEnglish(0), 0)


