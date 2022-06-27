from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, name, quantity):
        """увеличивает запас items"""
        ...

    @abstractmethod
    def remove(self, name, quantity):
        """уменьшает запас items"""
        ...

    @property
    @abstractmethod
    def get_free_space(self):
        """вернуть количество свободных мест"""
        ...

    @property
    @abstractmethod
    def items(self):
        """возвращает содержание склада в словаре {товар: количество}"""
        ...

    @property
    @abstractmethod
    def get_unique_items_count(self):
        ...


class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    def add(self, name, quantity):
        if name in self._items:
            self._items[name] += quantity
        else:
            self._items[name] = quantity
        self._capacity -= quantity

    def remove(self, name, quantity):
        res = self._items[name] - quantity
        if res > 0:
            # self._capacity = res
            self._items[name] = res
        else:
            del self._items[name]
        self._capacity += quantity

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        self._items = new_items
        self._capacity -= sum(self._items.values())

    @property
    def get_unique_items_count(self):
        return len(self._items.keys())


class Shop(Store):
    def __init__(self):
        super().__init__()
        self._capacity = 20


class Request:
    def __init__(self, info):
        self.info = self._split_info(info)
        self.from_ = self.info[4]
        self.to = self.info[6]
        self.amount = int(self.info[1])
        self.product = self.info[2]

    @staticmethod
    def _split_info(info):
        return info.split(" ")

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to}"

