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



## django 中的 Q 的作用?

在Django中，`Q`对象用于构建复杂的查询条件，它允许你组合多个查询条件，实现逻辑“或”（OR）和逻辑“与”（AND）操作。`Q`对象特别适用于需要根据多个条件进行过滤的场景，其中这些条件之间可能需要逻辑组合。

### 使用场景

1. 1.**逻辑“或”（OR）操作**：当需要根据多个可能的值来过滤数据时，可以使用`Q`对象来实现逻辑“或”操作。

2. 2.**逻辑“与”（AND）操作**：当需要同时满足多个条件时，可以使用`Q`对象来实现逻辑“与”操作。

### 示例

假设有一个`Book`模型，包含`title`和`author`字段：

```python
from django.db import models
from django.db.models import Q

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
```

#### 逻辑“或”操作

如果要查询书名包含"Python"或者作者是"John Doe"的书籍，可以使用`Q`对象：

```python
# 查询书名包含"Python"或者作者是"John Doe"的书籍
books = Book.objects.filter(Q(title__contains='Python') | Q(author='John Doe'))
```

#### 逻辑“与”操作

如果要查询书名既包含"Python"又包含"Guide"的书籍，可以使用`Q`对象：

```python
# 查询书名既包含"Python"又包含"Guide"的书籍
books = Book.objects.filter(Q(title__contains='Python') & Q(title__contains='Guide'))
```

### 注意事项

- `Q`对象在使用时需要从`django.db.models`导入。
- `Q`对象可以与`filter()`, `exclude()`, `get()`, `update()`, `delete()`等方法结合使用。
- 在使用`Q`对象时，可以使用`|`（逻辑“或”）和`&`（逻辑“与”）操作符来组合条件。
- `Q`对象可以嵌套使用，以构建更复杂的查询逻辑。



## django 中如何执行原生SQL?



在Django中，如果你需要执行原生SQL语句，可以使用`raw()`方法或`cursor()`方法。这两种方法允许你直接在数据库上执行自定义的SQL查询。

### 使用`raw()`方法

`raw()`方法允许你执行一个原生的SQL查询，并将结果映射到模型实例上。使用`raw()`时，你需要提供一个SQL查询字符串和一个可选的参数列表。

#### 示例

假设有一个`Book`模型：

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
```

使用`raw()`方法执行原生SQL查询：

```python
# 执行原生SQL查询
books = Book.objects.raw('SELECT * FROM myapp_book WHERE author = %s', ['John Doe'])
for book in books:
    print(book.title)
```

### 使用`cursor()`方法

`cursor()`方法允许你执行任何SQL语句，并通过数据库游标来处理结果。使用`cursor()`时，你需要手动管理游标和事务。

#### 示例

```python
from django.db import connection

# 使用cursor执行原生SQL查询
with connection.cursor() as cursor:
    cursor.execute('UPDATE myapp_book SET title = %s WHERE author = %s', ['New Title', 'John Doe'])
    connection.commit()
```

### 注意事项

- 使用原生SQL时，需要确保SQL语句的安全性，避免SQL注入攻击。
- `raw()`方法返回的是模型实例的查询集，可以直接迭代访问。
- `cursor()`方法返回的是数据库游标，需要手动处理事务和结果集。
- 在使用`raw()`和`cursor()`方法时，应尽量避免频繁执行复杂的SQL查询，以保持应用的性能和可维护性。

## only 和 defer 的区别?

在Django ORM中，`only()`和`defer()`是两种优化数据库查询的方法，它们用于减少查询时加载的数据量，从而提高查询效率。

### only()

`only()`方法用于指定只加载模型中特定的字段。当你知道只需要模型中的某些字段时，使用`only()`可以减少数据库查询时加载的数据量。

#### 示例

假设有一个`Book`模型：

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
```

使用`only()`方法只加载`title`和`author`字段：

```python
# 只加载title和author字段
books = Book.objects.only('title', 'author')
```

### defer()

`defer()`方法用于指定延迟加载模型中的某些字段。这意味着这些字段在查询时不会立即从数据库中加载，只有在你访问这些字段时才会从数据库中加载。

#### 示例

使用`defer()`方法延迟加载`price`字段：

```python
# 延迟加载price字段
books = Book.objects.defer('price')
```

### 区别

- **加载时机**：`only()`方法在初次查询时就加载指定的字段，而`defer()`方法则延迟加载指定的字段，直到这些字段被实际访问。
- **使用场景**：如果你确定只需要模型中的部分字段，使用`only()`可以减少初次查询的数据量。如果你只需要模型中的部分字段，并且这些字段可能不会被频繁访问，使用`defer()`可以进一步优化性能。
- **性能影响**：`only()`和`defer()`都可以减少数据库查询时加载的数据量，从而提高查询效率。选择使用哪一个取决于你的具体需求和数据访问模式。



## selectrelated和prefetchrelated 的区别?

在Django ORM中，`select_related`和`prefetch_related`是两种用于优化数据库查询的方法，它们用于减少数据库查询次数，提高查询效率。尽管它们的目的相似，但它们在处理关联数据时的机制和适用场景有所不同。

### select_related

`select_related`用于优化通过外键或一对一关系关联的查询。它通过SQL的`JOIN`操作来一次性获取相关联的对象，适用于需要获取关联对象数据的场景。

#### 示例

假设有一个`Book`模型和一个`Author`模型，它们通过外键关联：

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

使用`select_related`获取书籍及其作者信息：

```python
# 使用select_related获取书籍及其作者信息
books = Book.objects.select_related('author')
for book in books:
    print(book.title, book.author.name)
```

### prefetch_related

`prefetch_related`用于优化通过外键、多对多关系或反向关联获取的查询。它通过分别查询主表和关联表，然后在Python中进行合并，适用于需要获取大量关联对象数据的场景。

#### 示例

使用`prefetch_related`获取书籍及其作者信息：

```python
# 使用prefetch_related获取书籍及其作者信息
books = Book.objects.prefetch_related('author')
for book in books:
    print(book.title, book.author.name)
```

### 区别

- **查询机制**：`select_related`通过SQL的`JOIN`操作来一次性获取相关联的对象，而`prefetch_related`通过分别查询主表和关联表，然后在Python中进行合并。
- **适用场景**：`select_related`适用于通过外键或一对一关系关联的查询，`prefetch_related`适用于通过外键、多对多关系或反向关联获取的查询。
- **性能影响**：`select_related`适用于关联数据较少的场景，可以减少数据库查询次数。`prefetch_related`适用于关联数据较多的场景，可以减少数据库查询次数并提高查询效率。

## django 中 filter 和 exclude 的区别

### 区别

- **返回结果**：`filter()`返回满足条件的记录，而`exclude()`返回不满足条件的记录。
- **逻辑操作**：`filter()`执行的是逻辑“与”（AND）操作，即所有条件都必须满足；`exclude()`执行的是逻辑“非”（NOT）操作，即排除掉满足条件的记录。
- **使用场景**：`filter()`适用于需要筛选出符合特定条件的记录的场景，`exclude()`适用于需要排除掉某些特定条件的记录的场景。

## django中 values和values_list的区别?

在Django ORM中，`values()`和`values_list()`是两种用于查询数据库并返回特定字段值的方法。它们在返回数据的格式和用途上有所不同。

### values()

`values()`方法返回一个包含字典的查询集（QuerySet），每个字典代表一个数据库记录，其中的键是字段名，值是字段值。

#### 示例

假设有一个`Book`模型：

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
```

使用`values()`方法获取书籍的标题和作者：

```python
# 获取书籍的标题和作者
books = Book.objects.values('title', 'author')
for book in books:
    print(book['title'], book['author'])
```

### values_list()

`values_list()`方法返回一个包含元组的查询集（QuerySet），每个元组包含指定字段的值。

#### 示例

使用`values_list()`方法获取书籍的标题和作者：

```python
# 获取书籍的标题和作者
books = Book.objects.values_list('title', 'author')
for book in books:
    print(book[0], book[1])
```

### 区别

- **返回数据格式**：`values()`返回的是字典列表，而`values_list()`返回的是元组列表。
- **数据访问方式**：在`values()`中，通过字段名访问数据（如`book['title']`），在`values_list()`中，通过索引访问数据（如`book[0]`）。
- **用途**：`values()`适用于需要字段名作为键来访问数据的场景，`values_list()`适用于只需要字段值，不需要字段名的场景。

## 如何使用django orm批量创建数据？

在Django ORM中，批量创建数据可以通过`bulk_create`方法实现。这个方法允许你一次性创建多个对象，从而提高数据插入的效率。

### 使用`bulk_create`

`bulk_create`方法接受一个对象列表作为参数，并将这些对象批量插入到数据库中。使用这个方法时，需要注意以下几点：

- `bulk_create`不会调用模型的`save()`方法，也不会发送任何`pre_save`或`post_save`信号。
- `bulk_create`不支持设置`auto_now_add`或`auto_now`字段。
- `bulk_create`不支持设置外键或一对一字段的反向关联。

#### 示例

假设有一个`Book`模型：

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
```

使用`bulk_create`批量创建书籍数据：

```python
# 创建书籍数据列表
books_data = [
    {'title': 'Book 1', 'author': 'Author 1', 'price': 10.99},
     {'title': 'Book 2', 'author': 'Author 2', 'price': 12.99},
     # 添加更多书籍数据...
]

# 批量创建书籍
Book.objects.bulk_create([Book(**data) for data in books_data])
```



## django的Form和ModeForm 的作用?

在Django中，`Form`和`ModelForm`是用于处理表单数据的两种不同类。它们都位于`django.forms`模块中，但各自有不同的用途和特点。

### Form

`Form`类用于创建通用的表单，不直接与模型（Model）关联。它主要用于处理不直接映射到数据库模型的表单数据。

#### 特点

- **通用性**：适用于任何类型的表单数据处理，不依赖于特定的模型。
- **灵活性**：可以自定义表单字段，包括字段类型、验证规则等。
- **用途**：适用于创建登录表单、搜索表单、自定义数据输入表单等。

#### 示例

创建一个简单的登录表单：

```python
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
```

### ModelForm

`ModelForm`类用于创建与Django模型直接关联的表单。它自动根据模型的字段生成表单字段，并提供了保存表单数据到数据库的功能。

#### 特点

- **模型关联**：直接与Django模型关联，简化了表单与数据库之间的数据交互。
- **数据验证**：自动为表单字段添加数据验证规则，确保数据的正确性。
- **数据保存**：提供`save()`方法，可以将表单数据保存到数据库中。

#### 示例

创建一个与`User`模型关联的注册表单：

```python
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserRegistrationForm(ModelForm):
    class Meta:
         model = User
         fields = ['username', 'email', 'password']
```

### 区别

- **用途**：`Form`适用于不直接映射到数据库模型的表单，而`ModelForm`适用于需要与数据库模型交互的表单。
- **数据处理**：`Form`需要手动处理表单数据的验证和保存，`ModelForm`则可以自动处理这些操作。
- **灵活性**：`Form`提供了更高的灵活性，允许自定义表单的各个方面；`ModelForm`则在与模型字段直接关联时更为方便。



## 请简述 http 缓存机制。

请简述 http 缓存机制。





HTTP缓存机制是一种优化Web性能的技术，它允许浏览器或中间缓存服务器存储Web资源的副本，以便在后续请求时快速提供这些资源，减少服务器负载和网络延迟。HTTP缓存主要通过响应头来控制，涉及以下几个关键概念：

### 1. 缓存控制头

- **Cache-Control**：用于指定缓存策略，如`max-age`（资源在缓存中保持新鲜的最大时间，单位为秒）、`no-cache`（不使用缓存，必须验证资源是否过期）、`public`（资源可以被任何缓存存储）和`private`（资源只能被单个用户缓存）等。
- **Expires**：指定资源过期的具体时间点，过期后缓存资源将被视为过时。
- **Last-Modified**：资源最后修改的时间戳，用于后续请求时进行条件请求。
- **ETag**：资源的唯一标识符，用于后续请求时进行条件请求。

### 2. 条件请求

- **If-Modified-Since**：客户端在请求中包含资源的最后修改时间，服务器只在资源自该时间后有更新时才返回新内容。
- **If-None-Match**：客户端在请求中包含资源的ETag，服务器只在资源的ETag发生变化时才返回新内容。

### 3. 缓存流程

1. 1.**首次请求**：客户端向服务器请求资源，服务器返回资源和缓存控制头。

2. 2.**缓存存储**：浏览器或中间缓存服务器根据缓存控制头决定是否存储资源副本。

3. 3.**后续请求**：客户端再次请求相同资源时，浏览器会检查本地缓存，如果缓存有效则直接使用缓存，否则向服务器发送请求。

4. 4.**条件请求**：如果缓存控制头指示需要验证，客户端会发送包含`If-Modified-Since`或`If-None-Match`的请求，服务器根据资源是否更新决定返回新内容或304 Not Modified响应。

### 4. 缓存类型

- **私有缓存**：通常由浏览器维护，只供单个用户使用。
- **共享缓存**：由代理服务器或CDN（内容分发网络）维护，可供多个用户使用。

## 简述 django 下的（内建的）缓存机制

Django提供了一套内建的缓存框架，允许开发者缓存数据以提高应用性能。Django的缓存机制支持多种后端，包括内存、数据库、文件系统、缓存服务器等，使得开发者可以根据需要选择合适的缓存策略。

### Django缓存的关键组件

1. 1.**缓存后端**：定义了数据存储和检索的方式。Django支持多种缓存后端，如本地内存、数据库、文件系统、Memcached和Redis等。

2. 2.**缓存键**：用于唯一标识缓存中的数据项。

3. 3.**缓存值**：实际存储的数据。

4. 4.**缓存失效策略**：定义了数据何时从缓存中移除，包括过期时间、最大条目数等。

### Django缓存的使用

1. 1.**配置缓存**：在`settings.py`中配置缓存后端和相关参数。

2. 2.**缓存API**：Django提供了丰富的缓存API，包括`cache.get()`和`cache.set()`等方法，用于读取和存储缓存数据。

3. 3.**视图缓存**：可以使用`@cache_page`装饰器或`cache_page`中间件来缓存整个视图的输出。

4. 4.**模板缓存**：可以使用`{% cache %}`标签在模板中缓存部分渲染结果。

5. 5.**低级缓存API**：对于更复杂的缓存需求，Django提供了低级缓存API，允许更细致地控制缓存行为。

### Django缓存的类型

1. 1.**本地内存缓存**：适用于单进程环境，如开发环境。

2. 2.**数据库缓存**：使用数据库表来存储缓存数据。

3. 3.**文件系统缓存**：将缓存数据存储在文件系统中。

4. 4.**Memcached**：使用Memcached服务器来缓存数据，适用于多进程和分布式环境。

5. 5.**Redis**：使用Redis服务器来缓存数据，支持更复杂的数据结构和持久化。



## django中使用 memcached 作为缓存的具体方法？优缺点说明？

在Django中使用Memcached作为缓存后端，可以显著提高应用性能，尤其是在高流量和高并发的场景下。Memcached是一个高性能的分布式内存对象缓存系统，它通过在内存中缓存数据来减少数据库的访问次数。

### 使用Memcached的具体方法

1. 1.**安装Memcached**：首先确保你的系统中安装了Memcached服务。

2. 2.**配置Django**：在Django的`settings.py`文件中配置Memcached作为缓存后端。

```python
CACHES = {
     'default': {
         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
         'LOCATION': '127.0.0.1:11211',
     }
}
```

这里`LOCATION`是Memcached服务器的地址和端口。如果Memcached运行在本地的默认端口11211上，可以只写IP地址。

1. 3.**使用缓存API**：在Django中，你可以使用缓存API来存储和检索数据。

```python
from django.core.cache import cache

# 设置缓存数据
cache.set('my_key', 'my_value', timeout=300)  # timeout为缓存过期时间，单位为秒

# 获取缓存数据
value = cache.get('my_key')
```

### Memcached的优点

- **高性能**：由于Memcached将数据存储在内存中，读写操作非常快速。
- **分布式**：Memcached支持分布式部署，可以水平扩展以支持更大的负载。
- **简单易用**：Django提供了简单的API来使用Memcached，无需编写复杂的代码。
- **减少数据库负载**：通过缓存常用数据，可以显著减少对数据库的访问次数。

### Memcached的缺点

- **内存限制**：由于Memcached使用内存存储数据，因此存储空间有限。
- **持久性问题**：Memcached不支持数据持久化，重启服务会导致所有缓存数据丢失。
- **数据一致性**：在分布式环境中，数据的一致性可能难以保证，尤其是在多写场景下。
- **需要额外的维护**：需要维护Memcached服务器，包括监控、重启等。



## django 的缓存能使用 redis吗?如果可以的话，如何配置?

Django的缓存可以使用Redis作为后端。Redis是一个开源的高性能键值存储数据库，支持多种数据结构，如字符串、列表、集合、有序集合等，非常适合用作缓存系统。

### 配置Redis作为Django缓存后端

1. 1.**安装Redis**：首先确保你的系统中安装了Redis服务。

2. 2.**安装django-redis**：Django-redis是一个Django缓存后端，用于连接Redis服务器。可以通过pip安装：

3. ```bash
   pip install django-redis
   ```

4. 

5. 3.**配置Django**：在Django的`settings.py`文件中配置Redis作为缓存后端。

6. ```py
   CACHES = {
       'default': {
           'BACKEND': 'django_redis.cache.RedisCache',
           'LOCATION': 'redis://127.0.0.1:6379/1',  # Redis服务器地址和端口
           'OPTIONS': {
               'CLIENT_CLASS': 'django_redis.client.DefaultClient',
           }
       }
   }
   ```

7.  `在这里，`LOCATION`是Redis服务器的地址和端口。`OPTIONS`中的`CLIENT_CLASS`指定了使用Django-redis的默认客户端。

8. 4.**使用缓存API**：配置完成后，你就可以像使用其他缓存后端一样使用Redis缓存了。

9. ```py
   from django.core.cache import cache
   
   # 设置缓存数据
   cache.set('my_key', 'my_value', timeout=300)  # timeout为缓存过期时间，单位为秒
   
   # 获取缓存数据
   value = cache.get('my_key')
   ```

10. 

### Redis缓存的优点

- **高性能**：Redis使用内存存储数据，读写操作非常快速。
- **支持多种数据结构**：Redis支持字符串、列表、集合、有序集合等多种数据结构，适合处理复杂的数据存储需求。
- **持久化**：Redis支持数据持久化，可以通过RDB和AOF两种方式将数据保存到磁盘。
- **分布式**：Redis支持分布式部署，可以水平扩展以支持更大的负载。

### Redis缓存的缺点

- **内存限制**：由于Redis使用内存存储数据，因此存储空间有限。
- **数据一致性**：在分布式环境中，数据的一致性可能难以保证，尤其是在多写场景下。



## 谈谈你所知道的 Python web 框架。

### Django

- **特点**：Django是一个高级的Python Web框架，鼓励快速开发和干净、实用的设计。它遵循MVC（模型-视图-控制器）架构模式，内置了大量功能，如用户认证、内容管理、站点地图等。
- **适用场景**：适合开发内容管理系统、博客平台、电子商务网站等大型项目。

### Flask

- **特点**：Flask是一个轻量级的Web框架，适合快速开发小型到中型的Web应用。它灵活、可扩展，允许开发者根据需要添加组件。
- **适用场景**：适合开发小型网站、API、原型设计等。

### Pyramid

- **特点**：Pyramid是一个灵活的Python Web框架，支持多种数据库和模板引擎。它允许开发者从零开始构建应用，或使用现有的组件和库。
- **适用场景**：适合开发需要高度定制的Web应用。

### Bottle

- **特点**：Bottle是一个单文件的Web框架，适用于快速开发简单的Web应用。它内置了模板引擎和WSGI服务器。
- **适用场景**：适合开发小型Web应用、原型设计等。

### Tornado

- **特点**：Tornado是一个异步非阻塞的Web框架，适合开发需要处理大量并发连接的应用，如聊天应用、实时数据服务等。
- **适用场景**：适合开发需要高并发处理的Web应用。

### Sanic

- **特点**：Sanic是一个异步的Python Web框架，它允许开发者使用异步代码来处理HTTP请求，从而提高性能。
- **适用场景**：适合开发需要高性能的Web应用。

### CherryPy

- **特点**：CherryPy是一个简单、轻量级的Web框架，它允许开发者以面向对象的方式编写Web应用。
- **适用场景**：适合开发小型到中型的Web应用。



## django、flask、tornado框架的比较?

### Django

- **特点**：
  - 高级框架，遵循MVC架构模式。
  - 内置了大量功能，如用户认证、内容管理、站点地图等。
  - 强调“约定优于配置”，有明确的项目结构和约定。
  - 适合快速开发大型、复杂的应用。
- **适用场景**：
  - 内容管理系统（CMS）
  - 博客平台
  - 电子商务网站
  - 大型企业级应用
- **优势**：
  - 强大的功能和插件生态系统。
  - 完善的文档和社区支持。
  - 适合团队开发和大型项目。

### Flask

- **特点**：
  - 轻量级框架，灵活且可扩展。
  - 适合快速开发小型到中型的Web应用。
  - 支持插件扩展，社区活跃。
- **适用场景**：
  - 小型网站
  - API开发
  - 原型设计
  - 微服务架构
- **优势**：
  - 简单易学，入门门槛低。
  - 灵活性高，可以根据需要添加组件。
  - 适合个人开发者和小型团队。

### Tornado

- **特点**：
  - 异步非阻塞的Web框架，适合处理大量并发连接。
  - 适合开发需要实时处理的应用，如聊天应用、实时数据服务等。
  - 支持WebSocket和长轮询。
- **适用场景**：
  - 实时Web应用
  - 聊天应用
  - 高并发处理的Web服务
- **优势**：
  - 高性能，适合需要处理大量并发连接的场景。
  - 异步I/O模型，提高资源利用率。
  - 适合需要实时通信的应用。

### 总结

- **Django**：适合大型、复杂的应用开发，拥有丰富的内置功能和强大的社区支持。
- **Flask**：轻量级、灵活，适合快速开发小型到中型应用，易于扩展和自定义。
- **Tornado**：异步非阻塞框架，适合需要高并发处理和实时通信的应用。



## Python 中三大框架各自的应用场景？

### Django

- **内容管理系统（CMS）**：Django的管理后台和内容管理功能非常适合开发内容管理系统。
- **博客平台**：Django的内置认证系统和内容管理功能使其成为构建博客平台的理想选择。
- **电子商务网站**：Django的模型和表单系统非常适合处理商品、订单等数据。
- **大型企业级应用**：Django的可扩展性和安全性使其适用于大型企业级应用的开发。

### Flask

- **小型网站**：Flask的轻量级特性使其适合快速开发小型网站。
- **API开发**：Flask简洁的API设计使其成为开发RESTful API的理想选择。
- **原型设计**：Flask的灵活性和快速开发能力使其适合进行原型设计和产品迭代。
- **微服务架构**：Flask的轻量级和可扩展性使其适合构建微服务架构。

### Tornado

- **实时Web应用**：Tornado的异步非阻塞特性使其适合开发需要实时处理的应用，如聊天应用、实时数据服务等。
- **高并发处理的Web服务**：Tornado的高性能和高并发处理能力使其适合处理大量并发连接的Web服务。
- **Websocket应用**：Tornado支持Websocket，适合开发需要实时通信的应用。

### 总结

- **Django**：适合开发大型、复杂的应用，如内容管理系统、博客平台、电子商务网站和大型企业级应用。
- **Flask**：适合开发小型网站、API、原型设计和微服务架构。
- **Tornado**：适合开发需要实时处理和高并发处理的Web应用，如实时Web应用和Websocket应用。



## 什么是wsgi?

WSGI（Web Server Gateway Interface）是一个Python编程语言的接口规范，用于Web服务器和Python Web应用程序或框架之间的通信。WSGI旨在提供一个统一的方法来编写Python Web服务器和应用程序，使得它们可以更容易地相互配合工作。

### WSGI的主要特点

1. 1.**标准化**：WSGI定义了一个标准化的接口，使得Web服务器和Python Web应用程序可以独立于彼此进行开发和部署。

2. 2.**兼容性**：任何遵循WSGI规范的Web服务器都可以运行任何遵循WSGI规范的Web应用程序，反之亦然。

3. 3.**灵活性**：WSGI允许开发者在不同的服务器和应用程序之间进行选择，而不必担心兼容性问题。

### WSGI的工作原理

WSGI定义了两个主要组件：服务器（或网关）和应用程序。服务器负责接收HTTP请求并将其传递给应用程序，应用程序则负责处理请求并返回HTTP响应。

- **服务器**：接收HTTP请求，调用应用程序，并将应用程序的响应返回给客户端。
- **应用程序**：接收环境变量、开始响应和响应体的回调函数，处理请求并返回响应。

### WSGI的应用

WSGI被广泛应用于Python Web开发中，许多流行的Web框架和服务器都支持WSGI，如Django、Flask、Bottle等。此外，许多Web服务器也支持WSGI，如Gunicorn、uWSGI、mod_wsgi等。

### 结论

WSGI作为Python Web开发的一个重要标准，极大地促进了Python Web应用程序和服务器的互操作性。通过遵循WSGI规范，开发者可以更灵活地选择和组合不同的服务器和应用程序，从而构建出高效、可扩展的Web应用。

## 列举django 的内置组件

Django是一个高级的Python Web框架，它内置了许多组件和功能，旨在简化Web开发过程。以下是一些Django的内置组件：

### 1. ORM（对象关系映射器）

- Django的ORM允许开发者使用Python代码来操作数据库，而无需直接编写SQL语句。

### 2. 模板系统

- Django的模板系统允许将Python代码和HTML分离，使得设计和维护Web页面变得更加容易。

### 3. 表单处理

- Django提供了表单处理机制，包括表单的创建、验证和渲染。

### 4. 管理界面

- Django自带一个强大的管理界面，允许开发者轻松地管理网站内容。

### 5. 缓存框架

- Django提供了缓存框架，可以缓存页面、查询结果等，以提高网站性能。

### 6. 认证系统

- Django的认证系统包括用户认证、权限控制和会话管理。

### 7. 国际化和本地化

- Django支持国际化和本地化，使得开发多语言网站变得简单。

### 8. 内容管理系统（CMS）功能

- Django的CMS功能允许开发者构建内容丰富的网站。

### 9. 测试框架

- Django内置了测试框架，帮助开发者编写和运行测试用例。

### 10. 信号系统

- Django的信号系统允许在框架内部的特定事件发生时触发自定义代码。

### 11. 中间件

- Django的中间件框架允许在请求和响应处理过程中插入自定义代码。

### 12. 静态文件管理

- Django提供了静态文件管理机制，用于处理CSS、JavaScript和图片等静态资源。

### 13. 内置的分页工具

- Django的分页工具可以帮助开发者轻松实现分页功能。

### 14. 内置的RSS和Atom订阅

- Django支持生成RSS和Atom订阅源。

### 15. 内置的API框架

- Django REST framework是一个强大的、灵活的工具包，用于构建Web API。



## django中model的SlugField类型字段有什么用途

在Django中，`SlugField`是一个模型字段类型，主要用于存储简短的标签或标识符，通常用于URL的友好表示。"Slug"一词来源于新闻出版业，指的是文章标题的简短版本，通常包含字母、数字、下划线或连字符。

### SlugField的主要用途

1. 1.**URL友好**：`SlugField`生成的值可以作为URL的一部分，使得URL更加友好和易于理解。

2. 2.**唯一性**：虽然`SlugField`默认不强制唯一性，但可以通过设置`unique=True`参数来确保字段值的唯一性。

3. 3.**可读性**：`SlugField`生成的字符串通常包含单词和连字符，使得URL更加可读。

4. 4.**搜索引擎优化（SEO）**：使用`SlugField`生成的友好URL有助于搜索引擎优化，因为它们通常包含关键词。

5. 5.**数据库查询优化**：在数据库中使用`SlugField`可以提高查询效率，尤其是在需要根据标识符进行快速查找的场景。

### 示例

假设有一个`Article`模型，我们希望每个文章都有一个友好的URL标识符：

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
```

在这个例子中，`slug`字段可以存储文章标题的简短版本，例如："my-cool-article"。这个`slug`可以用于生成文章的URL，如`/articles/my-cool-article/`。

### 注意事项

- `SlugField`通常需要在保存模型实例之前手动设置其值，或者使用Django的信号或方法自动生成。
- 在生成`slug`时，通常会将标题转换为小写，并用连字符替换空格和其他非字母数字字符。
- 由于`slug`字段通常用于URL，因此在设计时应考虑其对SEO的影响。

通过使用`SlugField`，Django允许开发者创建更加友好和易于管理的URL结构，从而提升用户体验和网站的SEO表现。



## django 中想要验证表单提交是否格式正确需要用到form中的哪个方法

```
A. form.save()
B.form.save(commit=False)
C.form.verify()
D. form.is_valid()   √
```



## django常见的线上部署方式有哪几种？

Django的线上部署架构可以根据应用的规模、性能要求和预算等因素进行设计。以下是一个常见的Django线上部署架构示例：

### 1. 负载均衡器（Load Balancer）

- **作用**：负责分发流量到多个Web服务器，以提高应用的可用性和扩展性。
- **技术选择**：可以使用硬件负载均衡器或软件负载均衡器（如Nginx、HAProxy）。

### 2. Web服务器

- **作用**：处理客户端的HTTP请求，并将请求转发给Django应用。
- **技术选择**：常用的Web服务器有Nginx和Apache。Nginx因其高性能和轻量级而被广泛推荐。

### 3. 应用服务器

- **作用**：运行Django应用，处理业务逻辑。
- **技术选择**：可以使用Gunicorn、uWSGI等WSGI服务器运行Django应用。

### 4. 数据库服务器

- **作用**：存储和管理应用数据。
- **技术选择**：可以使用MySQL、PostgreSQL、SQLite等数据库系统。对于大型应用，推荐使用主从复制或分片技术来提高数据库的性能和可靠性。

### 5. 缓存系统

- **作用**：缓存频繁访问的数据，减少数据库的负载。
- **技术选择**：可以使用Redis、Memcached等内存缓存系统。

### 6. 文件存储

- **作用**：存储用户上传的文件和静态文件。
- **技术选择**：可以使用本地文件系统、云存储服务（如Amazon S3）或分布式文件系统。

### 7. 日志管理

- **作用**：收集和分析应用日志，帮助监控应用状态和性能。
- **技术选择**：可以使用ELK（Elasticsearch、Logstash、Kibana）堆栈或Graylog等日志管理工具。

### 8. 安全措施

- **作用**：保护应用免受攻击。
- **技术选择**：使用HTTPS、防火墙、DDoS防护、Web应用防火墙（WAF）等。

### 9. 持续集成/持续部署（CI/CD）

- **作用**：自动化测试和部署流程，提高开发效率和应用质量。
- **技术选择**：可以使用Jenkins、GitLab CI/CD、GitHub Actions等工具。

### 10. 监控和报警

- **作用**：监控应用的运行状态，及时发现和处理问题。
- **技术选择**：可以使用Prometheus、Grafana、New Relic等监控工具。

### 结论

一个典型的Django线上部署架构通常包括负载均衡器、Web服务器、应用服务器、数据库服务器、缓存系统、文件存储、日志管理、安全措施、CI/CD流程和监控报警系统。这样的架构设计旨在提高应用的可用性、性能和安全性。根据具体需求，可能还需要对架构进行调整和优化。



提供一个具体的Django线上部署架构示例，适用于中到大型Web应用：

### 1. 负载均衡器

- **技术选择**：Nginx或HAProxy
- **作用**：分发请求到多个Web服务器，提高可用性和扩展性。

### 2. Web服务器

- **技术选择**：Nginx
- **作用**：处理客户端的HTTP请求，提供静态文件服务。

### 3. 应用服务器

- **技术选择**：Gunicorn或uWSGI
- **作用**：运行Django应用，处理业务逻辑。

### 4. 数据库服务器

- **技术选择**：PostgreSQL或MySQL
- **作用**：存储和管理应用数据。

### 5. 缓存系统

- **技术选择**：Redis或Memcached
- **作用**：缓存频繁访问的数据，减少数据库负载。

### 6. 文件存储

- **技术选择**：Amazon S3或本地文件系统
- **作用**：存储用户上传的文件和静态文件。

### 7. 日志管理

- **技术选择**：ELK（Elasticsearch、Logstash、Kibana）堆栈
- **作用**：收集和分析应用日志。

### 8. 安全措施

- **技术选择**：Let's Encrypt（免费的HTTPS证书）、防火墙、DDoS防护、Web应用防火墙（WAF）
- **作用**：保护应用免受攻击。

### 9. 持续集成/持续部署（CI/CD）

- **技术选择**：Jenkins或GitLab CI/CD
- **作用**：自动化测试和部署流程。

### 10. 监控和报警

- **技术选择**：Prometheus和Grafana
- **作用**：监控应用的运行状态，及时发现和处理问题。

### 部署流程

1. 1.**代码部署**：使用Git进行版本控制，通过CI/CD工具自动部署代码到服务器。

2. 2.**静态文件处理**：使用Nginx或Django的`collectstatic`命令来收集静态文件。

3. 3.**数据库迁移**：使用Django的`migrate`命令来应用数据库迁移。

4. 4.**服务启动**：使用Gunicorn或uWSGI启动Django应用。

5. 5.**监控设置**：配置Prometheus和Grafana进行应用监控。

6. 6.**安全配置**：配置HTTPS证书、防火墙和WAF。

### 结论

这个架构组合提供了一个高可用、可扩展和安全的Django应用部署方案。它结合了多种技术和工具来确保应用的稳定运行和高效管理。根据应用的具体需求和资源，这个架构可以进一步调整和优化。

## django 请求的生命周期?

```
从用户输入url到用户看到网页的整个过程:
1.用户输入网址，浏览器发起请求
2.WsGI(服务器网关接口)创建 socket服务端，接受请求
3.中间件处理请求
4.url路由，根据当前请求的url找到相应的视图函数
5.进入view，进行业务处理，执行类或者函数，返回字符串
6.再次通过中间件处理相应7.WSGI返回响应8.浏览器渲染
```

![image-20240803210001048](WEB%E6%A1%86%E6%9E%B6-%E9%9D%A2%E8%AF%95%E9%A2%98.assets/image-20240803210001048.png)



## django 中如何在model保存前做一定的固定操作，比如写一句日志？

在Django中，如果你需要在模型保存前执行一些固定操作，比如写日志，你可以通过重写模型的`save()`方法来实现。`save()`方法是Django模型在保存数据到数据库之前调用的方法，通过重写它，你可以在保存数据之前添加自定义的逻辑。

### 示例

假设你有一个`Book`模型，并希望在每次保存书籍信息之前记录一条日志：

```python
from django.db import models
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

     def save(self, *args, **kwargs):
         # 在保存前执行的日志记录
         logger.info(f"Saving book: {self.title} by {self.author}")
         
         # 调用父类的save()方法完成保存操作
         super(Book, self).save(*args, **kwargs)
```

在这个例子中，`save()`方法首先记录了一条日志信息，然后调用父类的`save()`方法来完成实际的保存操作。这样，每次调用`Book`模型的`save()`方法时，都会先记录一条日志。

### 注意事项

- **调用父类方法**：在重写`save()`方法时，务必调用`super()`来确保父类的`save()`方法被调用，这样Django才能正确地处理模型的保存逻辑。
- **事务处理**：如果在保存过程中需要处理事务，确保在`save()`方法中正确处理事务的开始和提交。
- **性能考虑**：在`save()`方法中添加的逻辑应尽量高效，避免执行复杂的操作或长时间的阻塞调用。



## 简述django FBV和CBV?

Django框架中，FBV（Function-Based View）和CBV（Class-Based View）是两种不同的视图实现方式。它们各自有不同的特点和使用场景。

### FBV（Function-Based View）

- **定义**：FBV是基于函数的视图，即视图逻辑通过Python函数来实现。
- **特点**：
  - 简单直观：对于简单的视图逻辑，FBV更直观易懂。
  - 灵活性高：函数可以轻松地组合和重用。
  - 适合小型项目或简单的视图逻辑。
- **示例**：

```python
from django.http import HttpResponse

def my_view(request):
     return HttpResponse("Hello, world. You're at the polls index.")
```

### CBV（Class-Based View）

- **定义**：CBV是基于类的视图，即视图逻辑通过继承自Django提供的视图类来实现。
- **特点**：
  - 结构化：CBV通过类的继承和方法重写提供了更结构化的视图实现方式。
  - 功能丰富：Django提供了多种预定义的类视图，如`ListView`、`DetailView`等，这些类视图提供了丰富的功能。
  - 适合大型项目或复杂的视图逻辑。
- **示例**：

```python
from django.views import View
from django.http import HttpResponse

class MyView(View):
     def get(self, request, *args, **kwargs):
         return HttpResponse("Hello, world. You're at the polls index.")
```

### 总结

- **选择标准**：对于简单的视图逻辑，FBV可能更简单直接；而对于需要复用逻辑或更复杂功能的场景，CBV提供了更强大的结构化和功能。
- **灵活性与结构化**：FBV提供了更高的灵活性，而CBV则在结构化和功能复用方面表现更佳。
- **实际应用**：在实际开发中，可以根据项目的具体需求和开发者的偏好选择使用FBV或CBV。



## 如何给django CBV 的函数设置添加装饰器?

在Django中，给基于类的视图（Class-Based Views，CBV）的函数设置添加装饰器，可以通过在类中定义特定的方法，并在这些方法上应用装饰器来实现。以下是一个示例，展示如何给`ListView`的`get`方法添加装饰器：

### 示例

假设我们有一个`ListView`的子类`BookListView`，我们想给它的`get`方法添加一个装饰器`my_decorator`：

```python
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

     @method_decorator(login_required)
     def dispatch(self, *args, **kwargs):
          return super(BookListView, self).dispatch(*args, **kwargs)

     @method_decorator(login_required)
     def get(self, request, *args, **kwargs):
          # 其他逻辑...
          return super(BookListView, self).get(request, *args, **kwargs)
```

在这个例子中，我们使用了`method_decorator`来将`login_required`装饰器应用到`dispatch`和`get`方法上。`dispatch`方法是Django CBV的入口点，它会根据请求类型（GET、POST等）调用相应的方法（如`get`、`post`等）。通过在`dispatch`方法上应用装饰器，可以确保所有请求都会经过装饰器的处理。

### 注意事项

- **装饰器的选择**：确保你使用的装饰器适用于类视图的方法。例如，`login_required`装饰器适用于需要用户登录的视图。
- **方法的选择**：通常，你可能需要在`dispatch`方法上应用装饰器，以确保所有请求类型都经过装饰器处理。对于特定类型的请求（如GET或POST），你也可以在对应的方法上应用装饰器。
- **继承和重写**：如果你在子类中重写了父类的方法，确保在重写的方法上应用装饰器。



## django如何连接多个数据库并实现读写分离？

在Django中连接多个数据库并实现读写分离，通常需要使用Django的数据库路由（Database Routers）功能。数据库路由允许你根据应用的需要，将不同的数据库操作（如读取和写入）定向到不同的数据库。

### 步骤

1. 1.**配置数据库**：在Django的`settings.py`文件中配置多个数据库连接。

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db1',
        'USER': 'user1',
        'PASSWORD': 'password1',
        'HOST': 'localhost',
        'PORT': '',
    },
    'secondary': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db2',
        'USER': 'user2',
        'PASSWORD': 'password2',
        'HOST': 'localhost',
        'PORT': '',
    },
}
```

1. 2.**定义数据库路由**：创建一个数据库路由类，用于控制模型的读写操作应该使用哪个数据库。

```python
from django.db import router

class CustomRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'myapp':
            return 'secondary'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'myapp':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model=None, **hints):
        return True
```

在这个例子中，`myapp`应用的读操作将使用`secondary`数据库，而写操作将使用`default`数据库。

1. 3.**应用数据库路由**：在`settings.py`中指定数据库路由类。

```python
DATABASE_ROUTERS = ['path.to.CustomRouter']
```

1. 4.**使用模型**：在你的Django应用中使用模型，Django将根据数据库路由的规则自动选择数据库。

### 注意事项

- **数据库连接**：确保每个数据库的连接信息都正确配置。
- **路由逻辑**：根据你的应用需求，自定义数据库路由逻辑。例如，你可以根据模型的名称、应用标签或其他条件来决定使用哪个数据库。
- **事务处理**：在使用多个数据库时，需要特别注意事务的处理。Django的事务管理默认只对默认数据库有效，如果需要跨数据库事务，可能需要额外的处理。



## django的Form组件中，如果字段中包含choices参数，请使用两种方式实现数据源实时更新。

```
方式一：重写初始化方法，在构造方法中重新去数据库获取值
class UserForm(Form) :
    ut id = fields.ChoiceField(choices=())
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['ut_id'].choices =models.UserType.objects.all().values_list('id', 'title')


方式二：ModelChoiceField字段
class UserForm(Form) :#从另一张依赖表中提取数据ut id=ModelChoiceField(queryset=models.UserType.objects.all())
依赖表：
class UserType(models.Model):
    title = models.CharField(max_length=32)
```



## django 的Model中的ForeignKey 字段中的on_delete参数有什么作用？

在Django的模型中，`ForeignKey`字段用于定义模型之间的关联关系，其中`on_delete`参数是一个非常重要的属性，它指定了当关联的对象被删除时，当前对象应该如何处理。

### `on_delete`参数的作用

- **定义删除行为**：`on_delete`参数定义了当被关联的对象（即`ForeignKey`指向的对象）被删除时，当前对象（即包含`ForeignKey`字段的对象）的处理方式。
- **维护数据完整性**：通过设置`on_delete`参数，可以确保数据库中的数据完整性，防止出现孤立的外键引用。

### `on_delete`参数的选项

Django提供了多种`on_delete`参数的选项，包括但不限于：

- `CASCADE`：级联删除。当被关联的对象被删除时，当前对象也会被删除。这是默认选项。
- `PROTECT`：保护。当被关联的对象被删除时，会抛出`ProtectedError`异常，阻止删除操作。
- `SET_NULL`：设置为空。当被关联的对象被删除时，当前对象的外键字段会被设置为`NULL`。要求外键字段允许`NULL`值。
- `SET_DEFAULT`：设置默认值。当被关联的对象被删除时，当前对象的外键字段会被设置为默认值。
- `SET()`：设置为特定值。当被关联的对象被删除时，当前对象的外键字段会被设置为`SET()`函数中指定的值。
- `DO_NOTHING`：不采取任何操作。当被关联的对象被删除时，当前对象不会有任何改变。这可能会导致数据库中出现孤立的外键引用。

### 示例

假设有一个`Book`模型和一个`Author`模型，`Book`模型通过`ForeignKey`与`Author`模型关联：

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

在这个例子中，如果一个`Author`对象被删除，所有关联的`Book`对象也会被级联删除。

### 注意事项

- 选择合适的`on_delete`行为非常重要，因为它直接影响到数据的完整性和业务逻辑的正确性。
- 在设计数据库模型时，应仔细考虑`on_delete`参数的设置，确保它符合业务需求和数据完整性要求。





## django中csrf 的实现机制?

在Django中，CSRF（跨站请求伪造）的实现机制主要依赖于CSRF令牌（token）。CSRF是一种安全措施，用于防止恶意网站通过用户的浏览器向受信任的网站发送请求。Django通过在用户会话中存储一个CSRF令牌，并在表单提交时验证这个令牌来防止CSRF攻击。

### CSRF实现机制的步骤

1. 1.**生成CSRF令牌**：当用户登录到Django网站时，Django会在用户的会话中生成一个CSRF令牌，并将其存储在会话中。

2. 2.**在表单中包含CSRF令牌**：Django的表单系统会自动在每个POST表单中包含一个隐藏的CSRF令牌字段。这个字段的值是会话中的CSRF令牌。

3. 3.**提交表单时验证CSRF令牌**：当用户提交表单时，Django会检查表单中包含的CSRF令牌是否与会话中的CSRF令牌相匹配。如果匹配，则认为请求是合法的；如果不匹配或令牌缺失，则认为请求可能是CSRF攻击，Django将拒绝处理该请求。

### 示例

在Django模板中，使用`{% csrf_token %}`标签自动添加CSRF令牌：

```html
<form method="post">
    {% csrf_token %}
     <!-- 表单字段 -->
     <input type="submit" value="Submit">
</form>
```

### 注意事项

- **CSRF保护默认开启**：Django默认开启CSRF保护，以防止CSRF攻击。
- **CSRF令牌的唯一性**：每个用户的会话都有一个唯一的CSRF令牌，这增加了安全性。
- **跨域请求**：在处理跨域请求时，需要特别注意CSRF保护的配置，因为跨域请求可能无法携带CSRF令牌。
- **AJAX请求**：对于AJAX请求，需要在请求中包含CSRF令牌，可以通过设置`X-CSRFToken`请求头或在请求体中包含CSRF令牌。



 **CSRF**

CSRF（Cross-Site Request Forgery，跨站请求伪造）是一种常见的网络安全攻击方式，它利用了网站对用户浏览器的信任。攻击者通过诱导用户在已认证的Web应用中执行非预期的操作，从而达到恶意目的。例如，如果用户已经登录了银行网站，攻击者可能会诱使用户点击一个链接，导致用户在不知情的情况下向银行网站发送一个转账请求。

### CSRF攻击的原理

CSRF攻击通常涉及以下步骤：

1. 1.**用户登录**：用户登录到一个受信任的网站（如银行网站）。

2. 2.**攻击者诱导**：攻击者通过某种方式诱导用户访问一个恶意网站或点击一个恶意链接。

3. 3.**发送请求**：恶意网站或链接会向受信任的网站发送一个请求，这个请求看起来像是用户主动发起的，因为请求中包含了用户的会话信息（如Cookies）。

4. 4.**执行操作**：受信任的网站接收到请求后，由于信任用户的会话信息，会执行请求中的操作，如转账、更改密码等。

### CSRF的防御措施

为了防御CSRF攻击，Django等现代Web框架提供了多种机制：

1. 1.**CSRF令牌**：Django在用户会话中存储一个CSRF令牌，并在每个需要保护的表单中包含这个令牌。当表单提交时，Django会验证提交的令牌是否与会话中的令牌匹配。如果不匹配，请求将被拒绝。

2. 2.**SameSite Cookie属性**：现代浏览器支持`SameSite`属性，可以设置Cookie仅在同站请求中发送，从而减少CSRF攻击的风险。

3. 3.**安全的HTTP方法**：使用GET以外的HTTP方法（如POST、PUT、DELETE等）进行敏感操作，因为GET请求通常不会引起用户警觉。

4. 4.**验证用户意图**：要求用户在执行敏感操作前进行额外的验证，如输入密码、验证码等。

5. 5.**限制请求来源**：通过检查HTTP请求头中的`Referer`字段，确保请求来自预期的来源。



## 基于django使用ajax发送post 请求时，有哪种方法携带csrftoken?

在Django中，为了防止跨站请求伪造（CSRF）攻击，需要在发送AJAX POST请求时携带CSRF令牌。以下是几种常见的方法来在AJAX请求中携带CSRF令牌：

### 方法1：使用jQuery的ajaxSetup

如果你使用jQuery，可以在发送AJAX请求之前使用`$.ajaxSetup()`方法来全局设置CSRF令牌：

```javascript
$(document).ready(function(){
     $.ajaxSetup({
         beforeSend: function(xhr, settings) {
             if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                 xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
             }
         }
     });
});

function csrfSafeMethod(method) {
     // 这些HTTP方法不需要CSRF保护
     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
```

### 方法2：在AJAX请求中手动设置

在发送AJAX请求时，可以手动在请求头中设置CSRF令牌：

```javascript
$.ajax({
     type: "POST",
     url: "/your-endpoint/",
     data: {
         // 你的数据
     },
     beforeSend: function(xhr) {
         xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
     },
     success: function(data) {
         // 处理响应
     }
});
```

### 方法3：使用Django的CsrfViewMiddleware

Django的`CsrfViewMiddleware`中间件会自动在每个POST请求中检查CSRF令牌。如果你使用jQuery，确保在AJAX请求中包含CSRF令牌，如方法2所示。

### 方法4：使用Django的@csrf_exempt装饰器

如果你需要对特定视图禁用CSRF保护，可以在视图函数上使用`@csrf_exempt`装饰器：

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):
     # 你的视图逻辑
```

### 注意事项

- 确保在发送AJAX请求之前，CSRF令牌已经通过某种方式被包含在请求中。
- 如果你的网站使用了CORS（跨源资源共享），确保在CORS策略中允许携带凭证（如Cookies）。
- 在使用`@csrf_exempt`装饰器时要小心，因为它会使视图对CSRF攻击变得脆弱。



## django路由系统中name的作用？

在Django的路由系统中，`name`参数用于给URL模式命名，它具有以下作用：

### 1. URL反向解析

`name`参数允许你通过一个唯一的名称来引用URL模式，而不是硬编码URL。这在Django项目中非常有用，特别是在需要在模板、视图或其他地方引用URL时。

#### 示例

假设你有一个名为`article`的视图，你给它对应的URL模式命名：

```python
from django.urls import path
from . import views

urlpatterns = [
    path('articles/<int:year>/', views.article, name='article'),
]
```

在模板中，你可以使用`{% url %}`模板标签来引用这个URL：

```html
<a href="{% url 'article' year=2023 %}">2023年文章</a>
```

### 2. 代码可维护性

通过使用命名URL，你可以轻松地更改URL模式而不影响项目中引用该URL的代码。这使得代码更加灵活和可维护。

### 3. 团队协作

在团队协作中，命名URL有助于团队成员理解URL的用途和结构，从而提高代码的可读性和协作效率。

### 4. 项目文档

命名URL可以作为项目文档的一部分，帮助开发者快速理解项目中定义的URL结构。

### 注意事项

- 每个URL模式的名称必须是唯一的。
- 在使用`{% url %}`模板标签时，确保传递正确的参数，以匹配URL模式中定义的参数。



## django 的模板中 filter、simpletag、inclusiontag 的区别?

在Django模板系统中，`filter`、`simpletag`和`inclusiontag`是三种不同的模板标签，它们用于扩展模板的功能。

### Filter

- **定义**：模板过滤器（filter）用于对模板中的变量进行处理，返回处理后的结果。
- **使用场景**：适用于简单的数据转换或格式化。
- **示例**：`{{ value|upper }}`将`value`转换为大写。

### SimpleTag

- **定义**：简单标签（simpletag）用于执行更复杂的操作，可以接受任意数量的参数，并返回一个值。
- **使用场景**：适用于需要执行一些逻辑处理的场景，如生成统计数据、格式化日期等。
- **示例**：自定义一个返回当前时间的简单标签：

```python
from django import template

register = template.Library()

@register.simpletag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
```

在模板中使用：

```html
{% current_time "%Y-%m-%d %H:%M:%S" %}
```

### InclusionTag

- **定义**：包含标签（inclusiontag）用于渲染一个完整的HTML片段，并将上下文变量传递给这个片段。
- **使用场景**：适用于需要渲染一个包含多个变量的复杂HTML结构的场景。
- **示例**：自定义一个显示文章列表的包含标签：

```python
from django import template

register = template.Library()

@register.inclusion_tag('myapp/tags/latest_articles.html')
def latest_articles(count=5):
    articles = Article.objects.order_by('-publish_date')[:count]
    return {'articles': articles}
```

在模板中使用：

```html
{% load myapp_tags %}
{% latest_articles 10 as latest %}
<ul>
{% for article in latest.articles %}
    <li>{{ article.title }}</li>
{% endfor %}
</ul>
```

### 总结

- **Filter**：用于简单的数据处理，直接在模板中使用。
- **SimpleTag**：用于执行复杂的逻辑处理，返回一个值。
- **InclusionTag**：用于渲染一个完整的HTML片段，可以传递多个变量。



## django-debug-toolbar 的作用?

`django-debug-toolbar`是一个强大的Django开发工具，它提供了一个侧边栏，显示了当前请求/响应周期中的各种调试信息。这个工具对于开发和调试Django应用非常有用，因为它可以提供关于请求、数据库查询、缓存、信号、路由等的详细信息。

### 主要功能

1. 1.**请求详情**：显示当前请求的详细信息，包括请求方法、路径、查询参数、表单数据等。

2. 2.**SQL查询**：列出所有执行的数据库查询，包括查询时间、查询语句和返回的行数。

3. 3.**缓存使用**：显示缓存的使用情况，包括缓存命中和未命中次数。

4. 4.**信号**：列出在请求期间触发的Django信号。

5. 5.**模板**：显示渲染的模板及其上下文变量。

6. 6.**静态文件**：列出请求中使用的静态文件。

7. 7.**路由**：显示匹配当前请求的URL路由。

8. 8.**设置**：显示Django项目的设置信息。

9. 9.**时间线**：提供一个时间线视图，显示请求处理的各个阶段所花费的时间。

### 安装和配置

1. 1.**安装**：通过pip安装`django-debug-toolbar`：`pip install django-debug-toolbar `

2. 2.**配置**：在Django项目的`settings.py`文件中添加`debug_toolbar`到`INSTALLED_APPS`，并配置中间件：

3. ```py
   INSTALLED_APPS = [
       # ...
       'debug_toolbar',
       # ...
   ]
   
   MIDDLEWARE = [
       # ...
       'debug_toolbar.middleware.DebugToolbarMiddleware',
       # ...
   ]
   
   INTERNAL_IPS = [
       '127.0.0.1',
   ]
   ```

4. 

5. 3.**URL配置**：在项目的`urls.py`文件中添加`debug_toolbar`的URL配置：

6. ```py
   import debug_toolbar
   
   urlpatterns = [
       # ...
       path('__debug__/', include(debug_toolbar.urls)),
       # ...
   ]
   ```

7. 

### 注意事项

- `django-debug-toolbar`只应在开发环境中使用，不应在生产环境中启用。
- 确保`INTERNAL_IPS`设置包含你的开发机器的IP地址，以便`debug_toolbar`只对这些IP地址可见。



## django 中如何实现单元测试?

### 1. 编写测试用例

在你的应用目录下创建一个`tests.py`文件，用于编写测试用例。测试用例通常继承自`django.test.TestCase`类。

#### 示例

```python
from django.test import TestCase
from .models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
         # 设置测试环境，例如创建测试数据
         MyModel.objects.create(name="Test Model")

     def test_my_model(self):
         # 测试MyModel的某个功能
         obj = MyModel.objects.get(name="Test Model")
         self.assertEqual(obj.name, "Test Model")
```

### 2. 运行测试

使用Django的`manage.py`工具来运行测试：

```bash
python manage.py test
```

这将自动发现并运行所有应用中的测试用例。

### 3. 测试数据库

Django为测试提供了一个特殊的测试数据库，它在测试开始时创建，并在测试结束时销毁。这意味着测试不会影响生产数据。

### 4. 测试视图

Django的测试框架也支持测试视图。你可以使用`TestCase`类的`client`属性来模拟HTTP请求。

#### 示例

```python
class MyViewTestCase(TestCase):
    def test_my_view(self):
         response = self.client.get('/my-url/')
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, 'Expected Text')
```

### 5. 测试表单

测试表单时，可以使用`TestCase`类的`form_factory`方法来创建表单实例，并进行验证。

#### 示例

```python
from django.forms import Form

class MyFormTestCase(TestCase):
    def test_my_form(self):
         form_data = {'field': 'value'}
         form = MyForm(data=form_data)
         self.assertTrue(form.is_valid())
```

### 6. 测试模型方法

如果需要测试模型中的方法，可以直接在测试用例中调用这些方法，并验证结果。

#### 示例

```python
class MyModelTestCase(TestCase):
    def test_my_model_method(self):
         obj = MyModel.objects.create(name="Test Model")
         result = obj.my_model_method()
         self.assertEqual(result, expected_value)
```

### 注意事项

- 确保在`settings.py`中设置了`TEST_RUNNER`，Django默认使用`DiscoverRunner`。
- 测试用例应该独立于其他测试，避免相互影响。
- 测试用例应该尽可能覆盖所有可能的代码路径。



## 解释orm中 db first和code first的含义?

在ORM（对象关系映射）中，"db first"和"code first"是两种不同的数据库设计方法，它们描述了从数据库结构到代码模型的生成过程。

### DB First（数据库优先）

- **含义**：DB First方法是指先设计数据库，然后根据数据库的结构生成代码模型。在这种方法中，数据库的表结构是设计的起点，代码模型是基于这个结构来创建的。

- 步骤

  ：

  1. 1.设计数据库表结构。

  2. 2.创建数据库和表。

  3. 3.使用ORM工具根据数据库表结构生成代码模型。

- **适用场景**：适用于已有数据库结构，需要生成代码模型以便在应用程序中使用的情况。

### Code First（代码优先）

- **含义**：Code First方法是指先编写代码模型，然后根据代码模型生成数据库结构。在这种方法中，代码模型是设计的起点，数据库结构是基于代码模型来创建的。

- 步骤

  ：

  1. 1.编写代码模型（类和属性）。

  2. 2.使用ORM工具根据代码模型生成数据库表结构。

  3. 3.创建数据库和表。

- **适用场景**：适用于从零开始设计新应用，或者希望代码模型驱动数据库设计的情况。

### 选择DB First或Code First

选择DB First还是Code First取决于项目的具体需求和开发流程：

- **DB First**：适合已有数据库的情况，或者当数据库设计是项目的核心部分时。
- **Code First**：适合新项目，或者希望代码模型驱动数据库设计的情况，它提供了更大的灵活性和控制力。

在实际应用中，这两种方法可以结合使用，例如，可以先使用Code First方法设计核心模型，然后根据需要调整数据库结构，或者在现有数据库的基础上添加新的代码模型。



## django 中如何根据数据库表生成 model 类？

在Django中，如果你已经有了数据库表，但还没有相应的Django模型类，你可以使用Django的`inspectdb`命令来根据现有的数据库表自动生成Django模型类。这个命令会读取数据库中的表结构，并生成相应的Django模型代码。

### 使用步骤

1. 1.**运行`inspectdb`命令**：在命令行中运行`python manage.py inspectdb`，这将输出当前数据库中所有表的Django模型代码。

2. 2.**重定向输出到文件**：如果你想要将生成的模型代码保存到文件中，可以使用重定向操作符`>`。例如：

3. ```bash
   python manage.py inspectdb > models.py
   ```

4. 

5. 这会将所有表的模型代码输出到当前目录下的`models.py`文件中。

6. 3.**手动调整生成的代码**：生成的模型代码可能需要一些手动调整，比如添加字段的注释、设置`db_table`属性、添加模型方法等。

7. 4.**将模型添加到应用中**：将生成的模型类添加到你的Django应用的`models.py`文件中，并确保在`__init__.py`文件中导入这些模型。

### 注意事项

- `inspectdb`命令生成的模型代码是基于当前数据库表结构的快照，如果数据库表结构发生变化，需要重新运行`inspectdb`命令。
- 生成的模型代码可能不包含所有Django模型的高级特性，如`choices`、`related_name`等，这些需要手动添加。
- 生成的模型代码可能需要根据实际业务逻辑进行调整和优化。



## 使用orm和原生sql的优缺点?

### 使用ORM的优点

1. 1.**抽象层次高**：ORM抽象了数据库操作，开发者不需要编写SQL语句，而是通过操作对象来完成数据库操作。

2. 2.**数据库无关性**：ORM允许开发者编写与数据库无关的代码，使得代码可以在不同的数据库系统之间迁移。

3. 3.**安全性**：ORM可以防止SQL注入攻击，因为它自动处理数据的转义和引用。

4. 4.**维护性**：使用ORM编写的代码通常更易于维护和理解，因为代码更接近业务逻辑。

5. 5.**代码复用**：ORM提供了丰富的API，可以复用代码，减少重复工作。

### 使用ORM的缺点

1. 1.**性能开销**：ORM操作通常比原生SQL慢，因为它需要进行额外的映射和处理。

2. 2.**复杂查询限制**：对于非常复杂的查询，ORM可能不够灵活或效率低下。

3. 3.**学习曲线**：对于初学者来说，理解ORM的工作原理和最佳实践可能需要时间。

4. 4.**资源消耗**：ORM可能会消耗更多的内存和CPU资源，特别是在处理大量数据时。

### 使用原生SQL的优点

1. 1.**性能**：原生SQL通常比ORM更快，因为它直接与数据库交互，没有额外的抽象层。

2. 2.**灵活性**：对于复杂的查询和数据库特定的操作，原生SQL提供了更高的灵活性。

3. 3.**控制力**：开发者可以完全控制SQL语句，精确地执行所需的数据库操作。

### 使用原生SQL的缺点

1. 1.**数据库依赖性**：原生SQL代码通常与特定的数据库系统紧密相关，迁移数据库时需要修改代码。

2. 2.**安全性风险**：如果手动编写SQL语句，容易出现SQL注入等安全问题。

3. 3.**维护难度**：原生SQL代码可能难以理解和维护，特别是当查询变得复杂时。

4. 4.**重复工作**：对于常见的数据库操作，原生SQL可能需要重复编写相似的代码。



## django 的 contenttype 组件的作用?

Django的`contenttypes`组件是一个内置的应用，它提供了一种机制来动态地引用和操作Django项目中的任何模型。这个组件的核心是`ContentType`模型，它能够存储关于项目中所有其他模型的信息，包括模型的名称、应用标签和模型的Python路径。

### 主要作用

1. 1.**动态引用模型**：通过`ContentType`模型，可以动态地获取任何模型的类引用，这在需要在运行时根据名称或标识符来引用模型时非常有用。

2. 2.**通用关系**：`contenttypes`组件允许创建通用关系（generic relations），这意味着可以将任何模型实例关联到任何其他模型实例。这在需要灵活地关联不同类型的数据时非常有用。

3. 3.**管理通用权限**：在Django的权限系统中，`contenttypes`组件用于管理通用权限，允许为任何模型定义权限。

4. 4.**内容类型管理**：`contenttypes`组件提供了一种方式来查询和管理项目中所有模型的元数据，包括它们的名称和应用。

### 使用场景

- **通用视图和表单**：在创建通用视图和表单时，可以使用`contenttypes`来动态地处理不同的模型。
- **内容管理系统**：在内容管理系统（CMS）中，`contenttypes`可以用来创建和管理不同类型的内容。
- **插件系统**：在开发插件系统时，`contenttypes`可以用来动态地注册和管理插件类型。

### 示例

获取一个模型的类引用：

```python
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get(app_label='myapp', model='my_model')
model_class = content_type.model_class()
```

创建通用关系：

```python
from django.contrib.contenttypes.fields import GenericForeignKey

class MyModel(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
```



##      Django中哪里用到了线程?哪里用到了协程?哪里用到了进程?

在Django框架中，线程、协程和进程的使用主要取决于你如何配置和扩展Django应用。Django本身是一个同步框架，但提供了与异步编程和并发处理相关的工具和接口。

### 线程

Django使用线程主要在以下场景：

- **WSGI服务器**：当使用支持多线程的WSGI服务器（如Gunicorn的`--threads`选项）时，服务器会为每个请求创建一个新线程，从而允许并发处理多个请求。
- **数据库连接**：Django的数据库连接池可能会使用线程来管理数据库连接的创建和关闭。
- **缓存**：某些缓存后端（如memcached）可能在内部使用线程来优化性能。

### 协程

Django本身不直接使用协程，但你可以通过以下方式在Django中使用协程：

- **异步视图**：Django 3.1及以上版本支持异步视图。你可以使用`async def`定义异步视图，并在视图中使用`await`来调用异步函数。
- **异步中间件**：Django 3.1及以上版本支持异步中间件。你可以定义异步中间件来处理异步请求。
- **异步数据库操作**：Django的数据库后端支持异步操作，你可以使用异步数据库连接来执行异步查询。

### 进程

Django使用进程主要在以下场景：

- **多进程服务器**：使用多进程WSGI服务器（如uWSGI）时，每个进程可以独立处理请求，提高并发能力。
- **并发执行任务**：Django的`manage.py runserver`命令在开发模式下默认使用单进程，但可以通过`--noreload`选项来运行多个进程。
- **Celery任务队列**：在使用Celery等任务队列时，Django可以将任务分发到不同的进程中执行，实现任务的并发处理。

### 总结

Django框架本身主要使用线程和进程来处理并发请求，但随着Django 3.1及以上版本对异步视图和中间件的支持，协程也开始在Django中发挥作用。通过合理配置和使用异步工具，可以进一步提升Django应用的性能和并发处理能力。



## 对cookie与session的了解？他们能单独用吗?

### Cookie

Cookie是一种服务器发送到用户浏览器并保存在本地的一小块数据，它会在浏览器下次向同一服务器再发起请求时被携带并发送到服务器上。Cookie主要用于以下用途：

- **会话管理**：如用户登录状态、购物车中的商品等。
- **个性化设置**：如用户自定义的界面设置。
- **追踪分析**：如记录和分析用户行为。

### Session

Session是另一种服务器端的存储方式，用于存储特定用户会话所需的属性及配置信息。Session是基于Cookie实现的，但存储在服务器端，通常通过一个唯一的Session ID来识别不同的用户会话。

### Cookie与Session的使用

- **Cookie的使用**：当用户首次访问网站时，服务器会创建一个Session ID，并通过设置Cookie将这个Session ID发送给用户的浏览器。之后，用户的每次请求都会携带这个Session ID，服务器通过这个ID来识别用户并获取相应的Session数据。
- **Session的使用**：Session通常用于存储用户登录状态、购物车信息等需要在服务器端保持的数据。Session数据存储在服务器上，可以是内存、数据库或其他存储系统。

### 单独使用

- **单独使用Cookie**：可以用于存储一些不需要服务器端维护的简单信息，如用户界面设置等。但因为Cookie存储在客户端，所以不适用于存储敏感信息。
- **单独使用Session**：通常不单独使用，因为Session需要依赖于Cookie来传递Session ID。不过，如果是在服务器端直接通过Session ID来管理会话，也可以不直接使用Cookie。



- **单独使用Cookie**：可以，但仅限于存储非敏感信息。
- **单独使用Session**：不可以，因为Session依赖于Cookie来传递Session ID。

### 总结

Cookie和Session通常一起使用来实现Web应用的会话管理。Cookie用于在客户端存储会话标识符（Session ID），而Session用于在服务器端存储会话数据。单独使用Cookie或Session都有其局限性，通常需要结合使用来确保Web应用的安全性和功能性。



## django关闭浏览器，怎样清除 cookies 和 session?

### 作用

- **立即过期**：当`SESSION_EXPIRE_AT_BROWSER_CLOSE`设置为`True`时，一旦用户关闭浏览器，与该浏览器关联的会话将立即过期，无论会话的过期时间（`SESSION_COOKIE_AGE`）设置为多久。
- **安全性提升**：这种设置可以提高安全性，因为用户在关闭浏览器后，即使会话的过期时间还未到，会话也会立即失效，从而减少会话被滥用的风险。
- **用户体验**：对于不需要长时间保持登录状态的应用，这种设置可以提供更好的用户体验，因为用户不需要手动注销。

在Django的`settings.py`文件中，你可以通过设置`SESSION_EXPIRE_AT_BROWSER_CLOSE`为`True`来启用这个功能：

```python
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
```

### 注意事项

- 当`SESSION_EXPIRE_AT_BROWSER_CLOSE`设置为`True`时，`SESSION_COOKIE_AGE`设置将不再影响会话的过期时间，因为会话将在浏览器关闭时立即过期。
- 这种设置可能不适用于所有应用，特别是那些需要用户长时间保持登录状态的应用。



## 接口的幂等性是什么意思？

接口的幂等性（Idempotence）是指在多次执行同一个操作时，其结果与执行一次操作的结果相同。换句话说，无论操作被重复执行多少次，最终的状态都保持不变。

### 幂等性的应用

幂等性在接口设计中非常重要，特别是在分布式系统和Web服务中。它确保了即使在高并发或网络不稳定的情况下，系统的行为也是可预测和一致的。

### 例子

- **HTTP GET请求**：GET请求用于获取资源，多次执行同一个GET请求，返回的资源状态应该是一致的，因此GET请求是幂等的。
- **HTTP PUT请求**：PUT请求用于更新资源，如果多次执行同一个PUT请求，资源的状态应该保持最终更新后的状态，因此PUT请求通常是幂等的。
- **HTTP DELETE请求**：DELETE请求用于删除资源，多次执行同一个DELETE请求，资源应该保持被删除的状态，因此DELETE请求也是幂等的。

### 注意事项

- **非幂等操作**：某些操作天然不具备幂等性，例如POST请求用于创建资源，每次执行POST请求都会创建一个新的资源，因此POST请求不是幂等的。
- **幂等性与安全性**：幂等性并不意味着操作是安全的。例如，虽然DELETE请求是幂等的，但多次执行DELETE请求会导致资源被重复删除，这可能不是预期的行为。

### 结论

在设计接口时，确保操作的幂等性是非常重要的，它有助于提高系统的健壮性和可靠性。特别是在设计RESTful API时，幂等性是设计原则之一，有助于简化客户端和服务器之间的交互。



## Django 创建项目的命令？

django-admin startproject project_name

#创建app

django-admin startapp app_name



## Django创建项目后，项目文件夹下的组成部分（对mvt 的理解）？

在Django中创建一个新项目后，项目文件夹通常包含以下主要组成部分：

### 1. `manage.py`

- **作用**：`manage.py`是一个命令行工具，用于与Django项目交互。它提供了多种管理命令，如启动开发服务器、运行迁移、创建应用等。

### 2. 应用（App）文件夹

- **结构**：每个应用通常是一个独立的文件夹，包含模型（models.py）、视图（views.py）、模板（templates）、静态文件（static）等。
- **作用**：应用是Django项目的组成部分，负责处理特定的功能或数据。

### 3. `settings.py`

- **作用**：`settings.py`文件包含了Django项目的配置信息，如数据库设置、中间件、模板路径、静态文件路径等。

### 4. `urls.py`

- **作用**：`urls.py`文件定义了项目的URL模式和视图之间的映射关系。它告诉Django哪些URL应该由哪个视图处理。

### 5. `wsgi.py`

- **作用**：`wsgi.py`文件提供了与WSGI兼容的Web服务器的入口点，用于部署Django项目。

### 6. `__init__.py`

- **作用**：`__init__.py`文件将目录标记为Python包，使得目录中的模块可以被导入。

### 7. `asgi.py`

- **作用**：`asgi.py`文件提供了与ASGI兼容的Web服务器的入口点，用于部署异步Django项目。

### 8. 其他文件和文件夹

- **静态文件夹**：存放CSS、JavaScript、图片等静态文件。
- **模板文件夹**：存放HTML模板文件。
- **数据库文件**：如SQLite数据库文件（默认情况下，文件名为`db.sqlite3`）。

### 对MVT的理解

Django遵循MVT（Model-View-Template）架构模式：

- **Model（模型）**：负责与数据库交互，定义数据结构和操作数据库的逻辑。
- **View（视图）**：处理用户请求，调用模型获取数据，并决定使用哪个模板渲染响应。
- **Template（模板）**：定义如何展示数据，通常包含HTML和一些模板标签。

通过MVT架构，Django将业务逻辑、数据处理和展示分离，使得代码结构清晰，易于维护和扩展。



## 对MVC,MVT解读的理解?

MVC（Model-View-Controller）和MVT（Model-View-Template）是两种流行的Web应用架构模式，它们都旨在将应用的不同部分分离，以提高代码的可维护性和可扩展性。

### MVC（Model-View-Controller）

MVC模式将Web应用分为三个主要组件：

1. 1.**Model（模型）**：负责数据和业务逻辑。模型代表了应用的数据结构，通常与数据库交互，处理数据的获取、更新和存储。

2. 2.**View（视图）**：负责展示数据。视图是用户界面的组成部分，它从模型中获取数据，并将其展示给用户。

3. 3.**Controller（控制器）**：负责处理用户输入。控制器接收用户的输入（如点击按钮、提交表单等），并调用模型和视图来完成用户的请求。

### MVT（Model-View-Template）

Django框架采用的MVT模式与MVC类似，但有细微的差别：

1. 1.**Model（模型）**：与MVC中的模型相同，负责与数据库交互，定义数据结构和操作数据库的逻辑。

2. 2.**View（视图）**：在Django中，视图负责处理请求并返回响应。它决定使用哪个模板渲染响应，并可能从模型中获取数据。

3. 3.**Template（模板）**：负责展示数据。模板定义了如何展示数据，通常包含HTML和一些模板标签。在Django中，模板用于生成最终的HTML页面，然后由视图返回给用户。

### 对比

- **职责划分**：MVC和MVT都强调将数据处理、用户界面和业务逻辑分离，但MVT中的模板更专注于数据的展示，而MVC中的视图则可能包含更多的逻辑处理。
- **实现细节**：在MVC中，控制器是核心组件，负责协调模型和视图；而在MVT中，视图直接与模型交互，并使用模板来展示数据。
- **框架支持**：MVC是一个通用的架构模式，被许多不同的框架采用，如Ruby on Rails；MVT是Django特有的架构模式。



```
MVC设计模式核心：解耦，让不同的代码块之间降低耦合，增强代码的可扩展和可移植性，实现向后兼容。
M全拼为Model，主要封装对数据库层的访问，对数据库中的数据进行增、删、改、查操作。
v全拼为view，用于封装结果，生成页面展示的html内容。
c全拼为controller，用于接收请求，处理业务逻辑，与Model和view交互，返回结果。
```

![image-20240804182350852](WEB%E6%A1%86%E6%9E%B6-%E9%9D%A2%E8%AF%95%E9%A2%98.assets/image-20240804182350852.png)



```
Django中MVT设计模式-Django框架遵循MVc设计。
M全拼为Mode1，与MVC中的M功能相同，负责和数据库交互，进行数据处理。
v全拼为view，与Mvc中的c功能相同，接收请求，进行业务处理，返回应答。
T全拼为Template,与MVc中的v功能相同，负责封装构造要返回的html。
```

![image-20240804182430398](WEB%E6%A1%86%E6%9E%B6-%E9%9D%A2%E8%AF%95%E9%A2%98.assets/image-20240804182430398.png)



## 启动 Django 服务的方法？

```bash

python manage.py runserver   # 默认监听127.0.0.1:8000

python manage.py runserver 0.0.0.0:8000  #这会使得服务器在所有可用的网络接口上监听。

python manage.py runserver 8080   # 这会启动服务器在端口8080上监听。
```

### 注意事项

- **开发环境**：`runserver`命令仅适用于开发环境，不应在生产环境中使用。
- **自动重载**：Django开发服务器在检测到代码更改时会自动重新加载，这使得开发过程更加便捷。
- **并发处理**：默认情况下，Django开发服务器不支持高并发。对于生产环境，建议使用如Gunicorn、uWSGI等更健壮的WSGI服务器。



## 怎样测试 django 框架中的代码？

```
可以通过以下几种方式：
1.通过python的unittest、pytest库进行测试
2.通过使用第三方组件进行测试，比如django-debug-toolbar
3.通过django中单元测试进行测试
4.通过其他的工具进行测试- postman- jmeter
```



在Django框架中测试代码主要涉及编写和运行单元测试。Django提供了一个强大的测试框架，可以帮助你验证代码的正确性和功能。以下是进行Django代码测试的基本步骤：

### 1. 编写测试用例

在你的Django应用目录下创建一个`tests.py`文件，用于编写测试用例。测试用例通常继承自`django.test.TestCase`类。

#### 示例

```python
from django.test import TestCase
from .models import MyModel

class MyModelTestCase(TestCase):
     def setUp(self):
          # 设置测试环境，例如创建测试数据
          MyModel.objects.create(name="Test Model")

     def test_my_model(self):
          # 测试MyModel的某个功能
          obj = MyModel.objects.get(name="Test Model")
          self.assertEqual(obj.name, "Test Model")
```

### 2. 运行测试

使用Django的`manage.py`工具来运行测试：

```bash
python manage.py test
```

这将自动发现并运行所有应用中的测试用例。

### 3. 测试数据库

Django为测试提供了一个特殊的测试数据库，它在测试开始时创建，并在测试结束时销毁。这意味着测试不会影响生产数据。

### 4. 测试视图

Django的测试框架也支持测试视图。你可以使用`TestCase`类的`client`属性来模拟HTTP请求。

#### 示例

```python
from django.test import TestCase

class MyViewTestCase(TestCase):
     def test_my_view(self):
          response = self.client.get('/my-url/')
          self.assertEqual(response.status_code, 200)
          self.assertContains(response, 'Expected Text')
```

### 5. 测试表单

测试表单时，可以使用`TestCase`类的`form_factory`方法来创建表单实例，并进行验证。

#### 示例

```python
from django import forms
from django.test import TestCase

class MyFormTestCase(TestCase):
     def test_my_form(self):
          form_data = {'field': 'value'}
          form = MyForm(data=form_data)
          self.assertTrue(form.is_valid())
```

### 6. 测试模型方法

如果需要测试模型中的方法，可以直接在测试用例中调用这些方法，并验证结果。

#### 示例

```python
from django.test import TestCase
from .models import MyModel

class MyModelTestCase(TestCase):
     def test_my_model_method(self):
          obj = MyModel.objects.create(name="Test Model")
          result = obj.my_model_method()
          self.assertEqual(result, expected_value)
```

### 注意事项

- 确保在`settings.py`中设置了`TEST_RUNNER`，Django默认使用`DiscoverRunner`。
- 测试用例应该独立于其他测试，避免相互影响。
- 测试用例应该尽可能覆盖所有可能的代码路径。



## Django 中间件是如何使用的？

在Django中，中间件（Middleware）是位于请求和响应处理过程中的一个框架级钩子，它允许开发者在请求到达视图之前或响应返回给客户端之前执行代码。中间件可以用来实现各种功能，如身份验证、日志记录、会话管理等。

### 使用中间件的步骤

1. 1.**创建中间件类**：在你的Django应用目录下创建一个`middleware.py`文件，并定义一个中间件类。这个类需要实现`__init__`和`__call__`方法。

#### 示例

```python
from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
         self.get_response = get_response
         # 在这里可以初始化一些资源

     def __call__(self, request):
         # 在请求处理之前执行的代码
         response = self.get_response(request)
         # 在响应返回给客户端之前执行的代码
         return response
```

1. 2.**注册中间件**：在Django项目的`settings.py`文件中的`MIDDLEWARE`设置中添加你的中间件类的路径。

#### 示例

```python
MIDDLEWARE = [
     # ...
     'myapp.middleware.MyMiddleware',
     # ...
]
```

### 中间件的执行顺序

- `MIDDLEWARE`列表中的中间件按照列表的顺序执行。列表中的第一个中间件在请求处理的最开始执行，最后一个中间件在响应返回的最后执行。
- 如果中间件需要在请求处理的早期阶段执行，应该将其放在列表的前面；如果需要在响应返回的后期阶段执行，应该将其放在列表的后面。

### 注意事项

- 中间件应该尽量保持轻量级，避免执行复杂的逻辑或长时间的操作。
- 中间件的执行顺序很重要，不同的执行顺序可能会影响中间件的行为和性能。



## 有用过 Django REST framework 吗？谈谈你对它的理解

Django REST framework（DRF）是一个强大的、灵活的工具包，用于构建Web API。它基于Django框架，提供了一套丰富的工具和库，使得开发者可以更快速、更方便地构建和发布RESTful API。

### 功能特点

1. 1.**方便快捷**：DRF提供了许多现成的功能和组件，使得开发者可以快速构建出一个完整的API。

2. 2.**强大的功能**：DRF提供了许多功能，如内置的认证、权限控制、序列化、过滤、分页等。

3. 3.**与Django无缝集成**：DRF与Django完美结合，使得开发者可以很容易地在Django项目中添加API功能。

4. 4.**文档丰富**：DRF拥有详细的文档，使得开发者可以很容易地学习和使用。

### 安装和配置

- **安装**：可以使用pip命令进行安装：`pip install djangorestframework`。
- **配置**：安装完成后，需要在Django项目的`settings.py`文件中进行配置，将DRF添加到`INSTALLED_APPS`中。

### 序列化器

在DRF中，序列化器用于定义API的输出格式。序列化器可以将数据库模型或其它数据结构序列化为JSON格式。开发者需要定义一个数据模型，然后创建一个序列化器来序列化这个数据模型。

### 视图

在开发REST API时，视图中做的主要工作包括将请求的数据（如JSON格式）转换为模型类对象，操作数据库，以及将模型类对象转换为响应的数据（如JSON格式）。DRF提供了`APIView`类，它重写了Django的`as_view()`和`dispatch()`方法，添加了一些功能，如版本处理、认证、权限、访问频率限制等。

### 版本控制

DRF支持API版本控制，允许开发者为API的不同版本提供不同的视图和序列化器。这使得API的维护和升级变得更加容易。

### 权限和认证

DRF提供了多种权限和认证机制，如基于角色的权限控制、令牌认证、OAuth认证等，以确保API的安全性。

### 总结

Django REST framework是一个功能强大的工具包，它简化了RESTful API的开发过程，提供了丰富的功能和灵活的配置选项，使得开发者可以快速构建出安全、高效、可维护的Web API。



## Django HTTP 请求的处理流程？

Django的HTTP请求处理流程涉及多个组件和步骤，从接收请求到返回响应。以下是Django处理HTTP请求的基本流程：

- ### 1. 请求接收

  - 用户通过浏览器或其他客户端发起HTTP请求。
  - 请求通过网络发送到运行Django应用的WSGI服务器（如Gunicorn、uWSGI等）。

  ### 2. WSGI服务器处理

  - WSGI服务器接收HTTP请求，并根据WSGI规范将请求传递给Django应用。
  - WSGI服务器负责管理请求的生命周期，包括请求的接收和响应的发送。

  ### 3. URL路由

  - Django的URL路由器根据请求的URL匹配相应的视图函数或类。
  - Django使用`django.urls`模块中的`ResolverMatch`对象来确定要调用的视图。

  ### 4. 视图处理

  - Django创建一个`HttpRequest`对象，该对象包含了请求的所有信息，如GET、POST参数、请求头等。
  - Django调用相应的视图函数或类的`dispatch`方法。
  - 视图函数或类处理业务逻辑，如查询数据库、调用模型方法等。
  - 如果需要，视图函数会调用模板渲染方法，将数据传递给模板，生成HTML内容。
  - 视图函数返回一个`HttpResponse`对象，该对象包含了响应的内容和状态码。

  ### 5. 中间件处理

  - 在视图处理之前和之后，请求和响应会通过一系列中间件（`MIDDLEWARE`设置中定义的）。
  - 中间件可以修改请求和响应，执行额外的逻辑，如日志记录、权限检查等。

  ### 6. 响应返回

  - Django将`HttpResponse`对象转换为HTTP响应，并通过WSGI服务器发送回客户端。
  - WSGI服务器负责将HTTP响应发送给客户端。

  ### 7. 日志记录

  - Django会记录请求的相关信息，如请求方法、路径、状态码等，用于调试和监控。

  ### 8. 异常处理

  - 如果在请求处理过程中发生异常，Django的异常处理中间件会捕获并处理这些异常。
