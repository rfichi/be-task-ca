class CartRepo:
    def __init__(self):
        self.carts = {}

    def get_by_id(self, user_id):
        return self.carts.get(user_id)

    def save(self, cart):
        self.carts[cart.user_id] = cart
        return cart
