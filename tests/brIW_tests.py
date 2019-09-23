#!/Users/ehsc1997/anaconda3/bin/python3
import unittest
import unittest.mock
from source.app import *


class TestSuite(unittest.TestCase):

    def test_update_data_add(self):
        # arrange
        dictionary = {1: "Person 1", 5: "Person 2", 22: "Person 3", 13: "Person 4"}
        ids = list(dictionary.keys())
        input_data = ["Christos", "Connor", "", "Ralph", "", "", "Klaudijus", "Anjali"]

        # act
        actual_output = update_data_add(input_data, ids, dictionary)
        expected_output = {1: "Person 1", 5: "Person 2", 22: "Person 3", 13: "Person 4", 23: "Christos", 24: "Connor", 25: "Ralph", 26: "Klaudijus", 27: "Anjali"}

        # assert
        self.assertEqual(actual_output, expected_output)

    def test_update_data_remove_people(self):
        # arrange
        dictionary = {1: "Person 1", 5: "Person 2", 22: "Person 3", 13: "Person 4", 23: "Christos", 24: "Connor", 25: "Ralph", 26: "Klaudijus", 27: "Anjali"}
        ids = list(dictionary.keys())
        input_data = [2, 5, 3, 7]
        preferences = {1: 23, 27: 28, 22: 7, 26: 13}
        data_name = "people"

        # act
        actual_output = update_data_remove(data_name, input_data, ids, dictionary, preferences)
        expected_output = {1: "Person 1", 22: "Person 3", 13: "Person 4", 24: "Connor", 26: "Klaudijus", 27: "Anjali"}

        # assert
        self.assertEqual(actual_output, expected_output)

    def test_update_data_remove_drinks(self):
        # arrange
        dictionary = {1: "Drink 1", 5: "Drink 2", 22: "Drink 3", 13: "Drink 4", 23: "Drink 5", 24: "Drink 6", 25: "Drink 7", 26: "Drink 8", 27: "Drink 9"}
        ids = list(dictionary.keys())
        input_data = [2, 4, 3, 7]
        preferences = {1: 23, 27: 28, 22: 7, 26: 13}
        data_name = "drinks"

        # act
        actual_output = update_data_remove(data_name, input_data, ids, dictionary, preferences)
        expected_output = {1: "Drink 1", 13: "Drink 4", 23: "Drink 5", 24: "Drink 6", 26: "Drink 8", 27: "Drink 9"}

        # assert
        self.assertEqual(actual_output, expected_output)

    def test_people_preferences_menu(self):
        # arrange
        # act
        # assert
        pass

    def test_drink_preferences_menu(self):
        # arrange
        # act
        # assert
        pass

    @unittest.mock.patch("builtins.input", return_value =unittest.mock)
    def test_input_method(self, input_return):
        pass



if __name__ == "__main__":
    unittest.main()

#result = TestSuite.test_update_data_add()