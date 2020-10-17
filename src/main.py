from StockIndex import StockIndex

data = open('files/NDX_D1.csv', 'r')

firstLine = data.readline()
metadata = firstLine.split(',')
index = {
    'date': -1,
    'open': -1,
    'high': -1,
    'low': -1,
    'close': -1,
}
for column in metadata:
    if column == 'Date':
        index['date'] = metadata.index(column)
    if column == 'Open':
        index['open'] = metadata.index(column)
    if column == 'High':
        index['high'] = metadata.index(column)
    if column == 'Low':
        index['low'] = metadata.index(column)
    if column == 'Close':
        index['close'] = metadata.index(column)


nasdaq = StockIndex(data.readlines(), ',', index['date'], index['open'], index['high'], index['low'], index['close'])

high = nasdaq.allTimeHigh()
print(high)

lowerHigherRatio = nasdaq.dailyLowerHigherRatio()
print(lowerHigherRatio)

data.close()

