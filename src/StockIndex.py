class StockIndex:

    def __init__(self, path: str, separationChar: str = ',', dateString: str = 'Date', openString: str = 'Open', highString: str = 'High', lowString: str = 'Low', closeString: str = 'Close'):

        self.file = open(path, 'r')

        firstLine = self.file.readline()
        metadata = firstLine.split(separationChar)
        self.index = {
            'date': -1,
            'open': -1,
            'high': -1,
            'low': -1,
            'close': -1,
        }
        for column in metadata:
            if column == dateString:
                self.index['date'] = metadata.index(column)
            if column == openString:
                self.index['open'] = metadata.index(column)
            if column == highString:
                self.index['high'] = metadata.index(column)
            if column == lowString:
                self.index['low'] = metadata.index(column)
            if column == closeString:
                self.index['close'] = metadata.index(column)

        self.data = self.file.readlines()
        self.separationChar = separationChar

    def __del__(self):
        self.file.close()

    def allTimeHigh(self):
        allTimeHigh = 0.0
        allTimeHighDate = ''

        for line in self.data:
            values = line.split(self.separationChar)
            high = float(values[self.index['high']])
            date = values[self.index['date']]

            if high > allTimeHigh:
                allTimeHigh = high
                allTimeHighDate = date

        if allTimeHigh != 0.0 and allTimeHighDate != '':
            return {
                'value': allTimeHigh,
                'date': allTimeHighDate
            }

    def dailyLowerHigherRatio(self):
        dayCount = len(self.data)

        lowerCloseCount = 0
        higherCloseCount = 0
        sameCloseCount = 0
        lowerCloseDifference = 0.0
        higherCloseDifference = 0.0

        for line in self.data:
            values = line.split(self.separationChar)

            open = float(values[self.index['open']])
            close = float(values[self.index['close']])

            if close > open:
                higherCloseCount += 1
                diff = close - open
                higherCloseDifference += diff
            elif close < open:
                lowerCloseCount += 1
                diff = close - open
                lowerCloseDifference += diff
            else:
                sameCloseCount += 1

        if lowerCloseCount + higherCloseCount + sameCloseCount == dayCount:
            return {
                'higherClose': {
                    'count': higherCloseCount,
                    'pct': higherCloseCount / dayCount,
                    'avg': higherCloseDifference / higherCloseCount
                },
                'lowerClose': {
                    'count': lowerCloseCount,
                    'pct': lowerCloseCount / dayCount,
                    'avg': lowerCloseDifference / lowerCloseCount
                },
                'sameClose': {
                    'count': sameCloseCount,
                    'pct': sameCloseCount / dayCount
                },
            }

    def maxDaysInARow(self):
        higher = {
            'count': 0,
            'startDate': '',
            'endDate': '',
            'startValue': 0.0,
            'endValue': 0.0,
        }
        lower = {
            'count': 0,
            'startDate': '',
            'endDate': '',
            'startValue': 0.0,
            'endValue': 0.0,
        }
        highest = {
            'count': 0,
            'startDate': '',
            'endDate': '',
            'startValue': 0.0,
            'endValue': 0.0,
        }
        lowest = {
            'count': 0,
            'startDate': '',
            'endDate': '',
            'startValue': 0.0,
            'endValue': 0.0,
        }

        # detect first direction
        firstLine = self.data[0]
        firstValues = firstLine.split(self.separationChar)
        firstOpen = float(firstValues[self.index['open']])
        firstClose = float(firstValues[self.index['close']])

        # opposite values to trigger first day recognition
        if firstClose > firstOpen:
            lastDayWasLow = True
            lastDayWasHigh = False
        elif firstClose < firstOpen:
            lastDayWasHigh = True
            lastDayWasLow = False

        for line in self.data:
            values = line.split(self.separationChar)
            open = float(values[self.index['open']])
            close = float(values[self.index['close']])
            today = values[self.index['date']]

            if close > open:
                # first green day
                if lastDayWasLow:
                    # end red days counter
                    if lower['count'] > lowest['count']:
                        lowest['count'] = lower['count']
                        lowest['startDate'] = lower['startDate']
                        lowest['endDate'] = lower['endDate']
                        lowest['startValue'] = lower['startValue']
                        lowest['endValue'] = lower['endValue']
                    lower['count'] = 0
                    
                    # start green days counter
                    higher['count'] = 1
                    higher['startDate'] = today
                    higher['startValue'] = open

                # consecutive green day
                if lastDayWasHigh:
                    # continue green days counter
                    higher['count'] += 1
                    higher['endDate'] = today
                    higher['endValue'] = close

                lastDayWasHigh = True
                lastDayWasLow = False

            # same same as above, but different
            elif close < open:
                # first red day
                if lastDayWasHigh:
                    # end green days counter
                    if higher['count'] > highest['count']:
                        highest['count'] = higher['count']
                        highest['startDate'] = higher['startDate']
                        highest['endDate'] = higher['endDate']
                        highest['startValue'] = higher['startValue']
                        highest['endValue'] = higher['endValue']
                    higher['count'] = 0

                    # start red days counter
                    lower['count'] = 1
                    lower['startDate'] = today
                    lower['startValue'] = open

                # consecutive red day
                if lastDayWasLow:
                    # continue red days counter
                    lower['count'] += 1
                    lower['endDate'] = today
                    lower['endValue'] = close

                lastDayWasLow = True
                lastDayWasHigh = False

        return {
            'high': highest,
            'low': lowest
        }

    def dayAfterTwoDaysRatio(self):
        # counters
        occurrence = 0
        higherCount = 0
        lowerCount = 0
        sameCount = 0
        # total points (to calculate averages)
        higherTotal = 0.0
        lowerTotal = 0.0


        length = len(self.data)
        for i in range(2, length):
            # current value
            values = self.data[i].split(self.separationChar)
            open = float(values[self.index['open']])
            close = float(values[self.index['close']])
            currentHigher = close > open
            currentLower = close < open

            # previous value (-1)
            previousValues = self.data[i-1].split(self.separationChar)
            previousOpen = float(previousValues[self.index['open']])
            previousClose = float(previousValues[self.index['close']])
            # previousHigher = previousClose > previousOpen
            previousLower = previousClose < previousOpen
            
            # previous value (-2)
            previousValues2 = self.data[i-2].split(self.separationChar)
            previousOpen2 = float(previousValues2[self.index['open']])
            previousClose2 = float(previousValues2[self.index['close']])
            # previousHigher2 = previousClose2 > previousOpen2
            previousLower2 = previousClose2 < previousOpen2
            

            if previousLower2 and previousLower:
                occurrence += 1
                if currentHigher:
                    higherCount += 1
                    higherTotal += close - open
                elif currentLower:
                    lowerCount += 1
                    lowerTotal += open - close
                else:
                    sameCount += 1
        
        return {
            'occurrence': occurrence,
            'higher': {
                'count': higherCount,
                'pct': higherCount / occurrence,
                'avg': higherTotal / higherCount
            },
            'lower': {
                'count': lowerCount,
                'pct': lowerCount / occurrence,
                'avg': lowerTotal / lowerCount
            },
            'same': {
                'count': sameCount,
                'pct': sameCount / occurrence
            }
        }
