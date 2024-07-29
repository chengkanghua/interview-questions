'''
# Python基础
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

# 一行代码生成 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print( [i**2 for i in range(1,11)])

# 常用的字符串格式化?
print('我的名字%s,年龄:%d' % ('ckh', 18))
print("我的名字{} ,年龄:{}".format("ckh", 18))
name = 'ckh';age = 18
print(f'我的名字{name},年龄:{age}')

什么是断言 assert? 应用场景?
Python assert 语句，又称断言语句，可以看做是功能缩小版的 if 语句，它用于判断某个表达式的值，如果值为真，则程序可以继续往下执行；反之，Python 解释器会报 AssertionError 错误。
```py
mathmark = int(input())
#断言数学考试分数是否位于正常范围内
assert 0 <= mathmark <= 100
#只有当 mathmark 位于 [0,100]范围内，程序才会继续执行
print("数学考试分数为：",mathmark)

断言情况:
防御性编程
运行时对程序的逻辑检测
合约性检查(比如:前置条件,后置条件)
程序常量
检查文档

```
# 有两个字符串列表a和b,每个字符串是由逗号分隔的一些字符串:
```py
a = ['a,1','b,3,22','c,3,4']
b = ['a,2','b,1','d,2']
# c = ['a,1,2', 'b,3,22,1', 'c,3,4', 'd,2'] #得到c数组
c = []
for index,item in enumerate(a):
    if item[0] == b[index][0]:
        c.append(item + b[index][1:])
    else:
        c.append(item);
        c.append(b[index]);
print(c)

```
# 有一个多层嵌套的列表 A=[1,2,[3,4,["434",'535']]],写一段代码遍历A中的每一个元素并打印出来.
```py
A = [1,2,[3,4,["434",'535']]]
def pp(list1):
    for item in list1:
        if isinstance(item,list):
            pp(item)
        else:
            print(item)
pp(A)

```
# a = range(10);a[::-3]的结果是?
```py
a = [0,1,2,3,4,5,6,7,8,9]
print(a[::-3])  # [9, 6, 3, 0] #-3表示倒着走每次走3步

a = range(10)
print(a[::-3])  # range(9, -1, -3)# 从9倒着走每次走3步到-1停止 遍历出来的结果就是[9, 6, 3, 0]
```

# 下面哪个命令从虚拟环境中退出?
A deactivate    ✔
B exit
C quit
D 以上均可

# 将列表内的元素,根据位数合并成字典
```py
lst = [1,2,4,8,16,32,64,128,256,512,1024,32769,65536,4294967296]

dict1 = {}
for item in lst:
    key = len(str(item))
    if key not in dict1:
        dict1[key] = []
        dict1[key].append(item)
    else:
        dict1[key].append(item)

print(dict1)
# {
#  1: [1, 2, 4, 8],
#  2: [16, 32, 64],
#  3: [128, 256, 512],
#  4: [1024],
#  5: [32769, 65536],
#  10: [4294967296]
#  }

```
规则：
正数在前负数在后正数从小到大负数从大到小例：
排序前[7,-8,5,4,0,-2,-5]
排序后[0,4,5,7,-2,5,-8]
#补全代码：
sorted(lst, key=lambda x:___
```py
lst = [7, -8, 5, 4, 0, -2, -5]
sorted_lst = sorted(lst, key=lambda x: (x >= 0, abs(x)))
print(sorted_lst)   # [-2, -5, -8, 0, 4, 5, 7]
#这段代码中，lambda x: (x >= 0, abs(x)) 会为每个元素返回一个元组。如果 x 是正数或零，x >= 0 会是 True，否则是 False。abs(x) 是 x 的绝对值。由于Python在比较元组时首先比较第一个元素，然后是第二个元素，这将确保正数按照绝对值从小到大排序，而负数按照绝对值从大到小排序。

```
# 哈希冲突回避算法有哪几种,分别有什么特点?
哈希冲突是指两个或多个不同的键通过哈希函数算出到同一个哈希值.为了处理哈希冲突,多种算法被提出和使用.
1 开放寻址法
    双重哈希:使用另一个函数计算探测序列.
2 链表法:
    链表法通过在每个哈希桶中存储一个链表来解决冲突，链表中存储所有映射到该哈希桶的元素。当发生冲突时，只需将元素添加到对应哈希桶的链表中。这种方法简单且易于实现，且在哈希表的负载因子（即元素数量与哈希桶数量的比例）不是特别高时，性能通常很好。    
3 再哈希法
    当哈希表中的元素数量增加到一定程度，导致冲突变得频繁时，可以创建一个新的更大的哈希表，并使用另一个哈希函数重新计算所有元素的哈希值，然后将它们插入到新的哈希表中。这种方法可以减少冲突，但需要重新计算哈希值并移动元素，因此成本较高。

4 Cuckoo哈希
    Cuckoo哈希使用两个或多个哈希函数，每个元素可以位于多个哈希桶中。如果一个元素在插入时发现冲突，它会“踢走”那个位置的元素，并将那个元素移动到它的另一个哈希桶位置。如果那个位置也有冲突，这个过程会继续进行，直到找到一个空位。这种方法可以提供很好的性能，但实现起来相对复杂。
5 Hopscotch哈希
    Hopscotch哈希是一种平衡开放寻址法和链表法的策略。它允许元素在一定范围内“跳跃”到其他哈希桶，但仍然保持与原始哈希桶的联系。这种方法旨在减少聚集问题，同时保持较低的内存使用

# 简述Python的字符串驻留机制?
字符串驻留是一种在内存中仅保存一份相同且不可变字符串的方法。
小字符串驻留 长度小于等于20个字符的字符串
驻留范围:
1 字符串长度为0或1时，默认采用驻留机制；
2字符串长度大于1时，且 字符串中只包含大小写字母、数字、下划线(_) 时，采用驻留机制；
3对于 [-5,256]之间的整数数字，Python默认驻留 ；
4字符串 只在编译时进行驻留，而非运行时 。Python是解释型语言，但是事实上，它的解释器也可以是理解为是一种编译器，它负责将Python代码翻译成字节码，也就是.pyc文件；
5用乘法得到的字符串，如果结果长度 <=20且字符串只包含数字、字母大小写、下划线，支持驻留。长度>20，不支持驻留。这样的设计目的是为了保护.pcy文件不会被错误代码搞的过大。

# 以下代码输出的是什么?
````py
list=['a','b','c','d','e']
print(list[10:])   #  []
````
#  python 语言中哪些数据类型能为字典的key?
A.没有限制
B. 字母数字下划线
C. 字母
D. 可被hash的类型   ✔
可被hash的类型包括：
    整数 int
    浮点数 float
    字符串 str
    元组 tuple
    布尔值 bool
    None

#  以下两段代码输出一样吗?占用资源一样吗,什么时候用xrange 代替range?
# for i in range(1): print(i)
# for i in xrange(1): print(i)
在Python 2中，range()和xrange()是两个不同的函数，它们的行为略有不同：
range()函数会生成一个列表，包含指定范围内的所有整数。
xrange()函数则生成一个迭代器，它在迭代时才计算每个值，而不是一次性生成所有值。

python3中 range()已经类似python2的xrange()
使用xrange()可以节省内存，因为它不会一次性生成所有的数字。

#   如下代码 输出的值为啥?
import copy
a = [1, 2, 3, [4, 5], 6]
b = a
c = copy.copy(a)  # c :  [1, 2, 3, 引用[4, 5], 6]
d = copy.deepcopy(b)  # d : [1, 2, 3, [4, 5], 6]
b.append(10)  # a: [1, 2, 3, [4, 5], 6,10]  b: [1, 2, 3, [4, 5], 6,10]
c[3].append(11)  # c: [1, 2, 3, 引用[4, 5,11], 6]   a和b变量受到影响 [1, 2, 3, [4, 5,11], 6,10]
d[3].append(12)  # d : [1, 2, 3, [4, 5,12], 6]
print(a)  # [1, 2, 3, [4, 5,11], 6,10]
print(b)  # [1, 2, 3, [4, 5,11], 6,10]
print(c)  # [1, 2, 3, [4, 5,11], 6]
print(d)  # [1, 2, 3, [4, 5,12], 6]

# 按照字典的value字段进行排序
# d = {"a":26,"g":20,"e":20,"c":24,"d":23,"f":21,"b":25}
````py
d = {"a":26,"g":20,"e":20,"c":24,"d":23,"f":21,"b":25}

# 使用sorted函数和lambda表达式按字典的值进行排序
sorted_items = sorted(d.items(), key=lambda item: item[1])

# 将排序后的元组列表转换回字典（如果需要）
sorted_dict = dict(sorted_items)
print(sorted_items)  # 输出排序后的元组列表
print(sorted_dict)   # 输出排序后的字典
````
# 哪些PEP被认为涉及了代码规范:
A. PEP7
B. PEP8    ✔
C. PEP9
D. PEP10

# 下面那些是Python合法的标识符？那些是Python的关键字?
int32          # 合法，以字母开头。
40XL         #  不合法，因为标识符不能以数字开头。
saving$    # 合法，以字母开头，尽管包含特殊字符$，但在Python中是允许的。
ptint         # 合法，以字母开头。
this          # 合法，以字母开头。
self          # 合法，虽然它在类定义中用于引用实例本身，但作为标识符本身是合法的。
0x40L      # 不合法，因为标识符不能以数字开头。
true             # 合法，以字母开头。
big-daddy   # 不合法，因为标识符不能包含连字符-
True                python内置常量  不可以做标识符
if                   关键字
do                # 合法，以字母开头。
yield            关键字

定义：标识符是程序员自定义的名称，用于变量、函数、类、模块等。
在Python中，合法的标识符必须遵循以下规则：
1.标识符的第一个字符必须是字母（大写或小写）或下划线（_）。
2.标识符的其余部分可以由字母（大写或小写）、数字（0-9）或下划线（_）组成。
3.标识符不能是Python的关键字。
4.标识符区分大小写。
# 检查某个字符串是否是关键字
import keyword
print(keyword.iskeyword('yield'))   # True

# 从0-99中随机取出10个,要求不重复,可以自己设计数据结构.
````py
import random
list1 = []
while len(list1) < 10:
    num = random.randint(0,99)
    if num not in list1:
        list1.append(num)
print(list1)

````
````py
import random
numbers = list(range(100))
select_numbers = random.sample(numbers,10)
print(select_numbers)

import random
def select_random_numbers(total_numbers, sample_size):
    total_numbers = set(range(total_numbers))
    result = set()
    while len(result) <= sample_size:
        item = random.choice(list(total_numbers))
        result.add(item)
        total_numbers.remove(item)
    return result

result = select_random_numbers(100, 10)
print(result)

````
#  python 判断一个字典中是否有这些 key:"AAA","BB","C","DD","EEE"(不使用for while)

````py
# 假设这是我们的字典
my_dict = {'AAA': 1, 'BB': 2, 'C': 3, 'DD': 4, 'EEE': 5}
# 定义一个包含我们想要检查的键的列表
keys_to_check = ['AAA', 'BB', 'C', 'DD', 'e']
# 使用 all() 函数和生成器表达式来检查所有键是否都在字典中
# all_keys_present = all(key in my_dict for key in keys_to_check)
# all_keys_present = all(key in my_dict.keys()  for key in keys_to_check)
for key in keys_to_check:
    if key in my_dict:
        print(key)
# 输出结果
# print("所有指定的键都在字典中:", all_keys_present)
```
#  有一个list["this","is","a","Boy","!"],所有元素都是字符串,对他进行大小写无关的排序?
my_list = ["this", "is", "a", "Boy", "!"]
sorted_list = sorted(my_list, key=lambda x: x.lower())
print(sorted_list)  # ['!', 'a', 'Boy', 'is', 'this']

#  描述下dict的item() 方法与iteritems() 的不同
items()和iteritems()在Python 2中是两个不同的方法，分别返回列表和迭代器。而在Python 3中，items()方法返回一个迭代器，与Python 2中的iteritems()行为相同。在Python 3中，iteritems()方法已经被废弃，不再存在。

# 请列举你知道的python代码检测工具以及它们的区别。
它们通常用于代码风格检查、错误检测、性能分析等:
1.Pylint
检测代码中的错误、不符合代码标准的问题和潜在问题。
提供了大量的代码质量检查，包括代码风格、变量命名、变量未使用等。
支持自定义规则和扩展。
2.flake8
是一个代码检查工具，它结合了pyflakes、pycodestyle（原pep8）和McCabe复杂度检查。
pyflakes检查代码中未使用的变量、导入错误等。
pycodestyle检查代码是否符合PEP 8风格指南。
McCabe检查代码的复杂度，帮助识别代码中的复杂部分。
3.pycodestyle（原pep8）
专注于检查Python代码风格是否符合PEP 8风格指南。
检查缩进、空格、换行符、命名约定等。
不检查代码的逻辑错误。
4.mypy
进行静态类型检查，帮助发现类型相关的错误。
可以指定变量、函数参数和返回值的类型注解。
鼓励使用类型注解来提升代码的可读性和可维护性。
5.Bandit
专注于检测Python代码中的安全问题。
分析代码中的潜在安全风险，并给出修复建议。
适用于大型代码库的安全审计。
6.Pytest
主要是一个测试框架，但也可以用来检测代码中的问题。
允许编写详细的测试用例来检查代码的行为。
通过测试覆盖率来帮助识别未测试到的代码部分。
7.Coverage.py
用于测量代码的测试覆盖率。
可以帮助开发者了解哪些代码行被测试覆盖到了。
通常与pytest或其他测试框架结合使用。
8.Sphinx
主要用于生成项目的文档，但它也可以检测文档中的错误和不一致。
确保文档与代码保持同步，有助于减少文档错误。'

# 介绍一下 try  except的用法和作用?
在Python中，try和except是异常处理的关键部分，它们用于捕获和处理程序运行时可能发生的错误。
```py
try:
    # 尝试除以零
    result = 10 / 0
except ZeroDivisionError as e:
    # 处理除零错误
    print("不能除以零！错误信息:", e)
```
# 输入一个字符串,返回倒序排列的结果,如如: abcdef 返回 fedcba
```py
str = 'abcdef'
def resverse(word):
    return word[::-1]
print(resverse(str))
```
#  看代码写结果?
```py
alist = [2, 4, 5, 6, 7]
for var in alist:
    if var % 2 == 0:
        alist.remove(var)  # 第一次遍历 2删除了数组索引0位置2, 数字4就成了索引0,第二次遍历到了索引1就是5了
print(alist)  # [4, 5, 7]
```
# 现有alist = [3,1,-4,-2] ,按其元素的绝对值大小进行排序?
```py
alist = [3,1,-4,-2]
# sorted_alist = sorted(alist,key=lambda x:abs(x))
sorted_alist = sorted(alist,key=abs)
print(sorted_alist)
```
填空题
1.表达式3<4<5是哪一个表达式的缩写__ 3<4 and 4<5
2.获取Python 解释器版本的方法是:__ import sys; print(sys.version)
3.如果模块是被导入的__name__ 的值是值是___，如果模块是被直接执行的__name__的值是__     填写: __main__ , 模块名
4.Python的内存管理中，为了追踪内存中的对象，使用了__ 这一简单技术. 答:引用计数
5.Python的标准解释器是有c语言实现的，称为 __，有Java 实现的被称为___. 答: CPython , Jython

6.Python中,__语句能直接显示的释放内存资源.    答: del
7.Python的乘方运算符是__.     答   **

# 现有字典mydict和变量onekey，请写出从 mydict 中取出onekey 值的方法（不止一种写法，多写加分，并请叙述不同写法的区别，mydict中是否存在onekey的键值，不确定)

```py
value = mydict.get(onekey)  # 存在返回值对应值,不存在返回None
value = mydict[onekey] if onekey in mydict else None


if onekey in mydict:
    value = mydict[onekey]
else:
    value = None
```

# 现有一列表alist，请写出两种去除alist中重复元素的方法，其中：
1.要求保持原有列表中元素的排列顺序。
```py
alist = [1, 2, 3, 2, 1, 5, 6, 5, 5, 10]
seen = set()
new_list = []
for item in alist:
    if item not in seen:
        new_list.append(item)
        seen.add(item)
print(new_list)  # 输出: [1, 2, 3, 5, 6, 10]
```
2.无需考虑原有列表中元素的排列顺序。
```py
alist = [1, 2, 3, 2, 1, 5, 6, 5, 5, 10]
new_list = list(set(alist))
print(new_list)  # 输出可能是: [1, 2, 3, 5, 6, 10]，但顺序可能不同
```
# 哪些情况下，y！=x-(x-y)会成立?
在大多数情况下，y != x - (x - y) 不成立，除非在下述提到的特殊情况
1.整数溢出
2.浮点数精度
3.特殊值：在某些编程语言中，如Python，整数除以零会引发一个异常，而不是返回一个特定的值。如果 x 和 y 中的任何一个为零，那么 x - (x - y) 将引发异常，而 y 不会引发异常，因此 y != x - (x - y) 成立。

# 用Python实现99乘法表（用两种不同的方法实现）
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={i*j} ',end="\t")
    print()

for i in range(1,10):
    print(" ".join(f'{j}*{i}={i*j} ' for j in range(1,i+1)))

# 获取list中的元素个数，和向末尾追加元素所用的方法分别是什么？
```py
my_list = [1,2,3,4,5]
print("list个数:",len(my_list))
my_list.append(6)
print("追加后的list: ",my_list)
```
# 判断dict 中有没有某个key用的方法是什么？
key in dict   # 返回True 或False
dict.get(key)  # 没有key返回None   有的话返回1
key in dict.keys()   # 返回True 或False

# 如下代码示例，回答
l=range (100)
# 1.如何取第一到第三个元素用的是
print(l[0:3])
# 2.如何取倒数第二个元素
print(l[-2])
# 3.如何取后十个
print(l[-10:])

# 如何判断一个变量是否是字符串？
str1 = 'ssss'
print(isinstance(str2,str))
print( type(str1) is str)

# list和tuple有什么不同?
可变性:
语法:
性能: tuple 是不可变的, 有更高的性能, 内存占用更少.
用途: list用于需要修改的数据集.  tuple 用于固定的数据.

# a=dict(zip(("a","b","c","d","e"),(1,2,3,4,5)))请问a是什么？

zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。

答: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}  a是一个字典
a=dict(zip(("a","b","c","d","e"),(1,2,3,4,5)))
print(a)
print(list(zip(("a","b","c","d","e"),(1,2,3,4,5))))  # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

# 以下叙述正确的是
A.continue 语句的作用是结束整个循环的执行
B.只能在循环体和switch语句体内使用break语句    ✔
c.在循环体内使用break语句或者continue语句的作用相同
D.从多层循环嵌套中退出时，只能使用goto语句

# 读代码
for i in range(5,0,-1):
    print(i,end=' ')   # 5 4 3 2 1

# 选择正确的结果
x = 'foo'
y = 2
print(x+y)
#选择正确的结果
A.foo
B.foo foo
C.foo 2
D. 2
E. An exception is thrown    ✔

# 求结果
kvps = {"1":1,"2":2}
theCopy = kvps   # 可变类型是引用赋值  内存地址一样
kvps['1'] = 5
# print(id(kvps), id(theCopy))
sum = kvps['1'] + theCopy["1"]
print(sum)   # 10
A . 1
B . 2
C. 7
D. 10   ✔

# python里如何实现tuple和list的转化
tuple1 = (1,2,3)
print(list(tuple1))
list1 = [1,2,3]
print(tuple(list1))

# print(type(1 + 2L * 3.14))  # 要再python2中执行 输出: <class 'float'>
print(type(1 + 2 * 3.14))  # 输出: <class 'float'>
# 若k为整型，下列while循环执行的次数为多少? 算法复杂性是多少
# k=1000
# while k > 2
#     print(k)
#     k=k/2
答: 10次.   关于算法复杂性，这个循环的复杂性是O(log n)

# 以下何者是不合法的布尔表达式
# A. x in range(6)
# B.3=a      #这是一个不合法的布尔表达式, = 是一个赋值操作符
# C.e>5 and 4==f
# D. (x-6)>5

# python不支持的数据类型有
# A. char   # 虽然Python没有专门的char类型，但可以使用长度为1的字符串来表示单个字符。
# B. int
# C. float
# D. list
如果题目是询问Python中没有的特定类型,那么答案是A

# 如何在Python 中拷贝一个对象，并说明他们之间的区别？
答 : 深拷贝和浅拷贝 , 上面有

# 99（10进制）的八进制表示是什么？
a = 99
print( oct(a))  #  0o143

# 下列Python 语句正确的是
1.min = x is x<y=y   # 语法错误
2.max =x>y?x:y       # 语法错误 python中没有三元运算符,  而是使用x if condition else y的形式来实现三元运算。
3. if(x>y)print x      # 语法 if 后面缺少 :    print调用要加括号
4. while True:pass  #这个语句是正确的

#  list对象 alist=[{'name':'a','age':20}, {'name':'b','age':30}, {'name':'v','age':25},] 按alist中元素的age由大到小排序。
```py
alist=[{'name':'a','age':20}, {'name':'b','age':30}, {'name':'v','age':25},]
sort_list = sorted(alist, key=lambda x:x['age'],reverse=True)
print(sort_list)
```
# 关于Python程序的运行性能方面，有什么手段能提升性能？
答:  1使用 python内置的函数和库
2 避免全局变量,尽量使用局部变量
3 列表推导式
4 生成器表达式
5 使用 map() 和 filter() 函数  比等效的函数更快
6 优化算法和数据结构

# Python是如何进行内存管理的？Python的程序会内存泄漏吗？
内存管理: 引用计数+垃圾回收   分代回收
分代回收详细说明: Python的垃圾回收器还支持分代回收（generation garbage collection），这是一种优化技术，它将对象分为不同的代（generation），新创建的对象属于第一代，如果一个对象在多次垃圾回收中存活下来，它会被移动到下一代。由于大多数对象很快就会变得不可达，因此垃圾回收器主要关注较年轻的对象，这样可以提高垃圾回收的效率。
内存泄露: 可能发生,尤其是循环引用且没有正确管理时.
避免内存泄漏:
    - 尽量避免不必要的全局变量
    - 使用弱引用 （weakref模块）来打破循环引用。
    -  在不再需要对象时，显式地将其引用设置为None，帮助垃圾回收器回收对象。

# 说说有没有什么方面阻止或检测内存泄漏
阻止内存泄漏
1.
避免循环引用：确保对象之间不形成循环引用，特别是在使用自定义类和容器时。可以使用弱引用（weakref模块）来打破循环引用。
2.
使用上下文管理器：利用with语句和上下文管理器（如文件操作）来确保资源被正确释放。
3.
及时释放资源：对于文件、网络连接等资源，确保在不再需要时及时关闭或释放。
4.
使用__del__方法谨慎：避免在自定义类中使用__del__析构方法，因为垃圾回收器的执行时间是不确定的，依赖于__del__可能导致不可预测的行为。
5.
使用__slots__：如果类的实例不会增加新的属性，使用__slots__可以减少内存使用并提高性能。
检测内存泄漏
1.使用内存分析工具：如memory_profiler、objgraph等，这些工具可以帮助你监控程序的内存使用情况，识别内存泄漏。
2.定期检查引用计数：使用gc模块中的get_count()函数来检查当前的引用计数，这可以帮助你了解对象的引用情况。
3.代码审查：定期进行代码审查，特别是关注那些可能形成循环引用的部分。
4.单元测试：编写单元测试来验证代码的内存使用情况，确保在各种情况下内存都能被正确释放。
5.使用gc.collect()：在代码中显式调用gc.collect()来强制执行垃圾回收，检查是否有对象未被回收。

# 一个大小为100G的文件etl_log.txt,要读取文件中的内容，写出具体过程代码？
with open('etl_log.txt','r') as file:
    for line in file:
       # process(line)  # 处理每一行的数据

# 已知Alist=[1,2,3,1,2,1,3],如何根据Alist得到[1,2,3]
Alist=[1,2,3,1,2,1,3]
print(list(set(Alist)))  # 去重

# 已知stra='wqedsfsdrfweedqwedqw'
# 1.如何获取最后两个字符
# 2.如何获取第二个和第三个字符
stra='wqedsfsdrfweedqwedqw'
print(stra[-2:])
print(stra[1:3])

# 已知Alist=["a","b","c"],将Alist转化为'a,b,c'的实现过程
Alist=["a","b","c"]
print(','.join(Alist))

# 已知ip='192.168.0.100'代码实现提取各部分并写入列表。
ip='192.168.0.100'
list_ip = ip.split(".")
print(list_ip)

# python代码如何获取命令行参数？
```py
import sys
print('命令行参数: ',sys.argv)
print('脚本名称:', sys.argv[0])
if len(sys.argv) > 1:
    print('第一个参数:', sys.argv[1])

```
# 写代码，写出由tupleA和tupleB得到res的及具体实现过程
```py
tupleA = ('a','b','c','d','e')
tupleB = (1,2,3,4,5)
# res = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
res = dict(zip(tupleA,tupleB))
print(res)
```
# 选出一下表达式表述正确的选项
A. {1:0,2:0,3:0}
B. {'1':0,'2':0,'3':0}
C. {(1,2):0,(4,3):0}
D. {[1,2]:0,[4,3]:0}  # 错误，列表是可变类型，不能作为字典的键。
E. {{1,2}:0,{4,3}:0}  # 错误，集合是可变类型，不能作为字典的键。

# what gets parint ?
```py
kvps = {"1":1,"2":2}
theCopy = kvps.copy()   # 浅拷贝
kvps['1'] = 5
# print(id(kvps), id(theCopy))   #内存地址不一样了
sum = kvps['1'] + theCopy["1"]
print(sum)   # 6
```
# what gets print ?
numbers = [1,2,3,4]
numbers.append([5,6,7,8])
# print(numbers)  # [1, 2, 3, 4, [5, 6, 7, 8]]
print(len(numbers)) # 5

# what gets print ?
```py
names1 = ['Amir','Barry','Chaies','Dao']
if "amir" in names1:
    print(1)   # 输出1
else:
    print(2)
```
# Pyhton 包管理工具是?
A. APT
B. PIP  ✔
C. YUM
D. MAVEN

# 求结果
import math
print(math.floor(5.5))  # 5

# 关于Python的内存管理，下列说法错误的是
A.变量不必事先声明
B.变量无需先创建和赋值而直接使用 # 这是错误的。在Python中，你不能直接使用一个未创建和赋值的变量。尝试这样做会引发一个NameError异常。
c.变量无需指定类型
D.可以使用del释放资源

# 下面那个不是Python合法的标识符
# A. int32
# B.40xl  # 不合法，因为标识符不能以数字开头。
# C.self
# D. name

# 下列哪种说法是错误的
# A.除字典类型外，所有标准对象均可用于布尔测试 #这是错的,字典也可以用于布尔测试
# B.空字符串的布尔值是 False
# c.空列表对象的布尔值是False
# D.值为0的任何数字对象的布尔值是False

# 下列表达式为True是:  没有
A. 5+4j >2-3j
B 3>2>2
C (3,2) < ("a","b")
D "abc" > 'xyz'

# 关于Python的复数，下列说法错误的是
# A.表示复数的语法是 real+imagej
# B.实部和虚部都是浮点数  # 错误: 在Python中，实部和虚部可以是整数或浮点数。例如，3+4j和3.0+4.0j都是有效的复数表示。
# c.虚部后缀必须是j，且必须小写  # 错误的。虚部后缀可以是小写的j或大写的J。例如，3+4j和3+4J都是有效的复数表示。
# D.方法conjugate返回复数的共轭复数

# 关于字符串下列说法错误的是
A.字符应视为长度为1的字符串
B.字符串以\0标志字符串的结束  # 这是错误的。在Python中，字符串不是以\0（空字符）标志结束的。Python使用的是Unicode编码，字符串的结束是通过字符串对象的内部表示来确定的，而不是通过一个特定的字符。
c.既可以用单引号，也可以用双引号创建字符串D.在三引号字符串中可以包含换行回车等特殊字符

# 以下不能创建一个字典的语句是
A.dicl ={}
B.dic2 ={3:5}
C. dic3 ={[1,2,3]:"usetc"}  # 这是错误的。列表是可变类型，不能用作字典的键。
D. dic4 ={(1,2,3):"usetc"}

# 描述在python中的元祖，列表，字典的区别，并且分别写一段定义，添加，删除操作的代码片段。


# 看代码选结果
```py
names1 = ['Amir', 'Barry', 'Cales', 'Dao']
names2 = names1  # Python中的变量赋值实际上是对象的引用传递
names3 = names1[:]  # 切片时浅拷贝
names2[0] = 'Alice'  # names1 和names2发生改变 ['Alice', 'Barry', 'Cales', 'Dao']
names3[1] = "Bob"   # names3:  ['Amir', 'Bob', 'Cales', 'Dao']
sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':  #1+1
        sum += 1
    if ls[1] == 'Bob':   #10
        sum += 10
print(sum)  #12

A.11
B.12   ✔
c. 21
D.22
E.23

```
# 1 or2和1 and2输出分别是什么？为什么
1 or 2的输出是1。
1 and 2的输出是2。
or和and运算符的短路求值特性:
    or 运算符第一个为真就不会评估第二个操作数
    and 运算符第一个为假就不会评估第二个操作数

# 1<(2==2)和1<2==2的结果分别是什么，为什么
```py
“1 < (2==2)” 分析:“(2==2)” 结果为 True，即 1，而 ”1 < 1“ 为假，所以结果为 False。
“1 < 2==2” 分析: Python 是允许连续比较的，“1 < 2==2” 相当于 ”(1 < 2) and (2==2)“，所以结果为 True。
原文链接：https://blog.csdn.net/qq_44214671/article/details/111712853
```
# 如何打乱一个排好序的list对象alist
```py
import random
# 假设alist是一个已经排好序的列表
alist = [1, 2, 3, 4, 5]
# 使用random.shuffle()打乱列表
random.shuffle(alist)
# 打印打乱后的列表
print(alist)
```
# 如何查找一个字符串中特定的字符?find和index的差异？
```py
s = "Hello, world!"
index = s.find("world")  # 返回首次出现的索引位置,找不到返回-1
print(index)  # 输出: 7
index = s.index("world")  #  返回首次出现的索引位置, 找不到抛出一个ValueError异常。
print(index)
```
# 把aaabbcccd这种形式的字符串压缩成a3b2c3d1这种形式。
```py
str1 = 'aaabbcccd'
str2 = ''
tmpsum = 1
for i, v in enumerate(str1):
    # 第一个字符的处理
    if i == 0:
        str2 += v
        continue
    if v != str1[i - 1]:
        str2 += str(tmpsum)
        str2 += v
        tmpsum = 1
    else:
        tmpsum += 1
    # 结尾的处理
    if (i == len(str1) - 1):
        str2 += str(tmpsum)
print(str2)  # a3b2c3d1
```

```py
def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1]+str(count))
            count = 1
    compressed.append(s[-1]+str(count))
    return ''.join(compressed)

str1 = 'aaabbcccd'
compress_string = compress_string(str1)
print(compress_string)
```

# Python一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1+2+3.编程找出1000以内的所有完数。
```py
def is_perfect_number(number):
    # 计算因子之和
    sum_of_factors = sum([i for i in range(1, number) if number % i == 0])
    # 判断因子之和是否等于原数
    return sum_of_factors == number


# 找出1000以内的所有完数
perfect_numbers = [number for number in range(1, 1001) if is_perfect_number(number)]
print("1000以内的完数有：", perfect_numbers)  # [6, 28, 496]

sum([i for i in range(1, 6) if 6 % i == 0])
# 6%1=0
# 6%2=0
# 6%3=0
# 6%4=2
# 6%5=1
# sum([1, 2, 3])  =6    因子之和正好等于自己

```
# 输入一个字符串，输出该字符串中字符的所有组合.例如：输入字符串"1,2,3"，则输出为1,2,3,12,13,23,123（组合数，不考虑顺序，所以12和21是等价的)
```py
def comstring(string: str):
    tmp_list = string.split(',')
    result_list = tmp_list[:] # 切片浅拷贝 ,此变量用来存储最终结果
    for i in range(len(tmp_list)):
        tmp_str = ''
        for j in range(i + 1, len(tmp_list)):
            tmp_str += tmp_list[j]
            result_list.append(tmp_list[i] + tmp_list[j])
        if tmp_str != '' and len(tmp_str) > 1:
            result_list.append(tmp_list[i] + tmp_str)
            tmp_str = ''

    return ','.join(result_list)

result = comstring('1,2,3')
print(result) # 1,2,3,12,13,123,23
```
# 对于一个非空字符串，判断其是否可以有一个子字符串重复多次组成，字符串只包含小写字母且长度不超过10000
示例1：
1.输入"abab"
2.输出True
3.样例解释：输入可由"ab"重复两次组成
示例2：
1.输入"abcabcabc"
2.输出True
3.样例解释：输入可由"abc"重复三次组成
示例3：
1.输入"aba"
2.输出False

```py
def can_form_by_repeating_substring(s):
    if not s:
        return False
    # 计算字符串长度
    length = len(s)
    # 遍历所有可能的子字符串长度
    for i in range(1, length // 2 + 1):
        if length % i == 0:
            # 尝试将字符串分割为长度为i的子字符串
            substring = s[:i]
            # 检查是否所有子字符串都相同
            if all(s[j] == substring[j % len(substring)] for j in range(length)):
                return f'True\n样例解释：输入可由"{substring}"重复{length//len(substring)}次组成'

    return False

print(can_form_by_repeating_substring("abab"))  # 输出: True
print(can_form_by_repeating_substring("abcabcabc"))  # 输出: True
print(can_form_by_repeating_substring("aba"))  # 输出: False
```

# 函数
# 通过代码实现如下转换：
二进制转换成十进制：v=”0b1111011"  # int(v,2)
十进制转换成二进制：v=18           # bin(v)
八进制转换成十进制：v=“011"        # int(v,8)
十进制转换成八进制：v=30           # oct(v)
十六进制转换成十进制：v=“0x12”     # int(v,16)
十进制转换成十六进制：v=87         # hex(v)


# Python递归的最大层数?
默认情况下，Python的最大递归深度大约是1000层。
import sys
# 设置递归深度为2000
sys.setrecursionlimit(2000)

# 列举常见的内置函数?
zip  #将多个可迭代对象对应的元素打包成一个元组,然后返回这些元组组成的列表.
type 返回对象类型
sum  返回可迭代对象的总和
sorted   排序
reversed()  反转
range   返回一个整数序列
print    输出
len
id
isinstance(object,classinfo) 检查对象是否时类的实例
input  输入
format  将值转换为“格式化”表示形式。
enumerate(iterable, start=0)：返回一个枚举对象。
dir([object])：列出对象的所有属性。
all(iterable)：如果可迭代对象中的所有元素都为真，则返回True。
abs(x)：返回数字的绝对值。

# filter、map、reduce的作用?
```py
# map()函数是一个内置函数，用于对可迭代对象中的每个元素应用一个给定的函数，并返回一个迭代器，该迭代器生成应用函数后的结果
# map 语法: map(function,iterable,...)
list(map(abs, [-1, 3, -5, 8]))
# [1, 3, 5, 8]
list(map(lambda x: x.center(3, '#'), ['马云', '马化腾', '李彦宏']))
# ['#马云', '马化腾', '李彦宏']
# 自定义函数，计算3次方
def square(x):
    return x ** 3
list(map(square, [1, 2, 3, 4, 5]))
# [1, 8, 27, 64, 125]

# 使用 lambda 匿名函数
list(map(lambda x: x ** 3, [1, 2, 3, 4, 5]))
# [1, 8, 27, 64, 125]
# 提供了两个列表，对相同位置的列表数据进行相加
list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
# [3, 7, 11, 15, 19]
list(map(lambda x: x % 2 == 1, [1, 3, 2, 4, 1]))
# [True, True, False, False, True]

# reduce方法，顾名思义就是减少
# 语法：reduce(function,sequence[,initial]=>value) 参数2时一个序列或多个序列
from functools import reduce
nums = [6, 9, 4, 2, 4, 10, 5, 9, 6, 9]
print(sum(nums)) # 64
print(reduce(lambda val, x: val + x, nums)) # 64
# 累计减法
reduce(lambda x, y: x - y, [1, 2, 3, 4]) # -8

# 累计乘法
def multi(x, y):
    return x * y
reduce(multi, [1, 2, 3, 4]) # 24
reduce(lambda x, y: x * y, [1, 2, 3, 4]) # 24

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 语法：filter(function, iterable)
fil = filter(lambda x: x > 10, [1, 11, 2, 45, 7, 6, 13])
print(fil)
# < filter at 0x28b693b28c8 >  # 可迭代对象，不能直接查看
list(fil) # [11, 45, 13]


def isodd(num):
    if num % 2 == 0:
        return True
    else:
        return False

list(filter(isodd, range(1, 13))) # [2, 4, 6, 8, 10, 12]

# sorted() 函数对所有可迭代的对象进行排序操作。
# 语法：sorted(iterable,  key=None, reverse=False)

sort 与 sorted 区别：
sort 是应用在 list上的方法 操作的list,无返回值，sorted 可以对所有可迭代的对象进行排序操作,返回值时新的list

a = [5, 7, 6, 3, 4, 1, 2]
b = sorted(a)  # 保留原列表   # b :[1, 2, 3, 4, 5, 6, 7]

# 利用key
L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
sorted(L, key=lambda x: x[1]) # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
# 按年龄排序
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted(students, key=lambda s: s[2])
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
# 按降序
sorted(students, key=lambda s: s[2], reverse=True)
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# 降序排列
a = [1, 4, 2, 3, 1]
sorted(a, reverse=True)  # 返回值 [4, 3, 2, 1, 1]

'手机品牌-销量-售价'
info = [('Apple',800,9799),
       ('Xiaomi',40,3599),
       ('Oppo',40,4199),
       ('Vivo',100,4000),
       ('Huawei',40,6899),]
#正常排序
print(sorted(info))
# [('Apple', 800, 9799), ('Huawei', 40, 6899), ('Oppo', 40, 4199), ('Vivo', 100, 4000), ('Xiaomi', 40, 3599)]
#按销量排序
print(sorted(info,key = lambda x: x[1],reverse=True))
# [('Apple', 800, 9799), ('Vivo', 100, 4000), ('Xiaomi', 40, 3599), ('Oppo', 40, 4199), ('Huawei', 40, 6899)]
#按商品价格排序
print(sorted(info,key = lambda x: x[2],reverse=True))
# [('Apple', 800, 9799), ('Huawei', 40, 6899), ('Oppo', 40, 4199), ('Vivo', 100, 4000), ('Xiaomi', 40, 3599)]
#先价格 再销量排序
print(sorted(info,key = lambda x: (x[2],x[1]),reverse=True))
# [('Apple', 800, 9799), ('Huawei', 40, 6899), ('Oppo', 40, 4199), ('Vivo', 100, 4000), ('Xiaomi', 40, 3599)]


```
# 一行代码实现9*9乘法表
print('\n'.join([' '.join([f'{j}*{i}={i*j}' for j in range(1, i+1)]) for i in range(1, 10)]))

# 什么是闭包?
闭包（Closure）是编程语言中的一个概念.
在闭包中，函数可以访问在外部作用域中定义的变量，即使外部函数已经执行完毕。闭包允许函数记住并访问其定义时的词法环境，即使该函数在其他地方被调用。
闭包在很多编程场景中非常有用，例如：
创建装饰器（Decorators）
实现回调函数
保持状态信息
```py
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

my_closure = outer_function("Hello, World!")
my_closure()  # 输出: Hello, World!
```

# 简述生成器、迭代器、装饰器以及应用场景？
生成器（Generators）
生成器是一种特殊的迭代器，它允许你以一种延迟计算的方式生成一系列值。生成器使用yield关键字来返回值，而不是使用return。生成器在处理大量数据时非常有用，因为它不需要一次性将所有数据加载到内存中。
应用场景：
处理大型数据集，如文件读取、数据流处理。
生成序列，如斐波那契数列。
实现惰性求值，即只有在需要时才计算值。

迭代器（Iterators）
迭代器是一个实现了迭代协议的对象，它允许你逐个访问容器中的元素。迭代器有两个基本方法：__iter__()和__next__()。迭代器在Python中广泛用于循环和迭代操作。
应用场景：
遍历容器，如列表、元组、字典、集合等。
实现自定义的迭代模式。
与for循环和next()函数一起使用。


装饰器（Decorators）
装饰器是一种设计模式，它允许用户在不修改原有函数定义的情况下增加函数的新功能。装饰器本质上是一个函数，它接受另一个函数作为参数并返回一个新的函数。
应用场景：
日志记录：在函数执行前后添加日志记录。
性能测试：测量函数执行时间。
权限检查：在函数执行前进行权限验证。
缓存：缓存函数的返回值以避免重复计算。
异常处理：为函数添加异常处理逻辑。

# 使用生成器编写fib函数，函数声明为fib(max)，输入一个参数 max 值，使得该函数可以这样调用。
for i in range(0, 100):
    print(fib(1000))
并产生如下结果（斐波那契数列），1，1，2，3，5，8，13，21...

斐波那契数列: 它从两个初始数开始，之后的每个数都是前两个数的和。
```py
def fib(max):
    a, b ,counter = 0, 1 ,0
    while True:
        if counter > max: return
        yield a
        a,b=b,a+b
        counter += 1


# 使用fib函数
for i in fib(100):
    print(i,end=' ')
```
# # 一行代码，通过filter和lambda函数输出以下列表索引为奇数对应的元素。list_a=[12,213,22,2,2,2,22,2,2,32]
```py
list_a = [12, 213, 22, 2, 2, 2, 22, 2, 2, 32]
print(list(filter(lambda x: x % 2 != 0, list_a)))
```
# 写一个base62encode 函数，62进制。
```py
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(num, alphabet):
    """Encode a positive number into Base X and return the string.

    Arguments:
    - `num`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]
    arr = []
    arr_append = arr.append  # Extract bound-method for faster access.
    _divmod = divmod  # Access to locals is faster.
    base = len(alphabet)
    while num:
        num, rem = _divmod(num, base)
        arr_append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def decode(string, alphabet=BASE62):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for decoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num

print(encode(987654321,BASE62))  # 编码  14Q60p
print(decode("14Q60p",BASE62))  # 解码  987654321
```
# python一行 print 出1~100偶数的列表，(列表推导式，filter均可）
```py
print([  x for x in range(1,101) if x % 2 ==0])
print(list(filter(lambda x: x % 2 == 0, range(1, 101))))
```
# 解释生成器与函数的不同，并实现和简单使用generator.
生成器（Generator）和函数（Function）在Python中都是用来封装代码块以供重复使用的结构，但它们在执行方式和内存使用上存在显著差异。

函数（Function）
函数是执行一系列操作并返回一个值的代码块。当调用函数时，函数内的所有代码都会被执行，函数执行完毕后返回一个值，然后函数的执行环境被销毁，包括所有局部变量。

生成器（Generator）
生成器是一种特殊的迭代器，它允许你延迟计算一系列值，而不是一次性计算所有值。生成器使用yield关键字来返回一个值，并在下一次迭代时从上次返回的位置继续执行。生成器在每次迭代时只计算并返回一个值，因此它们在处理大量数据时非常有用，因为它们不需要一次性将所有数据加载到内存中。

生成器与函数的不同点
1.
执行方式：函数在调用时执行所有代码，生成器在每次迭代时只执行到yield语句。
2.
返回值：函数返回一个值后结束，生成器可以返回多个值，通过多次迭代。
3.
内存使用：函数在执行完毕后释放所有资源，生成器在迭代之间保持状态，只占用必要的内存。

# 实现简单的生成器
```py
def simple_generator():
    for i in range(5):
        yield i

# 使用生成器
gen = simple_generator()
print(next(gen))  # 输出: 0
print(next(gen))  # 输出: 1
print(next(gen))  # 输出: 2
print(next(gen))  # 输出: 3
print(next(gen))  # 输出: 4
# print(next(gen))  # 这里会抛出StopIteration异常，因为生成器已经耗尽
```
# 列表推导式和生成器表达式[i%2 for i in range(10)]和(i%2 for i in range(10))输出结果分别是什么?

```py
[i%2 for i in range(10)]  # 得到列表
# [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

(i%2 for i in range(10))  # 生成器对象
# <generator object <genexpr> at 0x0000018CDF0D2B48>

```
# map(str,[1,2,3,4,5,6,7,8,9])输出是什么？
```py
map(str,[1,2,3,4,5,6,7,8,9])
# <map object at 0x0000018CDF178278>  # 可迭代对象

print(list(map(str,[1,2,3,4,5,6,7,8,9]))) # ['1', '2', '3', '4', '5', '6', '7', '8', '9']
```
# python中定义函数时如何书写可变参数和关键字参数?
*args 用于接收额外的可变参数
**kwargs 用于接受额外的关键字参数
在函数内部,args是一个元组,kwargs 是一个字典

# Python3.5中enumerate 的意思是什么?
enumerate是一个内置函数，用于将一个可迭代对象（如列表、元组、字符串等）组合成一个索引序列，同时列出数据和数据下标，通常用于在for循环中获取元素的索引和值。
语法: enumerate(iterable, start=0)

# 说说Python 中的装饰器，迭代器的用法：描述下 dict的item方法与iteritems方法的不同
```py
Python中的装饰器
在不修改函数定义的情况下增加函数的新功能. 装饰器本质是一个函数.接受一个函数作为参数并返回一个新的函数.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

迭代器的用法
迭代器用于遍历集合(如列表,元组,字典,集合等)的工具. 实现了迭代协议,即定义了__iter__() 和__next__() 方法.
my_list = [1, 2, 3, 4, 5]
iterator = iter(my_list)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

dict的items方法与iteritems方法的不同
在Python 2中，dict对象提供了items()和iteritems()两种方法：
items()方法返回一个包含字典中所有键值对的列表。
iteritems()方法返回一个迭代器，它包含字典中所有键值对，但不返回列表。
在Python 3中，iteritems()方法被移除，items()方法返回一个迭代器，与Python 2中的iteritems()方法类似。


```

# 是否使用过functools中的函数?其作用是什么？
functools是Python标准库中的一个模块，它提供了一些用于高阶函数的工具，这些工具可以用于操作可调用对象（如函数）和它们的参数。functools模块中的函数可以用于函数编程、装饰器的创建和使用、以及函数的组合等。

functools.partial
partial函数用于创建一个新的可调用对象，这个对象将原函数的某些参数固定为预设的值。
```py
from functools import partial

def multiply(x, y):
    return x * y

# 创建一个新函数，将multiply函数的第二个参数固定为2
double = partial(multiply, 2)

print(double(4))  # 输出: 8
```
functools.reduce
reduce函数用于将一个二元操作函数累积地应用到可迭代对象的元素上，从而将可迭代对象缩减为单一的值。
```py
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)

print(result)  # 输出: 15
```

functools.total_ordering
total_ordering装饰器用于自动补全类的比较方法。如果你为类定义了__eq__和__lt__方法，total_ordering装饰器可以自动为你生成__le__、__gt__和__ge__方法。
```py
from functools import total_ordering

@total_ordering
class Product:
    def __init__(self, price):
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

p1 = Product(10)
p2 = Product(20)
p3 = Product(10)

print(p1 == p3)  # 输出: True
print(p1 < p2)   # 输出: True
print(p1 > p2)   # 输出: False
print(p1 >= p2)   # 输出: False
print(p1 <= p2)   # 输出: True
```
functools.lru_cache
lru_cache装饰器用于缓存函数的调用结果。它会存储最近的调用结果，当相同的参数再次出现时，可以直接返回缓存的结果，而不是重新计算。
```py
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # 输出: 55
```
functools.singledispatch
singledispatch装饰器用于创建泛函数。它允许你为不同的参数类型定义不同的函数实现。
```py
from functools import singledispatch

@singledispatch
def count(obj):
    print("Object:", obj)

@count.register
def _(obj: int):
    print("Integer:", obj)

@count.register
def _(obj: list):
    print("List:", obj)

count(1)       # 输出: Integer: 1
count([1, 2])  # 输出: List: [1, 2]
count("a")     # 输出: Object: a
```
# 如何判断一个值是函数还是方法?
inspect模块可以更准确地判断一个值是函数还是方法，特别是当涉及到类方法和静态方法时。需要注意的是，inspect.ismethod()只能用于判断实例方法，对于类方法和静态方法，需要使用inspect.isfunction()来判断。
```py
import inspect

def is_function(value):
    return inspect.isfunction(value)

def is_method(value):
    return inspect.ismethod(value)

# 示例
def my_function():
    pass

class MyClass:
    def my_method(self):
        pass

# 检查
print(is_function(my_function))  # 输出: True
print(is_method(MyClass.my_method))  # 输出: False
print(is_function(MyClass.my_method))  # 输出: True
print(is_method(MyClass().my_method))  # 输出: True

```
# lambda表达式格式以及应用场景？
在Python中，lambda表达式是一种创建匿名函数（即没有具体名称的函数）的简洁方式
lambda 参数列表: 表达式
应用在高阶函数参数上
sorted(numbers, key=lambda x: -x)

回调函数
# 使用map函数将列表中的每个元素乘以2
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # 输出: [2, 4, 6, 8, 10]

列表推导式
# 使用列表推导式和lambda表达式生成一个包含平方数的列表
squares = list(map(lambda x: x ** 2, range(10)))
print(squares)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

filter函数中
# 使用filter函数过滤出列表中的偶数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出: [2, 4, 6, 8, 10]

# pass的作用?
pass是一个空操作语句，它在语法上需要一个语句但程序逻辑上不需要执行任何操作时使用。pass语句通常用作占位符，以保持代码结构的完整性，直到你决定如何实现该部分代码。

# *arg和**kwarg作用?
args和**kwargs是两种特殊的参数，它们允许函数接收不定数量的参数。*args用于接收任意数量的位置参数，而**kwargs用于接收任意数量的关键字参数。
```py
def my_function(*args, **kwargs):
    print(args)   # 输出: (1, 2, 3)
    print(kwargs)   # 输出: {'a': 1, 'b': 2, 'c': 3}

my_function(1, 2, 3, a=1, b=2, c=3)
```
# 如何在函数中设置一个全局变量?
```py
# 定义一个全局变量
global_variable = 0
def update_global():
    global global_variable  # 声明要修改的是全局变量
    global_variable = 10  # 修改全局变量的值
    global global_var  # 声明一个全局变量
    global_var = 20

# 调用函数
update_global()

# 打印全局变量的值
print(global_variable)  # 输出: 10
print(global_var)   # 20

```
# 写出打印结果
```py
def func(a,b=[]):
    b.append(a)
    print(b)
func(1) #[1]
func(1) #[1,1]
func(1) #[1, 1, 1]
func(1) #[1, 1, 1, 1]

def func(a,b={}):
    b[a] = 'v'
    print(b)
func(1) # {1: 'v'}
func(2) # {1: 'v', 2: 'v'}
```
# 求结果: lambda
```py
def num():
    return [lambda x:i*x for i in range(4)]

print([m(2) for m in num()]) # [6,6,6,6]
```
# 简述 yield和yieldfrom关键字。
yield关键字用于生成器函数中，它暂停函数的执行，并返回一个值给调用者。当生成器的next()方法被调用时，函数会从上次yield的位置继续执行，直到遇到下一个yield语句或函数结束。
```py
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter))  # 输出: 1
print(next(counter))  # 输出: 2
```
yield from关键字用于生成器函数中，它用于将一个生成器的输出直接传递给另一个生成器。yield from后面跟一个可迭代对象，它会迭代这个对象，并将每个元素yield出来。
```py

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

def count_up_to_10(max):
    yield from count_up_to(max)
    yield max + 1

counter = count_up_to_10(5)
for num in counter:
    print(num)
```

# 请给出下面代码的输出结果?
```py

a = 1
def fun(a):
    a = 2
def fun(a):
    print(a)
a = []
def fun(a):
    a.append(1)
fun(a)
print(a) # [1]
```
# 全局变量和局部变量的区别，如何给function里面的一个全局变量赋值
区别:
作用域:
    全局变量:在函数外部定义的变量,可以在程序的任何地方修改和访问
    局部变量:在函数内部定义,只能在该函数内部访问和修改
生命周期:
    全局变量: 从定义开始直到程序结束
    局部变量: 从定义开始到函数执行结束
修改方式:
    全局变量: 在函数内部通过global 关键字修改
    局部变量: 在函数内部直接赋值修改
```py
# 定义一个全局变量
global_var = 0

def modify_global_var():
    global global_var   # 声明要修改的是全局变量
    global_var = 10    # 修改全局变量的值

# 调用函数
modify_global_var()

# 打印全局变量的值
print(global_var)   # 输出: 10
```
# 什么是lambda函数，下面这段代码的输出是什么
lambda函数是一个匿名函数,快速定义一个简单函数,只能包含一个表达式,不能包含复杂的语句(如循环,条件判断),配合高阶函数使用

```py

nums = range(2,20)
for i in nums:
    nums=filter(lambda x: x ==i or x % i,nums)
print(list(nums)) # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```
# 指出下面程序存在的问题
def Lastllindextem(src,index):
    return src.split("\")[-index]

1 字符串分割错误: 在Python字符串中，反斜杠\是一个转义字符，所以要表示一个字面上的反斜杠，你需要使用两个反斜杠\\。
2 索引可能越界: -1 表示列表的最后一个元素,-2表示倒数第二个元素.
3 函数命名表达不清楚.
4 返回值：如果index超出了分割后列表的范围，函数将抛出IndexError。通常，应该在函数中处理这种情况，例如通过返回None或抛出一个自定义的异常。

# 有一个数组[3,4,1,2,5,6,6,5,4,3,3]请写一个函数，找出该数组中没有重复的数的总和.(上面数据的没有重复的总和为1+2=3）
```py
list1 =[3,4,1,2,5,6,6,5,4,3,3]
def sum_of_unique_numbers(arr):
    count_dict = {}   # {3:2} 数字3 :出现次数
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1

    unique_sum = sum(num for num,count in count_dict.items() if count == 1)
    return unique_sum
print(sum_of_unique_numbers(list1))
print(sum_of_unique_numbers(list1))
```
# 求打印结果
arr = [1,2,3]
def bar():
    arr+=[5]
bar()
print(arr) # err

A. error   ✔
B. [5]
C. [1,2,3]
D. [1,2,3,4,5]

# 请写一个函数，计算出如下几个字母代表的数字
AB-CD=EF
EF+GH = PPP
# 这题不明白题意

# 请给出下面代码片段的输出
```py
def say_hi(func):
    def wrapper(*args, **kwargs):
        print("HI")
        ret = func(*args, **kwargs)
        print("BYE")
        return ret
    return wrapper

def say_yo(func):
    def wrapper(*args, **kwargs):
        print("YO")
        ret = func(*args, **kwargs)
        print("YO BYE")
        return ret
    return wrapper

@say_hi
@say_yo
def func():
    print("ROCK & ROLL")

func()

# HI
# YO
# ROCK & ROLL
# YO BYE
# BYE
```
# 请简述标准库中functools.wraps的作用
functools.wraps是一个装饰器，它用于将一个函数的元数据（如名称、文档字符串、注解等）复制到另一个函数上。
```py
from functools import wraps

def my_decorator(func):
    @wraps(func)

    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper

@my_decorator
def say_hello(name):
    """Greet someone with a simple hello."""
    print(f"Hello, {name}!")

# 使用装饰器后的函数
print(say_hello.__name__)  # 输出: say_hello
print(say_hello.__doc__)  # 输出: Greet someone with a simple hello.

```

# 请给出下面代码片段的输出?
```py
def test():
    try:
        raise ValueError("something wrong")  #抛出异常
    except ValueError as e: # 捕获异常 所以上面错误不会输出.
        print("Error occurred")
        return
    finally:   #最终都会执行这里
        print("Done")
test()
#Error occurred
#Done
```
# 下面的函数，哪些会输出1,2,3三个数字
```py
for i in range(3): # 0 1 2
    print(i)

alist = [0,1,2]
for i in alist:
    print(i+1)  #1 2 3

i= 1
while i<3:
    print(i)  # 1 2
    i+=1

for i in range(3):
    print(i+1) # 1 2 3
```

# 以下函数需要在其中引用一个全局变量k，请填写语句
def fun():
    global k  #填写的语句
    k = k+1

# 写出程序的输出结果.
```py
my_dict = {'a':0,'b':1}

def func(d):
    d["a"] =1
    return d

func(my_dict)  # my_dict : {'a':1,'b':1}
my_dict['c']=2 #  my_dict : {'a':1,'b':1,'c':2}
print(my_dict)
```
# 请把以下函数转化为python lambda匿名函数
def add(x,y):
    return x+y
```py
a = lambda x,y : x+y
print(a(1,3))
```
# def(a,b=[])这种写法有什么陷阱？
在Python中，函数参数默认值只在函数定义时计算一次，而不是在每次调用函数时计算。这意味着，如果默认值是一个可变对象（如列表、字典、集合等），那么每次调用函数时，如果未提供该参数，都会使用同一个默认对象的实例。
```py
def append_to_element(element, target=[]):
    target.append(element)
    return target

# 第一次调用函数，使用默认的空列表
print(append_to_element('a'))  # 输出: ['a']

# 第二次调用函数，仍然使用同一个列表
print(append_to_element('b'))  # 输出: ['a', 'b']

# 第三次调用函数，再次使用同一个列表
print(append_to_element('c'))  # 输出: ['a', 'b', 'c']
```
# 看代码 输出什么?
```py

def add_end(l=[]):
    l.append('end')
    return l

print(add_end())  # ['end']
print(add_end())  # ['end', 'end']
```
# 函数参数*args,**kwargs的作用是什么
*args接收可变参数 ,**kwargs 可变关键字参数
在函数内部 args是元组, kwargs 是字典

# 可变参数定义*args,**kwargs的区别是什么?并且写出下边代码的输入内容
```py
def foo(*args, **kwargs):
    print("args=",args)
    print("kwargs=",kwargs)
    print("-----------------")

if __name__ == '__main__':
    foo(1,2,3)
    foo(a=1,b=2,c=3)
    foo(1,2,3,4,a=1,b=2,c=3)
    foo("a",1,None,a=1,b="2",c=3)

# args= (1, 2, 3)
# kwargs= {}
# -----------------
# args= ()
# kwargs= {'a': 1, 'b': 2, 'c': 3}
# -----------------
# args= (1, 2, 3, 4)
# kwargs= {'a': 1, 'b': 2, 'c': 3}
# -----------------
# args= ('a', 1, None)
# kwargs= {'a': 1, 'b': '2', 'c': 3}
# -----------------
```
# 请写出log实现（主要功能时打印函数名）
```py
def log(func):
    def wrapper(*args, **kwargs):
        print('call now()')
        return func()
    return wrapper


@log
def now():
    print("2013-12-25")

now()
```
# Python 如何定义一个函数
A. class <name>(<Type> argl,<type> arg2, ……)
B. function <name>(argl,arg2,...)
C. def<name>(arg1, arg2,………)   ✔
D. def<name>(<type> argl, <type> arg2...)

# 选择代码运行的结果
```py
country_counter = {}

def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1

addone("China")
addone("Japan")
addone("china")
print(len(country_counter)) # 3

```
A. 0
B. 1
C. 2
D. 3  ✔
E. 4

# 选择输出结果
```py
def doff(arg1,*args):
    print(type(args))  # <class 'tuple'>
doff("applea","bananas","cherry")
```
A. str
B. int
C. tuple  ✔
D. list
E. dict

# 下面程序的输出结果是?
```py
d = lambda p: p * 2
t = lambda p: p * 3

x = 2
x = d(x)  # 4
x = t(x)  # 12
x = d(x)  # 24
print(x)

```
# 以下代码输出是什么，请给出答案并解释。请修改multipliers的定义来产生期望的结果
def multipliers():
    return [lambda x: x*i for i in range(4)]
print([m(2) for m in multipliers()])

当前代码的输出是 [6, 6, 6, 6]。
这是因为multipliers函数返回了一个列表，其中包含四个lambda函数。这些lambda函数都引用了同一个变量i，而i是在multipliers函数的for循环中定义的。
由于Python中的闭包特性，这些lambda函数捕获了i的引用，而不是在for循环中每次迭代时i的值。
当multipliers函数返回后，i的值为3（因为range(4)生成的是0, 1, 2, 3），
所以当调用这些lambda函数时，它们都使用了i的最终值3。
```py
# def multipliers():
#     return [lambda x: x*i for i in range(4)]  # [lambda,lambda,lambda,lambda] 是引用i,最终值i是3
# print([m(2) for m in multipliers()])

# 为了得期望结果 [0,2,6,12]
# 在定义lambda函数时捕获i的当前值
def multipliers():
    return [lambda x, i=i: x * i for i in range(4)]

print([m(2) for m in multipliers()])

```
# 有 0<x<=10,10<x<=20,20<x<=30,...,190<x<=200,200<x
这样的21个区间分别对应1-21 二十一个级别，请编写一个函数level(x)根据输入数值返回对应级别。
```py
def level(x):
    # 定义一个字典，其中键是区间，值是对应的级别
    switcher = {
        (0, 10): 1,
        (10, 20): 2,
        (20, 30): 3,
        (30, 40): 4,
        (40, 50): 5,
        (50, 60): 6,
        (60, 70): 7,
        (70, 80): 8,
        (80, 90): 9,
        (90, 100): 10,
        (100, 110): 11,
        (110, 120): 12,
        (120, 130): 13,
        (130, 140): 14,
        (140, 150): 15,
        (150, 160): 16,
        (160, 170): 17,
        (170, 180): 18,
        (180, 190): 19,
        (190, 200): 20,
        (200, float('inf')): 21,
    }
    # 遍历字典，检查输入的数值x是否在某个键（区间）内
    for key, value in switcher.items():
        if x>key[0] and x<=key[1]:
            return value
    # 如果输入的数值不在任何区间内，返回错误信息
    return "Value out of range"

# 测试函数
print(level(5))     # 应该返回 1
print(level(15))    # 应该返回 2
print(level(25))    # 应该返回 3
print(level(195))   # 应该返回 20
print(level(205))   # 应该返回 21
print(level(200))   # 应该返回 20

```

# 写函数
# 有一个数据结构如下所示，请编写一个函数从该结构数据中返回由指定的字段和对应的值组成的字典。如果指定字段不存在，则跳过该字段。
```py
data= {
    "time":"2016-08-005T13:13:05",
    "some_id":"ID1234",
    "grp1":{"fld1":1,"fld2":2},
    "xxx2":{"fld3":0,"fld4":0.4,},
    "fld6":11,
    "fld7":7,
    "fld46":8
}
# fields:由"|" 连接的以fld开头的字符串,如fld2|fld7|fld29
def select(data :dict):
    list_str=[]
    for key in data.keys():
        if key.startswith("fld"):
            list_str.append(key)
        if isinstance(data[key],dict):
            for key in data[key].keys():
                if key.startswith("fld"):
                    list_str.append(key)
    return "|".join(list_str)

print(select(data)) # fld1|fld2|fld3|fld4|fld6|fld7|fld46
```
# 补全代码:若要将N个task分配给N个worker同时去完成，每个worker分别都可以承担这N个task,但费用不同,下面的程序用回溯法计算总费用最小的一种工作分配方案，在该方案中，为每个worker分配1个task.程序中，N个task从0开始顺序编号，N个worker也从o开始顺序编号，主要的变量说明如下：
- ci：将任务i分配给worker j的费用
- task[i]：值为0表示task  i未分配，值为j表示task,i分配给worker j
- worker[k]值为o表示未分配task,值为1表示worker k已分配task;
- mincost：最小总费用


'''






