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
        lowerCloseDiffPct = 0.0
        higherCloseDifference = 0.0
        higherCloseDiffPct = 0.0

        for line in self.data:
            values = line.split(self.separationChar)

            open = float(values[self.index['open']])
            close = float(values[self.index['close']])

            diff = close - open
            diffPct = (close / open) - 1

            if close > open:
                higherCloseCount += 1
                higherCloseDifference += diff
                higherCloseDiffPct += diffPct
            elif close < open:
                lowerCloseCount += 1
                lowerCloseDifference += diff
                lowerCloseDiffPct += diffPct
            else:
                sameCloseCount += 1

        if lowerCloseCount + higherCloseCount + sameCloseCount == dayCount:
            return {
                'higherClose': {
                    'count': higherCloseCount,
                    'pct': higherCloseCount / dayCount,
                    'avg': higherCloseDifference / higherCloseCount,
                    'diff': higherCloseDiffPct / higherCloseCount
                },
                'lowerClose': {
                    'count': lowerCloseCount,
                    'pct': lowerCloseCount / dayCount,
                    'avg': lowerCloseDifference / lowerCloseCount,
                    'diff': lowerCloseDiffPct / lowerCloseCount
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
            'difference': 0.0,
        }
        lowest = {
            'count': 0,
            'startDate': '',
            'endDate': '',
            'startValue': 0.0,
            'endValue': 0.0,
            'difference': 0.0,
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

            # TODO same close does not break streak (should it?)
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
                        lowest['difference'] = lowest['endValue'] - lowest['startValue']
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
                        highest['difference'] = highest['endValue'] - highest['startValue']
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

    def maxDailyChange(self):
        maxIncreasePct = 0.0
        maxIncreaseDate = ''
        maxDecreasePct = 0.0
        maxDecreaseDate = ''

        for line in self.data:
            values = line.split(self.separationChar)
            open = float(values[self.index['open']])
            close = float(values[self.index['close']])
            date = values[self.index['date']]

            changePct = (close / open) - 1

            if close > open and changePct > maxIncreasePct:
                maxIncreasePct = changePct
                maxIncreaseDate = date
            if close < open and changePct < maxDecreasePct:
                maxDecreasePct = changePct
                maxDecreaseDate = date

        return {
            'up': {
                'pct': maxIncreasePct,
                'date': maxIncreaseDate,
            },
            'down': {
                'pct': maxDecreasePct,
                'date': maxDecreaseDate,
            }
        }

    # TODO: check if function dailyLowerHigherRatio() has become redundant -> dayAfterNDaysRatio with n = 0 returns same result
    def dayAfterNDaysRatio(self, n: int, down: bool = True):
        """
        Looks for N up/down days in a row and evaluates the following day

        Keyword arguments:
        n -- number of days in a row
        down -- whether to look for lower (True) or higher (false) closing days. Lower is default.
        """

        # counters
        occurrence = 0
        higherCount = 0
        lowerCount = 0
        sameCount = 0
        # for avg calc
        # total difference in points
        higherTotal = 0.0
        lowerTotal = 0.0
        # total difference in pct
        higherPctTotal = 0.0
        lowerPctTotal = 0.0

        length = len(self.data)
        # starting at n instead of 0 because n days in a row are checked backwards
        for i in range(n, length):
            # values of current row
            currentValues = self.data[i].split(self.separationChar)
            currentOpen = float(currentValues[self.index['open']])
            currentClose = float(currentValues[self.index['close']])
            currentHigher = currentClose > currentOpen
            currentLower = currentClose < currentOpen

            # master boolean; indicates whether all previous n days match criteria
            allNPreviousDaysMatch = True

            # iterate through n previous days
            for j in range(1, n + 1):
                previousValues = self.data[i-j].split(self.separationChar)
                previousOpen = float(previousValues[self.index['open']])
                previousClose = float(previousValues[self.index['close']])
                previousLower = previousClose < previousOpen
                previousHigher = previousClose > previousOpen

                # n days down requested (default)
                if down:
                    if allNPreviousDaysMatch and previousLower:
                        allNPreviousDaysMatch = True
                    else:
                        allNPreviousDaysMatch = False
                # n days up requested
                else:
                    if allNPreviousDaysMatch and previousHigher:
                        allNPreviousDaysMatch = True
                    else:
                        allNPreviousDaysMatch = False

            # count only if all n days match criteria
            if allNPreviousDaysMatch:
                occurrence += 1
                if currentHigher:
                    higherCount += 1
                    higherTotal += currentClose - currentOpen
                    higherPctTotal += (currentClose / currentOpen) - 1
                elif currentLower:
                    lowerCount += 1
                    lowerTotal += currentOpen - currentClose
                    lowerPctTotal += (currentClose / currentOpen) - 1
                else:
                    sameCount += 1

        if occurrence != 0:
            return {
                'down': True if down else False,
                'occurrence': occurrence,
                'higher': {
                    'count': higherCount,
                    'pct': higherCount / occurrence,
                    'avg': higherTotal / higherCount,
                    'diff': higherPctTotal / higherCount
                },
                'lower': {
                    'count': lowerCount,
                    'pct': lowerCount / occurrence,
                    'avg': - lowerTotal / lowerCount,
                    'diff': lowerPctTotal / lowerCount
                },
                'same': {
                    'count': sameCount,
                    'pct': sameCount / occurrence
                }
            }
        else:
            return {
                'occurrence': occurrence
            }
