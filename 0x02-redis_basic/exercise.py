#!/usr/bin/env python3
"""The Redis Module"""
from typing import Union, Callable

import redis
import uuid
class Cache:
    """Creation of Objects"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb(True)


    def storage(self, data:Union[str, bytes, int, float]) -> str:
        """store a value in redis"""
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(
            self,
            key: str,
            fn: Callable = None,
    ) -> Union[str, bytes, int, float]:
        """Retrieves a value from a Redis data storage.
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """Retrieves a string value from a Redis data storage.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieves an integer value from a Redis data storage.
        """
        return self.get(key, lambda x: int(x))

