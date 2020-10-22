from StockIndex import StockIndex
import pprint
import sheets

n = 2
down = True

# chaos for now TODO cleanup
firstRow = ['' for i in range(32)]
firstRow[0] = 'Time period'
firstRow[1] = 'ATH'
firstRow[2] = 'Date'
firstRow[3] = 'Closes higher'
firstRow[4] = 'Pct.'
firstRow[5] = 'Avg. points'
firstRow[6] = 'Closes lower'
firstRow[7] = 'Pct.'
firstRow[8] = 'Avg. points'
firstRow[9] = 'Closes same'
firstRow[10] ='Pct.'
firstRow[11] = 'Most consecutive higher days'
firstRow[12] = 'From date'
firstRow[13] = 'to date'
firstRow[14] = 'From points'
firstRow[15] = 'to points'
firstRow[16] = 'Difference'
firstRow[17] = 'Most consecutive lower days'
firstRow[18] = 'From date'
firstRow[19] = 'to date'
firstRow[20] = 'From points'
firstRow[21] = 'to points'
firstRow[22] = 'Difference'
firstRow[23] = str(n) + ' days ' + ('down' if down else 'up' ) + ' in a row' # TODO make dynamic
firstRow[24] = 'Higher the day after'
firstRow[25] = 'Pct.'
firstRow[26] = 'Avg.'
firstRow[27] = 'Lower the day after'
firstRow[28] = 'Pct.'
firstRow[29] = 'Avg.'
firstRow[30] = 'Same the day after'
firstRow[31] = 'Pct.'

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


    data = ['' for i in range(32)]
    data[0] = period
    data[1] = high['value']
    data[2] = high['date']
    data[3] = lowerHigherRatio['higherClose']['count']
    data[4] = lowerHigherRatio['higherClose']['pct']
    data[5] = lowerHigherRatio['higherClose']['avg']
    data[6] = lowerHigherRatio['lowerClose']['count']
    data[7] = lowerHigherRatio['lowerClose']['pct']
    data[8] = lowerHigherRatio['lowerClose']['avg']
    data[9] = lowerHigherRatio['sameClose']['count']
    data[10] =lowerHigherRatio['sameClose']['pct']
    data[11] = consecutiveDays['high']['count']
    data[12] = consecutiveDays['high']['startDate']
    data[13] = consecutiveDays['high']['endDate']
    data[14] = consecutiveDays['high']['startValue']
    data[15] = consecutiveDays['high']['endValue']
    data[16] = consecutiveDays['high']['difference']
    data[17] = consecutiveDays['low']['count']
    data[18] = consecutiveDays['low']['startDate']
    data[19] = consecutiveDays['low']['endDate']
    data[20] = consecutiveDays['low']['startValue']
    data[21] = consecutiveDays['low']['endValue']
    data[22] = consecutiveDays['low']['difference']
    data[23] = nDays['occurrence']
    data[24] = nDays['higher']['count']
    data[25] = nDays['higher']['pct']
    data[26] = nDays['higher']['avg']
    data[27] = nDays['lower']['count']
    data[28] = nDays['lower']['pct']
    data[29] = nDays['lower']['avg']
    data[30] = nDays['same']['count']
    data[31] = nDays['same']['pct']

    allDataRows.append(data)

# print(allDataRows)


sheets.insertIntoWorksheet('NASDAQ', firstRow, allDataRows)

print('\n...\nFinished successfully')