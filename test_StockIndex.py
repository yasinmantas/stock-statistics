import unittest
from src.StockIndex import StockIndex

class TestStockIndex(unittest.TestCase):

    def test_allTimeHigh(self):
        testData = StockIndex('C:/Users/Yasin/Documents/stock-statistics/test/fixture/NDX.csv', ',', 'Date', 'Open', 'High', 'Low', 'Close')

        high = testData.allTimeHigh()
        self.assertTrue('value' in high)
        self.assertTrue('date' in high)
        self.assertEqual(high['value'], 12204.750000)
        self.assertEqual(high['date'], '2020-10-12')
    
    def test_dailyLowerHigherRatio(self):
        testData = StockIndex('C:/Users/Yasin/Documents/stock-statistics/test/fixture/NDX.csv', ',', 'Date', 'Open', 'High', 'Low', 'Close')

        ratio = testData.dailyLowerHigherRatio()
        self.assertTrue('higherClose' in ratio)
        self.assertTrue('count' in ratio['higherClose'])
        self.assertTrue('pct' in ratio['higherClose'])
        self.assertTrue('avg' in ratio['higherClose'])
        self.assertTrue('lowerClose' in ratio)
        self.assertTrue('count' in ratio['lowerClose'])
        self.assertTrue('pct' in ratio['lowerClose'])
        self.assertTrue('avg' in ratio['lowerClose'])
        self.assertTrue('sameClose' in ratio)
        self.assertTrue('count' in ratio['sameClose'])
        self.assertTrue('pct' in ratio['sameClose'])

        self.assertEqual(ratio['higherClose']['count'], 6)
        self.assertAlmostEqual(ratio['higherClose']['avg'], 118.694987)
        self.assertEqual(ratio['lowerClose']['count'], 6)
        self.assertAlmostEqual(ratio['lowerClose']['avg'], -91.9431965)
        self.assertEqual(ratio['sameClose']['count'], 0)

    def test_maxDaysInARow(self):
        testData = StockIndex('C:/Users/Yasin/Documents/stock-statistics/test/fixture/NDX.csv', ',', 'Date', 'Open', 'High', 'Low', 'Close')

        nDays = testData.maxDaysInARow()

        self.assertEqual(nDays['high']['count'], 2)
        self.assertEqual(nDays['high']['startDate'], '2020-10-09')
        self.assertEqual(nDays['high']['endDate'], '2020-10-12')
        self.assertEqual(nDays['high']['startValue'], 11615.570313)
        self.assertEqual(nDays['high']['endValue'], 12088.110352)
        
        self.assertEqual(nDays['low']['count'], 2)
        self.assertEqual(nDays['low']['startDate'], '2020-10-13')
        self.assertEqual(nDays['low']['endDate'], '2020-10-14')
        self.assertEqual(nDays['low']['startValue'], 12131.070313)
        self.assertEqual(nDays['low']['endValue'], 11985.360352)



if __name__ == '__main__':
    unittest.main()

