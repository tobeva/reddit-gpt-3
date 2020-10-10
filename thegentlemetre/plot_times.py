import datetime
import matplotlib.pyplot as plt

from matplotlib.ticker import MultipleLocator


def _hour(d):
    return d.hour + d.minute / 60 + d.second / 3600


def plot(lines):
    datetimes = [datetime.datetime.fromtimestamp(int(t)) for t in lines]
    dates = [datetime.date(d.year, d.month, d.day) for d in datetimes]
    times = [_hour(d) for d in datetimes]

    for d in datetimes:
        print(d.hour)

    plt.style.use('ggplot')
    fix, ax = plt.subplots()

    plt.plot(dates, times, 'o')

    plt.title("Posts by reddit user /u/thegentlemetre")
    plt.xlabel("Date")
    plt.ylabel("Hour of Day")
    plt.ylim(0, 24)
    plt.grid(which='minor')
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(5))
    ax.xaxis.set_major_locator(MultipleLocator(1))
    plt.show()


f = open("times2.txt")
lines = f.readlines()
plot(lines)

