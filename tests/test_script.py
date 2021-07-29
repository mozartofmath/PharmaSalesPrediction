import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

from scripts.script import find_average, count_occurence
from scripts.preprocessing_functions import weekends, time_of_month, label_holidays

class TestCases(unittest.TestCase):
    def test_find_average(self):
        """
        Test that it retunrs the average of a given list
        """
        data = [1, 2, 3]
        result = find_average(data)
        self.assertEqual(result, 2.0)

    def test_input_value(self):
        """
        Provide an assertion level for arg input
        """
        
        self.assertRaises(TypeError, find_average, True)

class TestCountOccurence(unittest.TestCase):
    def test_count_occurence(self):
        """
        Test that it returns the count of each unique values in the given list
        """
        data = [0,0,9,0,8,9,0,7]
        result = count_occurence(data)
        output = {0: 4, 9: 2, 8: 1, 7: 1}
        self.assertAlmostEqual(result, output)

    def test_input_value(self):
        """
        Provide an assertion level for arg input
        """
        self.assertRaises(TypeError, count_occurence, True)

class TestWeekdays(unittest.TestCase):
    def test_weekdays(self):
        """
        Test that it returns 0 if the input day of week is not on the 
        weekend, and returns 1 if its on the weekend
        """
        data = [1,2,3,4,5,6,7]
        result = list(map(weekends,data))
        output = [0, 0, 0, 0, 0, 1, 1]
        self.assertAlmostEqual(result, output)

class TestTimeOfMonth(unittest.TestCase):
    def test_time_of_month(self):
        """
        Test that it returns the time of month, given the day
        """
        data = [1,5,10,11,20,21,30]
        result = list(map(time_of_month,data))
        output = [0, 0, 0, 1, 1, 2, 2]
        self.assertAlmostEqual(result, output)

class TestLabelHolidays(unittest.TestCase):
    def test_label_holidays(self):
        """
        Test that it returns the integer label for a holiday
        """
        data = ['z',0,'0','a','b','c']
        result = list(map(label_holidays,data))
        output = [5 ,0, 1, 2, 3, 4]
        self.assertAlmostEqual(result, output)

if __name__ == '__main__':
    unittest.main()
