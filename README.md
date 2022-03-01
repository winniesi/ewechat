# ewechat

以前有很多基于 Web 微信的库，比如 [itchat](https://github.com/littlecodersh/ItChat) 等，在微信限制 web 微信该协议后这些库就无法使用了。现在如果想 hook 微信出接口，基本都要使用一些付费的服务，比如 [wechaty PadLocal](https://wechaty.js.org/docs/puppet-services/padlocal/)，这也是我一直在用的服务，但是 wechaty 一直没有实现朋友圈等功能。

这个[E 云管家](https://wkteam.cn)也是基于微信 iPad 协议，价格和 PadLoacal 一样（每个微信号每月 200 元）。由于已经实现了我需要的朋友圈功能，所以最近把自己的服务迁移到了这里。

## ⚠️ 提示

我在使用这家服务，但并不作为推荐。与微信的 web 协议不同，如果使用这个服务，服务商可以获取你微信的**全部隐私**。而且这是对微信协议的破解，账号有被封禁的风险，请慎重使用。

## 开发进度

这个服务商的 API 接口非常简单，[官方文档](https://wkteam.cn)接口数量不多。为了方便**我自己**日常使用，我打算把官方 API 接口封装成 python SDK。代码比较简单，有时间的话我尽快写完。

## 使用方法

该包是基于服务商 API 实现的，请在服务商处注册并购买相应资源后再进行配置。请先阅读[服务商文档](https://wkteam.cn)，否则可能不理解相关的参数。

下载安装该包：

```shell
pip install ewechat
```

### 登录

```python
from ewechat import Wechat

# 实例化时请传入服务商提供的 url、账号和密码，
# 目的是为了获得授权码
my_wechat = Wechat(base_url=url, account="your_account", password="your_password")

# 如果已经获得了授权码，可以直接传入授权码
my_wechat = Wechat(base_url=url, auth=authorization)

# 进行登录，在弹出二维码后请用手机扫码登录
my_wechat.login_in()

# 登录完成后会在当前目录创建文件 logged_in
# 记录你的一些参数，参数的意义请参照服务商文档
```

### 通讯录

**初始化通讯录列表**

```python
my_wechat.init_address_list()
```

**获取通讯录列表**

```python
my_wechat.get_address_list()
```

**获取联系人信息**

```python
my_wechat.get_contact(wcId: str)
```

## 消息发送

**发送文本消息**

```python
my_wechat.send_text(wcId: str, content: str)
```

**发送文件消息**

```python
my_wechat.send_file(wcId: str, path: str, fileName: str)
```

**发送图片消息**

```python
my_wechat.send_image(wcId: str, content: str)
```

**发送视频消息**

```python
my_wechat.send_video(path: str, thumbPath: str)
```

**发送 URL 消息**

```python
my_wechat.send_url(wcId, title, url, description, thumbUrl)
```

## 消息接收

**设置消息接收地址**

返回 None 即设置成功，如果设置失败会引发异常。

```python
my_wechat.set_http_callback_url(self, httpUrl: str, type: int)
```

**取消消息接收**

```python
my_wechat.cancel_http_callback_url()
```

**下载图片**

```type``` 0是常规图片，1是高清图。

```python
my_wechat.get_msg_img(msgId: str, content: str, type: int = 1)
```

## 朋友圈

**获取指定好友朋友圈**

第一次使用 ```firstPageMd5``` 和 ```maxId``` 请留空。

```python
my_wechat.get_friend_circle(wcId: str, firstPageMd5: str = "", maxId: int = 0)
```

