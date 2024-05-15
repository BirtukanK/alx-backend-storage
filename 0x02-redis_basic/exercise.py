#!/usr/bin/env python3
""" Defines redis"""


import redis
import uuid
from typing import Union


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
