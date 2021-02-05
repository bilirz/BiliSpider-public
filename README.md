# 哔哩哔哩爬虫程序

[![License](https://img.shields.io/github/license/bilirz/BiliSpider.svg)](https://github.com/bilirz/BiliSpider/blob/main/LICENSE)

- 需要安装的库
    - `pip install requests`
    - `pip install aiohttp`

- BiliSpider
    - `spaceSpider.py` 哔哩哔哩用户爬虫(异步)
    - `UPSpider.py` 哔哩哔哩UP主爬虫(同步)

相关：哔哩哔哩百大UP主爬虫 [BPUSpider](https://github.com/bilirz/BPUSpider)

## 如何使用本项目

- 配置`cookie.txt` (只需要SESSDATA部分即可)，如有多个可以换行符分割。
- 配置`proxy.txt` 如有多个可以换行符分割。
- 定义的函数可以在`function.py`中查看。

## LICENSE

MIT [©bilirz](https://github.com/bilirz)
