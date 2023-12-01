class BackPack:
    """
    BackPack Class



    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [ ] Remove Item
    ToDo: [ ] List Items
    ToDo: [X] Count items
    ToDo: [ ] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items

    """

    def __init__(self, items):
        self._backpack = []
        if items is None:
            items = []
        if type(items) != "<class 'list'>":
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    def sort(self):
        self._backpack.sort()

    def count(self):
        return self._backpack.count()

    def list(self):
        pass

    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def remove(self, item):
        if item is not None:
            self._backpack.remove(item)
            self.sort()

    def in_backpack(self, item):
        """
        Complete this method using a binary search
        returns -1 or False if not found
        returns position if found
        :param item:
        :return: -1 | False | integer
        """
        low = 0
        high = len(self._backpack) - 1
        while low <= high:
            mid = (high + low) // 2
            that_item = self._backpack[mid]
            if that_item == item:
                return mid
            elif that_item < item:
                low = mid + 1
            elif that_item > item:
                high = mid - 1
        return -1