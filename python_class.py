# -*- coding:utf-8 -*-

# Python类里self和cls都可以用别的单词代替，类的方法有三种，
#
# 一是通过def定义的，需要至少传递一个参数，一般用self，必须通过一个类的实例去访问；
#
# 二是在def前面加上@classmethod，需要至少传递一个参数，一般用cls，支持类名和对象两种调用方式；
#
# 三是在def前面加上@staticmethod，参数可以为空，支持类名和对象两种调用方式；


class A:
    member = "Hello"

    def __init__(self):
        print "__构造函数__"

    def print1(self):
        print "print 1:", self.member

    def print2(kwarg):
        print "print 2:", kwarg.member

    @classmethod
    def print3(cls):
        print "print 3:", cls.member

    @classmethod
    def print4(kwarg):
        print "print 4:", kwarg.member

    @staticmethod
    def print5():
        print "print 5: Hello"

    @classmethod
    def print6(cls, obj="World"):
        print "print 6:", cls.member, obj

    @classmethod
    def print7(cls, obj):
        print "print 7:", cls.member, obj


a = A()

# A.print1()
a.print1()

# A.print2()
a.print2()

A.print3()
a.print3()

A.print4()
a.print4()

A.print5()
a.print5()

A.print6()
a.print6()

A.print6("World")
a.print6("World")

# A.print7()
# a.print7()

A.print7("World")
a.print7("World")
