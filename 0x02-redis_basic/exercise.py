#!/usr/bin/env python3
""" Defines redis"""


import redis
import uuid
from typing import Union, Callable


class Cache:
    ''' cache class defines store method'''
    def __init__(self):
        """ init method for Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method to store data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[
                                        str, bytes, int, float, None]:
        """ Method to get value"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        """ Method to get string values"""
        return self.get(key, fn=lambda d: d.decode('utf-8')
                        if isinstance(d, bytes) else d)

    def get_int(self, key: str) -> Union[int, None]:
        """ Method to get int values"""
        return self.get(key, fn=lambda d: int(d)
                        if isinstance(d, bytes) else d)
