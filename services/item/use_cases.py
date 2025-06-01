from services.item.entities import Item


class ItemUseCases:
    def __init__(self, item_repo):
        self.item_repo = item_repo

    def create_item(self, item_id: str, name: str):
        item = Item(item_id, name)
        return self.item_repo.create(item)

    def list_items(self):
        return self.item_repo.get_all()
