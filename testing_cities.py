import unittest
from city_functions import cities

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        city_country = cities("berlim", "alemanha")
        self.assertEqual(city_country,"Berlim, Alemanha")

    def test_city_country_population(self):
        city_country_population = cities("berlim","alemanha",50.213)
        self.assertEqual(city_country_population,"Berlim, Alemanha. Population: 50.213.")

unittest.main()
