# 爬虫, 算法,数据结构

## python 实现冒泡算法

冒泡排序是一种简单的排序算法，它重复地遍历要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。遍历数列的工作是重复进行直到没有再需要交换，也就是说该数列已经排序完成。

以下是使用Python实现冒泡排序的示例代码：

```python
def bubble_sort(arr):
    n = len(arr)  # 7
    # 遍历所有数组元素
    for i in range(n): # 0 - 6
        # Last i elements are already in place
        for j in range(0, n-i-1):  # 0 - (7-0-1)
            # 遍历数组从0到n-i-1
            # 交换如果找到的元素大于下一个元素
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# 测试冒泡排序函数
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array is:", sorted_arr)
```

### 算法解释

- **外层循环**：外层循环控制排序的轮数，对于有`n`个元素的数组，需要进行`n-1`轮排序。
- **内层循环**：内层循环负责在每一轮中进行相邻元素的比较和交换。每一轮排序后，最大的元素会被放置在正确的位置。
- **交换操作**：如果当前元素比下一个元素大，则交换它们的位置。

### 性能分析

- **时间复杂度**：冒泡排序的时间复杂度为`O(n^2)`，其中`n`是数组的长度。这是因为需要进行`n-1`轮比较，每轮比较最多进行`n-1`次比较。
- **空间复杂度**：冒泡排序的空间复杂度为`O(1)`，因为它只需要常数级别的额外空间。

冒泡排序是一种简单直观的排序算法，但它的效率较低，特别是对于大数据集来说。在实际应用中，通常会使用更高效的排序算法，如快速排序、归并排序等。

## 输入一个整数n，输出所有和为n连续正数序列

例如输入15，由于1+2+3+4+5和4+5+6和7+8都等于15，所以应该输出3个连续序列：

```
1-5
4-6
7-8

```

基本思路: 

- 使用两个指针，一个指向序列的起始位置，另一个指向序列的结束位置。
- 我们从1开始，逐步增加结束位置的指针，同时计算当前序列的和。
- 如果和小于n，我们继续增加结束位置的指针；如果和大于n，我们增加起始位置的指针；
- 如果和等于n，我们就找到了一个序列。

以下是Python代码实现：

```python
def findContinuousSequence(n):
    result = []
    start, end = 1, 2
    current_sum = 3  # 1+2

    while start < end:
        if current_sum == n:
            result.append((start, end))
            current_sum -= start
            start += 1
        elif current_sum < n:
            end += 1
            current_sum += end
        else:
            current_sum -= start
            start += 1

    return result

# 测试代码
n = 15
print(findContinuousSequence(n))
```

这段代码会输出所有和为n的连续正整数序列。例如，对于输入15，它会输出：

```
[(1, 5), (4, 6), (7, 8)]
```

这表示连续正整数序列1-5、4-6和7-8的和都等于15。



## 给定两个listA,B,请用Python找出A,B中相同的元素，A,B中不同的元素.

要找出两个列表A和B中相同的元素和不同的元素，可以使用Python的集合操作。以下是实现这一功能的代码：

```python
# 假设A和B是两个列表
A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7]

# 使用集合找出相同的元素
common_elements = list(set(A) & set(B))

# 使用集合找出不同的元素
unique_to_A = list(set(A) - set(B))
unique_to_B = list(set(B) - set(A))

print("相同的元素:", common_elements)
print("A中独有的元素:", unique_to_A)
print("B中独有的元素:", unique_to_B)
```

这段代码首先将列表A和B转换为集合，然后使用集合的交集操作找出两个列表中相同的元素，使用差集操作找出A中独有的元素和B中独有的元素。最后，将结果转换回列表形式并打印出来。

运行这段代码，你将得到以下输出：

```
相同的元素: [3, 4, 5]
A中独有的元素: [1, 2]
B中独有的元素: [6, 7]
```

这样，我们就成功地找出了两个列表中相同的元素和不同的元素。



### 下列叙述中错误的是：

```
A. 栈是线性结构
B.队列是线性结构
C.线性列表是线性结构
D.二叉树是线性结构      # 错误的
```

选项D“二叉树是线性结构”是错误的。二叉树不是线性结构，而是一种非线性数据结构。线性结构的特点是数据元素之间是一对一的关系，而二叉树的数据元素之间是一对多的关系，每个节点最多有两个子节点（左子节点和右子节点）。



## 一个栈的输入序列为1,2,3,4,5,则下列序列中不可能是栈的输出序列的是：

```
A. 1 5 4 3 2
B. 2 3 4 1 5
c. 1 5 4 2 3
D. 2 3 1 4 5
```

1. 对于选项 A：
   - 入栈顺序是 1,2,3,4,5。
   - 先 1 入栈，然后 1 出栈，此时栈为空；接着 2,3,4,5 依次入栈，然后 5 出栈，4 出栈，3 出栈，2 出栈，可以得到 1 5 4 3 2 的输出序列。
2. 对于选项 B：
   - 2 3 4 1 5 的输出序列是可行的。
   - 先 1,2 入栈，2 出栈；然后 3 入栈，3 出栈；接着 4 入栈，4 出栈；1 出栈，最后 5 入栈并出栈。
3. 对于选项 C：
   - 1 入栈然后 1 出栈；接着 2,3,4,5 入栈，此时 5 出栈，4 出栈，此时栈内元素从栈顶到栈底是 3,2，接下来不可能是 2 出栈后再 3 出栈，所以 1 5 4 2 3 不可能是栈的输出序列。
4. 对于选项 D：
   - 先 1,2 入栈，2 出栈；接着 3 入栈，3 出栈；1 出栈；然后 4 入栈，4 出栈, 5 入栈，5 出栈，，能得到 2 3 1 4 5 的输出序列。

综上所述，答案是 C。



## 判断一个字符串是否是IP

要判断一个字符串是否是有效的IP地址，可以使用Python的`ipaddress`模块。这个模块提供了处理IPv4和IPv6地址的功能。以下是一个简单的函数，用于检查字符串是否是有效的IPv4地址：

```python
import ipaddress


def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


# 测试
print(is_valid_ip('192.168.1.1'))  # 应该返回True
print(is_valid_ip('256.256.256.256'))  # 应该返回False
```

这个函数尝试将输入的字符串转换为`ipaddress.ip_address`对象。如果转换成功，说明字符串是一个有效的IP地址；如果抛出`ValueError`异常，则说明字符串不是有效的IP地址。



## 无重复字符串的最长子串，返回最长的长度

Python函数实现：

```python
def length_of_longest_substring(s):
    char_index_map = {}
    start = 0
    max_length = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)

     return max_length

# 测试
print(length_of_longest_substring("abcabcbb"))   # 应该返回3
print(length_of_longest_substring("bbbbb"))      # 应该返回1
print(length_of_longest_substring("pwwkew"))     # 应该返回3
```

这个函数使用一个字典`char_index_map`来记录字符最后出现的位置。`start`变量表示当前考虑的子串的起始位置。遍历字符串，如果遇到一个字符已经在字典中，并且其位置大于或等于`start`，则更新`start`到该字符上一次出现位置的下一个位置。每次迭代都更新`max_length`为当前子串长度和之前记录的最大长度之间的较大值。

这样，函数最终返回无重复字符的最长子串的长度。



## 给定一个只包括'(',')','{','}','[',']'的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。

左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

示例：输入："()[]{}"输出：true

```py
def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack


# 测试
print(isValid("()"))  # 应该返回True
print(isValid("()[]{}"))  # 应该返回True
print(isValid("(]"))  # 应该返回False
print(isValid("([)]"))  # 应该返回False
print(isValid("{[]}"))  # 应该返回True

```



## 给定一个已按照升序排列的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值index1和index2，其中 index1必须小于index2。

说明：返回的下标值（index1和 index2）不是从零开始的。

你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例：

输入:numbers=[2,7,11,15],target=9

输出：[1,2]解释：2与7之和等于目标数9。因此index1=1,index2=2。

```
定义两个指针，left指针指向列表的开头，right指针指向列表的末尾
while循环：
        如果两指针指向的数字之和大于0，right指针-1
        如果两指针指向的数字之和小于0，left指针+1
        如果两指针指向的数字等于0，right指针-1，left指针+1，并将指向的结果记录下来
        直到两指针交叉
```



我们可以使用一个简单的双指针方法。由于数组是有序的，我们可以从数组的两端开始，一个指针指向数组的开始位置，另一个指针指向数组的结束位置。然后，根据两个指针所指向的元素之和与目标值的比较结果，移动指针来寻找和为目标值的两个数。

以下是Python代码实现：

```python
def twoSum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# 测试代码
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # 输出应该是 [1, 2]
```

这段代码会返回一个列表，其中包含两个数的索引（从1开始计数），这两个数的和等于目标值。例如，对于输入`nums = [2, 7, 11, 15]`和`target = 9`，输出应该是`[1, 2]`，因为`nums[0] + nums[1] = 2 + 7 = 9`。



## 两个队列实现栈

要使用两个队列实现栈的功能，可以遵循以下步骤：

1. 1.**入栈（push）操作**：将元素添加到第一个队列中。

2. 2.**出栈（pop）操作**：将第一个队列中的所有元素（除了最后一个元素）移动到第二个队列中，然后返回第一个队列的最后一个元素作为栈顶元素。之后，交换两个队列的角色，以便下一个出栈操作可以使用。

以下是Python代码实现：

```python
from collections import deque

class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        # 压栈
        self.queue1.append(x)

    def pop(self):
        # 出栈
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        result = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def top(self):
        # 查看栈顶元素值
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        result = self.queue1[0]
        self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def empty(self):
        return len(self.queue1) == 0

# 测试代码
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())    # 输出应该是 2
print(stack.pop())    # 输出应该是 2
print(stack.empty())  # 输出应该是 False
```

这段代码定义了一个`MyStack`类，它使用两个队列来模拟栈的行为。`push`方法将元素添加到第一个队列中，`pop`方法将第一个队列中的元素移动到第二个队列中，只留下最后一个元素作为栈顶元素返回。`top`方法与`pop`方法类似，但会将最后一个元素放回第一个队列中。`empty`方法检查栈是否为空。



## 链表倒置

链表倒置（也称为链表反转）是将链表中的节点顺序颠倒的过程。在Python中，可以使用迭代或递归的方法来实现链表的倒置。以下是使用迭代方法的示例代码：



```py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev = None
    current = head
    while current:
        next_temp = current.next  # 保存下一个节点
        current.next = prev  # 反转当前节点的指针
        prev = current  # 移动prev和current指针
        current = next_temp
    return prev  # 新的头节点


# 测试代码
# 创建链表 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# 反转链表
new_head = reverseList(head)

# 打印反转后的链表
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

```





这段代码定义了一个`ListNode`类来表示链表节点，并实现了一个`reverseList`函数来反转链表。在`reverseList`函数中，我们使用三个指针：`prev`（指向当前节点的前一个节点），`current`（指向当前节点），和`next_temp`（临时保存下一个节点）。通过迭代遍历链表，逐个反转节点的指针方向，最终返回新的头节点。

运行测试代码，将输出反转后的链表：`4 -> 3 -> 2 -> 1 -> None`。



## 烫手山芋游戏介绍：6个孩子围城一个圈，排列顺序孩子们自己指定。第一个孩子手里有一个烫手的山芋，需要在计时器计时1秒后将山芋传递给下一个孩子，依次类推。规则是，在计时器每计时7秒时，手里有山芋的孩子退出游戏。该游戏直到剩下一个孩子时结束，最后剩下的孩子获胜。请使用队列实现该游戏策略，排在第几个位置最终会获胜。

要使用队列实现烫手山芋游戏策略，我们可以模拟游戏过程。游戏开始时，所有孩子都排在队列中。每7秒，队列的前端（即当前持有山芋的孩子）将被移除，游戏继续进行，直到队列中只剩下一个孩子。

以下是使用Python实现的代码：

```python
from collections import deque
import time

def hot_potato(children):
    queue = deque(children)
    while len(queue) > 1:
        for _ in range(7):   # 每7秒传递一次山芋
            queue.append(queue.popleft())  # 山芋传递给下一个孩子
        queue.popleft()  # 计时7秒后，当前持有山芋的孩子退出游戏
    return queue[0]  # 返回最后剩下的孩子

# 假设有6个孩子，编号为1到6
children = list(range(1, 7))
winner = hot_potato(children)
print(f"排在第{winner}个位置的孩子最终会获胜。")
```

这段代码首先创建一个队列，包含所有孩子的编号。然后，它模拟每7秒传递一次山芋的过程，直到队列中只剩下一个孩子。最后，返回最后剩下的孩子的编号。

运行这段代码，将输出最后获胜的孩子的编号。例如，如果输出是`排在第3个位置的孩子最终会获胜。`，这意味着编号为3的孩子最终会获胜。



## 爬虫面试题

### 1 掌握哪些基于爬虫的网络请求模块?

1. 1.**requests**：最流行的HTTP库之一，用于发送各种HTTP请求。它支持GET、POST、PUT、DELETE等请求方法，并且可以处理请求和响应的头部、参数、编码等。

2. 2.**urllib**：Python标准库中的一个模块，用于处理URL。它包含多个子模块，如`urllib.request`用于发送网络请求，`urllib.parse`用于解析URL，`urllib.error`用于处理请求错误。

3. 3.**aiohttp**：一个异步HTTP客户端/服务器框架，用于异步网络请求。它支持异步GET、POST等请求，适用于需要高并发处理的场景。

### 2.常见的数据解析方式

re,bs4,xpath,pyquery

- html解析   **beautifulsoup4**

- re 正则表达式

- xpath   支持XPath表达式 可以用来在HTML或XML文档中查找特定的元素

- **lxml**：除了HTML和XML解析外，lxml也支持XML的解析。

- pyquery  依赖于 `lxml` 或 `xml.etree.ElementTree` 作为解析器，因此在安装 `pyquery` 时，可能需要同时安装这些库。

  

### 3.列举在爬虫过程中遇到的哪些比较难的反爬机制

  -js加密,js混淆,cookie,代理

- 许多网站使用javascript 动态加载内容
- IP封禁
- -js加密,js混淆
- 速率限制



### 4.概述如何抓取动态加载数据

-基于抓包工具进行全局搜索

-如果数据加密了，搜索不到。



### 5.移动端数据抓取

-常用的抓包工具：fiddle,miteproxy

-教程：https://www.cnblogs.com/bobo-zhang/p/10068994.html

### 7.了解哪些爬虫框架？

- scrapy, pyspider

### 8.谈谈对scrapy的了解

-异步的框架，异步的实现是基于twisted 实现

-五大核心组件的工作流程

-常用的功能：

​				-管道，中间件

9.如何解析出携带标签的局部页面数据

- \<a>八佰\</a>,    使用bs4

### 10.scrapy核心组件之间的工作原理

Scrapy是一个快速、高层次的Web爬取和Web抓取框架，用于抓取网站并从页面中提取结构化的数据。Scrapy的核心组件包括：

1. 1.**Scrapy Engine（引擎）**：负责控制数据流在系统中所有组件之间的流动，并在不同组件间触发事件。

2. 2.**Scheduler（调度器）**：负责接收引擎发过来的请求，并按照一定的顺序（如先进先出）调度这些请求。

3. 3.**Downloader（下载器）**：负责下载Scrapy Engine发送的所有请求，并将下载的响应返回给引擎，然后引擎将响应传递给Spider。

4. 4.**Spider（爬虫）**：用户编写用于解析响应并提取数据的代码。Spider是Scrapy的核心，负责解析响应并生成Item和新的请求。

5. 5.**Item Pipeline（项目管道）**：负责处理由Spider生成的Item。典型的处理包括清理、验证和存储数据到数据库。

6. 6.**Downloader Middlewares（下载器中间件）**：位于Scrapy Engine和Downloader之间的组件，负责处理Engine发送给Downloader的请求和从Downloader返回的响应。

7. 7.**Spider Middlewares（爬虫中间件）**：位于Scrapy Engine和Spider之间的组件，负责处理Engine发送给Spider的请求和从Spider返回的Item和新的请求。

#### 工作原理

- **启动爬虫**：用户启动Scrapy爬虫，Scrapy Engine开始处理第一个Spider定义的URL。
- **请求调度**：Engine将请求传递给Scheduler，Scheduler将请求排队并按顺序调度。
- **下载响应**：Engine从Scheduler获取请求并传递给Downloader，Downloader下载响应并返回给Engine。
- **解析响应**：Engine将下载的响应传递给Spider，Spider解析响应并生成Item和新的请求。
- **处理Item和请求**：Engine将Item传递给Item Pipeline进行处理，同时将新的请求传递给Scheduler进行调度。
- **中间件处理**：在请求和响应的传递过程中，Engine会通过下载器中间件和爬虫中间件进行处理。

#### 总结

Scrapy通过其核心组件的协同工作，实现了高效的数据抓取和处理。每个组件都有明确的职责，通过Scrapy Engine的协调，整个爬虫系统能够高效地运行。用户可以通过自定义Spider和Item Pipeline来实现特定的数据抓取和处理逻辑，而下载器中间件和爬虫中间件则提供了扩展点，允许用户在请求和响应的处理过程中进行自定义操作。

### 11.scrapy中间件的应用

-种类（2个）

-作用

-类中常用的方法

### 12.如何实现全站数据爬取

- crawlSpider

### 13.如何检测网站数据更新？

-增量式

### 14.分布式实现原理

-分布式机群共享调度器和管道即可

### 15.如何提升爬取数据的效率（异步爬虫）

-线程池，多任务的异步协程，框架

### 16.列举你接触的反爬机制

-10种

### 18.scrapy如何实现持久化存储

-两种方式：管道，终端指令

### 19.谈谈对crawlspider的理解

-链接提取器&规则解析器

### 22 在爬虫中为什么需要是用 selenium? selenium和爬虫之间的关联是什么？

-爬取动态加载数据-实现模拟登录

### 23列举你所熟知的 selenium模块中的常用方法及其作用

#### 1. 初始化WebDriver

- `webdriver.Chrome()`：启动Chrome浏览器。
- `webdriver.Firefox()`：启动Firefox浏览器。
- `webdriver.Ie()`：启动Internet Explorer浏览器。
- `webdriver.Edge()`：启动Edge浏览器。

#### 2. 导航

- `driver.get(url)`：访问指定的URL。
- `driver.forward()`：向前导航到下一页。
- `driver.back()`：返回上一页。
- `driver.refresh()`：刷新当前页面。

#### 3. 元素操作

- `driver.find_element_by_id(id)`：通过ID查找元素。
- `driver.find_element_by_name(name)`：通过name属性查找元素。
- `driver.find_element_by_xpath(xpath)`：通过XPath查找元素。
- `driver.find_element_by_link_text(text)`：通过链接文本查找元素。
- `driver.find_element_by_partial_link_text(text)`：通过部分链接文本查找元素。
- `driver.find_element_by_tag_name(tag_name)`：通过标签名查找元素。
- `driver.find_element_by_class_name(class_name)`：通过类名查找元素。
- `driver.find_elements_by_*`：查找多个元素，返回元素列表。

#### 4. 输入操作

- `element.send_keys(keys)`：向元素发送键盘输入。
- `element.clear()`：清除元素中的内容。

#### 5. 等待操作

- `WebDriverWait(driver, timeout)`：等待直到某个条件成立。
- `expected_conditions`：提供了一系列预定义的等待条件，如`element_to_be_clickable`、`presence_of_element_located`等。

#### 6. 截图

- `driver.save_screenshot(filename)`：保存当前页面的截图。

#### 7. 关闭和退出

- `driver.close()`：关闭当前窗口。
- `driver.quit()`：退出WebDriver，关闭所有窗口。

#### 8. JavaScript执行

- `driver.execute_script(script, *args)`：执行JavaScript代码。

示例代码

```py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 启动浏览器
driver = webdriver.Chrome()

# 访问网页
driver.get("http://www.example.com")

# 查找元素并发送输入
elem = driver.find_element_by_id("kw")
elem.send_keys("selenium")

# 点击搜索按钮
elem.send_keys(Keys.RETURN)

# 等待元素可点击
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "su")))

# 执行JavaScript
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 截图
driver.save_screenshot("example.png")

# 关闭浏览器
driver.quit()
```



### 24解释在多任务异步协程中事件循环(loop)的作用是什么?

- 装载多个任务对象

- 可以让多个任务对象异步执行

### 25多任务异步协程是如何实现异步的?

- await关键字，wait方法

### 26.验证码如何处理?

- 打码平台

### 27.scrapy 和 scrapy-redis有什么区别?

```
Scrapy和scrapy-redis是两个不同的Python库，它们在Web爬取和数据抓取方面有不同的用途和特点。

Scrapy
Scrapy是一个快速、高层次的Web爬取和Web抓取框架，用于抓取网站并从页面中提取结构化的数据。Scrapy使用异步IO来提高爬取速度，支持多种数据提取方式，如XPath、CSS选择器等，并且具有强大的中间件和管道系统，可以方便地进行数据处理和存储。

Scrapy的主要特点包括：

高效的异步IO处理
强大的选择器系统
中间件和管道系统
支持多种数据存储方式，如数据库、文件等
可扩展性强，支持自定义组件
scrapy-redis
scrapy-redis是一个基于Redis的Scrapy扩展，它使用Redis作为队列和去重存储。scrapy-redis的主要目的是为了提高Scrapy爬虫的可扩展性和容错性，特别是在分布式爬取场景中。

scrapy-redis的主要特点包括：

使用Redis作为调度器（Scheduler）、去重存储（Item Pipeline）和请求队列
支持分布式爬取，可以轻松地在多台机器上部署爬虫
提供了基于Redis的去重机制，避免重复爬取相同的URL
支持持久化任务，即使爬虫重启，任务也不会丢失
区别总结
架构和存储：Scrapy使用内存和文件系统进行数据存储和请求调度，而scrapy-redis使用Redis数据库。
分布式爬取：scrapy-redis支持分布式爬取，Scrapy则需要额外的配置和组件来实现。
去重机制：scrapy-redis使用Redis的集合来实现去重，Scrapy则通过Item Pipeline和中间件实现。
容错性：scrapy-redis由于使用Redis，具有更好的容错性和任务持久化能力。
在选择使用Scrapy还是scrapy-redis时，需要根据项目需求和环境来决定。如果项目需要分布式爬取和高容错性，scrapy-redis可能是一个更好的选择。如果项目规模较小，或者不需要分布式爬取，Scrapy则可能更合适。


```



### 29.列出你知道header的内容以及信息

- Connection: keep-alive 或者closed，

- Referer:如果没有请求到数据，将该请求头作用到headers 中即可
