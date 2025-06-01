class CartItem:
    def __init__(self, item_id: str, quantity: int):
        self.item_id = item_id
        self.quantity = quantity


class Cart:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.items = []

    def add_item(self, item_id: str, quantity: int):
        for cart_item in self.items:
            if cart_item.item_id == item_id:
                cart_item.quantity += quantity
                return None
        self.items.append(CartItem(item_id, quantity))
