class BackPack:
    """
    BackPack Class

    Is the backpack in which the player class stores instances of the item class.
    """

    def __init__(self, items, money):
        """
        Parameters:
        items (list, optional): A list of items to fill the backpack.
        money (int, optional): The amount of money in the backpack - used to purchase items in the game.
        """
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
        """
        Sorts the items in the backpack.
        """
        self._backpack.sort()

    def add_money(self, amount):
        """
        Adds money to the backpack and updates the current amount held.
        Parameters:
            amount (int): The amount of money to add.
        """
        self.money += amount
        print(f"You now have ${self.money}")

    def remove_money(self, amount):
        """
        Removes money from the backpack and updates the current amount held.
        Parameters:
            amount (int): The amount of money to remove.
        """
        self.money -= amount
        print(f"You now have ${self.money}")

    def count(self):
        """
        Not currently used in my program - but returns the number of items held in the backpack.
        :return: int: the number of items
        """
        return self._backpack.count()

    def list(self):
        """
        Prints the list of items currently in the backpack.
        """
        if not self._backpack:
            print("Your backpack is empty.")
        else:
            print("You are currently holding:\n")
            for item in self._backpack:
                print(item)

    def add(self, item):
        """
        Allows additional items to be removed from the backpack.
        :param item: the item to be added to the backpack.
        """
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def remove(self, item):
        """
        Allows an item that is currently held in the backpack to be removed.
        :param item: the item to be removed from the backpack
        """
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
