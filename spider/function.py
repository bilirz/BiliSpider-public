import random


def deleteSpace(list):
    return [l for l in list if l != ""]


def randomAgent():
    with open("./spider/data/spider/User-Agent.txt", "r", encoding="utf-8-sig") as f:
        userAgents = f.read().split("\n")
    return random.choice(deleteSpace(userAgents))


def randomCookie():
    with open("./spider/data/spider/cookie.txt", "r", encoding="utf-8-sig") as f:
        cookies = f.read().split("\n")
    return random.choice(deleteSpace(cookies))


def randomProxy():
    with open("./spider/data/spider/proxy.txt", "r", encoding="utf-8-sig") as f:
        proxies = f.read().split("\n")
    item = {}
    item["http"] = random.choice(proxies)
    return item


def openUPList():
    with open("./spider/data/spider/UPList.txt", "r", encoding="utf-8-sig") as f:
        uids = f.read().split("\n")
        return deleteSpace(uids)
