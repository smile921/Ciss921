#!/usr/bin/env python
# -*- coding: GB2312 -*-
import re
import ast
import urllib
import httplib2

"""
create by hail
"""
class stockAPI():
    """
    http://fund.eastmoney.com/FBSJJ_zjl.html
    http://fund.eastmoney.com/cnjy_dwjz.html
    vip.stock.finance.sina.com.cn
    """
    def __init__(self):
        self.vip_host = "http://vip.stock.finance.sina.com.cn"
        self.sc_host  = "http://screener.finance.sina.com.cn"
        self.SSCore_uri = "/znxg/data/json.php/SSCore.doView"
        self.market_uri = "/quotes_service/api/json.php/Market_Center.getHQNodeData"
        self.industry = {"new_swzy":"生物制药", "new_ylqx":"医疗器械","new_dzxx":"电子信息", \
                         "new_cmyl":"传媒娱乐", "new_zhhy":"综合行业"}

    def _set_host(self, host):
        self.host = host

    def _http_request(self, uri, method, args):
        http = httplib2.Http()
        try:
            #LOG.debug("agent API:"+self.host+uri+"?"+urllib.urlencode(args))
            res, content = http.request(self.host + uri+"?"+urllib.urlencode(args),
                                    method)
        except IOError as e:
            content = """{"success":false, "data":"error %s"}""" %(e)

        content = re.sub(r'([{,]?)([a-z_]+):', r'\1"\2":', content)
        content = content.replace("true", "True")
        content = content.replace("false", "False")
        #LOG.debug("API result:" + content)
        return ast.literal_eval(content)


    def get_market_data(self, node):
        node_dict = {"page":1,"num":1000,"sort":"symbol","asc":1,\
                     "node":node,"symbol":"","_s_r_a":"init"}
        self._set_host(self.vip_host)
        sock_list = self._http_request(self.market_uri, "GET", node_dict)
        for sock in sock_list:
            print sock["symbol"],sock["name"]

    def get_sscore(self, node):
        sscore_dict = {"page":1,"num":2000,"sort":"","asc":0, \
                       "field0":"stocktype","field1":"sinahy","field2":"diyu", \
                       "value0":"*","value1":node,"value2":"*", \
                       "field3":"gb_g",   "min3": 0, "max3":1000000000}
        self._set_host(self.sc_host)
        sock_list = self._http_request(self.SSCore_uri, "POST", sscore_dict)
        if 'items' not in sock_list:
            print "========="+node
        else:
            for sock in sock_list['items']:
                if re.match('(sz|sh)30\d{4}',sock['symbol']) == None:
                    print sock["symbol"],sock["name"], self.industry[node], \
                        int(sock["ssmcap"]/1e8),int(sock["sstcap"]/1e8),sock["gb_g"],\
                        "http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/"+sock["symbol"].replace("sh","").replace("sz","")+"/displaytype/4.phtml"

if __name__ == '__main__':
    api = stockAPI()
    #api.get_market_data("sw_cm")
    for node in api.industry:
        #print node
        api.get_sscore(node)