import unittest
from pathlib import Path
from data_manipulator import DataManipulator


class TestDataManipulator(unittest.TestCase): # the class inherits from unittest.TestCase

    def setUp(self):
        self.data_manipulator = DataManipulator(Path("mock.json"))

    def test_good_date1(self):
        # setup
        data = {
            "value1": "1999/10/10 10:15:15"
        }
        final_good_data = {
            "value1": "2021-10-10 10:15:15"
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(final_data_to_check, final_good_data)

    def test_good_date2(self):
        # setup
        data = {
            "value1": "1900/01/01 00:00:00"
        }
        final_good_data = {
            "value1": "2021-01-01 00:00:00"
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(final_data_to_check, final_good_data)

    def test_good_date3_year2021(self):
        # setup
        data = {
            "value1": "2021/01/01 10:02:00"
        }
        final_good_data = {
            "value1": "2021-01-01 10:02:00"
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(final_data_to_check, final_good_data)

    def test_bad_date1(self):
        # setup
        data = {
            "value1": "1999/1010 10:15:15"
        }
        final_good_data = {
            "value1": "51:51:010101/9991"
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(final_data_to_check, final_good_data)

    def test_bad_date2(self):
        # setup
        data = {
            "value1": "2021/31/12 00:00:10"
        }
        final_good_data = {
            "value1": "01:00:0021/13/1202"
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(final_data_to_check, final_good_data)

    def test_bad_date3(self):
        # setup
        data = {
            "value1": "1997/10/10 10:15:15z"
        }
        final_good_data = {
            "value1": "z51:51:0101/01/7991"
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(final_data_to_check, final_good_data)

    def test_bad_date4(self):
        # setup
        data = {
            "value1": "2024/13/32 10:15:15"
        }
        final_good_data = {
            "value1": "51:51:0123/31/4202"
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(final_data_to_check, final_good_data)

    def test_good_str1(self):
        # setup
        data = {
            "value1": " a  bcd ef "
        }
        final_good_data = {
            "value1": "fedcba"
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(final_data_to_check, final_good_data)

    def test_good_str2(self):
        # setup
        data = {
            "value1": "a"
        }
        final_good_data = {
            "value1": "a"
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(final_data_to_check, final_good_data)

    def test_good_str3(self):
        # setup
        data = {
            "value1": " a1b2 cd!@# "
        }
        final_good_data = {
            "value1": "#@!dc2b1a"
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(final_data_to_check, final_good_data)

    def test_good_list1(self):
        # setup
        data = {
            "value1": ["bar", "baz", "foo", "bar", "baz", 5]
        }
        final_good_data = {
            "value1": ["bar", "baz", "foo", 5]
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(sorted(final_data_to_check), sorted(final_good_data))

    def test_good_list2(self):
        # setup
        data = {
            "value1": [5, 5, 1, "@", "@", 5]
        }
        final_good_data = {
            "value1": [5, 1, "@"]
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(sorted(final_data_to_check), sorted(final_good_data))

    def test_good_list3(self):
        # setup
        data = {
            "value1": []
        }
        final_good_data = {
            "value1": []
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(sorted(final_data_to_check), sorted(final_good_data))

    def test_int1(self):
        # setup
        data = {
            "value1": 1234567
        }
        final_good_data = {
            "value1": 1234567
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(final_data_to_check, final_good_data)

    def test_int2(self):
        # setup
        data = {
            "value1": 1
        }
        final_good_data = {
            "value1": 1
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(final_data_to_check, final_good_data)

    def test_double(self):
        # setup
        data = {
            "value1": 12.34
        }
        final_good_data = {
            "value1": 12.34
        }
        self.data_manipulator.load_data(data)

        # do the validation
        self.data_manipulator.process_data()

        # assert
        final_data_to_check = self.data_manipulator.json_data_dict
        self.assertEqual(final_data_to_check, final_good_data)


if __name__ == '__main__':
    unittest.main()
