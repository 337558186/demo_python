# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/16 9:48
@Auth ： magician
@Desc ： 基础知识
"""

# 入门  输入输出
def base():
    a = (str(input()))
    b = (list(input()))  # 创建一个空列表
    c = (tuple(input()))  # 创建一个空元组
    d = (set(input()))  # 创建一个空集合
    e = {}  # 创建一个空字典
    e_ElementName = input("请输入名称:")
    e_ValueContent = input("请输入内容:")
    e[e_ElementName] = e_ValueContent
    print("您输入的字串符:", a)
    print("列表结果:", b)
    print("元组结果:", c)
    print("集合结果:", d)
    print("字典结果:", e)


def base1():
    Love = '窗前明月光，'
    you = '疑是地上霜？'
    print(Love + you)

# 数据类型(数字)
def base2():
    a6, a5, a3, a2, a1 = 4 + 7j, 47.88, 47, 47.8, 47.88888
    a4 = False
    print(type(a1), type(a2), type(a3), type(a4), type(a5), type(a6))

# 运算符
def base3():
    a = 1314
    b = 521
    print(a + b, a - b, a * b, a / b, a % b, a ** b, pow(a, b), a // b, )

# 字符串 String
def base4():
    a = 'Hello', 'LWL'
    b = 'Hello''LWL'
    # 注意字串符a与b的区别，如有逗号，两个字串符一起输出，如没有两个字串符相互结合输出
    c, d = 'Hello', 'LWL'
    print(a)  # ('Hello', 'LWL')
    print(b)
    print(c, d)
    print(c + d)
    print(b[0:-2])
    print(c[0:-3])
    print(d[0:-1])
    print(c * 2, d * 2)  # 各输出两次
    print((c + d) * 2)  # 结合输出两次
    print('Hello,\nLWL')
    print(r'Hello,LWL')  # 加了r后转义字符失效
    e = 'Love LWL 1314'
    print(e[0], e[5])  # 输出指定索引位置的字母
    print(e[0], e[-2], e[3])  # Python与C语言字串符不同的地方在于Python字串符是不可以被改变的，
    # 如果向一个指定索引赋值，那么将会错误

# 列表 List
def base5():
    a = ['a', 'b', 'c', 3]  # 创建两个列表
    b = [4, 7, 'love', 'to', 'lwl', ',', 'never', 'change']
    print(a, b)
    print(a[0:1:3])  # 输出指定列表被切割后的指定数据
    print(a[3])  # 输出指定索引搜索的数据
    a[0:3] = 'A', 'B', 'C'  # 修改列表中指定数据，即可以直接修改
    print(a)
    b.append(347)  # append()函数用于在制定列表末尾添加新数值
    print(b)
    a[1] = []  # 移除a列表中指定索引数据
    print(a)
    print('a列表数据个数:', len(a), 'b列表数据个数:', len(b))  # len()函数用于统计列表数据个数
    c = [0, 1]  # 生成一个嵌入式列表
    d = [2, 3]
    e = [c, d]
    print(e)

    # 遍历
    for index in range(len(lis)):
        print("index =", index, "value =", lis[index])
    for index, value in enumerate(lis):
        print("index =", index, "value =", value)



# 元组 Tuple:元组的语法与列表差不多，不同之处就是元组使用小括号（），且括号中元素不能被改变
def base6():
    a = ('C/c++', 'Python', 2)  # 创建两个元组
    b = "菜鸟", "Love", "never change"
    print(a, b)

    a = ['C/C++', 'Python', 2, 4]  # 创建列表
    b = ["菜鸟", "Love", "never change"]
    c = a + b  # 相互结合
    c = tuple(c)  # 强制转换为元组
    print(len(c))  # 输出列表内数据个数
    d = ('3', '4', '7')
    print(max(d))  # 输出d元组内最大数值
    print(min(d))  # 输出d元组内最小数值，max()是判断最大值函数，min()反之

#Set（集合）是一种无序不重复元素的序列
def base7():
    a = {'a', 'b', 'c', 'd', 'a'}  # 创建集合a
    print(a)  # 因为集合是无序不重复元素序列，所以不会输出多出的a
    b = set('sdgsdggfdgdasrfdsf')  # 运用Set()函数创建集合b
    print(b)



#字典:dictionary
def base8():
    a = {'a': 'Python', 'b': '347', 'c': 'love'}  # 创建一个字典
    b = {'a': 'Javascript', 'b': 'Rust'}
    print(b)
    print(a['a'], a['c'])

    a = {'a': 'Python', 'b': '347', 'c': 'love'}  # 创建一个字典
    print(a)
    a.clear()  # 清除字典所有数据
    print(a)
    a.update({"name": "apple"}) # 追加或更新

    del a  # 删除字典
    print(a)

    # 遍历所有的key
    scores_dict = {'语文': 105, '数学': 140, '英语': 120}
    for key in scores_dict:
        print(key)
    # 遍历所有的value
    scores_dict = {'语文': 105, '数学': 140, '英语': 120}
    for value in scores_dict.values():
        print(value)
    # 遍历 键值对
    dict_1 = {"我": 5, "爱": 2, "你": 1, "祖": 13, "国": 14}
    for k, v in dict_1.items():
        print("字典中的键值对为:(%s:%s)" % (k, v))


if __name__ == '__main__':
    base()

