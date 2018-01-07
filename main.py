#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

from Patch import m_patch

URL = 'http://www.sdu.edu.cn'


def request_without_patch():
    """
    do requests to http://www.sdu.edu.cn without patch
    """
    req = requests.get(URL)
    return req.text[:496]


def request_with_patch():
    """
    do requests to http://www.sdu.edu.cn without patch
    """
    m_patch()
    req = requests.get(URL)
    return req.text[:496]


if __name__ == '__main__':
    print("BEFORE PATCH:")
    print("*" * 100)
    print(request_without_patch())
    print("*" * 100)
    print('\n')
    print("AFTER PATCH:")
    print("*" * 100)
    print(request_with_patch())
    print("*" * 1000)
