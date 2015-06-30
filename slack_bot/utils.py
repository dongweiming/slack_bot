#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import TimeoutError
from multiprocessing.pool import ThreadPool
from functools import wraps


def timeout(seconds):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            pool = ThreadPool(processes=1)
            async_result = pool.apply_async(fn, args=args, kwds=kwargs)
            try:
                return async_result.get(seconds)
            except TimeoutError:
                return kwargs.pop('default', {'text': 'timeout'})
        return wrapper
    return decorator
