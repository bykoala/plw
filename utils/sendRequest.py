from .common import contain_number,contain_english
from .operationFile import *
import requests

def getUrlResponeContent(url):
    data = requests.get(url)
    if data.status_code == 200:
        response_data = data.text
        tmp_data = response_data[response_data.index('kj_tablelist02'):]
        tmp_data = tmp_data[:tmp_data.index('</div>')]
        tmp_data = tmp_data[tmp_data.index('class="ball_orange">'):]
        # tmp_data = tmp_data.replace("<span class=\"ball-list red\"","").replace("</span>","").replace("\n","").replace("\r","").replace(">","").replace(" ","")
        # tmp_date = (filter(str.isdigit,tmp_data))
        # tmp_data = tmp_data.replace('class="ball_orange">','').replace("\n","").replace(" ", "").replace("\t","")
        tmp_data = tmp_data.replace('class="ball_orange">','').replace("li","").replace("\r","").replace("/>","").replace("<","").replace("</","").replace("\t","").replace("\n","").replace("/ul>","").replace(" ","")

        return tmp_data
    elif data.status_code == 404:
        return "continue"
    else:
        print(url)
        return "continue"

def data_from_net(start_num,end_num):
    result = ""
    count = 0
    for i in range(start_num,end_num+1):
        url = ""
        if i<10000:
            url = '0'+ str(i)
        # elif 10000 <= i < 20000:
            # url = "10" + str(i)
        else:
            url = str(i)
        # content = g.getUrlResponeContent("http://kaijiang.500.com/shtml/qxc/" + url + ".shtml")
        print("url:",url)
        content = getUrlResponeContent("http://kaijiang.500.com/shtml/plw/" + url + ".shtml")
        if content == "continue" or (not contain_number(content)):
            continue
        # content = url[2:] + "," + content
        content = url + "," + content
        print("content_url:",content)
        result = result + content + '\n'
        count += 1
    if isinstance(result,str):
        for i in result:
            #如果元素为空，则删除
            if i == '':
                content.remove(i)
    elif isinstance(result,list):
        for i in result:
            #如果元素为空，则删除
            if i == '':
                content.remove(i)
    return result
'''
if __name__ == "__main__":
    print("--------start--------------")
    # url_path = "http://kaijiang.500.com/shtml/plw/04001.shtml"
    # response_content = getUrlResponeContent(url_path) 
    # print(response_content)
    # rs = data_from_net(4000,20145)
    write_csv_from_net("get_result.csv",4000,4010)
    # print(rs)
    print("--------end--------------")
'''