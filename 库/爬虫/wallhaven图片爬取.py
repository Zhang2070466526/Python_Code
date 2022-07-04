import  requests
from bs4 import BeautifulSoup

url="https://wallhaven.cc/toplist?page=1"
r=requests.get(url)
r.encoding=r.apparent_encoding

soup=BeautifulSoup(r.text,"html.parser")
# print(soup.prettify())
tag=soup.body.section
n=0
ls=[]
for li in tag.find('ul').children:
    #缩略图
    a = li.find('a', {'target': '_blank', 'class': 'preview'})
    href = a.attrs['href']  # 大图url
    ls.append(href)
    # print(href)
    #
    # #大图
    # b_url = href
    # b_r= requests.get(url)
    # b_soup = BeautifulSoup(b_r.text,'html.parser')
    #
    #
    # b_Tag = b_soup.body.main.div
    # print(b_Tag)
    # # bigImg_src=bigTag.attrs['data-src']
    # # # print(bigTag.attrs['data-src'])
    #

    # n+=1
    # #保存图片
    # f = open("D:\\20704\\桌面\\小姐姐" + str(n) + ".jpg", 'wb')
    # f.write(requests.get(bigImg_src).content)
    # print("第{}张下载成功!".format(n))

    # import  os
    # r_url = requests.get(bigImg_src)
    # root = "D:\\20704\\桌面\\"
    # bigImg_name=bigImg_src.split('/')[-1]
    # print(bigImg_name)
    # path = root +str(n)+ bigImg_name# 要保存的地址
    # with open(path,'wb') as f:
    #     f.write(r_url.content) #写入r的二进制形式
# print("prettify")
# print(ls)


# for li in soup.find_all('ul'):
#     print(li)






# url="https://wallhaven.cc/w/pkzjg3"
# #<a class="preview" href="https://wallhaven.cc/w/pkzjg3" target="_blank"></a>
# r=requests.get(url)
# soup=BeautifulSoup(r.text,'html.parser')
# tag=soup.body.main.div.img
# print(tag.attrs['src'])
# # print(tag.artrs['src'])

count=1
for url in ls:
    try:
        b_r=requests.get(url, timeout=50)  # timeout 超时时间，超过时间会抛出异常
        b_r.raise_for_status()  # 如果状态码不是200,产生异常requests.HttPError
        b_r.encoding=b_r.apparent_encoding
        # print(b_r.text)

        b_soup = BeautifulSoup(b_r.text, 'html.parser')
        b_tag=b_soup.find_all('img')[-1]
        b_src=b_tag.attrs['src']
        # print(b_src)
        # print(requests.get(b_tag.attrs['src']))
        try:
            #保存
            r_url = requests.get(b_src)
            root = "D:\\20704\\桌面\\"
            b_name=b_src.split('/')[-1]
            path = root + b_name# 要保存的地址
            with open(path,'wb') as f:
                f.write(r_url.content) #写入r的二进制形式
            print('第{}张下载成功'.format(count))
        except:
            print("保存失败")
        count += 1
    except:
        print("产生异常")
print('prettify')
