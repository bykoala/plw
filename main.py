from utils.operationFile import *
from utils.sendRequest import *
from utils.common import *
from data.analysisData import *

if __name__ == "__main__":
    qijianshu=147
    rfilename = "data/get_result.csv"
    print("------start----------")
    write_csv_from_net(rfilename,4000,20147)
    print("------end----------")

    ####################################
    #1.先获取本地最新期数，然后判断是否继续向服务器请求新的数据
    #2.如果有新的数据，则在第一行插入新数据
    # mycsv.write_csv_from_net(wfilename,4100,19090)

    #获取本地现有的第一行数据
    # result = getLatest(rfilename)

    ###############################################
    #################批量tw回核####################
    ###############################################
    #最近N期的tw数
    bt_result = twFromData(reader_csv_base_tw(rfilename), qijianshu)
    # print(bt_result)
    cmd_loop(bt_result,qijianshu)
    #对最近N期tw数进行统计次数，并排序
    # print(tw_sort(tw_count(bt_result)))
    #通过tw，查询最近开的期数
    # for tw_num in  bt_result:
    #     print(getNumFromTw(tw_num))
    # print(getNumFromTw(bt_result,"26",1))

    #最大漏开
    # bt_result = reader_csv_base_tw(rfilename)
    # print(max_omission('82',bt_result))

    #最大连开
    # print(max_output('26',bt_result))

    #从本地文件中读取期数及其对应tw数
    # print(len(reader_csv_base(rfilename,0,20)))

    # read_from_csv_data_all(rfilename)
    # reader_csv_base_tw(rfilename)

    ############################################
    ############################################
    #从服务器获取新数据，并在本地数据集前面追加新数据
    # write_csv_from_net(rfilename, 0, 19102)

    '''
    #############################
    #######开奖数据回核###########
    #############################
    bt_result = ad.twFromData(operator_data.reader_csv_base_tw(rfilename))
    tw_num = '03'
    # print(tw_num)
    #通过tw，查询最近开的期数
    print(ad.getNumFromTw(tw_num,0))
    # 对最近N期tw数进行统计次数，并排序
    print(ad.tw_sort(operator_data.tw_count(bt_result)))
    #最大漏开
    print(ad.max_omission(tw_num,bt_result))

    #最大连开
    print(ad.max_output(tw_num,bt_result))

    #指定tw，查看指定期间数据中，tw总共出现的次数
    print(ad.twCountFromData(tw_num,bt_result))

    ##通过指定多少期(如100期)内，tw统计所指定出现的次数
    print(ad.twFromSetCount(tw_num,bt_result,qijianshu))
    '''