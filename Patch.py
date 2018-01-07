#!/usr/bin/env python
# -*- coding: utf-8 -*-
import chardet
import requests


def m_patch():
    """
    解决 requests 对于编码处理错误的问题。
    详情见: https://github.com/requests/requests/issues/1604
    """
    prop = requests.models.Response.content

    def content(self):
        _content = prop.fget(self)
        if self.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(_content)
            if encodings:
                self.encoding = encodings[0]
            else:
                self.encoding = chardet.detect(_content)['encoding']

            if self.encoding:
                try:
                    _content = _content.decode(self.encoding, 'replace').encode('utf8', 'replace')
                except:  # 服务器端的编码不正确的情况
                    self.encoding = self.apparent_encoding
                    _content = _content.decode(self.encoding, 'replace').encode('utf8', 'replace')
                self._content = _content
                self.encoding = 'utf8'

        return _content

    requests.models.Response.content = property(content)
