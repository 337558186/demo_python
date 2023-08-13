# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/18 17:57
@Auth ： magician
@Desc ： 函数
"""

def area(width, height):
    return width * height

# 同时存在必传参数和默认参数，形参的顺序必须是 (必传参数 , 默认参数)
def test1(a, b=3):
    print(a, b)

# 可变参数列表
def arithmetic_mean(*args):
    if len(args) == 0:
        return 0
    else:
        sum = 0
        for x in args:
            sum += x
        return sum/len(args)

# 可变参数
def myfun(a, *b, c=None):
    print(a)
    print(b)
    print(c)

# myfun(1, 2, 3, c=4)  可变参数(*)之后的参数必须指定参数名，否则就会被归到可变参数之中



# 关键字参数, 允许你传入0个或任意个含参数名的参数，自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# >>> person('Adam', 45, gender='M', job='Engineer')
# name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}




if __name__ == '__main__':
    # 固定参数
     print(area(5,4))
    # 可变参数
     print(arithmetic_mean(45, 32))
     print(arithmetic_mean(45))

