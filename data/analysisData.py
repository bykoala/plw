import operator
# from ...plw.utils.common import *
import sys,os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')
from utils.common import *
from utils.operationFile import *

def tw_sort(tw_dict):
    title = "头尾排序"
    sortResult = sorted(tw_dict.items(),key=operator.itemgetter(1),reverse=True)
    print("sortResult:",sortResult)
    analysisResultToTxt(title+"\n"+ "".join(['%s'%x[1] for x in sortResult]))
    return sortResult
################################################
################最大连开#########################
################################################
def max_output(tw,str_content=[]):
    title = "最大连开"
    # print("最大连开")
    print(title)
    count = 0
    tw_result = []
    # str_content = reader_csv_base_tw(rfilename)
    if len(str_content) <= 0:
        return
    result_num = ''
    out_count_previous = 0
    out_count_previous_num = 0
    count_num_flag = 0
    for datarow in str_content:
        result_data_num = datarow[0]
        result_data = datarow[1]
        #匹配
        if tw == result_data:
            count += 1
            if count == 1:
                out_count_ttmp = result_data_num
            if count > out_count_previous:
                count_num_flag += 1
                out_count_previous = count
            #最大连开第一次开奖的期数
            if count_num_flag == 1:
                result_num = out_count_ttmp
        else:
            #不匹配，则把刚刚匹配的最大次数保存下来
            if(count >= out_count_previous):
                out_count_previous = count
            count = 0
            count_num_flag = 0
    if len(result_num) == 0:
        analysisResultToTxt(title+"\n"+ '该tw在指定期间内，尚未开出')
        return  '该tw在指定期间内，尚未开出'
    analysisResultToTxt(title+"\n"+str(result_num)+","+str(out_count_previous))
    return result_num,out_count_previous
    #     result = result_data_num + result_data
    #     tw_result.append(result)

#获取当前本地数据最新期数数
def getLatest(fileName):
    result_data = []
    data = read_from_csv_data_all(fileName)
    count = 1
    for datarow in data:
        if count > 1:
            break
        result_data.append(listToString(datarow)[:-7])
        count+=1
    return round(float(result_data[0]))

#取tw数,end为距今的期数，如：10，则表示最近的10期tw
def twFromData(str_content,end=0):
    count = 1
    tw_result = []
    for datarow in str_content:
        if count > end and end > 0:
            break
        # result_data = datarow[5] + datarow[8]
        result_data = datarow[:]
        tw_result.append(result_data)
        count+=1
    return tw_result

#通过tw统计所指定数据中出现的次数
def twCountFromData(tw,str_content,end=0):
    title = "tw总共出现的次数"
    # print("tw总共出现的次数")
    print(title)
    count = 0
    for datarow in str_content:
        if count > end and end > 0:
            break
        if(datarow[1] == tw):
            count+=1
    analysisResultToTxt(title+"\n"+str(tw)+","+str(count))
    return tw,count

#通过指定多少期(如100期)内，tw统计所指定出现的次数
def twFromSetCount(tw,str_content,end=0):
    title = "tw在该期间出现的次数"
    # print("tw在该期间出现的次数")
    print(title)
    count_result = 0
    count = 0
    for datarow in str_content:
        if count_result > end-1 and end > 0:
            break
        if(datarow[1] == tw):
            count+=1
        count_result += 1
    analysisResultToTxt(title+"\n"+str(tw)+","+str(count))
    return tw,count

###############################
#最大漏开
def max_omission(tw,str_content=[]):
    title = "最大漏开"
    # print("最大漏开")
    print(title)
    count = 0
    tw_result = []
    # str_content = reader_csv_base_tw(rfilename)
    if len(str_content) <= 0:
        return
    tmp_num = ''
    tmp_count = 0
    for datarow in str_content:
        result_data_num = datarow[0]
        result_data = datarow[1]

        #匹配
        if tw == result_data:
            if count > tmp_count:
                tmp_count = count
                count = 0
            tmp_num = result_data_num
            # tmp_count = count
        else:
            count+=1
    if len(tmp_num) == 0:
        return  '该tw在指定期间内，尚未开出'
    analysisResultToTxt(title+"\n"+str(tmp_num)+","+str(tmp_count))
    return tmp_num,tmp_count
#############################

#当期期数开tw，则为0;skip参数为匹配次数,加入传1，则表示匹配一次后，继续往后匹配
def getNumFromTw(str_content,tw="00",skip=0):
    title = "最近开的期数"
    # print("最近开的期数")
    print(title)
    count = 0
    tw_result = []
    # str_content = read_from_csv_data_all(rfilename)
    if len(str_content) <= 0:
        analysisResultToTxt(title+"\n"+ "无原始数据")
        return "无原始数据"
    elif len(str_content) == 1:
        analysisResultToTxt(title+"\n"+ "数据异常")
        return "数据异常"
    for datarow in str_content:
        result_data_num = datarow[0]
        #如果调用的是reader_csv_base_tw，返回数据结果如：['19089', '53']
        if(len(datarow[1]) == 2):
            result_data = datarow[1]
        #如果调用的是reader_csv_base_all，返回数据结果如：['19089', '1234567']
        else:
            result_data = datarow[1][0:4:3]
        if tw == result_data :
            if skip == 0:
                analysisResultToTxt(title+"\n"+str(result_data_num)+","+str(count))
                return result_data_num,count
            elif skip > 0:
                count+=1
                skip -= 1
                continue
        count+=1
    # print("tw_result:",tw_result)
    analysisResultToTxt(title+"\n"+str(tw_result))
    return tw_result

###############################
###############################
def cmd_loop(bt_result,qijianshu=100):

    # 对最近N期tw数进行统计次数，并排序
    print(tw_sort(tw_count(bt_result)))
    # bt_result = tw_sort(tw_count(bt_result))
    for tw_num in  bt_result:
        title = "----------------------------------------------"
        print(title)
        tw_num = tw_num[1]
        print("tw:",tw_num)
        analysisResultToTxt(title+"\n"+str(tw_num))
        #最大漏开
        print(max_omission(tw_num,bt_result))
        #最大连开
        print(max_output(tw_num,bt_result))
        #通过tw，查询最近开的期数
        print(getNumFromTw(bt_result,tw_num,1))
        #对最近N期tw数进行统计次数，并排序
        # print("最近N期次数统计:\n",tw_sort(tw_count(bt_result)))
        #通过指定多少期(如100期)内，tw统计所指定出现的次数
        print(twFromSetCount(tw_num,bt_result,qijianshu))
        #指定tw，查看指定期间数据中，tw总共出现的次数
        print("数据量tw出现的次数:\n",twCountFromData(tw_num,bt_result))
