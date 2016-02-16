import tushare as ts
dfsh = ts.get_hist_data('sh',start='2016-01-05')
date = list(dfsh.index)
[today,last] = date[0:2]
df = ts.get_today_all() 
lastData = df.loc[:,['code','name','volume']]
lastData.to_json(today+'-unicode.json',orient='records')
lastData.to_json(today+'-gbk.json',orient='records',force_ascii=False) 
df.to_json(today+'-gbk-all.json',orient='records',force_ascii=False) 
print 'Done!'