from django.shortcuts import render
from django.http import HttpResponse
import requests


def test(request):
    url = 'https://www.baidu.com/s'
    params = {
        'ie': 'utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python3%20%E5%8F%91%E9%80%81get%E8%AF%B7%E6%B1%82',
        'op': 'python%2520%25E5%258F%2591%25E9%2580%2581get%25E8%25AF%25B7%25E6%25B1%2582',
        'rsv_pq': 'f771809b0000d56a',
        'rsv_t': '984b9z2d%2FGtWDjySpn4c2vyjpSLyY4b1EDRKrBZDxWbn%2Bzr2lPIfhUt7PAM',
        'ralang': 'cn&rsv_enter=1&inputT=196',
        'rsv_sug3': '105&rsv_sug1=84',
        'rsv_sug7': '100',
        'rsv_sug2': '0',
        'prefixsug': 'python%2526lt%253B%2520%25E5%258F%2591%25E9%2580%2581get%25E8%25AF%25B7%25E6%25B1%2582',
        'rsp': '1',
        'rsv_sug4': '1810'
    }

    re = requests.get(url, params)
    text = re.text.replace('location.replace(location.href.replace("https://","http://"));', '')
    print('get text: %s' % text)
    return HttpResponse(text)
