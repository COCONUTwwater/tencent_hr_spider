# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class HrspiderPipeline:
    # 初始化，连接库
    def __init__(self):
        print('初始化数据库连接')
        self.conn = mysql.connector.connect(
            host='',  # ip
            port='3306',  # 端口
            user='root',  # 登录账号
            password='',  # 登录密码
            database='',  # 库名
            use_unicode=True  # unicode
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        self.cur.execute(f"INSERT INTO tencent_hr VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                         (item['BGName'], item['CategoryName'], item['CountryName'],
                          item['Id'], item['IsCollect'], item['IsValid'], item['LastUpdateTime'],
                          item['LocationName'], item['PostId'], item['PostURL'], item['ProductName'],
                          item['RecruitPostId'], item['RecruitPostName'], item['Responsibility'],
                          item['SourceID'], item['Requirement']))
        self.conn.commit()
        # return item

    # 结束，关闭连接
    def close_spider(self, spider):
        print('关闭数据库资源')
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.conn.close()
