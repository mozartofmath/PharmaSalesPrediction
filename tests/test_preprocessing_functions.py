import unittest
import sys, os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join('..')))

from scripts.preprocessing_functions import weekends, time_of_month, label_holidays, days_from_holiday

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

class TestDaysFromHoliday(unittest.TestCase):
    def test_days_from_holiday(self):
        """
        Test that it returns the integer label for a holiday
        """
        dates = pd.DatetimeIndex(['1970-01-01','1970-01-03','1970-01-05'])
        holidays = pd.DatetimeIndex(['1970-01-02','1970-01-04'])
        result = days_from_holiday(dates, holidays)
        output = ([1, 1, 14], [14, 1, 1])
        self.assertAlmostEqual(result, output)

if __name__ == '__main__':
    unittest.main()
