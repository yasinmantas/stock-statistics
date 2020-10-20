from StockIndex import StockIndex
import pprint

nasdaq = StockIndex('C:/Users/Yasin/Documents/stock-statistics/files/NDX_D1.csv')

# high = nasdaq.allTimeHigh()
# pprint.pprint(high)

# lowerHigherRatio = nasdaq.dailyLowerHigherRatio()
# pprint.pprint(lowerHigherRatio)

# consecutiveDays = nasdaq.maxDaysInARow()
# pprint.pprint(consecutiveDays)

''' 
TODO: check if function dailyLowerHigherRatio() has become redundant 
-> dayAfterNDaysRatio with n = 0 returns same result
'''
nDays = nasdaq.dayAfterNDaysRatio(3, False)
pprint.pprint(nDays)