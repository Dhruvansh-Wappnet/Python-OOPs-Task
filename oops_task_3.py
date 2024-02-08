"""Online Shopping Cart"""

class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.__quantity = quantity
        
    def get_product_id(self):
        return self.product_id
    
    def get_product_name(self):
        return self.product_name
    
    def get_product_price(self):
        return self.price
    
    def get_product_quantity(self):
        return self.__quantity
    
    def update_product_quantity(self, new_qty):
        return self.__quantity + new_qty
    
class Customer:
    def __init__(self, customer_id, customer_name, email, address):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = email
        self.address = address
        
    def get_customer_id(self):
        return self.customer_id
    
    def get_customer_name(self):
        return self.customer_name
    
    def get_customer_email(self):
        return self.email
    
    def get_customer_address(self):
        return self.address
    
class ShoppingCart:
    def __init__(self, customer_id, customer_name, email, address, product_id, product_name, price, quantity):
        self.customer = Customer(customer_id, customer_name, email, address)
        # self.product = Product(product_id, product_name, price, quantity)
        self.products = []
        
    def add_product(self, product_name, quantity):
        self.items = (product_name, quantity)
        
            
        