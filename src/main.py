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

# allTimeLow = 0.0
allTimeHigh = 0.0
allTimeHighDate = ''

for line in data.readlines():
    values = line.split(',')

    for i in range(len(values)):

        if i == index['high']:
            high = float(values[i])

            if high > allTimeHigh:
                allTimeHigh = high
                allTimeHighDate = values[index['date']]




print('all time high was ' + str(allTimeHigh) + ' on ' + allTimeHighDate)

data.close()

