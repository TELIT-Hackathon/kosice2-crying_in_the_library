from matplotlib import pyplot
import pandas as pd


def time_troughput():
    series = pd.read_csv('throughput_datetime.csv', header=0, index_col=0, squeeze=True)
    series.plot()
    pyplot.show()

time_troughput()

