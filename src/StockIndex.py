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

        lowerClose = 0
        higherClose = 0
        sameClose = 0

        for line in self.data:
            values = line.split(self.separationChar)

            if values[self.closeIndex] > values[self.openIndex]:
                higherClose += 1
            elif values[self.closeIndex] < values[self.openIndex]:
                lowerClose += 1
            else:
                sameClose += 1

        if lowerClose + higherClose + sameClose == dayCount:
            return {
                'higherClose': higherClose,
                'higherClosePct': higherClose / dayCount * 100.0,
                'lowerClose': lowerClose,
                'lowerClosePct': lowerClose / dayCount * 100.0,
                'sameClose': sameClose,
                'sameClosePct': sameClose / dayCount * 100.0
            }


