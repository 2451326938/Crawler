#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

user_agent = [
# "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
# "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
# "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
# "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
# "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
# "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
# "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
# "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
# "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
# "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3"
# 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48',
# 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
]
i_headers = {'User-Agent': random.choice(user_agent)}
# i_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

# i_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
# i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
url = "http://hrb.58.com/chuzu/pn1/"
iplist = ['106.56.102.190',
        '115.46.99.180',
        '117.86.10.221',
        '117.86.206.57',
        '111.155.116.225',
        '106.56.102.90',
        '106.90.74.107',
        '106.56.102.43',
        '117.86.165.164',
        '119.5.1.51',
        '119.5.0.3',
        '122.246.49.47',
        '110.73.8.14',
        '114.231.71.72',
        '115.219.110.236',
        '171.113.159.117',
        '113.58.233.118',
        '182.88.164.134',
        '117.86.201.254',
        '111.226.188.4',
        '180.121.131.97',
        '59.173.73.126',
        '182.112.250.86',
        '171.38.24.173',
        '106.56.102.155',
        '119.5.1.21',
        '171.37.166.247',
        '110.73.6.24',
        '117.86.9.69',
        '121.31.176.22',
        '221.227.250.164',
        '175.155.208.35',
        '110.73.43.122',
        '117.86.8.22',
        '110.73.1.176',
        '106.8.17.90',
        '117.86.202.76',
        '175.155.24.6',
        '171.37.158.190',
        '222.186.45.135',
        '112.95.22.63',
        '221.227.248.214',
        '117.86.8.209',
        '111.72.154.95',
        '117.86.204.130',
        '112.90.37.19',
        '110.85.89.149',
        '180.118.240.39',
        '121.31.151.68',
        '123.55.3.23',]
proxy = {u'https':random.choice(iplist)}

