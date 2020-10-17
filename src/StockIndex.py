class StockIndex:

    #data should be a list
    def __init__(self, data, separationChar, dateIndex, openIndex, highIndex, lowIndex, closeIndex):
        self.data = data
        self.separationChar = separationChar
        self.dateIndex = dateIndex
        self.openIndex = openIndex
        self.highIndex = highIndex
        self.lowIndex = lowIndex
        self.closeIndex = closeIndex

    def allTimeHigh(self):
        allTimeHigh = 0.0
        allTimeHighDate = ''

        for line in self.data:
            values = line.split(self.separationChar)
            for i in range(len(values)):

                if i == self.highIndex:
                    high = float(values[i])

                    if high > allTimeHigh:
                        allTimeHigh = high
                        allTimeHighDate = values[self.dateIndex]

        if allTimeHigh != 0.0 and allTimeHighDate != '':
            return {
                'value': allTimeHigh,
                'date': allTimeHighDate
            }


    def dailyLowerHigherRatio(self):
        dayCount = len(self.data)

        lowerCloseCount= 0
        higherCloseCount = 0
        sameCloseCount = 0
        lowerCloseDifference = 0.0
        higherCloseDifference = 0.0

        for line in self.data:
            values = line.split(self.separationChar)

            open = float(values[self.openIndex])
            close = float(values[self.closeIndex])

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



