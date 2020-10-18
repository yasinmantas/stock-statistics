from StockIndex import StockIndex

nasdaq = StockIndex('C:/Users/Yasin/Documents/stock-statistics/files/NDX_D1.csv', ',', 'Date', 'Open', 'High', 'Low', 'Close')

high = nasdaq.allTimeHigh()
print(high)

lowerHigherRatio = nasdaq.dailyLowerHigherRatio()
print(lowerHigherRatio)

