import unittest
from weather_advice import get_recommendation

class TestWeatherAdvice(unittest.TestCase):
    def test_sunny(self):
        self.assertEqual(get_recommendation("sunny"), "Wear a t-shirt and sunglasses.")
    def test_rainy(self):
        self.assertEqual(get_recommendation("rainy"), "Don't forget your umbrella and a raincoat.")
    def test_cold(self):
        self.assertEqual(get_recommendation("cold"), "Make sure to wear a warm coat and a scarf.")
    def test_case_and_spaces(self):
        self.assertEqual(get_recommendation(" Sunny "), "Wear a t-shirt and sunglasses.")
    def test_unknown(self):
        self.assertEqual(get_recommendation("windy"), "Sorry, I don't have recommendations for this weather.")

if __name__ == "__main__":
    unittest.main()
