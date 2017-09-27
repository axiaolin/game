import re,requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
def liebiao(page):
    url=''.format(page)
    html=requests.get(url,headers=headers)
    h=html.content.decode()
    html.close()
    info=re.findall(r'<h4><a href="(.+?)" title="(.+?)" target="_blank" itemprop="name"',h)
    return info
def parse(info):
    url=info[0]
    company=info[1]
    html=requests.get(url,headers=headers)
    h=html.content.decode()
    html.close()
    mobe=re.search(r'手机：</label>(\d+?)</li>',h).group(1)
    name=re.search(r'<li><label>联系人：(.+?)</li>',h).group(1)
    name=re.sub(r'<.+?>','',name)
    return {'公司':company,'联系人':name,'电话':mobe}
if __name__=="__main__":
    for i in liebiao(1):
        print(parse(i))