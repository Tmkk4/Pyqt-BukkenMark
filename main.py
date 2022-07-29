# -*- coding:utf-8 -*-
"""
    2022/07/15
"""
# -*- coding:utf-8 -*-
"""
    SysDevA Final
    2022/07/15
    BukkenMark
    賃貸物件のブックマーク&比較 on PyQt (Python3.8.3)
"""
from time import sleep
from bs4 import BeautifulSoup
import requests


def fetch_bukken_info_on_suumo(url):
    """
     SUUMO((C)RECRUIT Co., Ltd)のサイトの物件詳細情報ページから物件情報を抽出
    :param url: 物件詳細のsuumoページのURL
    :return: 物件のデータ
    """
    target_url = url.format(1)
    req = requests.get(target_url)
    soup = BeautifulSoup(req.text)  # get the site's source codes'


def fetch_bukken_info_on_yahoo_realestate(url):
    """
    Yahoo不動産((C)Yahoo Japan Inc.)のサイトの物件詳細情報ページから物件情報を抽出
    :param url: 物件詳細のyahoo不動産ページのURL
    :return: 物件のデータ
    """


def save2csv(bukkens_info):
    """

    :param bukkens_info:
    :return:
    """


def compare_bukkens(bukken1_info, bukken2_info):
    """
    2物件を項目毎に比較して結果を返す
    :param bukken1:
    :param bukken2:
    :return:
    """


if __name__ == '__main__':
# main






