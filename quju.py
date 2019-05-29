# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests

class downloader(object):
 
    def __init__(self):
        self.server = 'http://www.fl5y.com'
        self.target = 'http://www.fl5y.com/xiazai/quju/index_'
        self.names = []   
        self.tmp_urls = []          
        self.urls = []

    def get_url(self):
        for i in range(1,11):
            tmp_url = self.target+str(i)+'.html'
            req = requests.get(url = tmp_url)
            html = req.text
            html = html.encode('latin1').decode('gbk')
            bf = BeautifulSoup(html,features="html.parser")
            texts = bf.find_all('table', class_ = 'table table-hover') 
            a_bf = BeautifulSoup(str(texts),features="html.parser")
            a = a_bf.find_all('a')
            for each in a:
                if each.get('title').split('-')[0]=='曲剧全场': 
                    self.names.append(each.get('title'))
                    self.tmp_urls.append(self.server + each.get('href'))

    def get_true_url(self):
        for each in self.tmp_urls:
            req = requests.get(url = each)
            html = req.text
            html = html.encode('latin1').decode('gbk')
            bf = BeautifulSoup(html,features="html.parser")
            texts = bf.find_all('span','btn btn-success icon-download-alt') 
            a_bf = BeautifulSoup(str(texts),features="html.parser")
            a = a_bf.find_all('a')
            self.urls.append(a[0].get('href'))

    def write_names(self):
        with open('已下载.txt','a+') as f:
            for each in self.names:
                f.write(each+'\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_url()
    dl.write_names()
    # dl.get_true_url()
    # print(dl.names)
    # print(dl.urls)