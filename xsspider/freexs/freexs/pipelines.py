# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
import pymysql


class FreexsPipeline(object):
    def __init__(self):
        setting = get_project_settings()
        self.host = setting.get('DB_HOST')
        self.port = setting.get('DB_PORT')
        self.user = setting.get('DB_USER')
        self.password = setting.get('DB_PASSWORD')
        self.db = setting.get('DB_DB')
        self.charset = setting.get('DB_CHARSET')
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db, charset=self.charset)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into freexs(xsname, author, classes, last_update, status, all_click_num, week_click_num,month_click_num, collect_num, words, intro, url, image_url) values("%s", "%s", "%s", "%s","%s", "%s", "%s", "%s","%s", "%s", "%s", "%s","%s")' %(item["xsname"], item["author"], item["classes"], item["last_update"], item["status"], item["all_click_num"], item["week_click_num"], item["month_click_num"], item["collect_num"], item["words"], item["intro"], item["url"], item["image_url"])
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

