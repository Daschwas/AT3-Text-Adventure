class BackPack:
    """
    BackPack Class
    """

    def __init__(self, items, money):
        self._backpack = []
        if items is None:
            items = []
        if type(items) != "<class 'list'>":
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()
        self.money = money

    def sort(self):
        self._backpack.sort()

    def add_money(self, amount):
        self.money += amount
        print(f"You now have ${self.money}")

    def remove_money(self, amount):
        self.money -= amount
        print(f"You now have ${self.money}")

    def count(self):
        return self._backpack.count()

    def list(self):
        if not self._backpack:
            print("Your backpack is empty.")
        else:
            print("You are currently holding:\n")
            for item in self._backpack:
                print(item)

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
        item_lower = item.lower()
        low = 0
        high = len(self._backpack) - 1
        while low <= high:
            mid = (high + low) // 2
            that_item = self._backpack[mid].lower()
            if that_item == item_lower:
                return mid
            elif that_item < item_lower:
                low = mid + 1
            elif that_item > item_lower:
                high = mid - 1
        return -1



