 

#### 1\. 准备你的项目

确保你的静态网站文件（如 HTML、CSS、JavaScript、图片等）都在一个[文件夹](https://so.csdn.net/so/search?q=%E6%96%87%E4%BB%B6%E5%A4%B9&spm=1001.2101.3001.7020)中。通常，项目结构如下：

```cobol
my-static-site/├── index.html├── styles/│   └── styles.css└── scripts/    └── script.js
```

#### 2\. 创建 Netlify 账户

如果你还没有 Netlify 账户，请访问 Netlify 官网 并注册一个免费账户。

#### 3\. 登录 Netlify

使用你的账户信息登录 Netlify。

![](https://i-blog.csdnimg.cn/direct/f78e4dd710464879b6dec4256f446549.png)

(图1）

#### 4\. 创建新站点

*   在 Netlify 的仪表板上，点击 "New site from Git"（从 Git 创建新站点）或 "Deploy manually"（手动部署）。

*   **如果选择 "Deploy manually"，你可以直接上传你的项目文件夹。将文件拖拽到指定区域便可等待上传**。(如下）

![](https://i-blog.csdnimg.cn/direct/f3a51b5588ac47fcae8138374f25312c.png)

（图2）

![](https://i-blog.csdnimg.cn/direct/64ad22d575624bf798226719fa96c963.png)

（图3）

![](https://i-blog.csdnimg.cn/direct/e0cc6a8b7800476d86bc75f8ad049503.png)

（图4）

![](https://i-blog.csdnimg.cn/direct/179b65d9cb0d429f90d5f7c7f7b53859.png)

（图5）

部署完成后，Netlify 会为你生成一个随机的站点 URL。你可以在 "Site settings" 中自定义你的站点名称。

#### 5\. 可能遇到的问题与解决方法

如果部署后出现如下图6的页面，可能是文件没有完全上传成功，这个时候尝试重新上传一下。

如果还是没有解决，可能是后台没有识别出你的HTML文件，尝试重命名文件，比如原先的是（1.html），改为（home.html)。

![](https://i-blog.csdnimg.cn/direct/307b0be308a0480397979884f2d917de.png)

（图6）

本文转自 <https://blog.csdn.net/2401_87523886/article/details/145889197>，如有侵权，请联系删除。