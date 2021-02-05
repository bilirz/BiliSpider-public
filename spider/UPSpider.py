"""
@author 认真猫
@create date ‎2021‎-01‎-21 ‏‎‏‎17:38:40
@desc 一个使用requests库的BiliBili UP主爬虫
"""
import requests
import csv
import time
import random
import sys
from function import *
from requests.adapters import HTTPAdapter

output_path = "./spider/data/upData.csv"
uid_list = openUPList()

headers = {"User-Agent": randomAgent(), "Cookie": randomCookie()}

card_url = "http://api.bilibili.com/x/web-interface/card?mid={}"
upstat_url = "http://api.bilibili.com/x/space/upstat?mid={}"

with open(output_path, "a", encoding="utf-8-sig", newline="") as f:
    csv_headers = [
        "mid",
        "name",
        "sex",
        "face",
        "fans",
        "attention",
        "archive",
        "article",
        "likes",
        "time",
    ]
    f_csv = csv.writer(f)
    f_csv.writerow(csv_headers)

    for u in uid_list:
        session = requests.session()
        session.mount("https://", HTTPAdapter(max_retries=3))
        card = session.get(
            card_url.format(u), headers=headers, proxies=randomProxy
        ).json()
        upstat = session.get(
            upstat_url.format(u), headers=headers, proxies=randomProxy
        ).json()
        if card["code"] == 0 | upstat["code"] == 0:
            row = [
                # 该UP主的UID
                card["data"]["card"]["mid"],
                # 该UP主的昵称
                card["data"]["card"]["name"],
                # 该UP主的性别
                card["data"]["card"]["sex"],
                # 该UP主的头像
                card["data"]["card"]["face"],
                # 该UP主的粉丝数
                card["data"]["card"]["fans"],
                # 该UP主的关注数
                card["data"]["card"]["attention"],
                # 该UP主的播放量
                upstat["data"]["archive"]["view"],
                # 该UP主的专栏量
                upstat["data"]["article"]["view"],
                # 该UP主的点赞量
                upstat["data"]["likes"],
                # 爬取该UP主的时间
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            ]
            f_csv.writerow(row)
        elif card["code"] == -412 or upstat["code"] == -412:
            print("请求被拦截")
            sys.exit()
        elif card["code"] == -400 or upstat["code"] == -400:
            print("请求错误")
        elif card["code"] == -404 or upstat["code"] == -404:
            print("用户不存在")
        else:
            print(str(card) + str(upstat))

        time.sleep(5)
