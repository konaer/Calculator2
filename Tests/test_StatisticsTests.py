import unittest
import numpy as np
from scipy import stats
from Statistics.Statistics import Statistics
from RandomNumberGenerator.NRandomNumbers import n_ramdom_int_number


class test(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()
        self.testData = n_ramdom_int_number(60,1,50)
        self.array = np.array(self.testData)

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, round(np.mean(self.array), 9))

    def test_median_statistics(self):
        median = self.statistics.median(self.testData)
        self.assertEqual(median, round(np.median(self.array),9))

    def test_Mode_statistics(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, np.argmax(np.bincount(self.testData)))

    def test_variance_statistics(self):
        variance = self.statistics.variance(self.testData)
        self.assertEqual(variance, round(np.var(self.array),9))

    def test_standardDeviation_statistics(self):
        standardDeviation = self.statistics.standardDeviation(self.testData)
        self.assertEqual(standardDeviation, round(np.std(self.array), 5))

if __name__ == '__main__':
    unittest.main()

