from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
start_date = '2004-08-19'
end_date = '2020-04-17'
google_data = data.DataReader('GOOGL','yahoo', start_date, end_date)
google_data.head(9)

google_data['Close'].plot()