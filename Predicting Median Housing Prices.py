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

