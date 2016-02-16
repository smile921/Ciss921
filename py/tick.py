# -*- coding: utf-8 -*-

import sys
import random
try:
    import tushare as ts
    from PyQt4 import Qt
    from PyQt4 import QtHelp
    from PyQt4 import QtCore
    from PyQt4 import QtGui
except ImportError:
    print(Qt.version)
    pass

class report_painter:
    '''绘制行情类'''
    def __init__(self,parent):

        #初始化
        self.parent = parent
        self.paint = QtGui.QPainter()
        self.paint.begin(self.parent)
 
        #设置抗锯齿
        #self.paint.setRenderHint(QtGui.QPainter.Antialiasing)
        #度量尺对象
        self.metrics = self.paint.fontMetrics()
         
        #设置字体库
        self.fonts = dict()
        self.fonts['default'] = QtGui.QFont('Serif', 9, QtGui.QFont.Light)
        self.fonts['yahei_14_bold']= QtGui.QFont('Serif',12,QtGui.QFont.Bold)
        self.fonts['yahei_14']= QtGui.QFont('Serif',12,QtGui.QFont.Light)
        self.setFont('default')

        #设置笔刷样式库
        self.pens = dict()
         
        #红色 1px粗  1px点 2px距 线条
        self.pens['red_1px_dashline'] =  QtGui.QPen( QtCore.Qt.red, 1, QtCore.Qt.DashLine) 
        self.pens['red_1px_dashline'].setDashPattern([1,2])

        #灰色 1px粗  1px点 2px距 线条
        self.pens['gray_1px_dashline'] =  QtGui.QPen( QtCore.Qt.gray, 1, QtCore.Qt.DashLine) 
        self.pens['gray_1px_dashline'].setDashPattern([1,2])

        #暗灰色 1px粗  1px点 2px距 线条
        self.pens['darkGray_1px_dashline'] =  QtGui.QPen( QtCore.Qt.darkGray, 1, QtCore.Qt.DashLine) 
        self.pens['darkGray_1px_dashline'].setDashPattern([1,2])

        #红色 1px粗 实线条
        self.pens['red'] = QtGui.QPen( QtCore.Qt.red, 1, QtCore.Qt.SolidLine)
        #红色 3px粗 实线条
        self.pens['red_2px'] = QtGui.QPen( QtCore.Qt.red, 2, QtCore.Qt.SolidLine)
        #红色 2px粗 实线条
        self.pens['red_3px'] = QtGui.QPen( QtCore.Qt.red, 3, QtCore.Qt.SolidLine)
        #黄色 1px粗 实线条
        self.pens['yellow'] = QtGui.QPen( QtCore.Qt.yellow, 1, QtCore.Qt.SolidLine)
        #白色 1px粗 实线条
        self.pens['white']  = QtGui.QPen( QtCore.Qt.white , 1, QtCore.Qt.SolidLine)
        #灰色 1px粗 实线条
        self.pens['gray']   = QtGui.QPen( QtCore.Qt.gray, 1, QtCore.Qt.SolidLine)
        #暗灰色 1px粗 实线条
        self.pens['darkGray']   = QtGui.QPen( QtCore.Qt.darkGray, 1, QtCore.Qt.SolidLine)
        #绿色 1px粗 实线条
        self.pens['green']   = QtGui.QPen( QtCore.Qt.green, 1, QtCore.Qt.SolidLine)
        #绿色 3px粗 实线条
        self.pens['green_2px']   = QtGui.QPen( QtCore.Qt.green, 2, QtCore.Qt.SolidLine)
        #亮蓝 1px粗  1px点 2px距 线条
        self.pens['cyan_1px_dashline'] =  QtGui.QPen( QtCore.Qt.cyan, 1, QtCore.Qt.DashLine) 
        self.pens['cyan_1px_dashline'].setDashPattern([3,2])
        #获得窗口的长和宽
        size      = self.parent.size()
        self.w    = size.width()
        self.h    = size.height()
 
        #设置grid的上下左右补丁边距
        self.grid_padding_left   = 45  #左侧补丁边距
        self.grid_padding_right  = 245 #右侧补丁边距
        #self.grid_padding_right  = 45  #右侧补丁边距
        self.grid_padding_top    = 25  #顶部补丁边距
        self.grid_padding_bottom = 17  #底部补丁边距
             
        #开始绘制
        self.start_paint()
 
 
        self.paint.end()   #结束
    '''绘制流程步骤'''
    def start_paint(self):
        self.PriceGridPaint()
        self.rightGridPaint()
        self.timelinePaint()
        self.topInfoPaint()
        self.rulerPaint()
        self.VolumeGridPaint()
        self.volumePaint()
        self.pricePaint()
        #self.xyPaint()
    '''设置使用的字体'''
    def setFont(self,code='default'):
        self.paint.setFont(self.fonts[code])
         
    '''设置使用的笔刷'''
    def setPen(self,code='default'):
        self.paint.setPen(self.pens[code])
         
    '''时间到时间轴坐标转换 '''
    def time2Pos(self,stime):
        import datetime
        t_915 = 9*3600+15*60
        t_1300 = 13*3600
        tt = datetime.datetime.strptime(stime,"%H:%M:%S").time()
        pos = tt.hour*3600+tt.minute*60+tt.second
        if pos < t_1300:
            return pos - t_915
        return pos - t_1300 + 7200 + 15*60

    '''绘制股价走势表格'''
    def PriceGridPaint(self):
        self.setPen('darkGray')
        self.paint.setBrush(QtCore.Qt.NoBrush)
         
        sum_width  = self.grid_padding_left+self.grid_padding_right
        sum_height = self.grid_padding_top+self.grid_padding_bottom
 
        grid_height = self.h-sum_height
 
        #画边框
        self.paint.drawRect(self.grid_padding_left,self.grid_padding_top,
                            self.w-sum_width,self.h-sum_height)
        #成交量和走势的分界线
        self.paint.drawLine(self.grid_padding_left,grid_height*0.7+self.grid_padding_top,
                            self.w-self.grid_padding_right,grid_height*0.7+self.grid_padding_top)
 
        #股票昨收中间线
        self.paint.drawLine(self.grid_padding_left+1,
                            grid_height*0.35+self.grid_padding_top,
                            self.w-self.grid_padding_right
                            ,grid_height*0.35+self.grid_padding_top)
 
        #其他线条
        self.paint.drawLine(0,self.h-self.grid_padding_bottom,self.w-self.grid_padding_right+44,self.h-self.grid_padding_bottom)
        self.paint.drawLine(0,self.h-self.grid_padding_bottom+16,self.w,self.h-self.grid_padding_bottom+16)
 
        self.paint.drawLine(self.w-self.grid_padding_right,0,
                            self.w-self.grid_padding_right,self.h-self.grid_padding_bottom+16)
        self.paint.drawLine(self.w-self.grid_padding_right+44,0,
                            self.w-self.grid_padding_right+44,self.h-self.grid_padding_bottom+16)
        self.setPen('yellow')
        self.paint.drawText(self.w-self.grid_padding_right+5,self.h-self.grid_padding_bottom-4,str('成交量'))
        self.setPen('white')
        #右下角文字
        #self.paint.drawText(self.w-self.grid_padding_right+12,self.h-self.grid_padding_bottom+12,str('实时'))
    '''绘制成交量走势表格'''
    def VolumeGridPaint(self):
        sum_width  = self.grid_padding_left + self.grid_padding_right
        sum_height = self.grid_padding_top  + self.grid_padding_bottom
         
        grid_height = self.h-sum_height
        max_volume = max(self.parent.stk_ticks['volume'])
        
        px_h_radio = max_volume/(grid_height*0.3)
         
        grid_num = 6
        x = grid_num
        cnt = grid_height*0.3/grid_num
        for i in range(0,grid_num):
            self.setPen('darkGray_1px_dashline')
            #计算坐标
            y1 = self.grid_padding_top+(grid_height*0.7)+i*cnt
            x1 = self.grid_padding_left
            x2 = self.grid_padding_left+self.w-sum_width
             
            self.paint.drawLine(x1,y1,x2,y1) #画价位虚线
             
            vol_int = int(cnt*x*px_h_radio)
            vol_str = str(vol_int)
            fw = self.metrics.width(vol_str) #获得文字宽度
            fh = self.metrics.height()/2   #获得文字高度
            self.setPen('yellow')
            self.paint.drawText(x2+40-fw,y1+fh,vol_str) #写入文字
            self.setPen('white')
            self.paint.drawText(x1-2-self.metrics.width(str(x)),y1+fh,str(x))    #写入文字
            x-=1
             
         
    '''绘制右侧信息栏和盘口等内容'''
    def rightGridPaint(self):
        self.setPen('darkGray')
        #绘制信息内容之间的分割线
        _h = 0
        _x = self.w-self.grid_padding_right+44
        self.paint.drawLine(self.w-1,0,self.w-1,self.h-self.grid_padding_bottom+16)
        self.paint.drawLine(0,0,0,self.h-self.grid_padding_bottom+16)
        self.paint.drawLine(0,_h,self.w,_h)
        _h+=23
        self.paint.drawLine(_x,_h,self.w,_h)
        _h+=24
        self.paint.drawLine(_x,_h,self.w,_h)
 
        _h+=93
        self.paint.drawLine(_x,_h,self.w,_h)
        _h+=20
        self.paint.drawLine(_x,_h,self.w,_h)
        _h+=93
        self.paint.drawLine(_x,_h,self.w,_h)
        _h+=123
        self.paint.drawLine(_x,_h,self.w,_h)
        _h+=23
        self.paint.drawLine(_x,_h,self.w,_h)

        #股票名称和代码
        self.setFont('yahei_14_bold')
        self.setPen('yellow')
        name_str = str('%s %s'%(self.parent.stk_quotes['code'][0],self.parent.stk_quotes['name'][0]))
        self.paint.drawText(_x+35,18,name_str)

        #委比和委差
        self.setFont('yahei_14')
        zx_str = str('最新 %.2f'%float(self.parent.stk_quotes['price'][0]))
        self.paint.drawText(_x+3  ,156,zx_str)
        self.setPen('gray')
        wb_str = str('委比')
        wc_str = str('委差')
        xs_str = str('现手')
        self.paint.drawText(_x+3  ,39,wb_str)
        self.paint.drawText(_x+100,39,wc_str)
        self.paint.drawText(_x+100,156,xs_str)
        fh = self.metrics.height()
         
        left_field_list = ['涨跌','涨幅','振幅','总手','总额','换手','分笔']
        i = 1
        for field in left_field_list:
            field_str = str(field)
            self.paint.drawText(_x+3,253+(i*17),field_str)
            i+=1
 
        mma = round(float(self.parent.stk_quotes['amount'][0])/float((self.parent.stk_quotes['volume'][0])),2)
        right_field_list = ['均价 %.2f'%mma,
                            '昨收 %.2f'%float(self.parent.stk_quotes['pre_close'][0]),
                            '今开 %.2f'%float(self.parent.stk_quotes['open'][0]),
                            '最高 %.2f'%float(self.parent.stk_quotes['high'][0]),
                            '最低 %.2f'%float(self.parent.stk_quotes['low'][0]),
                            '量比 ',
                            '均量 ']
         
        i = 1
        for field in right_field_list:
            field_str = str(field)
            self.paint.drawText(_x+100,253+(i*17),field_str)
            i+=1
 
        wp_str = str('外盘')
        np_str = str('内盘')
        self.paint.drawText(_x+3,395,wp_str)
        self.paint.drawText(_x+100,395,np_str)
        #卖①②③④⑤
         
        i = 0
        sell_queue = ['卖⑤  %.2f   %d' %(float(self.parent.stk_quotes['a5_p'][0]), float(self.parent.stk_quotes['a5_v'][0])),
                      '卖④  %.2f   %d' %(float(self.parent.stk_quotes['a4_p'][0]), float(self.parent.stk_quotes['a4_v'][0])),
                      '卖③  %.2f   %d' %(float(self.parent.stk_quotes['a3_p'][0]), float(self.parent.stk_quotes['a3_v'][0])),
                      '卖②  %.2f   %d' %(float(self.parent.stk_quotes['a3_p'][0]), float(self.parent.stk_quotes['a2_v'][0])),
                      '卖①  %.2f   %d' %(float(self.parent.stk_quotes['a1_p'][0]), float(self.parent.stk_quotes['a1_v'][0]))]
        for sell in sell_queue:
            sell_str = str(sell)
            self.paint.drawText(_x+3,62+(i*18),sell_str)
            i+=1
        #买①②③④⑤
        buy_queue = ['买①  %.2f   %d' %(float(self.parent.stk_quotes['b1_p'][0]), float(self.parent.stk_quotes['b1_v'][0])),
                     '买②  %.2f   %d' %(float(self.parent.stk_quotes['b2_p'][0]), float(self.parent.stk_quotes['b2_v'][0])),
                     '买③  %.2f   %d' %(float(self.parent.stk_quotes['b3_p'][0]), float(self.parent.stk_quotes['b3_v'][0])),
                     '买④  %.2f   %d' %(float(self.parent.stk_quotes['b4_p'][0]), float(self.parent.stk_quotes['b4_v'][0])),
                     '买⑤  %.2f   %d' %(float(self.parent.stk_quotes['b5_p'][0]), float(self.parent.stk_quotes['b5_v'][0]))]
        buys = []
        for buy in buy_queue:
            buy_str = str(buy)
            self.paint.drawText(_x+3,87+(i*18),buy_str)
            i+=1
 
        self.setPen('red_2px')
        self.paint.drawLine(_x+1,377,_x+99,377)
        self.paint.drawLine(_x+1,46,_x+65,46)
        self.setPen('green_2px')
        self.paint.drawLine(_x+102,377,_x+199,377)
        self.paint.drawLine(_x+67,46,_x+199,46)
        self.setFont('default')
         
    '''绘制左右侧的价格刻度'''
    def rulerPaint(self):
         
        sum_width  = self.grid_padding_left+self.grid_padding_right
        sum_height = self.grid_padding_top+self.grid_padding_bottom
 
        grid_height = self.h-sum_height
         
        high = float(self.parent.stk_quotes['high'][0])
        low  = float(self.parent.stk_quotes['low'][0])
        lastclose = float(self.parent.stk_quotes['pre_close'][0])
 
        top = high-lastclose
        bottom = lastclose-low
        if top>bottom:
            padding = top
        else:
            padding = bottom
             
        limit_top = lastclose+padding
        limit_low = lastclose-padding
 
 
        px_h_radio = (grid_height*0.7)/((limit_top-limit_low)*100)
 
        grid_num = 16
        cnt = grid_height*0.7/grid_num
         
        for i in range(0,grid_num):
            self.setPen('darkGray_1px_dashline')
            #计算坐标
            y1 = self.grid_padding_top+i*cnt
            x1 = self.grid_padding_left
            x2 = self.grid_padding_left+self.w-sum_width
             
            self.paint.drawLine(x1,y1,x2,y1) #画价位虚线
             
            price_float = (limit_top - ((i*cnt)/px_h_radio/100)) #计算价格
            price = '%4.2f'%(price_float) #格式化价格成str
             
            fw = self.metrics.width(price) #获得文字宽度
            fh = self.metrics.height()/2   #获得文字高度
 
            radio_float = (price_float/lastclose-1)*100 #计算波动百分比
            radio_str   = "%2.2f%%"%(radio_float)      #格式化百分比成str
 
            r_fw = self.metrics.width(radio_str)
            r_fh = self.metrics.height()/2
            #判断文字使用的颜色
            if price_float == lastclose:
                self.setPen('white')
            if price_float < lastclose:
                self.setPen('green')
                 
            self.paint.drawText(x1-fw-2,y1+fh,price) #写入文字
            self.paint.drawText(x2+40-r_fw,y1+r_fh,radio_str) #写入文字
    '''绘制x,y准星'''
    def xyPaint(self):
        if self.parent.m_x >= self.grid_padding_left and self.parent.m_x<=self.w-self.grid_padding_right and self.parent.m_y>=self.grid_padding_top and self.parent.m_y<=self.h-self.grid_padding_bottom:
            self.setPen('gray')
            x1 = self.grid_padding_left
            x2 = self.w-self.grid_padding_right
            y1 = self.grid_padding_top
            y2 = self.h-self.grid_padding_bottom
            self.paint.drawLine(x1+1,self.parent.m_y,x2-1,self.parent.m_y)
            self.paint.drawLine(self.parent.m_x,y1+1,self.parent.m_x,y2-1)
             
             
     
    '''绘制时间轴刻度'''
    def timelinePaint(self):
         
        fw = self.metrics.width('00:00') #计算文字的宽度
         
        sum_width  = self.grid_padding_left+self.grid_padding_right
        sum_height = self.grid_padding_top+self.grid_padding_bottom
         
        grid_width_a = self.w-sum_width-2
         
         
        y1 = self.grid_padding_top
        y2 = y1+(self.h-sum_height)
        grid_width = grid_width_a * (1-0.05882)
        grid_left = self.grid_padding_left + grid_width_a - grid_width
 
        #时间轴中线
        self.setPen('darkGray')
        x_pos = grid_width/2+grid_left
        self.paint.drawLine(x_pos,y1,x_pos,y2)
        self.paint.drawText(x_pos-fw/2,y2+12,str('13:00'))
         
        #时间轴09点15分
        x_pos = self.grid_padding_left
        self.paint.drawText(x_pos,y2+12,str('09:15'))

        #时间轴09点30分
        x_pos = grid_left
        self.paint.drawLine(x_pos,y1,x_pos,y2)
        self.paint.drawText(x_pos,y2+12,str('09:30'))
         
        #时间轴10点30分
        x_pos = grid_width*0.25+grid_left
        self.paint.drawLine(x_pos,y1,x_pos,y2)
        self.paint.drawText(x_pos-fw/2,y2+12,str('10:30'))
 
        #时间轴14点00分
        x_pos = grid_width*0.75+grid_left
        self.paint.drawLine(x_pos,y1,x_pos,y2)
        self.paint.drawText(x_pos-fw/2,y2+12,str('14:00'))
 
        #时间轴15点00分
        x_pos = grid_width+grid_left
        self.paint.drawText(x_pos-fw,y2+12,str('15:00'))
 
        #时间虚线 by 30min
        self.setPen('darkGray_1px_dashline')
        x_pos_array = [0.125,0.375,0.625,0.875]
        for i in x_pos_array:
            x_pos = grid_width*i+grid_left
            self.paint.drawLine(x_pos,y1,x_pos,y2)

         
    '''绘制表格上方的股票信息'''
    def topInfoPaint(self):
        self.setPen('yellow')
        #股票名称
        #stk_name = str(self.parent.stk_quotes['name'][0])
        stk_name = str('%s %s '%(self.parent.stk_quotes['code'][0],self.parent.stk_quotes['name'][0]));
        fw = self.metrics.width(stk_name) #计算文字的宽度
        self.paint.drawText(4+self.grid_padding_left,self.grid_padding_top-4,stk_name) 

        lastclose   = float(self.parent.stk_quotes['pre_close'][0])
        close       = float(self.parent.stk_quotes['price'][0])
        mma         = round(float(self.parent.stk_quotes['amount'][0])/float((self.parent.stk_quotes['volume'][0])),2)
        
        if lastclose>close:
            str_price = '%.2f -%.2f '%(close,lastclose-close)
        if lastclose==close:
            str_price = '%.2f +%.2f '%(close,0.00)
        if lastclose<close:
            str_price = '%.2f +%.2f '%(close,close-lastclose)

        fw_p = fw+self.metrics.width(str_price) #计算文字的宽度
        
        #均价线
        str_jjx = str('成交均价：')
        fw_jjx = fw_p+self.metrics.width(str_jjx) #计算文字的宽度
        self.paint.drawText(4+self.grid_padding_left+fw_p,self.grid_padding_top-4,str_jjx)      

        if lastclose>close:
            self.setPen('green')
        if lastclose==close:
            self.setPen('white')
        if lastclose<close:
            self.setPen('red')
         
        if mma>close:
            self.setPen('green')
        if mma==close:
            self.setPen('white')
        if mma<close:
            self.setPen('red')

        self.paint.drawText(4+self.grid_padding_left+fw,self.grid_padding_top-4,str(str_price))
        self.paint.drawText(4+self.grid_padding_left+fw_jjx,self.grid_padding_top-4,str('%.2f '%mma)) #均价线
        fw_mma = self.metrics.width(str('%.2f '%mma)) + fw_jjx

        #涨停价
        self.setPen('red')
        str_zt = str('涨停价:%.2f '%(lastclose*1.1))
        fw_zt = fw_mma+self.metrics.width(str_zt) #计算文字的宽度
        self.paint.drawText(4+self.grid_padding_left+fw_mma,self.grid_padding_top-4,str_zt)
        #跌停价
        self.setPen('green')
        self.paint.drawText(4+self.grid_padding_left+fw_zt,self.grid_padding_top-4,str('跌停价:%.2f '%(lastclose*0.9)))

    '''绘制股价走势'''
    def pricePaint(self):
        sum_width  = self.grid_padding_left+self.grid_padding_right
        sum_height = self.grid_padding_top+self.grid_padding_bottom
 
        grid_height = self.h-sum_height-2
         
        high = float(self.parent.stk_quotes['high'][0])
        low  = float(self.parent.stk_quotes['low'][0])
        lastclose = float(self.parent.stk_quotes['pre_close'][0])
        Open = float(self.parent.stk_quotes['open'][0])

        top = high-lastclose
        bottom = lastclose-low
        if top>bottom:
            padding = top
        else:
            padding = bottom
             
        limit_top = lastclose+padding
        limit_low = lastclose-padding
         
        h_radio = (grid_height*0.7)/((limit_top-limit_low)*100)
 
        #w_radio = (self.w-sum_width-2)/240.00
        w_radio = (self.w-sum_width-2)/(14400.00+900)
        w = self.grid_padding_left
         
        self.setPen('white')
        path = QtGui.QPainterPath()
        path.moveTo(w,(limit_top-Open)*100*h_radio+self.grid_padding_top)

        for idx,row in self.parent.stk_ticks.iterrows():
            price = float(row["price"])
            i = self.time2Pos(row["time"])
            w = i*w_radio+self.grid_padding_left
            y = (limit_top-price)*100*h_radio+self.grid_padding_top
            path.lineTo(w,y)
        self.paint.drawPath(path)


        #self.setPen('cyan_1px_dashline')
        #self.paint.drawLine(self.grid_padding_left+1,y,w-1,y)

        self.setPen('yellow')
        path = QtGui.QPainterPath()
        w = self.grid_padding_left
        path.moveTo(w,(limit_top-Open)*100*h_radio+self.grid_padding_top)

        sum_vol = 0
        sum_amt = 0
        for idx,row in self.parent.stk_ticks.iterrows():
            sum_vol = sum_vol + float(row["volume"])
            sum_amt = sum_amt + float(row["amount"])
            if sum_vol and sum_amt :
                price = sum_amt /(sum_vol*100)
            else:
                price = price #float(row["price"])
            i = self.time2Pos(row["time"])
            #print(i)
            w = i*w_radio+self.grid_padding_left
            y = (limit_top-price)*100*h_radio+self.grid_padding_top
            path.lineTo(w,y)
        self.paint.drawPath(path)
         
         
    '''绘制成交量'''
    def volumePaint(self):
        sum_width  = self.grid_padding_left + self.grid_padding_right
        sum_height = self.grid_padding_top  + self.grid_padding_bottom
 
        max_volume = max(self.parent.stk_ticks['volume'])
        
        w_radio = (self.w-sum_width-2)/(14400.00+900)
        h_radio = ((self.h-sum_height-2)*0.3)/max_volume
 
        y = (self.h-sum_height)+self.grid_padding_top
         
        for idx,row in self.parent.stk_ticks.iterrows():
            if '买' in row["type"] :
                self.setPen('red')
            elif '卖' in row["type"] :
                self.setPen('green')
            else:
                self.setPen('yellow')
            vol = float(row["volume"])
            i = self.time2Pos(row["time"])
            x   = i*w_radio+self.grid_padding_left
            y2  = h_radio*vol
            self.paint.drawLine(x,y-1,x,y-y2)


class Test(QtGui.QWidget):
    def __init__(self, parent=None, stk_code=None):
        QtGui.QWidget.__init__(self, parent)
        self.setMinimumSize(640, 430) #设置窗口最小尺寸
        self.setGeometry(300, 300, 960, 650)
        self.setWindowTitle(str('分笔明细图'))
        self.setStyleSheet("QWidget { background-color: black }")
        #self.setWindowIcon(QtGui.QIcon('ruby.png'))
        self.setMouseTracking(True)
        self.m_x = 0 #光标x轴位置
        self.m_y = 0 #光标y轴位置
        self.stk_code = stk_code
        if not stk_code :
            self.stk_code = '002076'
        self.updateData()
        
    def updateData(self):
        self.stk_quotes = ts.get_realtime_quotes(self.stk_code)
        self.stk_ticks  = ts.get_today_ticks(self.stk_code).sort_values(by="time")
        #df = df.sort("time")
        #df = ts.get_realtime_quotes(self.stk_code) 
        self.setWindowTitle(str(self.stk_quotes['date'][0] + ' 分笔明细图'))
        self.repaint()
        #self.updateData()
        
    def mouseMoveEvent(self, event):
        self.m_x =  int(event.x())
        self.m_y =  int(event.y())
        #self.stk_quotes = ts.get_realtime_quotes(self.stk_code)
        self.repaint()
    def paintEvent(self, event):
        report_painter(self)
 
app = QtGui.QApplication(sys.argv)
dt = Test(stk_code='600865')
dt.show()
app.exec_()
