from StockIndex import StockIndex
import pprint
import sheets

n = 2
down = True

# chaos for now TODO cleanup
firstRow = []
firstRow.append('Time period')
firstRow.append('ATH')
firstRow.append('Date')
firstRow.append('Closes higher')
firstRow.append('Pct.')
firstRow.append('Avg. points')
firstRow.append('Closes lower')
firstRow.append('Pct.')
firstRow.append('Avg. points')
firstRow.append('Closes same')
firstRow.append('Pct.')
firstRow.append('Most consecutive higher days')
firstRow.append('From date')
firstRow.append('to date')
firstRow.append('From points')
firstRow.append('to points')
firstRow.append('Difference')
firstRow.append('Most consecutive lower days')
firstRow.append('From date')
firstRow.append('to date')
firstRow.append('From points')
firstRow.append('to points')
firstRow.append('Difference')
firstRow.append(str(n) + ' days ' + ('down' if down else 'up' ) + ' in a row') # TODO make dynamic
firstRow.append('Higher the day after')
firstRow.append('Pct.')
firstRow.append('Avg.')
firstRow.append('Lower the day after')
firstRow.append('Pct.')
firstRow.append('Avg.')
firstRow.append('Same the day after')
firstRow.append('Pct.')

allDataRows = []

timePeriods = ['total', '85-89', '90-94', '95-99', '00-04', '05-09', '10-14', '15-19']

for period in timePeriods:
    if period == 'total':
        nasdaq = StockIndex('C:/Users/Yasin/Documents/stock-statistics/files/NDX_D1.csv')
    else:
        nasdaq = StockIndex('C:/Users/Yasin/Documents/stock-statistics/files/NDX_'+period+'.csv')

    high = nasdaq.allTimeHigh()
    # pprint.pprint(high)

    lowerHigherRatio = nasdaq.dailyLowerHigherRatio()
    # pprint.pprint(lowerHigherRatio)

    consecutiveDays = nasdaq.maxDaysInARow()
    # pprint.pprint(consecutiveDays)

    '''
    TODO: check if function dailyLowerHigherRatio() has become redundant
    -> dayAfterNDaysRatio with n = 0 returns same result
    '''
    nDays = nasdaq.dayAfterNDaysRatio(n, down)
    # pprint.pprint(nDays)


    data = []
    data.append(period)
    data.append(high['value'])
    data.append(high['date'])
    data.append(lowerHigherRatio['higherClose']['count'])
    data.append(lowerHigherRatio['higherClose']['pct'])
    data.append(lowerHigherRatio['higherClose']['avg'])
    data.append(lowerHigherRatio['lowerClose']['count'])
    data.append(lowerHigherRatio['lowerClose']['pct'])
    data.append(lowerHigherRatio['lowerClose']['avg'])
    data.append(lowerHigherRatio['sameClose']['count'])
    data.append(lowerHigherRatio['sameClose']['pct'])
    data.append(consecutiveDays['high']['count'])
    data.append(consecutiveDays['high']['startDate'])
    data.append(consecutiveDays['high']['endDate'])
    data.append(consecutiveDays['high']['startValue'])
    data.append(consecutiveDays['high']['endValue'])
    data.append(consecutiveDays['high']['difference'])
    data.append(consecutiveDays['low']['count'])
    data.append(consecutiveDays['low']['startDate'])
    data.append(consecutiveDays['low']['endDate'])
    data.append(consecutiveDays['low']['startValue'])
    data.append(consecutiveDays['low']['endValue'])
    data.append(consecutiveDays['low']['difference'])
    data.append(nDays['occurrence'])
    data.append(nDays['higher']['count'])
    data.append(nDays['higher']['pct'])
    data.append(nDays['higher']['avg'])
    data.append(nDays['lower']['count'])
    data.append(nDays['lower']['pct'])
    data.append(nDays['lower']['avg'])
    data.append(nDays['same']['count'])
    data.append(nDays['same']['pct'])

    allDataRows.append(data)

# print(allDataRows)


sheets.insertIntoWorksheet('NASDAQ', firstRow, allDataRows)

print('\n...\nFinished successfully')