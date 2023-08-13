# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/18 18:02
@Auth ： magician
@Desc ：IO读写与异常处理
"""
def read():
    # r只读 w只写 w+ 读取（更新）模式。若文件不存在，则创建文件，已存在，则重写文件  r+ 文件不存在失败
    f_or = open(r"F:\novels\English\textdemo.txt", 'r',encoding="utf8")  # 以只读的方式打开文件
    print(f_or.read())
    print(f_or.readline())  # 读取一行数据，可配合循环使用
    print(f_or.readlines())  # 读取成功，返回一个列表

def write():
    # 更新（覆写）,w+无法打印出来文件中的数据：
    context = "w+...hei,The computer grade examination is divided into four levels. "  # 字符串数据
    with open(r"F:\novels\English\textdemo.txt", 'w', encoding="utf8") as f:  # 以读写（更新）的方式打开文件
        f.write(context)  # 写数据
        print(f.readlines()) # w+无法打印出来文件中的数据：

    # a 追加模式打开的文件不能读取，且追加的内容是从第一行数据的末尾开始追加
    context = "a...hei,The computer grade examination is divided into four levels. "  # 字符串数据
    with open(r"F:\novels\English\textdemo.txt", 'a', encoding="utf8") as f:  # 以读写（更新）的方式打开文件
        f.write(context)  # 写数据
        print(f.read()) # a+无法打印出来文件中的数据：

# 异常处理
def abnormal():
    try:
        x = float(input('请输入设备成本：'))
        y = int(input('请输入分摊年数：'))
        z = x / y
        print('每年分摊金额为%.2f' % z)
    except ZeroDivisionError:
        print("发生异常，分摊年数不能为0.")
    except:
        print('输入有误')
    else:
        print("没有错误或异常")
    finally:
        print('不管是否有异常发生，始终执行finally部分的语句')




if __name__ == '__main__':
    print()
