
# 将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",“1001”转化成为"壹仟零壹元",数字的中文对应：零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖","拾", "佰", "仟", "万"，请试着实验一下。

#################################
# 阿拉伯数字转换成标准的中文货币
#################################

def Transformation():
    Inputnum = input()

    TransFor = {'0': '零', '1': '壹', '2': '贰',
                '3': '叁', '4': '肆', '5': '伍',
                '6': '陆', '7': '柒', '8': '捌',
                '9': '玖', }

    company = ['万', '仟', '佰', '拾', '元']

    # int(Inputnum), 将用户左侧输入的全为0的状况剔除
    StrNum = str(int(Inputnum))

    # 将输入的数字，转换成中文
    lst = []
    for _ in StrNum:
        lst.append(TransFor[_])

    # 通过切片操作,确定 zip函数中 company列表的起点
    company = company[5-len(StrNum):]
    ziplist = zip(lst, company)

    # 将zip函数的结果转换成一个整体
    Trans = "".join(''.join(_) for _ in ziplist)


    # 可读性修改
    for _ in ["零万", "零仟", "零佰", "零拾","零零零零", "零零零", "零零"]:
        if _ in Trans:
            Trans = Trans.replace(_,"零")
            if "零元" in Trans:
                Trans = Trans[:-2]+"元"

    print(Trans)


if __name__ =="__main__":
    Transformation()
    
# 注意下交互模式下的的提醒
