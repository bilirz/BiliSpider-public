"""
@author 认真猫
@create date ‎2021‎-01‎-20‎ ‏‎19:57:16
@desc 一个基于协程的BiliBili UP主爬虫
"""
import aiohttp
import asyncio
import time
import csv
from function import randomAgent

headers = {"User-Agent": randomAgent()}
# 需要存放文件的路径
output_path = "./spider/data/spaceData.csv"


async def fetch(session, url):
    async with session.get(url, verify_ssl=False, headers=headers) as response:
        response = await response.json()
        if response["code"] == 0:
            with open(output_path, "a", encoding="utf-8-sig", newline="") as f:
                row = [
                    # 该用户的UID
                    response["data"]["card"]["mid"],
                    # 该用户的昵称
                    response["data"]["card"]["name"],
                    # 该用户的性别
                    response["data"]["card"]["sex"],
                    # 该用户的头像
                    response["data"]["card"]["face"],
                    # 该用户的粉丝数
                    response["data"]["card"]["fans"],
                    # 该用户的关注数
                    response["data"]["card"]["attention"],
                    # 爬取该用户的时间
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                ]
                f_csv = csv.writer(f)
                f_csv.writerow(row)
        elif response["code"] == -412:
            print("请求被拦截")
        elif response["code"] == -400:
            print("请求错误")
        elif response["code"] == -404:
            print("用户不存在")
        else:
            print(str(response))


async def main():
    async with aiohttp.ClientSession() as session:
        # 生成需要爬取的URL
        url_list = [
            "https://api.bilibili.com/x/web-interface/card?mid=" + str(i + 1)
            for i in range(3)
        ]
        # 添加需要爬取的URL到task队列
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        await asyncio.wait(tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
