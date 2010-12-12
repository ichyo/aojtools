# coding: utf-8

import sys
from aojtools import api

if len(sys.argv) < 2:
    ps = api.problemcategory()
    d = {}
    for p in ps.problem:
        if p.category in d:
            d[p.category] += 1
        else:
            d[p.category] = 0
    for k in d:
        print k.ljust(15), d[k]
elif sys.argv[1] == 'help':
    print 'usage %s (|category-name|problem-id)'
elif sys.argv[1].isdigit():
    pid = sys.argv[1]
    p = api.problemcategory(id=pid)
    print p.problem[0].category
else:
    ps = api.problemcategory(category=sys.argv[1])
    for i,p in enumerate(sorted(ps.problem, key=lambda p: p.id)):
        print '%04d %f' % (p.id, p.score)
