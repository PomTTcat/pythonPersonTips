# -*- coding: utf-8 -*-



lll = ['1','2','3','4']
print lll
lll.reverse()
print lll

import os

templ_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test')
print templ_path