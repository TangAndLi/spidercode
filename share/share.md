## Selenium小操作

##### 1. 子框架切换

```python
1.网易云爬虫
此处略
2.登录QQ空间爬虫
此处略

driver = webdriver.Chrome()
driver.switch_to.frame(0)  # 1.用frame的index来定位，第一个是0
driver.switch_to.frame("frame1")  # 2.用id来定位
driver.switch_to.frame("myframe")  # 3.用name来定位
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  # 4.用WebElement对象来定位
driver.switch_to.parent_frame()  # 切换到父框架中
driver.switch_to.default_content()  # 切换到主页面
```

##### 2. 手机模拟

```python
from selenium import webdriver
from time import sleep

# 设置
mobileEmulation = {'deviceName': 'iPhone 6'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

# 启动driver
driver = webdriver.Chrome(options=options)

# 访问百度wap页
driver.set_window_size(375, 700)
# driver.get('http://m.baidu.com')
driver.get('http://m.taobao.com')
# driver.get('http://m.jd.com')
sleep(20)

driver.quit()
```

##### 3. Selenium + Requests + Cookie

使用selenium先进行登录,获取所有cookie,再使用requests进行加速爬取

```python
# cookie。每链接一次，TCP断开,再链接不行。
# selenium登陆，保持会话
```

```python
案例:CSDN
    
# 1.初始化CsdnSpider类
start_urls = ['https://passport.csdn.net/account/login',
                  "https://blog.csdn.net/hellocsz/article/details/80708996"]

# 初始化
def __init__(self):
    self.browser = None
    self.cookies = None
    # 传递给父类
    super(CsdnSpider, self).__init__()
    
# 2.重写middlewares.py
class LoginMiddleware(object):
    # 替换掉原来的函数，process_request
    def process_request(self, request, spider):
        if spider.name == "csdn":  # 指定仅仅处理这个名称的爬虫
            if request.url.find("login") != -1:  # 判断是否登陆页面

                spider.browser = webdriver.Chrome()  # 创建一个浏览器
                spider.browser.get(request.url)  # 爬虫访问链接
                time.sleep(5)
                print("login访问", request.url)

                spider.browser.find_element_by_link_text("账号登录").click()
                time.sleep(1)
                username = spider.browser.find_element_by_id("username")
                password = spider.browser.find_element_by_id("password")
                time.sleep(1)
                username.send_keys("15323844594")  # 账户
                time.sleep(2)
                PASSWORD = os.getenv('PASSWORD') or '123456'
                password.send_keys(PASSWORD)  # 密码
                time.sleep(3)
                click = spider.browser.find_element_by_class_name("logging")
                click.click()
                time.sleep(8)
                spider.cookies = spider.browser.get_cookies()  # 抓取全部的cookie
                # spider.browser.close()

                return HtmlResponse(url=spider.browser.current_url,  # 当前连接
                                    body=spider.browser.page_source,  # 源代码
                                    encoding="utf-8")  # 返回页面信息
            else:
                # spider.browser.get(request.url)
                # request.访问，调用selenium cookie
                # request模拟访问。统一selenium，慢，request,不能执行js
                print("request  访问")
                req = requests.session()  # 会话
                for cookie in spider.cookies:
                    req.cookies.set(cookie['name'], cookie["value"])
                req.headers.clear()  # 清空头
                new_page = req.get(request.url)
                # print("---------------------")
                # print(request.url)
                # print("---------------------")
                # print(new_page.text)
                # print("---------------------")
                # 页面
                time.sleep(3)
                return HtmlResponse(url=request.url,  # 当前连接
                                    body=new_page.text,  # 源代码
                                    encoding="utf-8")  # 返回页面信息
# 3.修改setting
DOWNLOADER_MIDDLEWARES = {
    'csdnlogin.middlewares.LoginMiddleware': 540,
}
```

##### 4. 视频下载工具---如需翻墙自行下载

you-get       youtube-dl     FFmpeg

pip install you-get

pip install youtube-dl

FFmpeg官网下

下载方式 :  you-get  -i  url

```python
项目主页：https://github.com/soimort/you-get
You-Get 主页：https://you-get.org/
You-Get 原版中文说明：https://github.com/soimort/you-get/wiki/中文说明/
'''
import  os
#普通下载
# --format=flvhd 一般格式flv
# --format= mp4  中等
os.system(r"you-get  -o  D:\    https://www.ixigua.com/a6565111498383819268/#mid=5775513958")
```

##### 5. Appium手机端的Selenium---如需翻墙自行下载

```python
1.安装node.js  node.js官网
	---->  appium server
    npm --registry http://registry.cnpmjs.org install -g appium
    使用npm的国内镜像可以安装，速度很不错。
    以后不想输入ip的话可以输入以下命令：
    npm config set registry http://registry.cnpmjs.org
    然后就可以直接输入 npm install -g appium 安装了
    或者
    1). 设置 npm 淘宝镜像 
    npm config set registry https://registry.npm.taobao.org 
    2). 设置 vsbuild 版本，之前下载的 Visual C++ Build Tools 是多少版本的是多少就设置多少 
    npm config set msvs_version 2015 
    3). 下载命令 
    如安装 1.6.5 版本 appium: 
npm install appium@1.6.5 -g --chromedriver_cdnurl=http://cdn.npm.taobao.org/dist/chromedriver

    -g 为全局安装 
    不带 @版本号 默认下载最新版本，截止目前最新版本为 1.7.2 
    因为 chromedriver 下载需要翻墙，有时候翻墙也不一定能成功下载下来，故指向淘宝镜像下载。
    等待命令完成安装即可。 
2.安装java jdk jre 1.8....   
		官网下载
		环境变量设置,参考网站: https://www.cnblogs.com/zlslch/p/5658399.html
3.安装安卓sdk  iOS...    -----> 安卓版本 2.3 以上 					    							参考网站: https://blog.csdn.net/love4399/article/details/77164500
4.安装appium client ---如需翻墙自行下载
	下载地址: https://github.com/appium/appium-desktop/releases/tag/v1.6.2
5.cmd: adb devices检查设备连接
	1)驱动手机,如果手机驱动没出来,驱动精灵更新一下
	2)使用安卓虚拟机 推荐 夜神 各种虚拟机
6.编写你的代码吧
7.安卓界面代码xml xpath  启动命令:uiautomatorviewer

pip install appium-python-client

# coding=utf-8
from appium import webdriver
import time
desired_caps = {
    "platformName": "Android",
    "deviceName": "Honor 9",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": ".main.MainActivity"
}
# 指定Appium Server
server = 'http://localhost:4723/wd/hub'


driver = webdriver.Remote(server, desired_caps)

time.sleep(4)
driver.find_element_by_xpath("//*[@class='android.widget.Button' and @index='16']").click()
.....

8.数据处理:  mitmproxy mitmducp 抓流 

Appium处理滑动方法是swipe
滑动API：Swipe（int start x,int start y,int end x,int y,duration) 
解释： 
int start x－开始滑动的x坐标；
int start y －开始滑动的y坐标 ；
int end x －结束点x坐标；
int end y －结束点y坐标； 
duration 滑动时间（默认5毫秒）。

还有各种API看文档吧,太多了
	API参考:https://blog.csdn.net/bear_w/article/details/50330565

已经安装好了mitmproxy，并且手机和PC处于同一个局域网下，同时也配置好了mitmproxy的CA证书，网上有很多相关的配置教程，这里我就略过了。
因为mitmproxy不支持windows系统，所以这里用的是它的组件之一mitmdump，它是mitmproxy的命令行接口，可以利用它对接我们的Python脚本，用Python实现监听后的处理。
在配置好mitmproxy之后,在控制台上输入mitmdump并在手机上打开抖音app，mitmdump会呈现手机上的所有请求，
手机和PC在同一个局域网内，设置代理为mitmproxy的代理地址，这样手机在访问互联网的时候流量数据包就会流经mitmproxy，mitmproxy再去转发这些数据包到真实的服务器，服务器返回数据包时再由mitmproxy转发回手机，这样mitmproxy就相当于起了中间人的作用，抓取到所有Request和Response，另外这个过程还可以对接mitmdump，抓取到的Request和Response的具体内容都可以直接用Python来处理，比如得到Response之后我们可以直接进行解析，然后存入数据库，这样就完成了数据的解析和存储过程。

我们可以使用命令启动mitmproxy，并把截获的数据保存到文件中，命令如下所示：
mitmdump -w outfile其中outfile的名称任意，截获的数据都会被保存到此文件中。
还可以指定一个脚本来处理截获的数据，使用-s参数即可：
mitmdump -s script.py
这里指定了当前处理脚本为script.py，它需要放置在当前命令执行的目录下。

	参考地址
    安装:  https://blog.csdn.net/hqzxsc2006/article/details/73199065
        安装:  https://cuiqingcai.com/5391.html
            代码处理:  http://www.bubuko.com/infodetail-2095811.html
                代码处理:   https://juejin.im/post/5ac9ea6d518825364001b5b9
        
from mitmproxy import ctx

def request(flow):
    request = flow.request
    info = ctx.log.info
    info(request.url)
    info(str(request.headers))
    info(str(request.cookies))
    info(request.host)
    info(request.method)
    info(str(request.port))
    info(request.scheme)
def response(flow):
    response = flow.response
    info = ctx.log.info
    info(str(response.status_code))
    info(str(response.headers))
    info(str(response.cookies))
    info(str(response.text))
..............
```

