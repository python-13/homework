import re
dict= {'1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍','6':'陆','7':'柒','8':'捌','9':'玖','0':'零'}
dict1= {'0':'','1':'拾','2':'佰','3':'仟','4':'万'}
def deepDone(word,begin):
    index=word.find('零',begin)
    if(word=='零元'):
        return word
    if(index==-1):
        return word
    else:
        if(word[index+1]=='元'):
            word=word[0:index]+word[index:].replace(word[index], '', 1)
            return word

        if(word[index+2]!='零'):            #壹佰零拾玖元
                                            #壹佰零玖元
            word=word[0:index]+word[index:].replace(word[index+1],'',1)
            word=deepDone(word,index+1)
        else:
            word=word[0:index]+word[index:].replace(word[index:index+2],'',1)
            #壹千壹百零拾零元
            word=deepDone(word,index)
    return word

def numtochn(num):
    word='元'
    str_num=str(num)
    i = 0
    for one in str_num[::-1]:
        num_dict = dict[one]  # 数字大写
       # print(num_dict)
        word_dict = dict1[str(i)]  # 单位大写
       # print(word_dict)
        word = word + word_dict + num_dict
        i += 1
    word = word[::-1]  # 对word做进一步的调整
    word = deepDone(word, 0)  # 对word进下一步处理 ，0 为word 中的位置
    word='人民币'+word+'整'
    return word

def  MyInput():
    num=input("请输入您想转化的数字：\n")
    #pattern=re.compile(r'^(([0-9]+)|([0-9]+\.[0-9]{1,2}))$')
    pattern=re.compile(r'^[1-9]\d*$')
    match=pattern.search(num)
    if match:
        if int(num)<100000:
            print('result: ',num)
            return num
    
    print('重新输入你的数字\n')
    return -1


if __name__=='__main__':
    #num=input("请输入您想转化的数字：\n")
    while True:
        num=MyInput()
        while((num==-1)):
            num=MyInput()
        print('你输入的数字为：',num)
        word=numtochn(num)
        print(word)
        
  # 函数实现的，编程的思路很棒，逻辑也很正确，考虑下代码是否可以优化
