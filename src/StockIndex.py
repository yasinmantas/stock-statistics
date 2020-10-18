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
            for i in range(len(values)):

                if i == self.index['high']:
                    high = float(values[i])

                    if high > allTimeHigh:
                        allTimeHigh = high
                        allTimeHighDate = values[self.index['date']]

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
                'higherClose': higherCloseCount,
                'higherClosePct': higherCloseCount/ dayCount * 100.0,
                'higherCloseAvg': higherCloseDifference / higherCloseCount,
                'lowerClose': lowerCloseCount,
                'lowerClosePct': lowerCloseCount/ dayCount * 100.0,
                'lowerCloseAvg': lowerCloseDifference / lowerCloseCount,
                'sameClose': sameCloseCount,
                'sameClosePct': sameCloseCount/ dayCount * 100.0
            }
