import requests
import re
from bs4 import BeautifulSoup



'''
robots.txt出现
    User-agent: *
    Disallow: /
即不允许任何爬虫爬取
'''


#不会




#
# import requests
# import re
# from bs4 import BeautifulSoup
# import bs4
#
# '''
# 数据线起始页https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306
# 数据线第二页https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
# 数据线第三页https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s=88
# '''
# def get_html_text(url):
#     try:
#         r=requests.get(url,timeout=30)
#         r.raise_for_status()
#         r.encoding=r.apparent_encoding
#         return r.text
#     except :
#         return '该网页请求连接失败'
#
# #通过脚本语言编写的html代码，不是完整的html语言，直接搜索相对比较简单
# #正则表达式原生字符串你还没有理解，最小匹配原则  视频时间11:20
# def parse_page(list_info,html):
#     try:
#         list_price=re.findall(r'"view_price":"[\d.]*"',html)
#         list_title=re.findall(r'"raw_title":".*?"',html)
#         list_location=re.findall(r'"item_loc":".*?"',html)
#         #list_num_payment=re.findall(r'"view_sales":"u"',html)
#         for i in range(len(list_price)):
#             price=eval(list_price[i].split(':')[1])
#             title=eval(list_title[i].split(':')[1])
#             location=eval(list_location[i].split(':')[1])
#             #num_payment=eval(list_num_payment.split(':')[1])
#             #list_info.append([price,num_payment,location,title])
#             list_info.append([price,location,title])
#     except :
#         print('解析网页出现异常')
#
# def print_goods_info(list_info):
#     #tplt='{:4}\t{:8}\t{:8}\t{:12}\t{:20}\t'
#     tplt='{:4}\t{:8}\t{:12}\t{:20}\t'
#     #print(tplt.format('序号','商品价格','付款人数','发货地址','商品名称'))
#     print(tplt.format('序号','商品价格','发货地址','商品名称'))
#     count=0
#     for goods in list_info:
#         count+=1
#         #print(tplt.format(count,goods[0],goods[1],goods[2],goods[3]))
#         print(tplt.format(count,goods[0],goods[1],goods[2]))
#
# if __name__ == '__main__':
#     goods='书包'
#     depth=2
#     start_url='https://s.taobao.com/search?q='+goods
#     list_info=[]
#     for i in range(depth):
#         try:
#             url=start_url+'&s='+str(44*i)
#             html=get_html_text(url)
#             parse_page(list_info,html)
#         except:
#             continue        #如果某一个页面出现了问题，则会跳过该页面的解析，而不会影响程序的整体运行
#     print_goods_info(list_info)
#
#
#














































# import requests
# import re
#
#
# def getHTMLText(url):
#     try:
#         header = {
#
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
#
#             'cookie': '__wpkreporterwid_=aefb6b69-d19a-4a15-1266-39cf90206004; t=d8a364d9af76d55fa07ca0aa02f0a802; cna=KglLGnAhsncCAXWIUw+hoyHB; sgcookie=E100iU6QqXMi1XVgQabvDdNbjV+Q8CWHawyGjVJSIW1rYt3Yl5n2tQI9cRk1ajVvUSADRY2OWmvqtRaMyrswTL3/EbifmNHqemn+AJr7GDjSVyETWuZb7ndgletAzuj9Dlkm; uc3=nk2=F5RHo3xh1yBJRA==&vt3=F8dCvClxS9k1B7H8sLw=&lg2=V32FPkk/w0dUvg==&id2=UNiMiO/PL3WxYw==; lgc=tb22767606; uc4=nk4=0@FY4MsTY8xjJPH1K0XNrNJi9zyr56&id4=0@Ug+TWIUbwLFoMBXAzJADPd7KxFal; tracknick=tb22767606; _cc_=W5iHLLyFfA==; thw=cn; ctoken=_7Y-iHbatMqLEHvuZqY9V3g1; lego2_cna=U4CMCUHE8THWYE2R0MUC0H4Y; mt=ci=-1_0; cookie2=1166385435f03047277ccc2b6e1b141f; _tb_token_=f1fe3ae33e5ea; _m_h5_tk=9d405f057fec79e2deb1cbbe825937cb_1652551280049; _m_h5_tk_enc=4257d692d74c64d7512d744e7f341e7f; uc1=cookie14=UoexMNH2agka0w==; isg=BFFRjIEQ1x8VWjsV7_K9WOBVYF3rvsUwskv-0DPmQpg32nEsew7NAP47eC48SV1o; tfstk=cmH5BgfXtab5fWdFU0t2LE3X_dwdZ2TbmQa-VEw3kCxD3ln5ibXa5DlstZ2Uvo1..; l=eBxK5ucrLzyHaQ-1BOfZourza77OIIRYYuPzaNbMiOCP_P5B5t0VW64hP4T6Cn1Vh682R3SvCNIkBeYBq3K-nxvtNSVsrVMmn'
#
#         }
#         r = requests.get(url, timeout=30, headers=header)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return ""
#
#
# def parsePage(ilt, html):
#     try:
#         plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
#         tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
#         for i in range(len(plt)):
#             price = eval(plt[i].split(':')[1])
#             title = eval(tlt[i].split(':')[1])
#             ilt.append([price, title])
#     except:
#         print("1312")
#
# def printGoodsList(ilt):
#     tplt = "{:4}\t{:8}\t{:16}"
#     print(tplt.format("序号","价格","商品名称"))
#     count = 0
#     for g in ilt:
#         count = count + 1
#         print(tplt.format(count,g[0],g[1]))
#
#
# def main():
#     goods = '手表'
#     depth = 2
#     start_url = 'https://s.taobao.com/search?q=' + goods
#     infoList = []
#     for i in range(depth):
#         try:
#             url = start_url + '&s=' + str(44 * i)
#             html = getHTMLText(url)
#             parsePage(infoList, html)
#         except:
#             continue
#     printGoodsList(infoList)
#
#
# main()
#




#
#
# # 导入requests和re正则库
# import requests
# import re
#
#
# # 定义第一个函数实现获取网页数据
# def getHTMLText(url, loginheaders):
#     try:
#         r = requests.get(url, headers=loginheaders, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         # print(r.text)
#         return r.text
#     except:
#         return ""
#
#
# # 定义一个函数实现把书包信息存储区来，包括编号，价格，名称
# def parsePage(ilt, html):
#     try:
#         # 要明白 .* 代表的是任意个不同字符,而不是说必须是任意个相同的字符,其他的也是类似
#         # re.findall()返回的是列表类型
#         # 利用正则表达式查找价格（"view_price":"任意个数的任意数字加点"）,所以正则表达式还可在小数点后加两个0写成r'\"view_price\"\:\"[\d\.]*00\"'
#         plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
#         # 利用正则表达式查找题目（"raw_title":"任意个数的任意字符"）
#         tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
#         # 循环遍历价格和题目，利用:分隔符获得值
#         for i in range(len(plt)):
#             price = eval(plt[i].split(':')[1])
#             title = eval(tlt[i].split(':')[1])
#             # 添加到ilt列表当中,二维元组列表
#             ilt.append([price, title])
#     except:
#         print("")
#
#
# # 打印题目和爬取的信息
# def printGoodsList(ilt):
#     # 定义输出格式
#     tplt = "{:4}\t{:8}\t{:16}"
#     print(tplt.format("序号", "价格", "商品名称"))
#     # 循环遍历打印爬取到的信息,第一种方式
#     for i in range(len(ilt)):
#         print(tplt.format(i + 1, ilt[i][0], ilt[i][1]))
#     # 第二种方式,g是从ilt循环遍历每元组的每项,g[0],g[1]是价格和题目
#     # count = 0
#     # for g in ilt:
#     #     count = count + 1
#     #     print(tplt.format(count, g[0], g[1]))
#
#
# # 定义主函数，写一下变量
# def main():
#     goods = '书包'
#     # depth是爬取的深度，也就是爬取几页
#     depth = 3
#     start_url = 'https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword' + goods
#     infoList = []
#     for i in range(depth):
#         try:
#             url = start_url + '&s=' + str(44 * i)
#             # 设置登录的头信息，注意cookie是登陆页面点击登录获取的头信息
#             loginheaders = {
#                 # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
#                 # "cookie": "t=4ddf8b70981503ff445f594236c71e96; thw=cn; cookie2=12bdc5dde93e3514edca199a193f232f; _tb_token_=e45e8be4e50be; _samesite_flag_=true; enc=201s0rRJEHeguaLLCC6IAbLJao3k%2FWpbaR4FH6jpx1T6haa1auRivMShxlx1S0Ul3c3meKsTzPUcwTv3aEzt1Q%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; alitrackid=www.taobao.com; lastalitrackid=login.taobao.com; mt=ci=0_0; JSESSIONID=C7EA2D8019D08587402413BDBF38AFF0; cna=k8/5Fvt7vU8CAbfIPj2evd1M; l=eBxklgrHqCn48L6LBOfZourza77TlIRfguPzaNbMiT5P_2fH75cAWZjFnt8MCnGVnsZw-354uljQBrT8xyUBh6Yl3ZQ7XPQo3dTh.; isg=BFFRjiZN687i_QTKjM76nskzYF3rvsUwkMIhzjPmIpg42nAseQpbAHY4fK48Ul1o; tfstk=cwyCBJqLmeYQTTeeQzsZTKVPlrkPZj_sj6gLA5hd3EP90jECibvqlvj4ZFvtMc1..; sgcookie=EjxPeg5aM1t9jg2xwmUNw; unb=2639049752; uc1=cookie14=UoTUMtQjutczRQ%3D%3D&cookie21=VFC%2FuZ9ajC0X15Rzt0LhxQ%3D%3D&pas=0&existShop=false&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D; uc3=nk2=2nZbzUmLMMCi2g%3D%3D&vt3=F8dBxGXMemSB7fdhNUQ%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&id2=UU6idYdXStUjdg%3D%3D; csg=8948e7ae; lgc=%5Cu90ED%5Cu5DDD%5Cu5DDD1998; cookie17=UU6idYdXStUjdg%3D%3D; dnk=%5Cu90ED%5Cu5DDD%5Cu5DDD1998; skt=b778092dd81708b9; existShop=MTU4ODQ3NzIxNQ%3D%3D; uc4=id4=0%40U2xvIZeyY044%2Fg4ssnvrOTWRM69N&nk4=0%402EwyHO%2FQs1K5Yt3PADSqX0DTequA; tracknick=%5Cu90ED%5Cu5DDD%5Cu5DDD1998; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=82b; _nk_=%5Cu90ED%5Cu5DDD%5Cu5DDD1998; cookie1=BvGDAyiO3yivOSSiEiVryF%2FdX85RndH78rFBY0y3kOc%3D"
#                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
#                 "cookie":' __wpkreporterwid_=aefb6b69-d19a-4a15-1266-39cf90206004; t=d8a364d9af76d55fa07ca0aa02f0a802; cna=KglLGnAhsncCAXWIUw+hoyHB; sgcookie=E100iU6QqXMi1XVgQabvDdNbjV+Q8CWHawyGjVJSIW1rYt3Yl5n2tQI9cRk1ajVvUSADRY2OWmvqtRaMyrswTL3/EbifmNHqemn+AJr7GDjSVyETWuZb7ndgletAzuj9Dlkm; uc3=nk2=F5RHo3xh1yBJRA==&vt3=F8dCvClxS9k1B7H8sLw=&lg2=V32FPkk/w0dUvg==&id2=UNiMiO/PL3WxYw==; lgc=tb22767606; uc4=nk4=0@FY4MsTY8xjJPH1K0XNrNJi9zyr56&id4=0@Ug+TWIUbwLFoMBXAzJADPd7KxFal; tracknick=tb22767606; _cc_=W5iHLLyFfA==; thw=cn; ctoken=_7Y-iHbatMqLEHvuZqY9V3g1; lego2_cna=U4CMCUHE8THWYE2R0MUC0H4Y; mt=ci=-1_0; cookie2=1166385435f03047277ccc2b6e1b141f; _tb_token_=f1fe3ae33e5ea; _m_h5_tk=9d405f057fec79e2deb1cbbe825937cb_1652551280049; _m_h5_tk_enc=4257d692d74c64d7512d744e7f341e7f; uc1=cookie14=UoexMNH2agka0w==; isg=BFFRjIEQ1x8VWjsV7_K9WOBVYF3rvsUwskv-0DPmQpg32nEsew7NAP47eC48SV1o; tfstk=cmH5BgfXtab5fWdFU0t2LE3X_dwdZ2TbmQa-VEw3kCxD3ln5ibXa5DlstZ2Uvo1..; l=eBxK5ucrLzyHaQ-1BOfZourza77OIIRYYuPzaNbMiOCP_P5B5t0VW64hP4T6Cn1Vh682R3SvCNIkBeYBq3K-nxvtNSVsrVMmn'
#             }
#             html = getHTMLText(url, loginheaders)
#             parsePage(infoList, html)
#         except:
#             continue
#     printGoodsList(infoList)
#
#
# main()
#
#
