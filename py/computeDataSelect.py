import tushare as ts
import pandas as pd
import numpy as np
dfsh = ts.get_hist_data('sh',start='2016-01-05')
date = list(dfsh.index)
[today,last] = date[0:2]
print 'read_json data from file '
dft = pd.read_json(today+'-gbk-all.json',orient='records', typ='frame',numpy=False) 
dfy = pd.read_json(last+'-gbk-all.json',orient='records', typ='frame',numpy=False) 

# pandas.read_json(path_or_buf=None, orient=None, typ='frame', dtype=True, convert_axes=True, 
# convert_dates=True, keep_default_dates=True, numpy=False, precise_float=False, date_unit=None) 
# Convert a JSON string to pandas object
tdata = dft.loc[:,['code','name','volume']]
ydata = dfy.loc[:,['code','name','volume']]

tdata =  tdata.set_index(['code'])
ydata =  ydata.set_index(['code'])
tdata['volumeLast']=ydata['volume']
tdata['rate']= tdata['volume']/tdata['volumeLast']
tdata.columns
alpha =1000
data = tdata[(tdata.volume>alpha) & (tdata.volumeLast>alpha) & (tdata.rate<20)].sort_values(by='rate')
data.sort_values(by='rate').to_excel('a.xls');
date  = [today,last]
print date 
print '------------------------------------------------------'
print data.head(10)
print  '\t\t\n'
print data.tail(10)
print '------------------------------------------------------'
print data[(data.rate>2) & (data.rate <5) ].head(20)
print  '\t\t\n'
print data[(data.rate>2) & (data.rate <5) ].tail(20)
print  '\t\t\n'