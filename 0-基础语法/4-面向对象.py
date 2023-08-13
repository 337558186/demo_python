# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/18 18:02
@Auth ： magician
@Desc ： 面向对象
实例方法：只有实例化对象之后才可以使用的方法，该方法的第一个形参接收的一定是对象本身！
"""

class people:
    name = ''
    age = 0
    #定义私有属性,子类无法访问父类的私有变量、方法，私有变量;只有本类的内部能直接调用，如果非要调用，可以间接通过._类名__私有变量 来调用私有变量
    __weight = 0

    #实例方法:最少也要包含一个 self 参数，用于绑定调用此方法的实例对象,实例方法通常会用类 对象直接调用
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))


    # 类方法：类名直接调用
    @classmethod
    def info(cls):
        cls.name
        print("正在调用类方法", cls.name)

    # 静态方法，可以使用类名，也可以使用类对象
    @staticmethod
    def info(add):
        print(add)


#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,name,topic):
        self.name = name
        self.topic = topic
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

#单继承示例
class student(people):
    grade = ''
    def __init__(self,name,age,weight,grade):
        #调用父类的构函
        people.__init__(self,name,age,weight)
        self.grade = grade
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

#多重继承
class sample(speaker,student):
    a =''
    def __init__(self,name,age,weight,grade,topic):
        student.__init__(self,name,age,weight,grade)
        speaker.__init__(self,name,topic)

# 单继承实例
s = student('ken',10,60,3)
#  实例方法通常会用类对象直接调用
s.speak()


# 多继承实例
test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法

# 类方法推荐使用类名直接调用，当然也可以使用实例对象来调用（不推荐）
people.info()