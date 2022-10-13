import zmq;
import json;


context = zmq.Context();
socket = context.socket(zmq.PUSH);
socket.connect("tcp://127.0.0.1:3346");

#初始化视图
def INIT(open,high,low,close,vol,date,title=None):
    params = {
        "method":"td.init",
        "params":{
            "title":title,
            "open":open.tolist(),
            "high":high.tolist(),
            "low":low.tolist(),
            "close":close.tolist(),
            "volume":vol.tolist(),
            "date":date.tolist(),
        }
    }
    socket.send(json.dumps(params).encode('utf-8'))

#画线
def PLOT(values,view = "TD_MAIN_VIEW",name = "LINE",color=0xffe66fda,style=None):
    params = {
        "method":"td.plot",
        "params":{
            "name":name,
            "view":view,
            "values":values,
            "color":color,
            "style":style,
        }
    }
    socket.send(json.dumps(params).encode('utf-8'))

#条形图
def BAR(values,view = "TD_MAIN_VIEW",name = "LINE",
    color=None,top_color=None,bottom_color=None,style=None,width=None):
    params = {
        "method":"td.bar",
        "params":{
            "name":name,
            "view":view,
            "values":values,
            "color":color,
            "top_color":top_color,
            "bottom_color":bottom_color,
            "style":style,
            "width":width,
        }
    }
    socket.send(json.dumps(params).encode('utf-8'))

# 添加标记
def MARK(cond,values,view = "TD_MAIN_VIEW",name = "MARK",style=None,font_family=None,icon=58795,color=0xffffffff):
    icons = [];
    for i in range(len(cond)):
        if(cond[i]):
            icons.append({
                "x":i,
                "y":values[i],
                "color":color,
                "icon":icon
            });

    params = {
        "method":"td.mark",
        "params":{
            "name":name,
            "view":view,
            "style":style,
            "font_family":font_family,
            "icons":icons,
        }
    }
    socket.send(json.dumps(params).encode('utf-8'))



def SEND(str):
    socket.send(str.encode('utf-8'))
