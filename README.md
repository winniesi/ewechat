# ewechat
以前有很多基于 Web 微信的库，比如 [itchat](https://github.com/littlecodersh/ItChat) 等，在微信限制 web 微信该协议后这些库就无法使用了。现在如果想 hook 微信出接口，基本都要使用一些付费的服务，比如 [wechaty PadLocal](https://wechaty.js.org/docs/puppet-services/padlocal/)，这也是我一直在用的服务，但是 wechaty 一直没有实现朋友圈等功能。

现在我开始用 [E 云管家](https://wkteam.cn)，同样基于微信的 iPad 协议，价格和 PadLoacal 一样（每个微信号每月200元）。由于实现了已经实现了我需要的朋友圈功能，而且使用比较简单，我准备把已经有的业务都迁移过去。

## ⚠️ 提示

虽然我在使用这家服务，但并不推荐其他人使用。和之前微信的 web 协议不同，如果使用这个服务，服务商可以获取你微信的**全部隐私**。

而且这是对微信协议的一种 hack，账号有一定被封禁的风险，再次提示，请慎重使用。

## 开发进度

这个厂商的 API 使用非常简单，[服务商文档](https://wkteam.cn)接口数量也不多。为了方便**我自己**日常使用，我打算把官方文档的接口包装成 python 库，目前已经完成登录功能。代码比较简单，有时间的话我尽快写完。

## 使用方法

该包是基于服务商服务实现的，请先在服务商网址注册并购买相应资源后再进行配置。

请先阅读[服务商文档](https://wkteam.cn)，否则可能不理解相关的参数。

下载安装该包：

```shell
git clone git@github.com:winniesi/ewechat.git
```

在你的代码里引入：

```python
from ewechat import Wechat

# 实例化时请传入服务商提供的 url、账号和密码
my_wechat = Wechat(base_url=url, account="your_account", password="your_password")

# 或者
# 如果已经获得了授权码，可以直接传入授权码
my_wechat = Wechat(base_url=url, auth=authorization)

# 进行登录，请用手机扫码登录
my_wechat.login_in()

# 登录完成后会在创建文件 logged_in
# 记录你的一些参数，参数的意义请参照服务商文档
```

目前只实现了登录，其他接口我会尽快完成。
