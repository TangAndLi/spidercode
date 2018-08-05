import time
from lxml import etree
import threading
import queue
import requests
from multiprocessing import Pool
import pymysql
from urllib.error import URLError
from threading import Lock
# 设置退出标志
parse_exit_flag = False
# 创建队列
spider_queue = queue.Queue()
# 创建解析队列
parse_queue = queue.Queue()

header = {
    'cookie':'shippingCountry=CN; SignedIn=0; GCs=CartItem1_92_03_87_UserName1_92_4_02_; SEED=5881204274060464616; mercury=true; cmTPSet=Y; _4c_mc_=011e69d0250b6b9bd0f4f4aa31d9e615; xdVisitorId=1190YPbzMBF531GTRxTgOBOXj49IoXy1e1B_gapWJk0JV-Y40CC; last_access_token=1533283590816; TS0111b70e=0112b7dea09f69aa587fd47be35d1d87ae78eb479ecc0793cd67aaabb3c7b1adadd0881ecf35c75cea92759ac675a82d0af00f4783; TS0132ea28=0112b7dea0fb6dbb07d4a2b2b64147a5827395969460c036e709f3d794fde3863b3e38a94d; ak_bmsc=A018C771748E2A0FBDD2B0D15EE307F7C7EFB72276470000D327645B4817510F~pl9xF+vZwz0QC9QwIlrCJz5VcERvqpcfJjZNtKqxBgSR706zm5WrVa+uzJxMH3QVG2Fp2/r/SNP6JEScLcAo6e3AefQzUjOlwdY43y4LyI8rKPoe9Wyf0dwiOu1ydEzpQzJK0M9NPDzE7kNXSonX5ZM14dB6xe8Wdovd2biz5QVC73BsGQNOpsRpF7Tee1J6AJJccYqtAq6Y8+B8cuvfnDWco11zvJSEfX6SCHgKVP0jxv3H+0GttXm8jdjEqoynH3; akavpau_www_www1_bcom=1533290758~id=bc7aee5b5f7946b133b55b7b78cc82e1; utag_main=v_id:0164fe5e2eb90055e255899bec000406d001e06500bd0$_sn:3$_ss:0$_st:1533292258625$vapi_domain:bloomingdales.com$ses_id:1533283052445%3Bexp-session$_pn:101%3Bexp-session; FORWARDPAGE_KEY=https%3A%2F%2Fwww.bloomingdales.com%2Fshop%2Fwomens-apparel%3Fid%3D2910; _ga=GA1.2.821696215.1533275945; _gid=GA1.2.1361579812.1533275945; mt.v=2.1293301870.1533275941460; rr_rcs=eF5jYSlN9jBMsUwzT05L1TUwMjPQNbFMNdRNTjI10TU3M7U0TrM0SLG0NOHKLSvJTOEzNbbUNdQ1BACLCg3v; atgRecVisitorId=1190YPbzMBF531GTRxTgOBOXj49IoXy1e1B_gapWJk0JV-Y40CC; atgRecSessionId=dhv_ESR_C7bc6Hzc3tfO6b8cVo1v15TAMHUl2WnSSzew9EbIXcqd!-1074214475!-562061040; s_sess=%20s_ppvl%3Dbcom%25253Awomen%25253Atops%252C6%252C6%252C949%252C1920%252C949%252C1920%252C1080%252C1%252CP%3B%20s_ppv%3Dbcom%25253Awomen%252C10%252C10%252C315%252C1920%252C315%252C1920%252C1080%252C1%252CP%3B; RT="sl=13&ss=1533289325508&tt=349191&obo=6&sh=1533290511113%3D13%3A6%3A349191%2C1533290457765%3D12%3A6%3A295843%2C1533290129183%3D11%3A5%3A295843%2C1533290107581%3D10%3A5%3A214509%2C1533290105501%3D9%3A5%3A143021&dm=bloomingdales.com&si=8eeea08e-b3de-447f-bc50-2b15604b3106&bcn=%2F%2F36fb6d10.akstat.io%2F&r=https%3A%2F%2Fwww.bloomingdales.com%2Fshop%2Fwomens-apparel%3Fid%3D2910&ul=1533290921191',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
}

class spider_Thread(threading.Thread):
    def __init__(self,s_id,s_queue,p_queue,*args,**kwargs):
        super().__init__(*args,*kwargs)
        self.id = s_id
        self.spider_queue = s_queue
        self.parse_queue = p_queue

    def run(self):
        while True:
            time.sleep(4)
            # 退出条件
            if self.spider_queue.empty():
                break
            url = self.spider_queue.get(block=False)
            try:
                response = requests.get(url = url,headers=header)
                # time.sleep(3)
                # 将数据put到 解析队列中
                self.parse_queue.put(response.text)
                print('%d线程开始爬取数据%s:'%(self.id,url))
            except URLError as e:
                print('网络请求错误',e)
            finally:
                # 发送消息判断队列是否为空
                # 将发送的消息放再最后 即使请求失败也不会导致上下文堵塞
                self.spider_queue.task_done()

class parse_Thread(threading.Thread):
    def __init__(self,s_id,p_queue,cursor,db,*args,**kwargs ):
    # def __init__(self,s_id,p_queue,fp,*args,**kwargs ):
        super().__init__(*args,*kwargs)
        self.id = s_id
        self.parse_queue = p_queue
        self.cursor = cursor
        self.db = db
        # self.fp = fp

    def run(self):
        while True:
            global parse_exit_flag
            if parse_exit_flag:
                break
            try:
                # 获取数据
                data = self.parse_queue.get(block=False)
                self.parse(data)
                print('%d线程解析数据成功'% self.id)
                # 解析完成发送消息
                self.parse_queue.task_done()
            except Exception:
                pass

    def parse(self,data):
        html_etr = etree.HTML(data)
        print('解析好的网页：',html_etr)
        div_list = html_etr.xpath('//div[@id="row_0"]/ul/li/div/ul/li')
        for div in div_list:
            image_one = div.xpath(".//div/a/div/img[1]/@src ")[0]
            image_two = div.xpath('.//div/a/div/img[2]/@src')[0]
            title = div.xpath('.//div[2]//a/span')[0].text
            log = div.xpath('.//div[2]/div/a/text()')[1].strip()
            price = div.xpath('.//div//div/div[@class="priceInfo"]/div//span[1]')[0].text.strip()
            prices = price.split(' ')[1]
            try:
                Arrival = div.xpath('.//div[@class="productThumbnail"]//div//div[@class="badge"]/span/text()')[0]
            except:
                Arrival = None

            # print(image_one,image_two,title,log,prices,Arrival)
            sql = 'insert into shopping (image_one,image_two,title,log,prices,Arrival) values("%s","%s","%s","%s","%s","%s")'%(image_one,image_two,title,log,prices,Arrival)
            try:
                self.cursor.execute(sql)
                self.db.commit()
            except:
                self.db.rollback()

def request_code(url,headers):
     responses = requests.get(url=url,headers=headers)
     print(url,'请求地址')
     html_etr = etree.HTML(responses.text)
     # print(html_etr,'1111111')
     url_item2 = []
     # 获取页数对象
     try:
         page_sun = html_etr.xpath('//div/ul[@class="newPagination"]/li[@class="paginateContainer"]/ul/li')
        # 获取页数
         if page_sun:
             page_num = (len(page_sun) // 2)
             print(page_num,'获取的页数')

             for i in range(1,page_num+1):
                 index = url.find('?')
                 url2 = url[:index] + '/Pageindex/' + str(i) + url[index:]  # 拼接请求url
                 url_item2.append(url2)
         else:
             url_item2.append(url)
     except URLError as e:
         print('该页面没有找到页码',e)

    # 将数据加入队列
     for spider_url in url_item2:
         spider_queue.put(spider_url)

    # 创建spider线程
     for i in range(4):
        spider_Thread(i,spider_queue,parse_queue).start()

     # 连接数据库
     db = pymysql.connect(host = 'localhost',user = 'root',password = 'root',port = 3306,db = 'insertsq',charset='utf8')
     cursor = db.cursor()

     # fp = open('./shopping.txt','w',encoding = 'utf-8')

    # 创建parse线程
     for i in range(4):
        # parse_Thread(i,parse_queue,fp).start()
        parse_Thread(i,parse_queue,cursor,db).start()

     # 执行队列锁
     spider_queue.join()
     parse_queue.join()

     # 设置退出标志
     global parse_exit_flag
     parse_exit_flag = True

     #  关闭数据库连接
     db.close()
     # fp.close()

# 请求函数
def req_init(urls):
    response = requests.get(url = urls,headers = header)
    html_etree = etree.HTML(response.text)
    # return html_etree
    # print(etree.tostring(html_etree))
# 网页连接列表
# def parse_list(html_etree):
    url_item = []
    # url_lists = html_ etree.xpath('//div[@class="flexLabelLinksContainer"]/ul/li//a/@href')
    # 获取列表页
    url_lists = html_etree.xpath('//ul[@class="categoryHeader"]/li/ul/li/a/@href')
    #//div[@class="categoryTree bcom"]/ul/li/ul/li/a/@href
    for url_list in url_lists:
        # url = 'https://www.bloomingdales.com'+ url_list.split("&")[0]
        url = url_list.split("&")[0]
        url_item.append(url)

    # for url in url_item:
    #     threading.Thread(target = reqeust_code,args = (url,)).start()
    res_list,num = [],0
    # 开启进程
    pp = Pool(4)
    for url in url_item[:16]:
        print(url)
        time.sleep(4)
        res = pp.apply_async(request_code,args = (url,header,))
        res_list.append(res)
    pp.close()
    pp.join()

if __name__ == '__main__':
    url = 'https://www.bloomingdales.com/shop/womens-apparel?id=2910'
    req_init(url)
    # parse_list(html_list)






















