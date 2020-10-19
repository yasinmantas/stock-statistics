class StockIndex:

    def __init__(self, path: str, separationChar: str, dateString: str, openString: str, highString: str, lowString:str, closeString: str):
        
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
                    'pct': higherCloseCount / dayCount * 100.0,
                    'avg': higherCloseDifference / higherCloseCount
                },
                'lowerClose': {
                    'count': lowerCloseCount,
                    'pct': lowerCloseCount / dayCount * 100.0,
                    'avg': lowerCloseDifference / lowerCloseCount
                },
                'sameClose': {
                    'count': sameCloseCount,
                    'pct': sameCloseCount / dayCount * 100.0
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


    # def countNDaysInARow(self, n: int, down: bool):

    #     for i in range(len(self.data)):
    #         line = self.data[i]

    #         values = line.split(self.separationChar)

    #         found = 0

    #         if (down):
    #             if values[self.index['close']] < values[self.index['open']]:
    #                 found += 1
    #                 while found < n:
    #                     j = i + 1
    #                     nextLine = self.data[j]
    #                     nextLineValues = nextLine.split(self.separationChar)
    #                     if nextLineValues[self.index['close']] < nextLineValues[self.index['open']]:
    #                         found += 1
    #                         print(found)
    #                     else:
    #                         found = n
    #                     j += 1

    #         # else:
    #         #     if values[self.index['close']] > values[self.index['open']]: