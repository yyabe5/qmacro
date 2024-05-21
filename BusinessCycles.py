import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas_datareader as pdr
import numpy as np

# set the start and end dates for the data
start_date = '1960-01-01'
end_date = '2022-01-01'

# download the data from FRED using pandas_datareader
japan_gdp = web.DataReader('GDPC1', 'fred', start_date, end_date)
china_gdp = web.DataReader('MKTGDPCNA646NWDB', 'fred', start_date, end_date)
log_japan_gdp = np.log(japan_gdp)
log_china_gdp = np.log(china_gdp)

# calculate the quarterly percent change in real GDP
japan_gdp_pct_change = japan_gdp.pct_change(4)
china_gdp_pct_change = china_gdp.pct_change(4)

# apply a Hodrick-Prescott filter to the data to extract the cyclical component
japan_cycle = sm.tsa.filters.hpfilter(log_japan_gdp)
china_cycle = sm.tsa.filters.hpfilter(log_japan_gdp)

# Plot the original time series data
plt.plot(log_japan_gdp, label="Japan GDP (in log)")
plt.plot(log_china_gdp, label="China GDP (in log)")

# Add a legend and show the plot
plt.legend()
plt.show()

