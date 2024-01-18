Name:- Hari singh r
Batch id :-DSWDMCOD 25082022 B

a)	Check whether the MPG of Cars follows Normal Distribution

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import scipy.stats as stats

df=pd.read_csv("D:/assignments of data science/13 confidence 1/Cars.csv")
df

fig = sm.qqplot(df.MPG, line='45',fit=True,dist=stats.norm)
plt.show()

b)   Check Whether the Adipose Tissue (AT) and Waist Circumference(Waist) 
from wc-at data set follows Normal Distribution 

dp=pd.read_csv("D:/assignments of data science/13 confidence 1/wc-at.csv")
dp
fige = sm.qqplot(dp.Waist,line='45',fit=True,dist=stats.norm)
figer = sm.qqplot(dp.AT,line='45',fit=True,dist=stats.norm)



##################################################################################################################

Q10) Consider a company that has two different divisions. The annual profits from the two divisions are independent and have distributions Profit1 ~ N(5, 3^2) and Profit2 ~ N(7, 4^2) respectively. Both the profits are in $ Million. Answer the following questions about the total profit of the company in Rupees. Assume that $1 = Rs. 45
A.	Specify a Rupee range (centered on the mean) such that it contains 95% probability for the annual profit of the company.
B.	Specify the 5th percentile of profit (in Rupees) for the company
C.	Which of the two divisions has a larger probability of making a loss each year?

Ans:-
import numpy as np
from scipy import stats
from scipy.stats import norm
import statistics as st
# Mean profits from two different divisions of a company = Mean1 + Mean2
Mean = 5+7
print('Mean Profit is Rs', Mean*45,'Million')
Mean Profit is Rs 540 Million
# Variance of profits from two different divisions of a company = SD^2 = SD1^2 + SD2^2
SD = np.sqrt((9)+(16))
print('Stdev is Rs', SD*45, 'Million')
Standard Deviation is Rs 225.0 Million
# A. Specify a Rupee range (centered on the mean) such that it contains 95% probability for the annual profit of the company.
print('Range is Rs',(stats.norm.interval(0.95,540,225)),'in Millions')
Range is Rs (99.00810347848784, 980.9918965215122) in Millions
# B. Specify the 5th percentile of profit (in Rupees) for the company
# To compute 5th Percentile, we use the formula X=μ + Zσ; wherein from z table, 5 percentile = -1.645
X= 540+(-1.645)*(225)
print('5th percentile of profit (in Million Rupees) is',np.round(X,))
5th percentile of profit (in Million Rupees) is 170.0
# C. Which of the two divisions has a larger probability of making a loss in a given year?
# Probability of Division 1 making a loss P(X<0)
stats.norm.cdf(0,5,3)
0.0477903522728147
# Probability of Division 2 making a loss P(X<0)