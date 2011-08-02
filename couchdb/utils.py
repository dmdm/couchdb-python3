# -*- coding: utf-8 -*-
import sys

def import_stdlib(name, *items):
    '''Because sometimes __import__ doesn't works correctly'''
    _ = sys.path.pop(0)
    module = __import__(name, {}, {}, items)
    sys.path.insert(0, _)
    res = []
    for item in items:
        res.append(getattr(module, item))
    return res or module