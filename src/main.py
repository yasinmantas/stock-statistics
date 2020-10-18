from StockIndex import StockIndex
import pprint

nasdaq = StockIndex('C:/Users/Yasin/Documents/stock-statistics/files/NDX_D1.csv', ',', 'Date', 'Open', 'High', 'Low', 'Close')

# high = nasdaq.allTimeHigh()
# pprint.pprint(high)

# lowerHigherRatio = nasdaq.dailyLowerHigherRatio()
# pprint.pprint(lowerHigherRatio)

consecutiveDays = nasdaq.maxDaysInARow()
pprint.pprint(consecutiveDays)

