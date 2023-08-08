"""Implements abstract and concrete cache clients.
"""

import json
from abc import ABC, abstractmethod
from pathlib import Path


class Cache(ABC):
    """An abstract cache.
    """

    @abstractmethod
    def store(self, key: str, value: object) -> None:
        """Adds a new key-value pair to the cache.

        Args:
            key (`str`): The lookup value for the cached object.

            value (`object`): The cached object.

        Returns:
            None
        """
        raise NotImplementedError
    

    @abstractmethod
    def fetch(self, key: str) -> object:
        """Fetches an object from the cache.

        Args:
            key (`str`): The lookup value for the cached object.

        Returns:
            (`object`): The cached object.
        """
        raise NotImplementedError
    

class LocalFileCache(Cache):
    """Caches objects by writing them to disk.
    """

    def __init__(self, cache_fpath: Path) -> None:
        """Initializes a new instance of a `LocalFileCache`.

        Args:
            cache_fpath (`Path`): The path to the file used 
                to hold cached objects.

        Returns:
            None
        """
        self._cache_fpath = cache_fpath
        if not cache_fpath.exists():
            self._cache = {}
        else:
            with open(cache_fpath, "r") as f:
                self._cache = json.load(f)


    def __del__(self) -> None:
        """Writes the in-memory cache entries to disk. Called
        after the current instance falls out of reference or
        the program ends.

        Args:
            None

        Returns:
            None
        """
        if self._cache:
            with open(self._cache_fpath, "w") as f:
                json.dump(self._cache, f, indent=2)


    def store(self, key: str, value: object) -> None:
        """Adds a new key-value pair to the cache, overriding
        any existing entries.

        Args:
            key (`str`): The lookup value for the cached object.

            value (`object`): The cached object.

        Returns:
            None
        """
        self._cache[key] = value


    def fetch(self, key: str) -> object:
        """Fetches an object from the cache.

        Args:
            key (`str`): The lookup value for the cached object.

        Returns:
            (`object`): The cached object.
        """
        self._cache.get(key)