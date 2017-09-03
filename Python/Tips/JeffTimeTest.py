# -*- coding: utf-8 -*-
# timeInfo


import types, os, re, cgi, sys, time, datetime, functools, mimetypes, threading, logging, urllib, traceback

_RE_TZ = re.compile('^([\+\-])([0-9]{1,2})\:([0-9]{1,2})$')
_TIMEDELTA_ZERO = datetime.timedelta(0)

class UTC(datetime.tzinfo):

    def __init__(self, utc):
        utc = str(utc.strip().upper())
        mt = _RE_TZ.match(utc)
        if mt:
            minus = mt.group(1)=='-'
            h = int(mt.group(2))
            m = int(mt.group(3))
            if minus:
                h, m = (-h), (-m)
            self._utcoffset = datetime.timedelta(hours=h, minutes=m)
            self._tzname = 'UTC%s' % utc
        else:
            raise ValueError('bad utc time zone')

    def utcoffset(self, dt):
        return self._utcoffset

    def dst(self, dt):
        return _TIMEDELTA_ZERO

    def tzname(self, dt):
        return self._tzname

    def __str__(self):
        return 'UTC tzinfo object (%s)' % self._tzname

    __repr__ = __str__


tz0 = UTC('+00:00')
print tz0.tzname(None)

tz8 = UTC('+8:00')

from datetime import datetime
u = datetime.utcnow().replace(tzinfo=tz0)
l1 = u.astimezone(tz8)
l2 = u.replace(tzinfo=tz8)
d1 = u - l1
d2 = u - l2
print d1.seconds
print d2.seconds
'''
A UTC tzinfo object. 

>>> tz0 = UTC('+00:00')
>>> tz0.tzname(None)
'UTC+00:00'
>>> tz8 = UTC('+8:00')
>>> tz8.tzname(None)
'UTC+8:00'
>>> tz7 = UTC('+7:30')
>>> tz7.tzname(None)
'UTC+7:30'
>>> tz5 = UTC('-05:30')
>>> tz5.tzname(None)
'UTC-05:30'
>>> from datetime import datetime
>>> u = datetime.utcnow().replace(tzinfo=tz0)
>>> l1 = u.astimezone(tz8)
>>> l2 = u.replace(tzinfo=tz8)
>>> d1 = u - l1
>>> d2 = u - l2
>>> d1.seconds
0
>>> d2.seconds
28800
'''