a = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']

while True:
    price = input('The price is:')
    if price.isdigit():
        break
    else:
        print('bad number,Please repeat the number again')

price = price.strip(' ').lstrip('0').strip(' ')

length = len(price)
if length == 1:
    print(a[int(price[0])] + '元')

elif length == 2:
    if price[1] == '0':
        print('{}拾元'.format(a[int(price[0])]))
    else:
        print('{}拾{}元'.format(a[int(price[0])], a[int(price[1])]))

elif length == 3:
    if price[1] == '0' and price[2] == "0":
        print('{}佰元'.format(a[int(price[0])]))
    elif price[2] == '0':
        print('{}佰{}拾元'.format(a[int(price[0])], a[int(price[1])]))
    else:
        print('{}佰{}拾{}元'.format(a[int(price[0])], a[int(price[1])], a[int(price[2])]))

else:
    if price[1] == '0' and price[2] == "0" and price[3] == '0':
        print('{}仟元'.format(a[int(price[0])]))
    elif price[2] == '0' and price[3] == "0":
        print('{}仟{}佰元'.format(a[int(price[0])], a[int(price[1])]))
    elif price[3] == '0':
        print('{}仟{}佰{}拾元'.format(a[int(price[0])], a[int(price[1])], a[int(price[2])]))
    elif price[1] == '0' and price[2] == '0':
        print('{}仟零{}元'.format(a[int(price[0])], a[int(price[3])]))
    else:
        print('{}仟{}佰{}拾{}元'.format(a[int(price[0])], a[int(price[1])], a[int(price[2])], a[int(price[3])]))
        
# 实现的思路很好，不过代码有点小问题，测试1011和预期的结果不符，再改改哈
