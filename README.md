# Wap 

基于pytest的UI自动化测试运行wrapper

## 如何使用

### 1. 下载项目

* 通过`git`命令下载

```
git clone http://172.19.81.132:8061/suwenhui/iwc_auto_test_wap.git
```

* 直接下载压缩包

点击网页中下载按钮, 下载后解压

### 2. 安装依赖

#### 2.1 环境依赖

* Python3.x
* Chrome浏览器
* ChromeDriver 下载对应Chrome浏览器的版本(`浏览器设置` -> `帮助` -> `关于Google Chrome`), 你可以在`https://npm.taobao.org/mirrors/chromedriver`下载到对应的操作系统的版本

#### 2.2 python依赖

* [selenium](https://www.seleniumhq.org/docs/03_webdriver.jsp)

```
pip.exe install selenium
```

* [Pytest](http://doc.pytest.org/en/latest/getting-started.html)

```
pip.exe install -U pytest pytest-cov pytest-forked pytest-html pytest-metadata pytest-repeat pytest-rerunfailures pytest-xdist python-dateutil
```

下面依赖和cv相关可以不用下载

* [scikit-image](https://scikit-image.org/download.html)

```
pip.exe install scikit-image
```

* [opencv](https://github.com/skvark/opencv-python)

```
pip.exe install opencv-python
```

### 3. 运行

#### 3.1 设置`settings.py`

根据`settings.py`中的说明, 配置你的运行环境中的路径.

#### 3.2 执行命令(在项目根路径下打开命令行)

下面的脚本指定了`cases/mobile`目录下的`test_helloworld.py`的脚本, 同时有1个浏览器运行用例, 失败后重跑2次

```
D:\Anaconda3\python.exe main.py --type mobile --title testTitle --parallel 1 --script test_helloworld.py --reruns 2 --headless 1
```

支持运行参数查看: `python.exe main.py -h`

```
usage: main.py [-h] [--headless {0,1}] [-t {mobile,pc}]
           [--title TITLE] [--script SCRIPT] [--testing_url TESTING_URL]
           [--baseline_url BASELINE_URL] [--parallel PARALLEL]
           [--reruns RERUNS] [--mock MOCK]

optional arguments:
  -h, --help            show this help message and exit
  --headless {0,1}      0: 后台运行浏览器, 1: 前台运行浏览器
  -t {mobile,pc}, --type {mobile,pc}
                        mobile: 运行模拟手机浏览器用例, pc: 运行浏览器用例
  --title TITLE
  --script SCRIPT       指定运行的脚本
  --testing_url TESTING_URL
                        测试链接地址
  --baseline_url BASELINE_URL
                        对比链接地址, 默认不对比
  --parallel PARALLEL   用例并行运行个数(会启动n个浏览器), 1为默认
  --reruns RERUNS       用例失败后重跑次数, 默认不重跑
  --mock MOCK           是否使用mock接口, 默认不使用
 ```

## 项目结构

```
├── ...
├── cases                   # 自动化测试用例
│   ├── mobile              # 测试用例
├── core                    # 框架基本内容
│   ├── ai                  # AI相关工具类: 基于opencv图片相似度比对等
│   ├── pytest              # pytest相关
│   ├── templates           # 用例模板
│   ├── util                # 基础工具deprecated
│   ├── selenium.py         # selenium工具
│   └── main_helper.py      
├── conftest.py             # 框架pytest conftest, 提供pytest运行参数设置
├── main.py                 # 入口main
└── settings.py             # 配置文件: 环境变量, 运行路径等
```

## Q&A

```
Q1: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
```

```
A1: 问题原因，openssl版本过低或者不存在。Windows环境下：解决方法为进入 https://slproweb.com/products/Win32OpenSSL.html 链接，
下载Win OpenSSL，下载对应位数的操作系统MSI安装即可。
```

```
Q2: ImportError: DLL load failed while importing etree: 找不到指定的模块。
```

```
A2: 问题原因，lxml 版本与 Scrapy 版本不匹配。解决方式如下：1.卸载 lxml，2.重新安装 lxml，将会安装 lxml 的最新版本。
命令分别为： pip uninstall lxml 、 pip install lxml
```
