import re                                                   #加载正则模块
x_list = ['元','拾','佰','仟']
y_list = []
numin = input('plz enter num:')
transin = '0123456789'                                       #制作转换表格
transout = '零壹贰叁肆伍陆柒捌玖'
transtab = numin.maketrans(transin,transout)
numout = numin.translate(transtab)
if len(numin)<=4:
    for z in range(len(numout)):                             #利用列表增加单位
        y_list.append(numout[z])
        y_list.append(x_list[len(numout)-z-1])
    money=''.join(y_list)                                    #列表转换字符串
    for i in ("零千", "零佰", "零拾"):                       #正则表达式替换特殊情况
        money = re.sub(i, "零", money)
    money = re.sub("零+", "零", money)
    if '零元' in money:
        money = re.sub('零元', "元", money)
    print(money)
else:
    print('num too long!')