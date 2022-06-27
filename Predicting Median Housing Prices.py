"""
Created on Thu Jun 23 21:08:27 2022

Prediciting Median Housing Prices with
GDP, Median Wage, Inflation Rate, Unemployment Rate

@author: ryantvackner
@date: 06/23/2022
"""

# import packages
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.sandbox.regression.predstd import wls_prediction_std

import matplotlib.pyplot as plt
import pandas as pd

# import data
root = 'https://raw.githubusercontent.com/ryantvackner/predictng-median-housing-prices/main/'

median_housing_price = pd.read_csv(root + 'MedianSalesPriceofHouses.csv')
consumer_price_index = pd.read_csv(root + 'ConsumerPriceIndex.csv')
gross_domestic_product = pd.read_csv(root + 'GrossDomesticProduct.csv')
median_weekly_nominal_earnings = pd.read_csv(root + 'MedianWeeklyNominalEarnings.csv')
unemployment_rate = pd.read_csv(root + 'UnemploymentRate.csv')

# merge data frames into one data frame by date
df = (median_weekly_nominal_earnings.merge(median_housing_price, on='DATE')
      .merge(consumer_price_index, on='DATE')
      .merge(gross_domestic_product, on='DATE')
      .merge(unemployment_rate, on='DATE'))

# rename the columns of the data frame
df.rename(columns={'LES1252881500Q':'median_weekly_nominal_earnings', 
                   'MSPUS':'median_housing_price', 
                   'CORESTICKM159SFRBATL':'consumer_price_index',
                   'GDP':'gross_domestic_product',
                   'UNRATE':'unemployment_rate'}, inplace = True)
