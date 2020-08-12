import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'

with open (filename, 'r' ) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high and low temperature from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

print(highs)

plt.style.use('classic')
fig, ax= plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor= 'blue', alpha= 0.1)

# Format plot.
plt.title("Daily high and low temperature - 2018", fontsize = 20)
plt.xlabel("", fontsize= 14)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize = 14)
plt.tick_params(axis='both', which= 'major', labelsize = 16)

plt.show()
