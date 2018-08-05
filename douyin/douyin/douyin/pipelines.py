# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from douyin.items import DouyinVideoItem, DouyinUserItem
from scrapy.utils.project import get_project_settings
import pymysql


# class MysqlBase(object):
#     def __init__(self):
#         setting = get_project_settings()
#         self.host = setting.get('DB_HOST')
#         self.port = setting.get('DB_PORT')
#         self.user = setting.get('DB_USER')
#         self.password = setting.get('DB_PASSWORD')
#         self.db = setting.get('DB_DB')
#         self.charset = setting.get('DB_CHARSET')
#         self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db, charset=self.charset)
#         self.cursor = self.conn.cursor()
#
#     def process_item(self, item, spider):
#         return item
#
#     def close_spider(self, spider):
#         self.cursor.close()
#         self.conn.close()


class DouyinPipeline(object):
    def __init__(self):
        # super(MysqlBase, self).__init__()
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
        if isinstance(item, DouyinVideoItem):
            sql_select = """SELECT * FROM video_douyin WHERE aweme_id=%s"""
            self.cursor.execute(sql_select, (item['aweme_id'],))
            if self.cursor.rowcount:
                sql = 'UPDATE video_douyin SET digg_count={},comment_count={},share_count={} WHERE aweme_id={}'.format(
                        item["digg_count"], item["comment_count"], item["share_count"], item["aweme_id"])
                self.cursor.execute(sql)
                self.conn.commit()
                return item

            sql = '''insert into video_douyin (author_user_id, video_desc, aweme_id, play_addr, download_addr, origin_cover, digg_count, comment_count, share_count,share_url) values("%s","%s", "%s", "%s", "%s","%s", "%s", "%s", "%s","%s")''' % (
                    item["author_user_id"], item["video_desc"], item["aweme_id"], item["play_addr"], item["download_addr"],
                    item["origin_cover"], item["digg_count"], item["comment_count"], item["share_count"], item["share_url"])
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except pymysql.err.ProgrammingError as e:
                sql = '''insert into video_douyin (author_user_id, aweme_id, play_addr, download_addr, origin_cover, digg_count, comment_count, share_count,share_url) values("%s", "%s", "%s", "%s","%s", "%s", "%s", "%s","%s")''' % (
                    item["author_user_id"],  item["aweme_id"], item["play_addr"],
                    item["download_addr"],
                    item["origin_cover"], item["digg_count"], item["comment_count"], item["share_count"],
                    item["share_url"])
                self.cursor.execute(sql)
                self.conn.commit()
            return item

        if isinstance(item, DouyinUserItem):
            sql_select = 'select author_user_id from user_douyin where author_user_id=%s;' % item['author_user_id']
            self.cursor.execute(sql_select)
            if self.cursor.rowcount:
                return item

            sql_insert = '''insert into user_douyin (author_user_id, uid, bind_phone, create_time, constellation, avatar_medium, follow_status,follower_status, school_name, school_type, birthday, nickname, signature, region, gender, unique_id) values('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s','%s', '%s', '%s', '%s','%s', '%s', '%s','%s');''' % (
                    item["author_user_id"], item["uid"], item["bind_phone"], item["create_time"], item["constellation"], item["avatar_medium"],
                    item["follow_status"], item["follower_status"], item["school_name"], item["school_type"], item["birthday"],
                    item["nickname"], item["signature"], item["region"], item["gender"], item["unique_id"])
            try:
                self.cursor.execute(sql_insert)
                self.conn.commit()
            except pymysql.err.ProgrammingError as e:
                sql_insert = '''insert into user_douyin (author_user_id) value ({});'''.format(item['author_user_id'])
                self.cursor.execute(sql_insert)
                self.conn.commit()
            return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()



# class DouyinPipeline(object):
#     def process_item(self, item, spider):
#         return item
