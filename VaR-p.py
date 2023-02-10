from scipy.stats import norm
import pandas as pd
import pandas_datareader.data as wb
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

tickers = ["aapl", "nvda", "googl", "tsla"]
ponderacion = np.array([.5,.2,.2,.1])

data = pd.DataFrame()
for x in tickers:
    data[x] = yf.download(x, '2013-1-1')['Adj Close']

returns = data.pct_change()    #divide el ultimo valor en el anteultimo  (n/n-1)
cov_matrix = returns.cov()     #covarianza de los retornos
returns_mean = returns.mean()  #promedio
portfolio_mean = returns_mean.dot(ponderacion)
portfolio_stdev = np.sqrt(ponderacion.T.dot(cov_matrix).dot(ponderacion))  

investment = float(150000)
mean_investment = (1+portfolio_mean) * investment
stdev_investment = investment * portfolio_stdev

conf_level = 0.05
cut = norm.ppf(conf_level, mean_investment, stdev_investment)
var_id = investment - cut
num_days = int(100)

var_array = []

print('\nLa perdida maxima de tu cartera con ' + str(investment) + ' eur\ncon un nivel de confianza del ' + str((1-conf_level)*100) + ' % y para los siguientes ' + str(num_days)+' dias es de:\n ')

for i in range(1, num_days):
    var_array.append(np.round(var_id*np.sqrt(i),2))
    print('A ' + str(i) + ' dias VaR(' + str((1-conf_level)*100)+ '%) = '+ str((np.round(var_id*np.sqrt(i),2))))
    
plt.xlabel('Dias')
plt.ylabel('Perdida maxima de nuestra cartera')
plt.title('Perdima maxima de la cartera para el periodo')
plt.plot(var_array, 'b')
plt.show()
