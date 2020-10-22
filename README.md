# stock-statistics

This is a Python app, which calculates basic statistical parameters of a stock (index). The data is read as a CSV file (I use Yahoo Finance to download historical data).


**Implemented features**
* all time high
* ratio of days with price increase and days with price decrease
* maximum of price increasing/decreasing days in a row
* detect n days in a row and trend (higher lower ratio) for the day after
* Google Sheets Access


**Ideas / TODO**
* filter by dates
* automate csv prep by dates
* iterate through dayAfterNDaysRatio() with different params (days and up/down)
* transposed export to sheet
* 
