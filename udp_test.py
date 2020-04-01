from matplotlib import pyplot as plt
import numpy as np


# 相加运算
def add(numb_1, numb_2):
    result = numb_1 + numb_2
    max_num = (2 ** 16) - 1
    # 当加法溢出的时候回卷
    while result > max_num:
        result = result - max_num
    return result


# 把十进制的运算结果转换成16位二进制数字，并且去掉'0b'
def result_process(n):
    n1 = bin(n)
    number = n1[2:]
    if len(number) < 16:
        number = '0' + number
    return number


# 把三个数字相加的结果进行反码运算，求出检验和
def create_udp(number):
    if number[0] == '0':
        udp = '1'
    elif number[1] == '1':
        udp = '0'
    else:
        print('发生错误')
    for i in range(1, 16):
        if number[i] == '0':
            udp = udp + '1'
        elif number[i] == '1':
            udp = udp + '0'
        else:
            print('发生错误')
    return udp


def test_udp(udp, result):
    # 把输入的三个数字和检验和相加
    test_result = udp + result
    test_result = result_process(test_result)
    test_list = []
    for num in test_result:
        test_list.append(num)
    x = np.arange(1, 17)
    plt.title('UDP test')
    plt.plot(x, test_list, "ob")
    plt.show()


if __name__ == '__main__':
    # 接收用户输入的三个二进制数字
    num_1 = input('请输入第一个数字')
    num_2 = input('请输入第二个数字')
    num_3 = input('请输入第三个数字')
    # 把输入的二进制数字转换成十进制
    num_1 = int(num_1, 2)
    num_2 = int(num_2, 2)
    num_3 = int(num_3, 2)
    # 计算前两个数相加的结果
    result1 = add(num_1, num_2)
    # 把上边的和与第三个数字相加
    result2 = add(result1, num_3)
    # 将运算结果转换成16位二进制数字并输出
    result = result_process(result2)
    print('三个数字相加的结果为', result)
    # 由运算结果求得检验和
    udp = create_udp(result)
    print('检验和为', udp)
    # 检查该分组中是否出现差错
    int_udp = int(udp, 2)
    test_udp(int_udp, result2)


