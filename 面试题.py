'''
# print调用python中底层的什么方法？
答：sys.stdout.write方法，往控制台打印字符串

位与字节的关系？
位（bit）是计算机数据存储的最小单位，二进制0或1就是一位，
即1字节=8位

# b、B、kB、MB、GB的关系？
1 b = 8 B   bit这是最小的数据单位，表示一个二进制位。
1 B = 8 b   Byte这是基本的数据存储单位，通常用来表示文件大小。
1 KB = 1024 B   表示千字节。1MB（兆字节）等于1024kB，
1 MB = 1024 KB  表示兆字节。1GB（吉字节）等于1024MB，
1 GB = 1024 MB  表示吉字节。1TB（太字节）等于1024GB

# ascii、unicode 、utf-8、gbk 区别？
ASCII主要用于英文文本，简单易用；
Unicode是一个全球性的标准，支持所有语言的字符；
UTF-8是Unicode的一种实现方式，可变长编码，兼容ASCII，广泛应用于互联网；
GBK专门用于中文字符编码，兼容GB2312，但在全球字符集支持方面不如UTF-8。

# 字节码和机器码的区别？
字节码是一种中间状态的二进制代码，需要转译后才能成为机器码；而机器码是计算机硬件可直接识别和执行的低级编码语言。字节码具有跨平台性，而机器码则依赖于具体的硬件架构。

# 三元运算编写格式？
条件表达式 ? 表达式1 : 表达式2

# python2和python3区别？
字符串处理：
Python 2默认使用ASCII编码，而Python 3默认使用Unicode编码。
在Python 2中，字符串和字节串是相同的类型，而在Python 3中，字符串和字节串是不同的类型，需要使用b前缀来表示字节串。
print语句：
Python 2中的print是一个语句，不需要括号；而在Python 3中，print变成了一个函数，必须用括号括起
整数除法：
在Python 2中，整数除法的结果仍然是整数（例如：3 / 2 == 1），而在Python 3中，整数除法的结果是浮点数（例如：3 / 2 == 1.5）

# python2和python3中的int和long的区别？
在Python 2中，int和long分别代表不同精度的整数类型，而Python 3则将这两种类型合并为单一的int类型，使其具有任意精度并简化了代码编写和内存管理。

# python中 xrange和range的区别？
返回类型： range函数返回一个列表对象，xrange函数返回一个生成器对象，
如果你需要处理较小的数据集且希望代码简洁明了，可以使用range()；如果需要处理大量数据并关注内存使用效率，则应选择xrange()。在Python 3.x中，推荐统一使用range()，因为它的行为已经与Python 2.x中的xrange()

# python 中字符串反转？
```py
name = 'wupeiqi'
reversed = name[::-1]
print(reversed)

s= "abcdef"
b = list(s)
b.reverse()
reversed_s = ''.join(b)
print(reversed_s)
```
# python中xreadlines和readlines的区别？
返回类型：
readlines()方法返回一个包含所有行的列表。这意味着它会一次性将整个文件内容读入内存，并解析成一个字符串列表。
xreadlines()方法返回一个生成器对象，逐行读取文件内容。这使得它在处理大文件时更加高效，因为不需要一次性将整个文件加载到内存中
使用场景：
当需要逐行读取文件且文件较大时，推荐使用xreadlines()或其替代方案（如文件对象的迭代器）以节省内存
。
对于小文件或者对内存要求不高的情况，可以使用readlines()方法，因为它操作简单且直接

# python中 列举布尔值为False的常见值
None
False
0
""
[]
()
{}

# python中 字符串、列表、元组、字典常用的方法
string:
    len(s)  ： 获取字符长度
    s[0]  ： 访问索引字符
    s[0] = '新字符' ： 无法修改

    string.find(s,beg=0,end=None) 查找字串的位置
    string.count(s)  返回s字符串的出现的次数
    string.replace("s",'d') s替换成d

    "xxx %s xxx" % (value1,value2)
    "xxx {age} xxx".format(age=18)
    f'xxx{name}xxx'

    'string' + "string2"
    '+'.join(['a','b','c'])
    .split    分割字符串

    string.lower()
    string.upper()
    string.center
list:
    [1,2,3]
    list[0]
    list.append(obj)
    list.insert(i,obj)
    list.extend(iterable)
    list.remove(obj)
    list.pop() 弹出最后一个元素
    list.clear()
    list.sort() 原地排序
    list.reverse() 反转
    list.index(obj) 返回匹配到的元素索引
    list.count(obj) 统计obj出现的次数
tuple：
    (1,2,3)
    tuple[0]
    tuple.count(value)
    tuple.index(value) 返回第一个匹配值的索引
    tuple[start:end] 切片
    (1,2,3) + (4.5.6) 连接元组
dict:
    {key:value,key:value,..}
    dict['key']  访问
    dict.get(key,default) 根据键获取值,没有则返回默认值
    dict.update(key,value)
    dict.pop(key) 移除
    dict.clear()  清空
# python中is和== 区别?
== 对比的是两个对象的值是否相等.
is 操作符比较的是两个对象的内存地址是不是同一个位置.

# python深拷贝和浅拷贝的区别?
深拷贝: 新拷贝了一份对象与原对象是不同内存地址，修改对象中的任何值，都不会改变原对象的值。
浅拷贝: 新拷贝的对象仍然指向原对象的内存地址,修改值发生变化会影响原对象的值.
浅拷贝（影子克隆）：只复制对象的基本类型，对象类型，仍属于原来的引用
深拷贝（深度克隆）：不仅复制对象的基本类，同时也复制原对象的对象，完全是新对象产生的
copy.copy 浅拷贝
copy.deepcopy   深拷贝

# python的垃圾回收机制?
Python的垃圾回收机制主要包括引用计数、标记-清除和分代回收三种策略高效地管理内存，避免内存泄漏和循环引用问题，从而保证程序的稳定性和高效性

# python的可变类型和不可变类型的区别?
可变类型: list dict set
不可变类型: int float str tuple
可变类型允许在不改变内存地址的情况下修改其内容,
不可变类型需要新创建对象来实现修改,每次修改内存地址发生变化.

# 求结果
v = dict.fromkeys(["k1","k2"],[])  # 返回字典,参数1:key列表,参数2:默认值
print(v)  # {'k1': [], 'k2': []}
v['k1'].append(666)
print(v)  # {'k1': [666], 'k2': [666]}
v['k1'] = 777
print(v)   # {'k1': 777, 'k2': [666]}

# python 一行代码删除列表中重复的值?
mylist=[1,2,3,4,5,6,3,5,6]
print(list(set(mylist)))

# python实现'1,2,3'变成['1','2','3']
print('1,2,3'.split(","))  //['1', '2', '3']

# ['1', '2', '3'] 变成 [1, 2, 3]
list1 = ['1', '2', '3']
n = len(list1)
for i in range(n):
    list1[i] = int(list1[i])
print(list1)  //[1, 2, 3]

# 比较 a=[1,2,3]和b=[(1),(2),(3)] 以及c=[(1,),(2,),(3,)]的区别?
a = [1,2,3]
b = [(1),(2),(3) ]
c = [(1,),(2,),(3,) ]
print(f'他们分别都是列表：{a},{b},{c}')
print(f'他们的类型都是：{type(a)},{type(b)},{type(c)}')
print(f'其中元素类型为：{[type(x) for x in a]},{[type(x) for x in b]},{[type(x) for x in c]}')
他们分别都是列表：[1, 2, 3],[1, 2, 3],[(1,), (2,), (3,)]
他们的类型都是：<class 'list'>,<class 'list'>,<class 'list'>
其中元素类型为：[<class 'int'>, <class 'int'>, <class 'int'>],[<class 'int'>, <class 'int'>, <class 'int'>],[<class 'tuple'>, <class 'tuple'>, <class 'tuple'>]

注意: (1) 表示int (1,) 加逗号表示tuple元祖类型


'''




