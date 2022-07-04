
import bs4.element
import requests
from bs4 import BeautifulSoup
import bs4

url="https://www.shanghairanking.cn/rankings/bcur/2022"
try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html=r.text
except:
    html=""

soup=BeautifulSoup(html,'html.parser')
data=[]
for tr in soup.find('tbody').children:#tr就是一个大学信息

    if isinstance(tr,bs4.element.Tag):
        tds=tr('td') #tds=tr.find_all('td')
        # print(tds)
        top=tds[0].div.string.replace('\n',"").strip()# 去除换行符和空格   排名
        name=tds[1].div.a.string.replace('\n','').strip()    #  大学名
        province=tds[2].text.replace('\n',"").strip()  # 省份
        type=tds[3].text.replace('\n','').strip()   # 类型
        score=tds[4].string.replace('\n','').strip()  # 总分
        level=tds[5].string.replace('\n','').strip()  # 办学层次
        data.append([top,name,province,type,score,level])
# print(data)
#学校名称槽用中文空格填充,解决对齐问题
print("{0:^2}\t{1:{6}^10}\t{2:^4}\t{3:^3}\t{4:^3}\t{5:^3}".format("排名",'学校名称','省份','类型','总分','办学层次',chr(12288)))
for i in range(len(data)):
    univ=data[i]#每一个大学的信息
    print("{0:^2}\t{1:{6}^10}\t{2:^4}\t{3:^3}\t{4:^3}\t{5:^3}".format(univ[0],univ[1],univ[2],univ[3],univ[4],univ[5],chr(12288)))


"""
        top=tr.find_all('div',re.compile('ranking')) #排名
        print(top[0].string)
        name=tr.find_all('a','name-cn')#大学名
        print(name[0].string) #<class 'bs4.element.NavigableString'>
        province=tr.find_all('td',"")
        print(province)

"""



# def getHTMLText(url):#获取url网页内容
#     try:
#         r=requests.get(url,timeout=30)
#         r.raise_for_status()
#         r.encoding=r.apparent_encoding
#         return r.text
#     except:
#         return ""
#
# def fillUnivList(ulist,html):#提取网页内容中所需信息到列表ulist中
#     soup=BeautifulSoup(html,'html.parser')
#     for tr in soup.find('tbody').children:#tr就是一个大学信息（遍历tbody的儿子节点即tr）
#         if isinstance(tr,bs4.element.Tag):#过滤非标签类型的其他信息
#             tds=tr('td')#将所有td标签存入tds列表中
#             top=tds[0].div.string.replace("\n","").strip()
#             name=tds[1].a.string.replace("\n","").strip()
#             province=tds[2].text.replace('\n','').strip()
#             type=tds[3].text.replace('\n','').strip()
#             score=tds[4].string.replace('\n',"").strip()
#             level=tds[5].text.replace('\n',"").strip()
#             ulist.append([top,name,province,type,score,level])
#     return ulist
#
#
# def printUnivList(ulist,num):#利用数据结构展示并输出结果
#     print("{:^2}\t{:^10}\t{:^4}\t{:^3}\t{:^3}\t{:^3}".format("排名",'学校名称','省份','类型','总分','办学层次'))
#     for tick in range(num):
#         u=ulist[tick]
#         print("{:^2}\t{:^10}\t{:^4}\t{:^3}\t{:^3}\t{:^3}".format(u[0],u[1],u[2],u[3],u[4],u[5]))
#
#
# def main():
#     uinfo=[] #大学信息
#     url="https://www.shanghairanking.cn/rankings/bcur/2022"
#     html=getHTMLText(url)
#     fillUnivList(uinfo,html)
#     printUnivList(uinfo,20)#20所学校信息
#
# main()