
# from urllib import request,parse
import urllib.request
import urllib.parse
import re


def get_html(req):
    response = urllib.request.urlopen(req)
    res_html = response.read().decode('utf-8')
    pattern = re.compile(r'<tr class="odd">(.*?)</tr>',re.S)
    ip_list = pattern.findall(res_html)
    # print(ip_list)
    for item in ip_list:
        ip_patterns = re.compile('(25[0-5]\.|2[0-4]\d\.|1\d{2}\.|[1-9]\d\.|\d\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)',re.S)

        ip_data = ip_patterns.search(item)

        host_patterns = re.compile(r'(\d{2,6})')
        host_data = host_patterns.search(item)
        # print(ip_data)
        print('ip地址为:%s 端口为:%s' % (ip_data.group(),host_data.group()))




def main():
    url = 'http://www.xicidaili.com/nn/'

    headers = {
        'Accept':' */*',
        'Accept-Language':' zh-CN,zh;q=0.9',
        'Connection':' keep-alive',
        'Host':' hm.baidu.com',
        'If-None-Match':' 5c3b05459187e67c077312cdbbe0a08c',
        'Referer':' http://www.xicidaili.com/nn/',
        'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie':' BAIDUID=A56FDCF3F2FFF6E6848D0703341886EC:FG=1; BIDUPSID=A56FDCF3F2FFF6E6848D0703341886EC; PSTM=1525660571; HMACCOUNT=BBB3CB5E8BE6A3F6; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1437_21121_26350_20930; PSINO=7; HMVT=6bcd52f51e9b3dce32bec4a3997715ac|1528005508|; BCLID=11740774069474897488; BDSFRCVID=S64sJeC62wWhRX57LkmAhMndP4fN8Q6TH6aI5UoouSi9z5W9oqRYEG0PDM8g0KubbazpogKK3gOTH4nP; H_BDCLCKID_SF=tJPfoCtMfIP3fP36qRrhh4At-fT0bI62aKDsLJ7I-hcqEIL45pJs0lv0jPvjLJO3BCobbIbDBDnGMxbSj4QojqLehpoga6cEJGk8W-j4yl5nhMJeXj7JDMP0-x5KhJOy523iob3vQpPMDxtuD68We5v-DNDs-bbfHDr0Lnbq2RREKROvhjRP3-PyyxomtjjH5HRAbJ_5BPtW8bnEh4OmhJF_D-PtLUkqKCO3_n7MJDozs4JJXJ5t34uRQttjQU3ufIkja-5tKt3GqJ7TyU45bU47yaOXQTIHJnkDoItyfIvbfP0k2Jo_h-F_hxrjetJyaR3e2PbbWJ5TMCo63P7C-j5WXMRfK4vuaDnTbquhQpC-ShPC-tPh3t4e5Jb0qRItQb5yQxow3l02VhbEe-t2ynLV-xQEbPRMW20e0h7mWIb_VKF4j5taD5ObeaRf-b-XM6TXWnTqaJT2KROvhjRzQnLyyxomtjjfQKbN3CL5BnvbbJnEh4Om0x6L3-FqLUkqKC8t-R7ObxOEbtFG3TroKqD4QttjQU3ufIkja-5tKJj0qb7TyU45bU47yaOXQTIHJnkDoItyfIvbfP0k2Jo_h-F_hxrjetJyaR0J_qQbWJ5TMCo63P7CW5QWXM4JtPvuaDnT_nQkfUD-ShPC-fuh3t4e5Jb0qRItQb5yQxow3l02VhbEe-t2ynLV-xQEbPRMW20e0h7mWIb_VKF4D60WejoQjaRf-b-X5I6J3C5aHJOoDDvFLTO5y4LdjG5C5J3BHC_f2nv4WJnYDRbM5UQDDbKX3-Aq5xcUQJ6LQn5Ibt5AJbcChhoDQfbQ0hQuqP-jW5TahnjEbb7JOpkRbUnxy50H0aCHtT-Dtn4OVIv5b-0_Jt5kh-rHh4FQqxby26ngJJneaJ5nJDobSnn-W5_bX-PDLf7u2t3TJIcwVUDKQpP-HqIG3tno5qtteqCtL5cy-GrkKl0MLpbYbb0xynoD-4_hKMnMBMPe52OnaIb8LIcjqR8Zj60MD6QP',
    }

    start_page = int(input('请输入你想爬取的起始页面:'))
    end_page = int(input('请输入你想爬取的结束页面:'))

    for page in range(start_page, end_page+1):
        print("正在爬取第%s页......"%(page))
        url = url + str(page)
        req = urllib.request.Request(url = url, headers = headers)
        get_html(req)
        print('结束第%s页!'%(page))


if __name__ == '__main__':
    main()







