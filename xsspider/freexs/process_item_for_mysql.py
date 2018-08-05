#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
import pymysql
import json

def process_item():
    # 创建redis数据库连接
    rediscli = redis.Redis(host="10.36.137.121", port=6379, db=0)

    # 创建mysql数据库连接
    mysqlcli = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="freexs")

    offset = 0

    while True:
        # 将数据从redis里pop出来
        source, data = rediscli.blpop("fxsspider_redis:items")
        item = json.loads(data)
        try:
            # 创建mysql 操作游标对象，可以执行mysql语句
            cursor = mysqlcli.cursor()
            sql = 'insert into freexs(xsname, author, classes, last_update, status, all_click_num, week_click_num,month_click_num, collect_num, words, intro, url, image_url) values("%s", "%s", "%s", "%s","%s", "%s", "%s", "%s","%s", "%s", "%s", "%s","%s")' % (
            item["xsname"], item["author"], item["classes"], item["last_update"], item["status"], item["all_click_num"],
            item["week_click_num"], item["month_click_num"], item["collect_num"], item["words"], item["intro"],
            item["url"], item["image_url"])

            cursor.execute(sql)
            # 提交事务
            mysqlcli.commit()
            # 关闭游标
            cursor.close()
            offset += 1
            print(offset)
        except:
            pass


if __name__ == "__main__":
    process_item()
