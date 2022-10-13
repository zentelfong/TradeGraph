import sys;
import pandas as pd;
import tg;
import json;
from  mytt import *;

kBuy  = 1;
kSell = 2;
INS_LIST = [];

# 保存指令
def SaveIns(S,INS):
    for i in range(len(S)):
        if(S[i]):
            INS_LIST[i] = INS;

def BUY(S):
    SaveIns(S,kBuy);

def SELL(S):
    SaveIns(S,kSell);

# 过滤
def AUTOFILTER():
    state = kSell;
    for i in range(len(INS_LIST)):
        if INS_LIST[i] != state and INS_LIST[i] != 0:
            state = INS_LIST[i];
        else:
            INS_LIST[i] = 0;



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


while True:
    input1 = input("请输入内容：").strip()

    if input1 == 'q':
        sys.exit();
    elif input1 == 'i':
        tg.INIT(open=OPEN,high=HIGH,low=LOW,close=CLOSE,vol=VOL,date=DATE,title="股票");
    elif input1 == '5':
        tg.PLOT(MA5.tolist(),name="MA5");
    elif input1 == '0':
        tg.PLOT(MA10.tolist(),name="MA10",color=0xfff0861e);
    elif input1 == 'm':
        tg.PLOT(dea.tolist(),name="DEA",color=0xff0da5da,view="MACD_VIEW");
        tg.PLOT(dif.tolist(),name="DIF",color=0xffcc731c,view="MACD_VIEW");
        tg.BAR(macd.tolist(),name="MACD",top_color=0xff6f7680,bottom_color=0xff12783c, view="MACD_VIEW");    
    elif input1 == 'b':
        upper,mid,lower = BOLL(CLOSE);
        tg.PLOT(upper.tolist(),name="UPPER",color=0xFFFFC90E);
        tg.PLOT(mid.tolist(),name="MID",color=0xFFFFAEC9);
        tg.PLOT(lower.tolist(),name="LOWER",color=0xFF0CAEE6);
    elif input1 == 'f':
        tg.MARK(macd>0,CLOSE);

    else:
        tg.SEND(input1.encode('utf-8'));






