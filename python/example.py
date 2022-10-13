import pandas as pd;
import tg;
import json;
from  mytt import *;


def load_json(path):   
    lines = []     #  第一步：定义一个列表， 打开文件
    with open(path) as f:  
        for row in f.readlines(): # 第二步：读取文件内容 
            if row.strip().startswith("//"):   # 第三步：对每一行进行过滤 
                continue
            lines.append(row)                   # 第四步：将过滤后的行添加到列表中.
    return json.loads("\n".join(lines))       #将列表中的每个字符串用某一个符号拼接为一整个字符串，用json.loads()函数加载，这样就大功告成啦！！



days = load_json("trade.json");

df = pd.DataFrame(days,columns=["open","high","low","close","volume","date"])


OPEN = df.iloc[:,0].values;
HIGH = df.iloc[:,1].values;
LOW  = df.iloc[:,2].values;
CLOSE = df.iloc[:,3].values;
VOL = df.iloc[:,4].values;
DATE = df.iloc[:,5].values;

MA5=MA(CLOSE,5)
MA10=MA(CLOSE,10)

dif,dea,macd = MACD(CLOSE)

#初始化
tg.INIT(open=OPEN,high=HIGH,low=LOW,close=CLOSE,vol=VOL,date=DATE,title="股票");

tg.PLOT(MA10.tolist(),name="MA10",color=0xfff0861e);
tg.PLOT(dea.tolist(),name="DEA",color=0xff0da5da,view="MACD_VIEW");
tg.PLOT(dif.tolist(),name="DIF",color=0xffcc731c,view="MACD_VIEW");
tg.BAR(macd.tolist(),name="MACD",top_color=0xff6f7680,bottom_color=0xff12783c, view="MACD_VIEW");    




