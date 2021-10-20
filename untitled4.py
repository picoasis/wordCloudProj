#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:48:53 2021

@author: picoasis
"""

import requests

r = requests.request('GET','http://www.baidu.com')
print(r.status_code)