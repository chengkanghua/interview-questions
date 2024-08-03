# 前端



## 什么是css初始化 ? 有什么好处?

CSS初始化（CSS Reset）是指在开始编写CSS样式之前，先重置所有浏览器默认的CSS样式，以消除不同浏览器之间的默认样式差异。这通常通过引入一个CSS重置样式表来实现，该样式表包含了一系列的CSS规则，用于将所有HTML元素的默认样式设置为统一的初始状态。

### CSS初始化的好处

1. 1.**一致性**：通过重置浏览器默认样式，可以确保网页在不同浏览器中具有一致的外观和行为。

2. 2.**可控性**：初始化CSS后，开发者可以完全控制网页的样式，从一个干净的起点开始设计样式，而不是从浏览器的默认样式开始。

3. 3.**减少样式冲突**：不同的浏览器可能有不同的默认样式，CSS初始化有助于避免这些默认样式之间的冲突。

4. 4.**提高开发效率**：使用CSS初始化可以避免在开发过程中反复调整和修复因浏览器默认样式引起的样式问题，从而提高开发效率。

5. 5.**跨浏览器兼容性**：CSS初始化有助于解决跨浏览器兼容性问题，因为所有浏览器的默认样式都被重置到一个统一的状态。

### 常见的CSS初始化库

- **Normalize.css**：一个现代的、更加细致的CSS重置库，它保留了一些有用的默认样式，同时修复了浏览器的bug和不一致之处。
- **Reset.css**：一个更为彻底的CSS重置库，它几乎移除了所有元素的默认样式，让开发者从零开始设计样式。

### 使用方法

通常，你可以通过在HTML文档的`<head>`部分引入一个CSS初始化库来实现CSS初始化：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 引入CSS初始化库 -->
    <link rel="stylesheet" href="path/to/normalize.css">
</head>
<body>
    <!-- 页面内容 -->
</body>
</html>
```

通过使用CSS初始化，你可以确保网页在不同浏览器中具有一致的外观和行为，同时提高开发效率和样式控制的精确度。



## 简述浮动的特征和清除浮动的方法？

### 浮动的特征

1. 1.**脱离文档流**：当元素应用了浮动（如`float: left`或`float: right`），它会脱离正常的文档流，不再占据原来的空间，而是浮动到容器的左侧或右侧。

2. 2.**影响布局**：浮动元素会影响周围元素的布局，因为它们不再占据空间，可能导致后续元素环绕浮动元素显示。

3. 3.**高度塌陷**：浮动元素的父容器不会自动扩展其高度以包含浮动元素，这可能导致父容器高度塌陷。

### 清除浮动的方法

1. 1.**使用`clear`属性**：在浮动元素之后添加一个具有`clear`属性的元素（如`<div style="clear: both;"></div>`），可以防止后续元素环绕浮动元素。

2. 2.**使用伪元素清除浮动**：

3. ```css
   .clearfix::after {
       content: "";
       display: table;
       clear: both;
   }
   ```

4. 在父容器上添加`.clearfix`类，并使用伪元素`::after`来清除浮动。这种方法不会影响布局，是推荐的做法。

5. 3.**设置父容器的`overflow`属性**：

6. ```css
   .parent {
       overflow: auto;
   }
   ```

7. 

8.  通过设置父容器的`overflow`属性为`auto`或`hidden`，可以创建一个新的块格式化上下文（Block Formatting Context），从而包含浮动元素。

9. 4.**使用`<br clear="all" />`标签**：在HTML中，可以使用`<br clear="all" />`标签来清除浮动，但这种方法不推荐使用，因为它混合了样式和内容。



## JavaScript(或jQuery)如何选择一个id 为main的容器

```js
// 使用原生JavaScript
var mainContainer = document.getElementById('main');

// 使用jQuery
var mainContainer = $('#main');
```



## JavaScript(或jQuery)如何选择一个class为menu的容器

```js
// 使用原生JavaScript
var menuContainers = document.getElementsByClassName('menu');

// 使用jQuery
var menuContainers = $('.menu');
```



## 简述什么是浏览器时间流

浏览器时间流（Browser Event Loop）是浏览器中用于处理JavaScript代码执行和事件处理的机制。它允许JavaScript代码在单线程环境中异步执行，同时响应用户交互、网络请求和其他事件。浏览器时间流的关键概念包括事件队列（Event Queue）、宏任务（Macrotasks）和微任务（Microtasks）。

### 事件队列

事件队列是一个先进先出的队列，用于存放待处理的事件。当事件发生时（如用户点击、定时器到期、网络请求完成等），这些事件会被放入事件队列中等待处理。

### 宏任务

宏任务是事件队列中的任务类型之一，它们通常包括：

- 脚本执行（如`<script>`标签中的代码）
- 定时器（如`setTimeout`和`setInterval`）
- I/O操作
- 用户交互（如点击、滚动等）

### 微任务

微任务是另一种类型的事件队列任务，它们通常包括：

- `Promise`的回调函数
- `MutationObserver`的回调函数
- `process.nextTick`（Node.js环境）

### 浏览器时间流的工作流程

1. 1.**执行宏任务**：浏览器开始执行宏任务队列中的任务，直到队列为空。

2. 2.**执行微任务**：在每个宏任务执行完毕后，浏览器会检查并执行微任务队列中的所有任务，直到微任务队列为空。

3. 3.**渲染**：在执行完所有宏任务和微任务后，浏览器会进行渲染更新，如DOM变更、样式变更等。

4. 4.**重复步骤1-3**：浏览器继续监听事件队列，等待新的宏任务和微任务。

### 重要性

浏览器时间流机制对于理解JavaScript的异步编程模型至关重要。它解释了为什么某些代码会异步执行，以及如何控制代码的执行顺序。通过合理利用宏任务和微任务，开发者可以编写出更高效、响应性更强的Web应用。



## 用css如何隐藏一个元素

### 1. `display: none;`

将元素的`display`属性设置为`none`，这会使元素完全从文档流中消失，不仅隐藏了元素，还释放了该元素所占的空间。

```css
.hidden-element {
     display: none;
}
```

### 2. `visibility: hidden;`

将元素的`visibility`属性设置为`hidden`，这会使元素不可见，但它仍然占据原来的空间。

```css
.hidden-element {
     visibility: hidden;
}
```

### 3. `opacity: 0;`

通过设置元素的`opacity`属性为`0`，元素虽然不可见，但仍然占据空间。这种方法适用于需要元素在隐藏时仍保持在页面布局中的情况。

```css
.hidden-element {
     opacity: 0;
}
```

## 一行css实现padding上下左右分别为1px,2px,3px,4px

```
.element {
     padding: 1px 2px 3px 4px;
}
```



## 前后端分离的基本原理。

```
前后端分离是一种现代Web开发架构模式，它将前端（客户端）和后端（服务器端）的开发工作分开进行，使得它们可以独立开发、测试和部署。这种模式的核心在于前后端通过API接口进行数据交互，而不是传统的模板渲染方式。

基本原理
1.
独立开发：前端开发者和后端开发者可以使用不同的技术栈和开发工具，独立进行开发工作。前端开发者主要关注用户界面和用户体验，后端开发者则关注数据处理和业务逻辑。
2.
API接口：前后端通过定义好的API接口进行通信。前端通过HTTP请求（如GET、POST、PUT、DELETE等）向后端发送请求，并接收JSON或XML格式的数据作为响应。
3.
数据交互：前端使用JavaScript（或框架如React、Vue.js等）来处理用户交互，并通过AJAX（Asynchronous JavaScript and XML）技术与后端进行异步数据交互。
4.
前后端分离的优势：
提高开发效率：前后端可以并行开发，减少等待时间，提高开发效率。
技术栈灵活：前后端可以使用各自最适合的技术栈，提高开发质量。
易于维护和扩展：由于前后端分离，系统更易于维护和扩展。
前后端解耦：前端和后端的耦合度降低，使得系统更加灵活，便于应对需求变化。
实现方式
前端：使用HTML、CSS和JavaScript（或前端框架）构建用户界面，并通过AJAX调用后端API接口获取数据。
后端：使用服务器端语言（如Node.js、Python、Java等）和数据库技术（如MySQL、MongoDB等）处理业务逻辑和数据存储，并提供API接口供前端调用。
结论
前后端分离是现代Web开发中的一种流行架构模式，它通过API接口实现前后端的解耦，提高了开发效率和系统的可维护性。这种模式使得前端和后端可以独立开发和部署，适应了快速变化的Web开发需求
```





## 前后端分离的通信数据安全

```
前后端分离的通信数据安全是确保Web应用安全的关键部分。由于前后端通过API接口进行数据交互，因此需要采取一系列措施来保护数据传输的安全性。以下是一些常用的方法和最佳实践：

1. 使用HTTPS
加密传输：使用HTTPS协议代替HTTP协议，确保数据在传输过程中被加密，防止数据被截获或篡改。
证书验证：确保服务器的SSL/TLS证书有效且由受信任的证书颁发机构签发，以防止中间人攻击。
2. 数据加密
敏感数据加密：对敏感数据（如密码、个人信息等）在存储和传输前进行加密处理。
使用安全的加密算法：选择经过验证的安全加密算法，如AES、RSA等。
3. API安全
身份验证：实现身份验证机制，如OAuth、JWT（JSON Web Tokens）等，确保只有授权用户可以访问API。
权限控制：对API进行权限控制，确保用户只能访问他们被授权的数据和功能。
4. 输入验证
防止注入攻击：对所有输入数据进行验证，防止SQL注入、XSS攻击等。
使用参数化查询：在与数据库交互时使用参数化查询，避免直接将用户输入拼接到SQL语句中。
5. 输出编码
防止XSS攻击：对输出到HTML页面的数据进行适当的编码，防止跨站脚本攻击（XSS）。
6. 安全的API设计
API版本管理：合理设计API版本，避免因版本变更导致的安全漏洞。
限制请求频率：对API请求进行频率限制，防止恶意攻击和滥用。
7. 安全的会话管理
会话超时：设置合理的会话超时时间，防止会话劫持。
安全的Cookie属性：使用HttpOnly和Secure属性标记Cookie，防止跨站脚本攻击（XSS）和数据泄露。
8. 定期安全审计
代码审查：定期进行代码审查，检查潜在的安全漏洞。
安全测试：进行安全测试，如渗透测试，以发现和修复安全问题。
```



给ul设置样式为：背景色黑色，给ul下的ui设置样式为：宽度30px,背景红色

```css
ul {
  background-color: black;
}

ul li {
  width: 30px;
  background-color: red;
}
```



## 用bootstrap 写一个响应式栅格，一个页面分左右两栏，大屏情况下分6/6,小屏情况下分为12/12（大屏：屏幕>=992px,小屏;992px>=屏幕>=768px）

```html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bootstrap Grid Example</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
  <div class="container">
    <div class="row">
      <!-- 左侧栏 -->
      <div class="col-lg-6 col-md-12">
        <div class="card">
          <div class="card-body">
            左侧内容
          </div>
        </div>
      </div>
      <!-- 右侧栏 -->
      <div class="col-lg-6 col-md-12">
        <div class="card">
          <div class="card-body">
            右侧内容
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
```



### 解释

- `container`类用于包裹栅格系统，确保内容居中并有适当的边距。
- `row`类用于创建栅格行。
- `col-lg-6`表示在大屏幕（屏幕宽度大于或等于992px）下，该列占据12列中的6列。
- `col-md-12`表示在中等屏幕（屏幕宽度在768px到991px之间）下，该列占据12列中的全部12列。



## 写一个正则表达式获取HTML源码中的编码，如下的编码是；utf-8 怎么通过 Python 的 re模块获得？

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Title</title>
    </head>
</html>
```



```python
import re

html_source = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
</html>
"""

# 使用正则表达式匹配charset属性
match = re.search(r'<meta charset="([^"]*)"', html_source)
if match:
    encoding = match.group(1)
    print(f"HTML source encoding is: {encoding}")
else:
    print("No encoding found in HTML source.")
```



## 如何创建响应式布局?

建响应式布局通常涉及使用CSS框架（如Bootstrap）或自定义CSS来确保网页在不同设备和屏幕尺寸上都能良好显示。以下是创建响应式布局的基本步骤：

### 1. 使用媒体查询（Media Queries）

媒体查询允许你根据不同的屏幕尺寸应用不同的CSS样式。例如：



```css
/* 默认样式 */
.container {
     width: 100%;
}

/* 当屏幕宽度小于768px时 */
@media (max-width: 768px) {
     .container {
         width: 100%;
     }
}

/* 当屏幕宽度在768px到992px之间时 */
@media (min-width: 768px) and (max-width: 992px) {
     .container {
         width: 750px;
     }
}

/* 当屏幕宽度大于992px时 */
@media (min-width: 992px) {
     .container {
         width: 970px;
     }
}
```

### 2. 使用响应式框架

Bootstrap等前端框架提供了现成的响应式布局工具，如栅格系统。例如：



```html
<div class="container">
  <div class="row">
    <div class="col-md-4">Column 1</div>
    <div class="col-md-4">Column 2</div>
    <div class="col-md-4">Column 3</div>
  </div>
</div>
```

在Bootstrap中，`col-md-4`表示在中等屏幕尺寸（如桌面显示器）下，每列占据容器宽度的1/3。Bootstrap的栅格系统会自动调整列宽以适应不同屏幕尺寸。

### 3. 使用弹性盒子（Flexbox）

CSS的弹性盒子（Flexbox）布局模型提供了一种更灵活的方式来创建响应式布局：



```css
.container {
     display: flex;
     flex-wrap: wrap;
}

.container > div {
     flex: 1;
     min-width: 200px;
}
```

在这个例子中，`.container`使用`display: flex;`来启用弹性盒子布局，`flex-wrap: wrap;`允许子元素在必要时换行。每个子元素`div`使用`flex: 1;`来平均分配空间，并设置`min-width`以确保在小屏幕上也能保持一定的布局效果。

### 4. 使用视口单位

视口单位（如`vw`和`vh`）可以根据视口的大小来设置元素的尺寸，使布局更加灵活：



```css
.container {
     width: 100vw; /* 宽度为视口宽度 */
     height: 100vh; /* 高度为视口高度 */
}
```



## 你曾经使用过哪些前端框架？

 1.**React**：由Facebook开发，广泛用于构建用户界面的JavaScript库。它使用虚拟DOM来提高性能，并支持组件化开发。

2.**Vue.js**：一个渐进式JavaScript框架，用于构建用户界面。它易于上手，且具有灵活的组件系统。

 3.**Bootstrap**：一个流行的前端框架，用于快速开发响应式和移动优先的项目。它提供了一套丰富的组件和工具。

4.**jQuery**：虽然不是框架，但作为JavaScript库，它简化了HTML文档遍历、事件处理、动画和Ajax交互。



## 什么是ajax请求？并使用jQuery 和XMLHttpRequest对象实现一个 ajax 请求。

AJAX（Asynchronous JavaScript and XML）是一种在无需重新加载整个页面的情况下，能够更新部分网页的技术。它允许Web应用在后台与服务器交换数据，并在不中断用户操作的情况下更新页面。

```js

// 使用jQuery的$.ajax方法发送GET请求
$.ajax({
   url: 'https://api.example.com/data', // 请求的URL
   type: 'GET', // 请求类型，可以是GET或POST
   dataType: 'json', // 预期服务器返回的数据类型
   success: function(data) {
       // 请求成功时的回调函数
       console.log('Data received:', data);
   },
   error: function(xhr, status, error) {
       // 请求失败时的回调函数
       console.error('Request failed:', status, error);
   }
});
```

### 使用XMLHttpRequest对象实现AJAX请求

```js
// 创建XMLHttpRequest对象
var xhr = new XMLHttpRequest();

// 配置请求类型、URL和异步处理方式
xhr.open('GET', 'https://api.example.com/data', true);

// 设置请求成功时的回调函数
xhr.onload = function() {
   if (xhr.status >= 200 && xhr.status < 300) {
       // 请求成功，处理响应数据
       console.log('Data received:', JSON.parse(xhr.responseText));
   } else {
       // 请求失败，处理错误
       console.error('Request failed:', xhr.status);
   }
};

// 设置请求失败时的回调函数
xhr.onerror = function() {
   console.error('Request failed to complete');
};

// 发送请求
xhr.send();
```





## 如何在前端实现轮询？

在前端实现轮询通常是指定期向服务器发送请求，以获取最新的数据或状态更新。轮询可以通过JavaScript的`setInterval`函数实现，该函数允许你设置一个定时器，定期执行特定的函数。

### 使用原生JavaScript实现轮询

```js

// 设置轮询间隔时间（例如，每5秒轮询一次）
var pollingInterval = 5000;

// 轮询函数
function poll() {
    // 发送AJAX请求到服务器
    fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => {
        // 处理获取到的数据
        console.log('Received data:', data);
    })
    .catch(error => {
        // 处理错误情况
        console.error('Polling failed:', error);
    });
}

// 启动轮询
setInterval(poll, pollingInterval);
```

### 使用jQuery实现轮询

```js
// 设置轮询间隔时间（例如，每5秒轮询一次）
var pollingInterval = 5000;

// 轮询函数
function poll() {
    $.ajax({
        url: 'https://api.example.com/data',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            // 处理获取到的数据
            console.log('Received data:', data);
        },
        error: function(xhr, status, error) {
            // 处理错误情况
            console.error('Polling failed:', status, error);
        }
    });
}

// 启动轮询
setInterval(poll, pollingInterval);
```

### 使用vue

```vue
<template>
  <div>
    <p>数据: {{ data }}</p>
    <button @click="stopPolling">停止轮询</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: null,
      pollingInterval: null
    };
  },
  methods: {
    fetchAndUpdateData() {
      // 使用fetch API发送请求
      fetch('https://api.example.com/data')
        .then(response => response.json())
        .then(data => {
          this.data = data;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    startPolling() {
      // 设置轮询间隔时间（例如，每5秒轮询一次）
      this.pollingInterval = setInterval(this.fetchAndUpdateData, 5000);
    },
    stopPolling() {
      // 清除轮询定时器
      clearInterval(this.pollingInterval);
    }
  },
  mounted() {
    // 组件挂载后开始轮询
    this.startPolling();
  },
  beforeDestroy() {
    // 组件销毁前停止轮询
    this.stopPolling();
  }
};
</script>
```





## 如何在前端实现长轮询？

长轮询（Long Polling）是一种服务器端和客户端通信的技术，它允许服务器在有新数据时才发送响应给客户端，而不是客户端定期发送请求。长轮询通常用于实现实时通信，如聊天应用、实时通知等场景。

### 实现长轮询的基本步骤：

1. 1.**客户端发起请求**：客户端向服务器发送一个HTTP请求。

2. 2.**服务器延迟响应**：服务器收到请求后，不立即响应，而是等待有新数据或超时。

3. 3.**服务器响应数据**：一旦有新数据或超时，服务器将数据作为响应发送给客户端。

4. 4.**客户端处理数据**：客户端接收到数据后，进行处理（如更新界面、发送新的长轮询请求等）。

5. 5.**循环步骤**：客户端在处理完数据后，立即发起新的长轮询请求。



### 使用原生JavaScript实现长轮询

```js
function longPolling() {
  // 发送长轮询请求
  fetch('https://api.example.com/data', {
    method: 'GET',
    headers: {
      'Accept': 'application/json'
    }
  })
  .then(response => {
    if (response.ok) {
      return response.json();
    }
    throw new Error('Network response was not ok.');
  })
  .then(data => {
    // 处理数据
    console.log('Received data:', data);
    // 立即发起新的长轮询请求
    longPolling();
  })
  .catch(error => {
    // 处理错误情况
    console.error('Long polling failed:', error);
    // 短暂延迟后发起新的长轮询请求
    setTimeout(longPolling, 1000);
  });
}

// 启动长轮询
longPolling();
```

### 使用jQuery实现长轮询

```js
function longPolling() {
  $.ajax({
    url: 'https://api.example.com/data',
    type: 'GET',
    dataType: 'json',
    success: function(data) {
      // 处理数据
      console.log('Received data:', data);
      // 立即发起新的长轮询请求
      longPolling();
    },
    error: function(xhr, status, error) {
      // 处理错误情况
      console.error('Long polling failed:', status, error);
      // 短暂延迟后发起新的长轮询请求
      setTimeout(longPolling, 1000);
    }
  });
}

// 启动长轮询
longPolling();
```



## vuex的作用？

Vuex是Vue.js应用程序的状态管理模式和库。它提供了一种集中式存储管理应用的所有组件状态，并以相应的规则保证状态以一种可预测的方式发生变化。Vuex的主要作用包括：

### 1. 状态管理

在大型的Vue.js应用中，组件之间可能会共享很多状态（如用户登录信息、列表数据等）。Vuex允许你将这些共享状态抽取出来，以一个“store”（存储）的形式集中管理。这样，无论在应用的哪个组件中需要修改状态，都可以通过统一的接口进行操作。

### 2. 组件间状态共享

通过Vuex，可以轻松实现跨组件的状态共享。组件不需要直接相互传递状态，而是通过访问store中的状态来实现数据的共享。

### 3. 可预测的状态变更

Vuex通过其核心概念“mutation”来处理状态变更。所有的状态变更都是通过提交mutation来完成的，这样可以确保状态变更的可追踪性和可预测性。

### 4. 支持开发调试

Vuex提供了强大的开发工具，如Vue Devtools，它允许开发者在浏览器中检查和调试应用的状态，这对于大型应用的开发和维护非常有帮助。

### 5. 优化性能

Vuex通过其“getter”（获取器）功能，允许组件高效地读取状态。当store中的状态发生变化时，只有需要该状态的组件会重新渲染，从而优化了性能。

### 6. 代码组织和维护

使用Vuex可以使得应用的状态逻辑更加集中和模块化，这有助于代码的组织和维护，尤其是在大型项目中。

### 总结

Vuex是Vue.js应用中管理状态的重要工具，它通过集中式存储管理应用的所有组件状态，使得状态管理变得简单和高效。通过Vuex，可以轻松实现跨组件的状态共享，保证状态变更的可预测性，并优化应用的性能。同时，Vuex还提供了强大的开发工具，帮助开发者更好地调试和维护应用。





## vue 中的路由的拦截器的作用？

在Vue.js中，路由拦截器通常指的是使用Vue Router提供的导航守卫（Navigation Guards）功能。路由拦截器的作用是允许你在路由发生变化之前或之后执行一些逻辑，比如权限验证、数据加载、页面跳转前的确认等。

### Vue Router 导航守卫的类型

1. 1.**全局守卫**：全局守卫可以应用于所有的路由，包括`beforeEach`、`beforeResolve`和`afterEach`。

2. 2.**路由独享守卫**：可以为特定的路由配置守卫，如`beforeEnter`。

3. 3.**组件内守卫**：在组件内部定义的守卫，如`beforeRouteEnter`、`beforeRouteUpdate`和`beforeRouteLeave`。

### 路由拦截器的作用

1. 1.**权限验证**：在用户访问特定路由前进行权限检查，确保用户具有访问该路由的权限。

2. 2.**数据加载**：在进入路由前加载必要的数据，如从API获取数据，以确保页面加载时数据已经准备就绪。

3. 3.**页面跳转确认**：在用户尝试离开当前页面时，可以弹出确认对话框，防止用户不小心丢失未保存的数据。

4. 4.**记录日志**：记录用户的路由访问历史，用于分析用户行为或生成日志。

5. 5.**动态设置标题**：根据路由动态设置页面标题。

6. 6.**条件性重定向**：根据某些条件（如用户登录状态）重定向到不同的路由。

7. ### 示例：全局前置守卫

8. ```javascript
   router.beforeEach((to, from, next) => {
     // 检查用户是否登录
     if (to.matched.some(record => record.meta.requiresAuth)) {
       // 这里应该进行实际的登录状态检查
       if (!localStorage.getItem('user-token')) {
         // 如果用户未登录，则重定向到登录页面
         next({ path: '/login', query: { redirect: to.fullPath } });
       } else {
         next();
       }
     } else {
       next();
     }
   });
   ```

9. 

10. 

11. 

## axios的作用？

Axios是一个基于Promise的HTTP客户端，用于浏览器和node.js环境。它允许你以一种简洁、一致的方式发送HTTP请求，并处理响应。Axios的主要作用和特点包括：

### 1. 简洁的HTTP请求发送

使用Axios，你可以轻松地发送GET、POST、PUT、DELETE等HTTP请求。它提供了简洁的API，使得发送请求和处理响应变得非常简单。

### 2. 支持Promise

Axios基于Promise，这意味着你可以使用`.then()`和`.catch()`方法来处理异步请求的成功和失败情况，或者使用`async/await`语法来处理异步请求。

### 3. 请求和响应拦截器

Axios允许你添加请求拦截器和响应拦截器。请求拦截器可以在请求发送之前修改请求，而响应拦截器可以在响应到达之前修改或处理响应。

### 4. 跨平台支持

Axios不仅可以在浏览器中使用，还可以在Node.js环境中使用，使得前后端可以共享相同的HTTP请求代码。

### 5. 配置灵活

Axios提供了丰富的配置选项，如请求超时、请求头、请求体等，使得你可以根据需要灵活地配置HTTP请求。

### 6. 错误处理

Axios提供了错误处理机制，使得你可以轻松地捕获和处理请求错误。

### 示例：使用Axios发送GET请求

```javascript
axios.get('https://api.example.com/data')
  .then(function (response) {
    // 处理响应数据
    console.log(response.data);
  })
  .catch(function (error) {
    // 处理错误情况
    console.error(error);
  });
```

### 示例：使用Axios发送POST请求

```javascript
axios.post('https://api.example.com/data', {
    firstName: 'Fred',
    lastName: 'Flintstone'
  })
  .then(function (response) {
    // 处理响应数据
    console.log(response.data);
  })
  .catch(function (error) {
    // 处理错误情况
    console.error(error);
  });
```



## 列举 vue 的常见指令。

Vue.js 提供了一系列的指令（Directives），这些指令以`v-`为前缀，用于在HTML模板中绑定数据或执行特定的逻辑。以下是一些Vue.js中常见的指令：

### 1. `v-bind`（缩写为 `:`）

用于动态地绑定一个或多个属性，或一个组件的prop到表达式。

```html
<!-- 完整语法 -->
<a v-bind:href="url">Link</a>

<!-- 缩写 -->
<a :href="url">Link</a>
```

### 2. `v-model`

创建双向数据绑定，常用于表单元素。

```html
<input v-model="message" placeholder="edit me">
<p>Message is: {{ message }}</p>
```

### 3. `v-for`

用于基于源数据多次渲染一个元素或模板块。

```html
<ul>
  <li v-for="item in items" :key="item.id">
    {{ item.text }}
  </li>
</ul>
```

### 4. `v-if`, `v-else-if`, `v-else`

用于条件性地渲染一块内容。这块内容只会在指令的表达式返回truthy值的时候被渲染。

```html
<div v-if="Math.random() > 0.5">
  Now you see me
</div>
```

### 5. `v-show`

根据表达式的真假切换元素的显示状态。

```html
<h1 v-show="ok">Hello!</h1>
```

### 6. `v-on`（缩写为 `@`）

用于监听DOM事件，并在触发时执行一些JavaScript代码。

```html
<button v-on:click="counter += 1">Add 1</button>
```

### 7. `v-html`

用于设置元素的innerHTML。注意，使用`v-html`时要小心，因为它可能会导致跨站脚本（XSS）攻击。

```html
<div v-html="rawHtml"></div>
```

### 8. `v-once`

表示元素或组件只渲染一次。随后的重新渲染，元素/组件及其所有的子节点将被视为静态内容并跳过。

```html
<span v-once>This will never change: {{ msg }}</span>
```

### 9. `v-pre`

跳过这个元素和它的子元素的编译过程。可以用来显示原始的Mustache标签。

```html
<span v-pre>{{ this will not be compiled }}</span>
```

### 10. `v-cloak`

这个指令保持在元素上直到关联实例结束编译。和CSS规则如`[v-cloak] { display: none }`一起用时，这个指令可以隐藏未编译的Mustache标签直到实例准备完毕。

```html
<div v-cloak>
  {{ message }}
</div>
```



​	

## 简述jsonp 及其原理?

JSONP（JSON with Padding）是一种技术，用于在不同源（跨域）之间进行数据传输。由于浏览器的同源策略限制，直接从不同源请求数据通常会受到限制。JSONP通过动态创建`<script>`标签的方式绕过这一限制，允许跨域请求数据。

### JSONP的原理

1. 1.**客户端请求**：客户端（浏览器）向服务器发送一个带有特定回调函数名的请求。这个回调函数名通常由客户端动态生成，并通过URL参数（如`callback`）传递给服务器。

2. 2.**服务器响应**：服务器接收到请求后，将数据包装在一个由客户端提供的回调函数名中，并返回给客户端。返回的数据格式通常是`callback(data)`，其中`data`是服务器返回的数据。

3. 3.**客户端处理**：客户端接收到返回的数据后，会执行这个回调函数，并将数据作为参数传递给这个函数。这样，客户端就可以处理从服务器返回的数据了。

### JSONP的使用示例

假设客户端需要从`http://example.com/data`获取数据：

1. 1.**客户端请求**：

2. ```js
   var callbackName = 'myCallback'; // 动态生成回调函数名
   var script = document.createElement('script');
   script.src = 'http://example.com/data?callback=' + callbackName;
   document.head.appendChild(script);
   ```

3. 

4. 2.**客户端定义回调函数**： 

5. ```js
   window.myCallback = function(data) {
     console.log('Received data:', data);
   };
   ```

6. 

7. 3.**服务器响应**：

8. ```js
   // 假设请求的回调函数名是 myCallback
   myCallback({ "name": "John", "age": 30 });
   ```

9. 

### JSONP的限制

- **安全性问题**：由于JSONP依赖于动态创建`<script>`标签，因此存在跨站脚本攻击（XSS）的风险。服务器需要确保返回的数据是安全的，不会执行恶意代码。
- **只能用于GET请求**：JSONP仅支持GET请求，因为`<script>`标签只能发起GET请求。
- **数据格式限制**：JSONP通常用于传输JSON格式的数据，但也可以传输其他格式的数据，只要服务器返回的数据格式符合客户端回调函数的预期。

### 结论

JSONP是一种简单有效的跨域数据传输技术，尤其适用于那些不支持CORS（跨源资源共享）的老旧服务器。然而，由于其安全性和功能限制，现代Web开发中更推荐使用CORS来处理跨域请求。

## 简述 cors 及其原理？

CORS（Cross-Origin Resource Sharing，跨源资源共享）是一种安全机制，允许一个域（源）的Web应用访问另一个域的资源。它通过在HTTP请求中添加特定的头部信息来实现跨域访问控制。

### CORS的原理

1. 1.**预检请求（Preflight Request）**：当浏览器检测到一个跨域请求时，它会首先发送一个OPTIONS请求作为预检请求。预检请求包含`Origin`头部，表明请求的源，以及`Access-Control-Request-Method`头部，表明实际请求的HTTP方法。服务器响应预检请求时，会包含`Access-Control-Allow-Origin`头部，指定哪些源可以访问资源，以及`Access-Control-Allow-Methods`头部，表明允许的HTTP方法。

2. 2.**实际请求**：如果预检请求成功，浏览器会发送实际的跨域请求。实际请求同样包含`Origin`头部。服务器响应实际请求时，会包含`Access-Control-Allow-Origin`头部，表明允许的源。

3. 3.**其他CORS头部**：`Access-Control-Allow-Headers`：服务器可以指定哪些头部可以被客户端访问。`Access-Control-Allow-Credentials`：服务器可以指定是否允许发送凭证（如cookies）。`Access-Control-Expose-Headers`：服务器可以指定哪些头部可以被客户端访问。

### CORS的使用示例

假设客户端需要从`https://api.example.com/data`获取数据：

1. 1.**浏览器发送预检请求**： 

2. ```http
   OPTIONS /data HTTP/1.1
   Host: api.example.com
   Origin: https://client.example.com
   Access-Control-Request-Method: GET
   ```

3. 

4. 2.**服务器响应预检请求**：

5. ```http
   HTTP/1.1 204 No Content
   Access-Control-Allow-Origin: https://client.example.com
   Access-Control-Allow-Methods: GET, POST, OPTIONS
   ```

6. 

7. 3.**浏览器发送实际请求**：

8. ```http
   GET /data HTTP/1.1
   Host: api.example.com
   Origin: https://client.example.com
   ```

9. 

10. 4.**服务器响应实际请求**： 

11. ```http
    HTTP/1.1 200 OK
    Content-Type: application/json
    Access-Control-Allow-Origin: https://client.example.com
    ```

12. 

### CORS的限制

- **同源策略**：CORS基于同源策略，只允许同源或被明确允许的跨源请求。
- **服务器配置**：服务器必须正确配置CORS相关的HTTP头部，否则跨域请求将失败。
- **凭证限制**：默认情况下，跨域请求不发送凭证（如cookies）。如果需要发送凭证，服务器必须在`Access-Control-Allow-Credentials`头部中明确允许。

### 结论

CORS是一种重要的机制，用于在遵守同源策略的前提下，允许跨域资源共享。通过在HTTP请求和响应中添加特定的头部信息，CORS确保了跨域请求的安全性和可控性。在现代Web开发中，CORS是实现跨域数据交互的推荐方法。



## 看代码写结果

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

</body>
<script>
    // 示例1
    // var name = "张开"
    // function func() {
    //     var name = "李开"
    //     function inner() {
    //         console.log(name)
    //     }
    //     return inner
    // }
    // var ret = func()
    // ret()  //李开

    //示例2
    // function func() {
    //     if (1==1) {
    //         var name= "李开"
    //     }
    //     console.log(name)  //李开
    // }
    // func()

    // 示例3
    // var name = "张开"
    // function func() {
    //     var name = "李开"
    //     function inner() {
    //         var name = "刘开"
    //         console.log(name)  // 刘开
    //     }
    //     return inner()
    // }
    // func()

    //示例4
    // function func() {
    //     console.log(name) //underfined
    //     var name = '李开'
    // }
    // func()

    //示例5
    // var name = "张开"
    // function Foo(){
    //     this.name =  '李开'
    //     this.func = function () {}
    //     console.log(this.name)  //李开
    // }
    // var obj = new Foo();
    // obj.func()

    // 示例6
    // var name = "张开"
    // var info = {
    //     name:"李开",
    //     func: function() {
    //         console.log(111, this.name); //111 '李开'
    //         (function () {
    //             console.log(222,this.name) // 222 '张开' //function里的this默认是windows
    //         })()
    //     }
    // };
    // info.func()

    var name = "张开"
    var info = {
        name: '李开',
        func: function(){
            console.log(111,this.name)  // 111 '李开'
            var that = this;
            (function() {
                console.log(222, that.name)  // 222 '李开'
            })()
        }
    };
    info.func()
    
</script>
</html>
```



# Django 和web部分面试题

## 简述http协议及常用请求头

HTTP（HyperText Transfer Protocol，超文本传输协议）是一种用于分布式、协作式和超媒体信息系统的应用层协议。它定义了客户端和服务器之间进行数据传输的规则和格式。HTTP是互联网上应用最广泛的协议之一，主要用于Web浏览器和服务器之间的通信。

### HTTP协议的特点

- **无状态**：HTTP协议本身是无状态的，这意味着服务器不会保存任何关于客户端请求的状态信息。为了实现状态管理，引入了如Cookies和Session等机制。
- **基于请求/响应模型**：HTTP协议采用客户端发送请求，服务器响应请求的模式。
- **灵活**：HTTP允许传输任意类型的数据对象，通过在请求头中指定`Content-Type`来指示数据类型。

### 常用的HTTP请求头

1. 1.**Accept**：客户端可以接受的内容类型列表。

2. 2.**Accept-Encoding**：客户端可以接受的编码格式列表，如gzip、deflate等。

3. 3.**Accept-Language**：客户端可以接受的语言列表。

4. 4.**Authorization**：包含用于身份验证的凭证信息。

5. 5.**Content-Type**：请求体中数据的MIME类型，如`application/json`、`text/html`等。

6. 6.**Cookie**：客户端存储的键值对信息，用于身份验证和状态管理。

7. 7.**Host**：请求的服务器域名和端口号。

8. 8.**User-Agent**：客户端软件的名称和版本信息。

9. 9.**Referer**：当前请求的来源URL，用于追踪请求来源。

10. 10.**Connection**：控制当前事务完成后，是否关闭网络连接。常见的值有`keep-alive`和`close`。

### 示例：一个简单的HTTP请求头

```http
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

在这个示例中，客户端向`www.example.com`的`/index.html`发送了一个HTTP GET请求。请求头中包含了客户端的类型、接受的内容类型、语言偏好、编码格式、连接方式等信息。

HTTP响应头是服务器发送给客户端（通常是Web浏览器）的一系列信息，用于描述响应的内容、服务器信息、缓存控制等。以下是一些常见的HTTP响应头及其用途：

1. **Content-Type** 描述响应内容的MIME类型，如`text/html`、`application/json`等。

### 2. **Content-Length**响应体的长度，以字节为单位。

3. **Content-Encoding**响应体的编码格式，如`gzip`、`deflate`等。

4. **Content-Language**响应内容的语言。

5. **Content-Location**指示响应内容的URL。

6. **Content-Disposition**告诉浏览器如何处理响应内容，通常用于文件下载。

7. **Cache-Control**控制缓存行为，如`no-cache`、`max-age=3600`等。

8. **Date**服务器生成响应的日期和时间。

9. **Last-Modified**资源最后修改的日期和时间。

10. **ETag**资源的唯一标识符，用于缓存验证。

11. **Expires**响应内容的过期日期和时间。

12. **Server**服务器软件的名称和版本。

13. **Set-Cookie**设置Cookie，用于身份验证和状态管理。

14. **Location**用于重定向，指示客户端应该访问的URL。

15. **Status** HTTP状态码及其描述。

### 示例：一个简单的HTTP响应头

```http
HTTP/1.1 200 OK
Date: Wed, 21 Oct 2023 07:28:00 GMT
Server: Apache/2.4.1 (Unix)
Content-Type: text/html; charset=UTF-8
Content-Length: 1234
Connection: close
```

在这个示例中，服务器成功响应了一个HTTP请求，状态码为200（OK）。响应头中包含了响应的日期、服务器信息、内容类型、内容长度和连接方式等信息。



HTTP报文：

Http报文包括请求报文和响应报文两大部分，其中请求报文由请求行（requestline）、请求头（header）、空行和请求体四个部分组成。而响应报文由状态行、响应头部、空行和响应体四个部分组成.

HTTP请求方法：

GET：请求指定的页面信息，并返回实体主体。

HEAD：类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头。

POST：向指定资源提交数据进行处理请求（例如提交表单或者上传文件)。数据被包含在请求体中。

PUT：从客户端向服务器传送的数据取代指定的文档的内容。

DELETE：请求服务器删除指定的页面。



## 列举http常见的请求方法

```
HTTP请求方法：
GET：请求指定的页面信息，并返回实体主体。
HEAD：类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头。
POST：向指定资源提交数据进行处理请求(例如提交表单或者上传文件)。数据被包含在请求体中。
PUT：从客户端向服务器传送的数据取代指定的文档的内容。
DELETE：请求服务器删除指定的页面。

GET与POST区别：
GET在浏览器回退时是无害的，而POST会再次提交请求。
GET请求会被浏览器主动缓存，而POST不会，除非手动设置。
GET请求参数会被完整保留在浏览器历史记录里，而PO.ST中的参数不会被保留。
GET请求在URL中传送的参数是有长度限制的，而POST没有限制。
GET参数通过URL传递，POST放在Request body中。
```



## 列举http常见的状态码

```
Http 状态码：
状态代码有三位数字组成，第一个数字定义了响应的类别，共分五种类别：
1xx：指示信息—表示请求已接收，继续处理。
2xx：成功—表示请求已被成功接收、理解、接受。
3xx：重定向一要完成请求必须进行更进一步的操作。
4xx:客户端错误一请求有语法错误或请求无法实现。
5xx：服务器端错误一服务器未能实现合法的请求

常见的两种错误状态码：
403 Forbidden   //对被请求页面的访问被禁止
404 Not Found  //请求资源不存在，比如：输入了错误的URL
```



## http和https的区别

HTTP（HyperText Transfer Protocol，超文本传输协议）和HTTPS（HyperText Transfer Protocol Secure，超文本传输协议安全）都是用于在客户端和服务器之间传输数据的协议，但它们之间存在一些关键的区别：

### 1. 安全性

- **HTTP**：不提供加密措施，数据以明文形式传输，容易受到中间人攻击（MITM）和数据泄露。
- **HTTPS**：在HTTP的基础上加入了SSL/TLS协议，对数据进行加密，确保数据传输的安全性。

### 2. 端口

- **HTTP**：默认使用端口80。
- **HTTPS**：默认使用端口443。

### 3. URL标识

- **HTTP**：URL以`http://`开头。
- **HTTPS**：URL以`https://`开头。

### 4. 证书

- **HTTP**：不需要SSL证书。
- **HTTPS**：需要SSL证书来验证服务器的身份，并建立加密连接。

### 5. 性能

- **HTTP**：由于没有加密过程，HTTP的性能通常略高于HTTPS。
- **HTTPS**：由于加密和解密的过程，HTTPS的性能通常略低于HTTP，但随着现代硬件和优化技术的发展，性能差异已经变得非常小。

### 6. 使用场景

- **HTTP**：适用于对安全性要求不高的场景，如内部网络、测试环境等。
- **HTTPS**：适用于需要保护数据隐私和安全的场景，如电子商务、银行服务、在线支付等。



## 简述 websocket 协议及实现原理

WebSocket是一种在单个TCP连接上进行全双工通信的协议。它允许服务器和客户端之间进行实时双向通信，适用于需要即时通信的应用场景，如在线聊天、实时游戏、股票交易等。

### WebSocket协议的特点

- **全双工通信**：客户端和服务器可以同时发送和接收消息。
- **持久连接**：一旦建立连接，WebSocket保持连接直到被显式关闭，不需要像HTTP那样频繁地建立和断开连接。
- **低延迟**：由于是持久连接，消息传输的延迟非常低。
- **轻量级**：WebSocket协议的头部信息较小，减少了传输开销。

### WebSocket实现原理

WebSocket协议的实现基于以下步骤：

1. 1.**握手**：客户端通过HTTP协议发起一个特殊的请求，请求升级到WebSocket协议。这个请求包含必要的头部信息，如`Upgrade: websocket`和`Connection: Upgrade`，以及一个`Sec-WebSocket-Key`用于验证。

2. 2.**服务器响应**：服务器接收到握手请求后，如果支持WebSocket协议，会返回一个状态码为101的响应，表示协议切换。同时，服务器会返回一个`Sec-WebSocket-Accept`头部，包含经过服务器处理的客户端提供的`Sec-WebSocket-Key`。

3. 3.**连接建立**：握手成功后，WebSocket连接建立，客户端和服务器可以开始双向通信。

4. 4.**数据传输**：数据以帧的形式传输，每个帧包含操作码（指示帧类型，如文本、二进制等）和负载数据。WebSocket协议定义了帧的格式和如何处理不同类型的帧。

5. 5.**关闭连接**：任何一方都可以发送一个关闭帧来终止连接。收到关闭帧的一方会发送一个关闭帧作为响应，然后关闭TCP连接。

### WebSocket的应用

WebSocket协议广泛应用于需要实时数据交换的Web应用中。例如，聊天应用使用WebSocket来实现实时消息传递，游戏服务器使用WebSocket来同步游戏状态，股票交易平台使用WebSocket来实时更新股票价格等。



## django 中如何实现 websocket?

在Django中实现WebSocket，可以使用`channels`库，它是一个扩展，允许Django应用处理WebSocket和其他类型的实时通信。以下是使用`channels`实现WebSocket的基本步骤：

### 1. 安装channels

首先，需要安装`channels`库。可以通过pip安装：

```bash
pip install channels
```

### 2. 配置Django项目

在Django项目的`settings.py`文件中，需要添加`channels`到`INSTALLED_APPS`列表，并配置WebSocket的路由：



```python
# settings.py

INSTALLED_APPS = [
    # ...
    'channels',
    # ...
]

# 配置WebSocket路由
ASGI_APPLICATION = 'your_project.routing.application'
```

还需要定义一个ASGI应用程序，通常在项目的`routing.py`文件中：

```python
# your_project/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from your_app import consumers

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter([
        path('ws/your-consumer/', consumers.YourConsumer.as_asgi()),
    ]),
})
```

### 3. 创建WebSocket消费者

创建一个消费者（Consumer），它类似于Django的视图，用于处理WebSocket连接。消费者需要继承自`channels.generic.websocket.WebSocketConsumer`：



```python
# your_app/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class YourConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': 'Hello, ' + message
        }))
```

### 4. 前端连接WebSocket

在前端，使用JavaScript的`WebSocket`对象连接到Django后端的WebSocket端点：

```javascript
var socket = new WebSocket('ws://localhost:8000/ws/your-consumer/');

socket.onmessage = function(event) {
    var message = event.data;
    console.log('Received message: ' + message);
};

socket.onopen = function(event) {
    console.log('Connection established');
};

socket.onclose = function(event) {
    console.log('Connection closed');
};
```

### 5. 运行Django开发服务器

使用Django的ASGI服务器运行开发服务器：

```bash
python manage.py runserver
```

### 注意事项

- `channels`库支持异步编程，因此消费者中的方法通常需要是异步的。
- 在生产环境中，建议使用更健壮的ASGI服务器，如Daphne或Uvicorn，来运行Django项目。
- WebSocket的实现细节可能根据`channels`库的版本和Django的版本有所不同，需要参考相应的文档。



## 从输入http://www.baidu.com/到页面返回，中间都是发生了什么？

```
1. 输入网址并提交
用户在浏览器地址栏输入http://www.baidu.com/并按下回车键。
2. 解析URL
浏览器解析输入的URL，确定协议（HTTP）、域名（www.baidu.com）和路径（/）。
3. DNS查询
浏览器向DNS服务器查询域名对应的IP地址。这个过程可能包括：
浏览器缓存：检查浏览器是否已经缓存了该域名的IP地址。
操作系统缓存：检查操作系统的DNS缓存。
路由器缓存：检查路由器的DNS缓存。
ISP DNS服务器：如果以上缓存都没有，浏览器会向ISP提供的DNS服务器查询。
根DNS服务器：如果ISP的DNS服务器没有记录，它会向根DNS服务器查询，然后是顶级域名服务器（如.com），最后是权威DNS服务器（如baidu.com的DNS服务器）。
4. 建立TCP连接
浏览器使用解析出的IP地址和默认的HTTP端口（80）或HTTPS端口（443）与服务器建立TCP连接。这个过程包括三次握手，确保双方都准备好进行数据传输。
5. 发送HTTP请求
一旦TCP连接建立，浏览器会发送一个HTTP GET请求到服务器，请求指定的资源。请求包括请求行（如GET / HTTP/1.1）、请求头（如Host、User-Agent等）和可能的请求体（对于POST请求）。
6. 服务器处理请求
服务器接收到HTTP请求后，根据请求的资源路径处理请求。对于静态资源，服务器直接从文件系统中获取资源；对于动态资源，服务器可能需要执行一些后端逻辑（如数据库查询）来生成响应。
7. 发送HTTP响应
服务器处理完请求后，会发送一个HTTP响应给浏览器。响应通常包括状态码（如200表示成功）、响应头（如Content-Type指定内容类型）和响应体（实际的页面内容）。对于HTML页面，响应体通常包含HTML标记、CSS和JavaScript代码。
8. 渲染页面
浏览器接收到响应后，会根据响应头中的Content-Type来决定如何处理响应体。如果响应体是HTML内容，浏览器会解析HTML并渲染页面。浏览器会解析HTML标记，创建DOM树，然后根据CSS样式渲染页面，并执行JavaScript代码。
9. 关闭连接
一旦页面渲染完成，浏览器可能会关闭TCP连接，或者保持连接以备后续的请求。对于HTTP/1.1，服务器默认使用持久连接（Keep-Alive），允许在同一个TCP连接上发送和接收多个请求/响应。
10. 用户交互
用户可以与页面进行交互，如点击链接、提交表单等，这将触发新的HTTP请求，重复上述过程。
11. 浏览器缓存
浏览器可能会对某些资源（如图片、CSS文件、JavaScript文件等）进行缓存，以便在用户再次访问相同页面时加快加载速度。
12. 安全性考虑
如果使用HTTPS，整个过程会通过SSL/TLS加密，确保数据传输的安全性。
13. 浏览器插件和扩展
浏览器插件和扩展可能会在页面加载过程中执行额外的操作，如广告拦截、页面分析等。
14. 资源加载优化
浏览器会尝试并行加载资源，如同时加载图片、CSS和JavaScript文件，以提高页面加载速度。
15. 页面渲染优化
浏览器会使用一些优化技术，如重排（Reflow）和重绘（Repaint）的最小化，来提高页面渲染的效率。

整个过程涉及了网络通信、数据解析、资源处理、页面渲染和用户交互等多个方面，是现代Web开发和用户体验的关键组成部分。
```



## 请简述浏览器是如何获取一枚网页的？

```
其过程如下：
1.在用户输入目的URL后，浏览器先向DNS服务器发起域名解析请求；
2.在获取了对应的IP后向服务器发送请求数据包；
3.服务器接收到请求数据后查询服务器上对应的页面，并将找到的页面代码回复给客户端；
4.客户端接收到页面源代码后，检查页面代码中引用的其他资源，并再次向服务器请求该资源；
5.在资源接收完成后，客户端浏览器按照页面代码将页面渲染输出显示在显示器上。
```



## Python web开发中，跨域问题产生的原理和解决思路是?

### 跨域问题产生的原理

跨域问题产生的原理基于浏览器的同源策略（Same-Origin Policy）。同源策略是一种安全机制，用于限制一个源的文档或脚本如何与另一个源的资源进行交互。一个源由协议、域名和端口号定义。如果两个URL的协议、域名和端口号都相同，则它们属于同一个源；否则，它们属于不同的源。

当一个Web页面尝试通过JavaScript发起一个跨域的HTTP请求时，浏览器会阻止这个请求，除非服务器端明确允许跨域请求。这种限制是为了防止恶意网站读取其他网站的敏感数据。

### 解决思路

解决跨域问题有几种常见的方法：

1. 1.**JSONP（JSON with Padding）**：JSONP是一种技术，通过动态创建`<script>`标签的方式绕过同源策略的限制。服务器需要将响应数据包裹在一个回调函数中返回。客户端需要定义一个回调函数来处理这个数据。

2. 2.**CORS（Cross-Origin Resource Sharing，跨源资源共享）**：CORS是现代浏览器支持的一种标准机制，允许服务器指定哪些源可以访问资源。服务器在响应头中添加`Access-Control-Allow-Origin`字段，指定允许的源。可以通过设置`Access-Control-Allow-Methods`和`Access-Control-Allow-Headers`来控制允许的HTTP方法和头部。

3. 3.**代理服务器**：在服务器端设置一个代理服务器，将跨域请求转发到目标服务器。客户端向代理服务器发送请求，代理服务器再向目标服务器发送请求，并将响应返回给客户端。这种方法可以隐藏真实的请求源，从而绕过同源策略。

4. 4.**使用WebSockets**：WebSockets不使用HTTP协议，因此不受同源策略限制。可以通过建立一个WebSocket连接来实现跨域通信。

5. 5.**使用服务器端代理**：在客户端和目标服务器之间建立一个服务器端代理。客户端向代理发送请求，代理再向目标服务器发送请求，并将响应返回给客户端。这种方法可以避免客户端直接发起跨域请求。

### 结论

跨域问题的解决方法取决于具体的应用场景和需求。CORS是最常用的方法，因为它简单且被现代浏览器广泛支持。在某些情况下，使用代理服务器或JSONP可能更合适。对于实时通信，WebSockets是一个很好的选择。



## django对数据查询结果排序怎么做，降序怎么做？

在Django中，对数据查询结果进行排序可以通过在查询集中使用`order_by`方法来实现。`order_by`方法允许你指定一个或多个字段名，Django将根据这些字段对查询结果进行排序。

### 升序排序

默认情况下，使用`order_by`进行排序是升序（ascending）的。例如，如果你有一个`Book`模型，你可以这样对书名进行升序排序：

```py
from myapp.models import Book

# 对书名进行升序排序
books = Book.objects.order_by('title')
```

### 降序排序

要进行降序（descending）排序，需要在字段名前加上负号`'-'`。例如，对书名进行降序排序：

```py
# 对书名进行降序排序
books = Book.objects.order_by('-title')
```

### 多字段排序

你还可以根据多个字段进行排序，只需在`order_by`方法中列出这些字段名即可。例如，先按出版日期降序排序，如果出版日期相同，则按书名升序排序：

```py
# 先按出版日期降序排序，再按书名升序排序
books = Book.objects.order_by('-publish_date', 'title')
```



## django的 orm 中如何查询 id 不等于5的元素？

在Django的ORM中，要查询`id`不等于5的元素，可以使用`exclude`方法结合字段查找。`exclude`方法用于排除满足特定条件的记录。

```py
from myapp.models import MyModel

# 查询id不等于5的元素
objects = MyModel.objects.exclude(id=5)
```

### 字段查找

Django ORM支持多种字段查找方式，例如：

- `exact`：精确匹配。
- `iexact`：不区分大小写的精确匹配。
- `contains`：包含。
- `icontains`：不区分大小写的包含。
- `gt`：大于。
- `gte`：大于等于。
- `lt`：小于。
- `lte`：小于等于。
- `in`：在列表中。
- `startswith`：以...开始。
- `endswith`：以...结束。
- `range`：在指定范围内。

### 结合使用字段查找

你还可以结合使用多个字段查找来构建更复杂的查询条件。例如，如果你想排除`id`等于5且`name`等于"John"的记录，可以这样写：

```python
# 排除id等于5且name等于"John"的记录
objects = MyModel.objects.exclude(id=5, name='John')
```

### 注意事项

- `exclude`方法返回的是一个查询集（QuerySet），它不会立即执行数据库查询，只有在需要数据时（如迭代查询集或调用`list()`方法）才会执行。
- 请确保字段名与你的模型中定义的字段名一致。



## 使用 Django 中 model flter 条件过滤方法,把下边 sql 语句转化成 python 代码

```sql
select * from companywhere title like "gabc%" or mecount>999 order by createtime desc;

models.company.objects.filter(Q(title__contains='abc') or Q(weight__gt=999)).order_by('creatime').reverse()
```





```py
from django.db.models import Q
from myapp.models import Company

# 使用Django ORM进行查询
companies = Company.objects.filter(
    Q(title__contains='abc') | Q(mecount__gt=999)
).order_by('-createtime')
```

这段代码中：

- `Q(title__contains='abc') | Q(mecount__gt=999)`：使用`Q`对象来构建复杂的查询条件，`|`表示逻辑“或”。
- `order_by('-createtime')`：使用`order_by`方法对查询结果进行排序，`-`表示降序。



## 列举django orm 中你了解的所有方法？

Django ORM（对象关系映射）提供了丰富的API来操作数据库，

### 查询集（QuerySet）方法

- `filter(**kwargs)`: 返回满足给定查找参数的查询集。
- `exclude(**kwargs)`: 返回不满足给定查找参数的查询集。
- `get(**kwargs)`: 返回满足给定查找参数的单个对象，如果没有找到或找到多个对象会抛出异常。
- `create(**kwargs)`: 创建并保存一个新对象。
- `bulk_create(objs, batch_size=None)`: 批量创建多个对象。
- `update_or_create(defaults=None, **kwargs)`: 如果对象存在则更新，不存在则创建。
- `count()`: 返回查询集中对象的数量。
- `first()`: 返回查询集中的第一个对象。
- `last()`: 返回查询集中的最后一个对象。
- `exists()`: 检查查询集是否包含至少一个对象。
- `order_by(*fields)`: 根据指定的字段对查询集进行排序。
- `reverse()`: 反转查询集中的对象顺序。
- `distinct()`: 返回一个去重的查询集。
- `values(*fields)`: 返回一个包含字典的查询集，每个字典代表一个对象。
- `values_list(*fields, flat=False)`: 返回一个包含字段值的元组列表。
- `dates(field_name, kind, order='ASC')`: 返回一个包含日期的查询集。
- `datetimes(field_name, kind, order='ASC', tzinfo=None)`: 返回一个包含日期时间的查询集。
- `none()`: 返回一个空的查询集。
- `all()`: 返回查询集的副本。

### 模型（Model）方法

- `save(*args, **kwargs)`: 保存当前对象到数据库。
- `delete()`: 删除当前对象。
- `refresh_from_db(using=None)`: 从数据库重新加载当前对象的字段值。
- `classmethod objects.get(**kwargs)`: 获取满足给定查找参数的单个对象。
- `classmethod objects.create(**kwargs)`: 创建并保存一个新对象。
- `classmethod objects.get_or_create(defaults=None, **kwargs)`: 如果对象存在则获取，不存在则创建。
- `classmethod objects.update_or_create(defaults=None, **kwargs)`: 如果对象存在则更新，不存在则创建。

### 查询（Query）方法

- `resolve_expression(expr, *args, **kwargs)`: 解析表达式。
- `complex_filter(lookups)`: 应用复杂的过滤条件。
- `get_query_set()`: 获取查询集。
- `as_manager()`: 将Query对象转换为Manager对象。

### 其他

- `F表达式`: 允许在查询中引用模型字段的值。
- `Q对象`: 用于构建复杂的查询条件。
- `Prefetch对象`: 用于优化关联对象的查询。



## django 中的 F的作用?

在Django中，`F`对象用于引用模型字段的值，而不需要从数据库中检索该值。这在需要对数据库中的字段值进行比较或更新时非常有用，尤其是在需要引用同一模型实例的多个字段时。

### F对象的使用场景

1. 1.**字段值比较**：在数据库层面直接比较两个字段的值，而不需要先将值加载到Python代码中。

2. 2.**字段值更新**：在数据库层面直接更新字段的值，而不需要先从数据库中检索该值。

### 示例

假设有一个`Book`模型，其中包含`price`和`discount`字段：

python



复制

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
```

#### 字段值比较

如果要查询`price`字段大于`discount`字段的书籍，可以使用`F`对象：

```python
from django.db.models import F

# 查询price大于discount的书籍
books = Book.objects.filter(price__gt=F('discount'))
```

#### 字段值更新

如果要更新`price`字段的值，使其等于`price`字段的值加上`discount`字段的值，可以使用`F`对象：

```python
# 更新price字段的值
Book.objects.update(price=F('price') + F('discount'))
```

### 注意事项

- `F`对象在使用时需要从`django.db.models`导入。
- 使用`F`对象进行字段值比较或更新时，操作直接在数据库层面执行，这可以提高性能，尤其是在处理大量数据时。
- `F`对象可以用于任何支持字段查找的Django ORM方法，如`filter()`, `exclude()`, `update()`等。