#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time : 2017/05/24
# @Author : Iric
# @File : hello.py
from bs4 import BeautifulSoup
import requests


class Crawler(object):
    url = 'https://www.zhihu.com/api/v4/members/zhang-zhi-wei-20-93/publications'
    params = {
        'include': 'data%5B*%5D.cover%2Cebook_type%2Ccomment_count%2Cvoteup_count',
        'offset': '0',
        'limit': '5'
    }
    re = requests.get(url, params)
    soup = BeautifulSoup(re.text)

    def print_prettify(self):
        print(self.soup.prettify())


if (__name__ == '__main__'):
    print('do crawler:')
    Crawler.print_prettify(Crawler())
    print('end crawler')
