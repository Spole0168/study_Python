#!/usr/bin/python
#coding=UTF-8
a = 21
b = 10
c = 0

print "a+b =",a + b ;
print "a-b =", a-b;
print "a*b=",a*b;
print "a/b=",a/b;

print "a**b=",a**b;
print "a%b=",a%b;
print "a//b=",a//b;

if (a == b):
    print "1 - a 等于 b"
else:
    print "1 - a 不等于 b"

if (a != b):
    print "2 - a 不等于 b"
else:
    print "2 - a 等于 b"

if (a <> b):
    print "3 - a 不等于 b"
else:
    print "3 - a 等于 b"

if (a < b):
    print "4 - a 小于 b"
else:
    print "4 - a 大于等于 b"

if (a > b):
    print "5 - a 大于 b"
else:
    print "5 - a 小于等于 b"

# 修改变量 a 和 b 的值
a = 5
b = 20
if (a <= b):
    print "6 - a 小于等于 b"
else:
    print "6 - a 大于  b"

if (b >= a):
    print "7 - b 大于等于 a"
else:
    print "7 - b 小于 a"
a = 21
b = 10
c = a + b
print "1 - c 的值为：", c

c += a
print "2 - c 的值为：", c

c *= a
print "3 - c 的值为：", c

c /= a
print "4 - c 的值为：", c

c = 2
c %= a
print "5 - c 的值为：", c

c **= a
print "6 - c 的值为：", c

c //= a
print "7 - c 的值为：", c

a = 10
b = 20
print a>b and b;
print a<b and a-b;
print 2 and a+b;
print 40 or b;
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
if(a in list):
    print  "a in list ";
else:
    print  "a not in list";
a = 20
b = 20

if(a is b):
    print "a is b";
else:
    print "a is not b";
if(a == b ):
    print "a==b";
