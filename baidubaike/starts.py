import  scrapy
from  scrapy import cmdline
#pycharm执行风格
#cmdline.execute(["scrapy","crawl","ctospider","-o","51cto.json"])

cmdline.execute(["scrapy","crawl","baike","-o","5.json"])