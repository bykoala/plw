

import re
import os

#是否含有英文字符，有则True，无则False
def contain_english(content):
    #如果是list，则执行下面逻辑
    if isinstance(content,list):
        for i in content:
            #如果元素为空，则删除
            if i == '':
                content.remove(i)
            i = listToString(i)
            #如果元素为英文字符，则删除
            if bool(re.search('[a-zA-Z]', i)):
                content.remove(i)
        #如果最终剩余的元素为0，则表示content全部为英文字母，返回True，否则返回False
        if len(content) < 1:
            return True
        else:
            return False
    #如果为字符串，则执行下面逻辑
    elif isinstance(content,str):
        return bool(re.search('[a-zA-Z]', content))

def contain_number(content):
    #如果是list，则执行下面逻辑
    if isinstance(content,list):
        for i in content:
            #如果元素为空，则删除
            if i == '':
                content.remove(i)
            i = listToString(i)
            #如果元素为阿拉伯数字，则删除
            # if bool(re.search('[0-9]{7}', i)):
            if bool(re.search('[0-9]{5,7}', i)):
                content.remove(i)
        #如果最终剩余的元素为0，则表示content全部为英文字母，返回True，否则返回False
        if len(content) < 1:
            return True
        else:
            return False
    #如果为字符串，则执行下面逻辑
    elif isinstance(content,str):
        return  bool(re.search('[0-9]{5,7}',content))

#形如{'00',0}
def init_dict():
    tw_dict={}
    for i in range(0,10):
        for k in range(0,10):
            tw_dict[str(i)+str(k)]=0
    return tw_dict

#data_list格式形如：['19089', '53']
def tw_count(data_list):
    tw_dict = init_dict()
    for tw in data_list:
        # print(tw)
        if tw_dict[tw[1]] > 0:
            tw_dict[tw[1]] += 1
        else:
            tw_dict[tw[1]] = 1
    return tw_dict



# print(not contain_number('1234567'))
#通过\n为分隔符，对字符串进行分割并重新倒序组装
def enterKeySplit(strs_content):
    strs = str(strs_content).split('\n')
    strs.reverse()
    for i in range(len(strs)):
        if strs[i] == '':
            continue
        elif i != len(strs) -1 :
            strs[i] = strs[i] + '\n'
        else:
            strs[i] = strs[i]

    return strs


def IsNotExistFile(fileName):
    return os.access(fileName, os.F_OK)

#切片转字符串
def listToString(str_content):
    result_data = "".join(str_content).replace('\t','')
    return result_data