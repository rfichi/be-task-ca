class ItemRepo:
    def __init__(self):
        self.items = {}

    def create(self, item):
        if not self.items.get(item.item_id):
            self.items[item.item_id] = item
            return item
        return None

    def get_all(self):
        return list(self.items.values())

    def get_by_id(self, item_id):
        return self.items.get(item_id)
