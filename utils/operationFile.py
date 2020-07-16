import csv
import sys
from .common import *
from .sendRequest import *

#获取当前本地数据，返回data，数据结果形如：['19089', '1234567']
def read_from_csv_data_all(fileName):
    data = []
    result_data = []
    try:
        with open(fileName) as f:
            reader = csv.reader(f)
            # header = next(reader)
            data = [row for row in reader]
    except csv.Error as e:
        print('Error reading CSV file at line %s:%s',reader.line_num,e)
        sys.exit(-1)
    return data

#读取csv文件,返回数据结果如：['19089', '53'],start_num表示距今多少期，end_num表示结束期数距今多少期
def reader_csv_base_tw(filename,start_num=0,end_num=0):
    result_data = []
    data = read_from_csv_data_all(filename)
    # data = read_from_csv(filename)

    count = 0
    for datarow in data:
        if start_num > count:
            count += 1
            continue
        elif end_num < count and end_num != 0:
            break
        result_data_num = str.split(datarow[0],' ')
        result_data_value = str.split(datarow[1][0:4:3],' ')
        result_data.append(result_data_num+result_data_value)
        count += 1
    return result_data

#将字符串写入csv文件
def write_to_csv(filename,content):
    print("write_to_csv:",content)
    if len(content)==0 or contain_english(content):
        return
    try:
        with open(filename,'r+') as f:
            old = f.read()
            f.seek(0)
            f.write(listToString(content) + '\n')
            f.write(old)
    except csv.Error as e:
        print('Error Write CSV %s',e)
        sys.exit(-1)

#形如
def write_csv_from_net(wfilename,start_num,end_num):
    #1.先判断wfilename文件是否存在，若不存在，则新建
    file_status = IsNotExistFile(wfilename)
    #file_status为true，表示文件已存在，则需获取本地文件里面的数据
    if file_status:
        latest_num = getLatest(wfilename)
        #end_num比latest_num大，表示有服务器有新的数据
        if end_num > latest_num and latest_num > 0:
            start_num = latest_num + 1
        else:
            print("服务器无新数据")
            return
    content = data_from_net(start_num, end_num)
    content = enterKeySplit(content)
    write_to_csv(wfilename,content)

#获取当前本地数据最新期数数
def getLatest(fileName):
    result_data = []
    data = read_from_csv_data_all(fileName)
    if len(data) < 1:
        return 4000
    count = 1
    for datarow in data:
        if count > 1:
            break
        # result_data.append(listToString(datarow)[:-7])
        result_data.append(listToString(datarow)[:-5])
        count+=1
    return round(float(result_data[0]))

#分析结果写入txt文件
def analysisResultToTxt(result,filePath='./data/analysis_rest.txt'):
    print("开始写入.......")
    print("result:%s",result)
    try:
        with open(filePath,'a') as f:
            f.writelines(result + "\n")
    except IOError as e:
        print("error write txt %s",e)
        sys.exit(-1)
    print("写入.......end!")


