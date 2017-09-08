# -*- coding: utf-8 -*-

testString = 'hhhhhhh'

import mimetypes


print mimetypes.types_map.get(testString.lower(), 'application/octet-stream')



