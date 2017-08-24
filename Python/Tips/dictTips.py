# -*- coding: utf-8 -*-


print '-------dict 小技巧-------'
haha = 'haha'
params = dict(haha='nini')

kw = dict(use_unicode=False, charset='utf8',
          collation='utf8_general_ci', autocommit=False)

defaults = dict(use_unicode=True, charset='utf8',
                collation='utf8_general_ci', autocommit=False)

# 如果该k,v和kw中的一致，则直接添加到参数中。如果不一致，则以defaults中的为准。
for k, v in defaults.iteritems():
    params[k] = kw.pop(k, v)  # kw.pop(k, v) 和 kw.pop(k) 返回的都是v
params.update(kw)  # update 添加字典

# 也可以如下，直接添加。
params['buffered'] = True
params['buffered1'] = True
params['buffered2'] = True
params['buffered2'] = True

