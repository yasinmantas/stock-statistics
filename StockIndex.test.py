import unittest
from src.StockIndex import StockIndex

class TestStockIndex(unittest.TestCase):

    def test_allTimeHigh(self):
        testData = StockIndex('C:/Users/Yasin/Documents/stock-statistics/test/fixture/testdata.csv')

        high = testData.allTimeHigh()
        self.assertTrue('value' in high)
        self.assertTrue('date' in high)
        self.assertEqual(high['value'], 136)
        self.assertEqual(high['date'], '2020-10-27')

    def test_dailyLowerHigherRatio(self):
        testData = StockIndex('C:/Users/Yasin/Documents/stock-statistics/test/fixture/testdata.csv')

        ratio = testData.dailyLowerHigherRatio()

        self.assertEqual(ratio['higherClose']['count'], 16)
        self.assertEqual(ratio['higherClose']['pct'], 16/27)
        self.assertEqual(ratio['higherClose']['avg'], 2.75)
        self.assertAlmostEqual(ratio['higherClose']['diff'], (39.18 / 16) / 100, 3)
        self.assertEqual(ratio['lowerClose']['count'], 9)
        self.assertEqual(ratio['lowerClose']['pct'], 1/3)
        self.assertEqual(ratio['lowerClose']['avg'], -28 / 9)
        self.assertAlmostEqual(ratio['lowerClose']['diff'], (-23.8 / 9) / 100, 3)
        self.assertEqual(ratio['sameClose']['count'], 2)
        self.assertEqual(ratio['sameClose']['pct'], 2/27)

    def test_maxDaysInARow(self):
        testData = StockIndex('C:/Users/Yasin/Documents/stock-statistics/test/fixture/testdata.csv')

        nDays = testData.maxDaysInARow()

        # TODO test again after checking task
        # self.assertEqual(nDays['high']['count'], 5)
        # self.assertEqual(nDays['high']['startDate'], '2020-10-16')
        # self.assertEqual(nDays['high']['endDate'], '2020-10-20')
        # self.assertEqual(nDays['high']['startValue'], 112)
        # self.assertEqual(nDays['high']['endValue'], 125)

        self.assertEqual(nDays['low']['count'], 3)
        self.assertEqual(nDays['low']['startDate'], '2020-10-10')
        self.assertEqual(nDays['low']['endDate'], '2020-10-12')
        self.assertEqual(nDays['low']['startValue'], 117)
        self.assertEqual(nDays['low']['endValue'], 107)

    def test_dayAfterNDaysRatio(self):
        testData = StockIndex('C:/Users/Yasin/Documents/stock-statistics/test/fixture/testdata.csv')

        twoDaysDown = testData.dayAfterNDaysRatio(2, True)
        self.assertEqual(twoDaysDown['occurrence'], 3)
        self.assertEqual(twoDaysDown['higher']['count'], 2)
        self.assertEqual(twoDaysDown['higher']['pct'], 2/3)
        self.assertEqual(twoDaysDown['higher']['avg'], 3)
        self.assertAlmostEqual(twoDaysDown['higher']['diff'], (5.34 / 2) / 100, 3)
        self.assertEqual(twoDaysDown['lower']['count'], 1)
        self.assertEqual(twoDaysDown['lower']['pct'], 1/3)
        self.assertEqual(twoDaysDown['lower']['avg'], -3)
        self.assertAlmostEqual(twoDaysDown['lower']['diff'], -2.73 / 100, 3)
        self.assertEqual(twoDaysDown['same']['count'], 0)
        self.assertEqual(twoDaysDown['same']['pct'], 0)

        threeDaysUp = testData.dayAfterNDaysRatio(3, False)
        self.assertEqual(threeDaysUp['occurrence'], 4)
        self.assertEqual(threeDaysUp['higher']['count'], 2)
        self.assertEqual(threeDaysUp['higher']['pct'], 0.5)
        self.assertEqual(threeDaysUp['higher']['avg'], 2)
        self.assertAlmostEqual(threeDaysUp['higher']['diff'], (3.27 / 2) / 100, 3)
        self.assertEqual(threeDaysUp['lower']['count'], 2)
        self.assertEqual(threeDaysUp['lower']['pct'], 0.5)
        self.assertEqual(threeDaysUp['lower']['avg'], -3)
        self.assertAlmostEqual(threeDaysUp['lower']['diff'], (-5.06 / 2) / 100, 3)
        self.assertEqual(threeDaysUp['same']['count'], 0)
        self.assertEqual(threeDaysUp['same']['pct'], 0)


if __name__ == '__main__':
    unittest.main()

