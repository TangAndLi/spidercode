
import requests
from lxml import etree

# url ='https://www.bloomingdales.com/shop/womens-apparel/activewear-workout-clothes?id=11817'
# url = 'https://www.bloomingdales.com/shop/womens-apparel/blazers?id=1005879'
url='https://www.bloomingdales.com/shop/fashion-lookbooks-videos-style-guide/clothing?id=1001037'
header = {
    'cookie':'shippingCountry=CN; SignedIn=0; GCs=CartItem1_92_03_87_UserName1_92_4_02_; SEED=5881204274060464616; mercury=true; cmTPSet=Y; _4c_mc_=011e69d0250b6b9bd0f4f4aa31d9e615; xdVisitorId=1190YPbzMBF531GTRxTgOBOXj49IoXy1e1B_gapWJk0JV-Y40CC; last_access_token=1533283590816; TS0111b70e=0112b7dea09f69aa587fd47be35d1d87ae78eb479ecc0793cd67aaabb3c7b1adadd0881ecf35c75cea92759ac675a82d0af00f4783; TS0132ea28=0112b7dea0fb6dbb07d4a2b2b64147a5827395969460c036e709f3d794fde3863b3e38a94d; ak_bmsc=A018C771748E2A0FBDD2B0D15EE307F7C7EFB72276470000D327645B4817510F~pl9xF+vZwz0QC9QwIlrCJz5VcERvqpcfJjZNtKqxBgSR706zm5WrVa+uzJxMH3QVG2Fp2/r/SNP6JEScLcAo6e3AefQzUjOlwdY43y4LyI8rKPoe9Wyf0dwiOu1ydEzpQzJK0M9NPDzE7kNXSonX5ZM14dB6xe8Wdovd2biz5QVC73BsGQNOpsRpF7Tee1J6AJJccYqtAq6Y8+B8cuvfnDWco11zvJSEfX6SCHgKVP0jxv3H+0GttXm8jdjEqoynH3; akavpau_www_www1_bcom=1533290758~id=bc7aee5b5f7946b133b55b7b78cc82e1; utag_main=v_id:0164fe5e2eb90055e255899bec000406d001e06500bd0$_sn:3$_ss:0$_st:1533292258625$vapi_domain:bloomingdales.com$ses_id:1533283052445%3Bexp-session$_pn:101%3Bexp-session; FORWARDPAGE_KEY=https%3A%2F%2Fwww.bloomingdales.com%2Fshop%2Fwomens-apparel%3Fid%3D2910; _ga=GA1.2.821696215.1533275945; _gid=GA1.2.1361579812.1533275945; mt.v=2.1293301870.1533275941460; rr_rcs=eF5jYSlN9jBMsUwzT05L1TUwMjPQNbFMNdRNTjI10TU3M7U0TrM0SLG0NOHKLSvJTOEzNbbUNdQ1BACLCg3v; atgRecVisitorId=1190YPbzMBF531GTRxTgOBOXj49IoXy1e1B_gapWJk0JV-Y40CC; atgRecSessionId=dhv_ESR_C7bc6Hzc3tfO6b8cVo1v15TAMHUl2WnSSzew9EbIXcqd!-1074214475!-562061040; s_sess=%20s_ppvl%3Dbcom%25253Awomen%25253Atops%252C6%252C6%252C949%252C1920%252C949%252C1920%252C1080%252C1%252CP%3B%20s_ppv%3Dbcom%25253Awomen%252C10%252C10%252C315%252C1920%252C315%252C1920%252C1080%252C1%252CP%3B; RT="sl=13&ss=1533289325508&tt=349191&obo=6&sh=1533290511113%3D13%3A6%3A349191%2C1533290457765%3D12%3A6%3A295843%2C1533290129183%3D11%3A5%3A295843%2C1533290107581%3D10%3A5%3A214509%2C1533290105501%3D9%3A5%3A143021&dm=bloomingdales.com&si=8eeea08e-b3de-447f-bc50-2b15604b3106&bcn=%2F%2F36fb6d10.akstat.io%2F&r=https%3A%2F%2Fwww.bloomingdales.com%2Fshop%2Fwomens-apparel%3Fid%3D2910&ul=1533290921191',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
}
response = requests.get(url=url,headers= header)
html_etr = etree.HTML(response.text)
print(html_etr)
url_item2 = []
page_sun = html_etr.xpath('//div/ul[@class="newPagination"]/li[@class="paginateContainer"]/ul/li')
print(len(page_sun)//2)
# url ='https://www.bloomingdales.com/shop/womens-apparel/juniors-clothing-for-teenage-girls/Pageindex/2?id=1038668'
index = url.find('?')
i = 2
url = url[:index]+'/Pageindex/'+str(i)+url[index:]
print(url)

# list = [1,2,3,4,5,6,7,8,9,0]
# print(list[:3])