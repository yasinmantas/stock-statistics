from StockIndex import StockIndex
import pprint
import Sheets

nasdaq = StockIndex('C:/Users/Yasin/Documents/stock-statistics/files/NDX_D1.csv')

high = nasdaq.allTimeHigh()
pprint.pprint(high)

lowerHigherRatio = nasdaq.dailyLowerHigherRatio()
pprint.pprint(lowerHigherRatio)

consecutiveDays = nasdaq.maxDaysInARow()
pprint.pprint(consecutiveDays)

''' 
TODO: check if function dailyLowerHigherRatio() has become redundant 
-> dayAfterNDaysRatio with n = 0 returns same result
'''
n = 2
down = True
nDays = nasdaq.dayAfterNDaysRatio(n, down)
pprint.pprint(nDays)


# chaos for now TODO cleanup
firstRow = ['' for i in range(31)]
firstRow[0] = 'ATH'
firstRow[1] = 'Date'
firstRow[2] = 'Closes higher'
firstRow[3] = 'Pct.'
firstRow[4] = 'Avg. points'
firstRow[5] = 'Closes lower'
firstRow[6] = 'Pct.'
firstRow[7] = 'Avg. points'
firstRow[8] = 'Closes same'
firstRow[9] = 'Pct.'
firstRow[10] = 'Most consecutive higher days'
firstRow[11] = 'From date'
firstRow[12] = 'to date'
firstRow[13] = 'From points'
firstRow[14] = 'to points'
firstRow[15] = 'Difference'
firstRow[16] = 'Most consecutive lower days'
firstRow[17] = 'From date'
firstRow[18] = 'to date'
firstRow[19] = 'From points'
firstRow[20] = 'to points'
firstRow[21] = 'Difference'
firstRow[22] = str(n) + ' days ' + ('down' if down else 'up' ) + ' in a row' # TODO make dynamic
firstRow[23] = 'Higher the day after'
firstRow[24] = 'Pct.'
firstRow[25] = 'Avg.'
firstRow[26] = 'Lower the day after'
firstRow[27] = 'Pct.'
firstRow[28] = 'Avg.'
firstRow[29] = 'Same the day after'
firstRow[30] = 'Pct.'


data = ['' for i in range(31)]
data[0] = high['value']
data[1] = high['date']
data[2] = lowerHigherRatio['higherClose']['count']
data[3] = lowerHigherRatio['higherClose']['pct']
data[4] = lowerHigherRatio['higherClose']['avg']
data[5] = lowerHigherRatio['lowerClose']['count']
data[6] = lowerHigherRatio['lowerClose']['pct']
data[7] = lowerHigherRatio['lowerClose']['avg']
data[8] = lowerHigherRatio['sameClose']['count']
data[9] = lowerHigherRatio['sameClose']['pct']
data[10] = consecutiveDays['high']['count']
data[11] = consecutiveDays['high']['startDate']
data[12] = consecutiveDays['high']['endDate']
data[13] = consecutiveDays['high']['startValue']
data[14] = consecutiveDays['high']['endValue']
data[15] = consecutiveDays['high']['difference']
data[16] = consecutiveDays['low']['count']
data[17] = consecutiveDays['low']['startDate']
data[18] = consecutiveDays['low']['endDate']
data[19] = consecutiveDays['low']['startValue']
data[20] = consecutiveDays['low']['endValue']
data[21] = consecutiveDays['low']['difference']
data[22] = nDays['occurrence']
data[23] = nDays['higher']['count']
data[24] = nDays['higher']['pct']
data[25] = nDays['higher']['avg']
data[26] = nDays['lower']['count']
data[27] = nDays['lower']['pct']
data[28] = nDays['lower']['avg']
data[29] = nDays['same']['count']
data[30] = nDays['same']['pct']


Sheets.insertIntoWorksheet('NASDAQ Test', firstRow, data)

print('\n...\nFinished successfully')