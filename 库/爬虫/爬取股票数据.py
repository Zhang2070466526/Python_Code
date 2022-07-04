import requests
import traceback
import re
import bs4
from bs4 import BeautifulSoup


url="http://quote.eastmoney.com/center/gridlist.html#us_chinese_internet"
def getHtmlText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "Error!"

html=getHtmlText(url)
# html='<table id="table_wrapper-table" class="table_wrapper-table"><thead><tr role="row"><th style="" class="listview-col-number sorting_disabled" rowspan="1" colspan="1" aria-label="序号"><span style="color: rgb(51, 51, 51); --darkreader-inline-color:#c8c3bc;" data-darkreader-inline-color="">序号</span><b class="icon"></b></th><th style="" class="listview-col-Name sorting" rowspan="1" colspan="1" aria-label="名称" data-key="f14"><span>名称</span><b class="icon"></b></th><th style="" class="listview-col-Close sorting" rowspan="1" colspan="1" aria-label="最新价(美元)" data-key="f2"><span>最新价(美元)</span><b class="icon"></b></th><th style="" class="listview-col-Change sorting" rowspan="1" colspan="1" aria-label="涨跌额" data-key="f4"><span>涨跌额</span><b class="icon"></b></th><th style="" class="listview-col-ChangePercent sorting_desc" rowspan="1" colspan="1" aria-label="涨跌幅" data-key="f3"><span>涨跌幅</span><b class="icon"></b></th><th style="" class="listview-col-Open sorting" rowspan="1" colspan="1" aria-label="开盘价" data-key="f17"><span>开盘价</span><b class="icon"></b></th><th style="" class="listview-col-Hign sorting" rowspan="1" colspan="1" aria-label="最高价" data-key="f15"><span>最高价</span><b class="icon"></b></th><th style="" class="listview-col-Low sorting" rowspan="1" colspan="1" aria-label="最低价" data-key="f16"><span>最低价</span><b class="icon"></b></th><th style="" class="listview-col-PreviousClose sorting" rowspan="1" colspan="1" aria-label="昨收价" data-key="f18"><span>昨收价</span><b class="icon"></b></th><th style="" class="listview-col-undefined sorting" rowspan="1" colspan="1" aria-label="总市值(美元)" data-key="f20"><span>总市值(美元)</span><b class="icon"></b></th><th style="" class="listview-col-undefined sorting" rowspan="1" colspan="1" aria-label="市盈率" data-key="f115"><span>市盈率</span><b class="icon"></b></th></tr></thead><tbody><tr class="odd"><td>1</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/105.BZUN">宝尊电商</a></td><td><span class="red">7.64</span></td><td><span class="red">0.84</span></td><td class="mywidth2"><span class="red">12.35%</span></td><td><span class="red">7.12</span></td><td><span class="red">7.77</span></td><td><span class="red">7.08</span></td><td>6.80</td><td>5.17亿</td><td>-14.98</td></tr><tr class="even"><td>2</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/106.LEJU">乐居</a></td><td><span class="red">0.35</span></td><td><span class="red">0.03</span></td><td class="mywidth2"><span class="red">9.38%</span></td><td><span class="red">0.34</span></td><td><span class="red">0.38</span></td><td><span class="green">0.31</span></td><td>0.32</td><td>4788.79万</td><td>-0.32</td></tr><tr class="odd"><td>3</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/105.XNET">迅雷</a></td><td><span class="red">1.23</span></td><td><span class="red">0.10</span></td><td class="mywidth2"><span class="red">8.85%</span></td><td><span class="red">1.17</span></td><td><span class="red">1.25</span></td><td><span class="red">1.14</span></td><td>1.13</td><td>8300.73万</td><td>69.70</td></tr><tr class="even"><td>4</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/106.BABA">阿里巴巴</a></td><td><span class="red">87.99</span></td><td><span class="red">6.90</span></td><td class="mywidth2"><span class="red">8.51%</span></td><td><span class="red">82.12</span></td><td><span class="red">88.36</span></td><td><span class="red">82.00</span></td><td>81.09</td><td>2385.33亿</td><td>23.46</td></tr><tr class="odd"><td>5</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/105.BIDU">百度</a></td><td><span class="red">116.94</span></td><td><span class="red">9.06</span></td><td class="mywidth2"><span class="red">8.40%</span></td><td><span class="red">112.40</span></td><td><span class="red">117.97</span></td><td><span class="red">112.05</span></td><td>107.88</td><td>417.96亿</td><td>26.06</td></tr><tr class="even"><td>6</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/105.MOMO">挚文集团</a></td><td><span class="red">5.06</span></td><td><span class="red">0.30</span></td><td class="mywidth2"><span class="red">6.30%</span></td><td><span class="red">4.85</span></td><td><span class="red">5.22</span></td><td><span class="red">4.84</span></td><td>4.76</td><td>10.04亿</td><td>-2.20</td></tr><tr class="odd"><td>7</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/105.TOUR">途牛</a></td><td><span class="red">0.51</span></td><td><span class="red">0.03</span></td><td class="mywidth2"><span class="red">6.25%</span></td><td><span class="red">0.50</span></td><td><span class="red">0.54</span></td><td><span class="green">0.47</span></td><td>0.48</td><td>6308.40万</td><td>-3.31</td></tr><tr class="even"><td>8</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/105.JD">京东</a></td><td><span class="red">51.55</span></td><td><span class="red">2.88</span></td><td class="mywidth2"><span class="red">5.92%</span></td><td><span class="red">49.96</span></td><td><span class="red">52.35</span></td><td><span class="red">49.71</span></td><td>48.67</td><td>805.08亿</td><td>-144.18</td></tr><tr class="odd"><td>9</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/105.FTNT">防特网</a></td><td><span class="red">281.55</span></td><td><span class="red">14.89</span></td><td class="mywidth2"><span class="red">5.58%</span></td><td><span class="red">272.56</span></td><td><span class="red">283.49</span></td><td><span class="red">272.34</span></td><td>266.66</td><td>451.96亿</td><td>70.84</td></tr><tr class="even"><td>10</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/106.CMCM">猎豹移动</a></td><td><span class="red">0.76</span></td><td><span class="red">0.04</span></td><td class="mywidth2"><span class="red">5.56%</span></td><td><span class="red">0.76</span></td><td><span class="red">0.76</span></td><td><span class="green">0.71</span></td><td>0.72</td><td>1.07亿</td><td>1.69</td></tr><tr class="odd"><td>11</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/105.NTES">网易</a></td><td><span class="red">92.46</span></td><td><span class="red">4.50</span></td><td class="mywidth2"><span class="red">5.12%</span></td><td><span class="red">90.60</span></td><td><span class="red">93.05</span></td><td><span class="red">90.60</span></td><td>87.96</td><td>607.28亿</td><td>22.97</td></tr><tr class="even"><td>12</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/105.VNET">世纪互联</a></td><td><span class="red">5.99</span></td><td><span class="red">0.27</span></td><td class="mywidth2"><span class="red">4.72%</span></td><td><span class="red">5.81</span></td><td><span class="red">6.15</span></td><td><span class="red">5.81</span></td><td>5.72</td><td>8.89亿</td><td>11.34</td></tr><tr class="odd"><td>13</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/105.WB">微博</a></td><td><span class="red">21.18</span></td><td><span class="red">0.84</span></td><td class="mywidth2"><span class="red">4.13%</span></td><td><span class="red">20.97</span></td><td><span class="red">21.80</span></td><td><span class="red">20.50</span></td><td>20.34</td><td>51.84亿</td><td>12.10</td></tr><tr class="even"><td>14</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/105.SOHU">搜狐</a></td><td><span class="red">14.44</span></td><td><span class="red">0.53</span></td><td class="mywidth2"><span class="red">3.81%</span></td><td><span class="red">14.14</span></td><td><span class="red">14.77</span></td><td><span class="red">14.09</span></td><td>13.91</td><td>5.52亿</td><td>0.59</td></tr><tr class="odd"><td>15</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/106.FENG">凤凰新媒体</a></td><td><span class="red">0.45</span></td><td><span class="red">0.01</span></td><td class="mywidth2"><span class="red">2.27%</span></td><td><span class="fair">0.44</span></td><td><span class="red">0.46</span></td><td><span class="fair">0.44</span></td><td>0.44</td><td>3275.57万</td><td>-0.81</td></tr><tr class="even"><td>16</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/106.YRD">宜人金科</a></td><td><span class="red">1.84</span></td><td><span class="red">0.02</span></td><td class="mywidth2"><span class="red">1.10%</span></td><td><span class="fair">1.82</span></td><td><span class="red">1.85</span></td><td><span class="green">1.74</span></td><td>1.82</td><td>1.55亿</td><td>7.14</td></tr><tr class="odd"><td>17</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/106.ZPIN">智联招聘</a></td><td><span class="fair">-</span></td><td><span class="fair">-</span></td><td class="mywidth2"><span class="fair">-</span></td><td><span class="fair">-</span></td><td><span class="fair">-</span></td><td><span class="fair">-</span></td><td>-</td><td>-</td><td>-</td></tr><tr class="even"><td>18</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/106.WUBA">58同城</a></td><td><span class="fair">-</span></td><td><span class="fair">-</span></td><td class="mywidth2"><span class="fair">-</span></td><td><span class="fair">-</span></td><td><span class="fair">-</span></td><td><span class="fair">-</span></td><td>-</td><td>-</td><td>-</td></tr><tr class="odd"><td>19</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/105.SINA">新浪</a></td><td><span class="fair">-</span></td><td><span class="fair">-</span></td><td class="mywidth2"><span class="fair">-</span></td><td><span class="fair">-</span></td><td><span class="fair">-</span></td><td><span class="fair">-</span></td><td>43.26</td><td>-</td><td>-</td></tr><tr class="even"><td>20</td><td class="mywidth"><a href="//quote.eastmoney.com/unify/r/105.JOBS">前程无忧</a></td><td><span class="fair">-</span></td><td><span class="fair">-</span></td><td class="mywidth2"><span class="fair">-</span></td><td><span class="fair">-</span></td><td><span class="fair">-</span></td><td><span class="fair">-</span></td><td>60.90</td><td>41.07亿</td><td>40.87</td></tr></tbody></table>'
# soup=BeautifulSoup(html,'html.parser')
# tds=[]
# stockInfo=[]
# for tr in soup.find('tbody').children:
#     if isinstance(tr, bs4.element.Tag):
#         tds=tr.find_all('td')
#         print(tds)
#         name=tds[1].string
#         latestPrice=tds[2].string
#         stockInfo.append([name,latestPrice])
# print(stockInfo)


lst=[]
soup=BeautifulSoup(html,'html.parser')
a=soup.find_all('a')
print(a)
for i in a:
    try:
        href=i.attrs['href']
        lst_s=re.findall(r"[s][hz]\d{6}",href)[0]  #<a href="http://quote.eastmoney.com/flash/sz300059.html">行情</a>
        #根据雪球网的网址，股票代码前面的字母均需要变为大写
        lst.append(lst_s.upper())
        # print(lst_s)
    except:
        continue
for lists in lst:
    print(lists)












# def getHtmlText(url):
#     pass
#
# def getStockList(lst,stockURL):  #股票信息列表   lst：保存数据的列表      stockURL:爬取股票的url
#     pass
#
# def getStockInfo(lst,stockURL,fpath):   #每一只个股的股票信息   fpath:文件保存路径
#     pass
#
#
# def main():
#     stock_list_url=
#
#
#
# main()

















#
# #-------------------------------------------------------------------------------
# #任务：定向爬取股票数据
# #技术路线：requests-BeautifulSoup-re
# #股票列表获取：东方财富网
# #股票信息获取：雪球网
# #因为雪球网与百度股票的html是不一样的，因此只能通过搜索一个个属性中的数值来爬取
# #在这里仅爬取股票名称，股票价格，股票当前状态与交易时间
# #该代码的爬取结果：前小部分的股票仅能爬取到名字，后面大部分都能爬取到名称，价格，状态和时间，原因未知
# #-------------------------------------------------------------------------------
# import requests
# from bs4 import BeautifulSoup
# import traceback
# import re
#
# def getHTMLText(url,code='utf-8'):
#     try:
#         #东方财富网的列表数据可以直接获取，但是爬取雪球网需要就行浏览器的伪装
#         kv={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
#         r=requests.get(url,headers=kv,timeout=30)
#         r.raise_for_status()
#         r.encoding=code
#         return r.text
#     except:
#         return "1?"
#
# #从东方财富网爬取股票代码，并存入到列表中
# def getStockList(lst,stockURL):
#     html=getHTMLText(stockURL)
#     soup=BeautifulSoup(html,'html.parser')
#     a=soup.findAll('a')
#     for i in a:
#         try:
#             href=i.attrs['href']
#             lst_s=re.findall(r"[s][hz]\d{6}",href)[0]
#             #根据雪球网的网址，股票代码前面的字母均需要变为大写
#             lst.append(lst_s.upper())
#         except:
#             continue
#     for lists in lst:
#         print(lists)
#
# #从雪球网获取每个股票代码对应的股票信息
# def getStockInfo(lst,stockURL,fpath):
#     count=0
#     for stock in lst:
#         url=stockURL+stock
#         html=getHTMLText(url)
#         try:
#             #如果网页为空，则跳过这一次，继续循环
#             if html=="":
#                 continue
#             infoDict={}
#             soup=BeautifulSoup(html,'html.parser')
#
#             #stock_name_Info=soup.find('div',attrs={'class':'page-row'})
#             #.find如果无法查找到该属性，会返回NoneType，其值为None
#             #字典的更新需要一对键值对
#             name=soup.find('div',attrs={'class':'stock-name'})
#             if name is None:
#                 infoDict.update({'股票名称':'查询不到该股票'})
#                 #print("查询不到该股票")
#             else:
#                 infoDict.update({'股票名称':name.text.split()[0]})
#
#             #stockInfo=soup.find_all('div',attrs={'class':'stock-info'})[0]
#             price=soup.find('div',attrs={'class':'stock-current'})
#             if price is None:
#                 infoDict.update({'当前价格':'查询不到当前价格'})
#                 #print("无当前价格")
#             else:
#                 infoDict.update({'当前价格':price.text.split()[0]})
#
#             flags=soup.find(attrs={'class':'stock-flag'})
#             if flags is None:
#                 infoDict.update({'当前状态':'查询不到当前状态'})
#                 #print("无当前状态")
#             else:
#                 infoDict.update({'当前状态':flags.text.split()[0]})
#
#             times=soup.find('div',attrs={'class':'stock-time'})
#             if times is None:
#                 infoDict.update({'交易时间':'查询不到交易时间'})
#                 #print("无交易时间")
#             else:
#                 infoDict.update({'交易时间':times.span.text.split()[0]})
#
#             #keyList=stockInfo.find_all('td')
#             #valueList=stockInfo.find_all('span')
#
#             #for i in range(len(keyList)):
#                 #key=keyList[i].text
#                 #val=valueList[i].text
#                 #infoDict[key]=val
#
#             with open(fpath,'a',encoding='utf-8') as f:
#                 f.write(str(infoDict)+'\n')
#                 count=count+1
#                 print('\r当前速度：{:.2f}%'.format(count*100/len(lst)),end="")
#                 #print("文件已经保存")
#         except:
#             traceback.print_exc()
#             count=count+1
#             print('\r当前速度：{:.2f}%'.format(count*100/len(lst)),end="")
#             #print("2?")
#             continue
#
# def main():
#     stock_list_url='http://quote.eastmoney.com/stock_list.html'
#     stock_info_url='https://xueqiu.com/S/'
#     output_file='F:\TecentstockInfo.txt'
#     slist=[]
#     getStockList(slist,stock_list_url)
#     getStockInfo(slist,stock_info_url,output_file)
#
#
# if __name__ == '__main__':
#     main()
#
