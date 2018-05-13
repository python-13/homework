import re

ChinaNumData = {1: '壹', 2: '贰', 3: '叁', 4: '肆', 5: '伍', 6: '陆', 7: '柒', 8: '捌', 9: '玖', 0: '零'}
Unit = ['元', '拾', '佰', '仟', '万']


def NumTrans(UserInput):
    """docstring"""
    Data = UserInput[::-1]
    Transform = ''
    count = 0
    if len(UserInput) == 1:
        Transform = ChinaNumData[int(UserInput)] + '元整'
    else:
        for i in Data:
            Transform = Transform + Unit[Data.index(i, count)] + ChinaNumData[int(i)]
            count += 1

    Transform = Transform[::-1] + '元整'
    for i in ['零仟', '零佰', '零拾', ]:
        Transform = re.sub(i, '零', Transform)

    Transform = re.sub('零+', '零', Transform)
    Transform = re.sub('零元', '', Transform)
    print(Transform)


def main():
    """docstring"""
    while 1:
        UserInput = input('请输入小于99999的数字')
        while 1:
            if len(UserInput) <= 5:
                NumTrans(UserInput)
                break
            else:
                print('输入的数字超出范围')
                break


if __name__ == '__main__':
    main()
    
 # 老哥很厉害，继续加油，为了目标加油前进
