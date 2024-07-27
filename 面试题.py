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



'''


