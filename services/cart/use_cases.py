from services.cart.entities import Cart


class CartUseCases:
    def __init__(self, cart_repo):
        self.cart_repo = cart_repo

    def add_item_to_cart(self, user_id: str, item_id: str, quantity: int):
        cart = self.cart_repo.get_by_id(user_id) or Cart(user_id)
        cart.add_item(item_id, quantity)
        return self.cart_repo.save(cart)

    def get_cart(self, user_id: str):
        return self.cart_repo.get_by_id(user_id) or Cart(user_id)
