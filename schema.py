from pydantic import BaseModel
class Orders(BaseModel):
    customer_id : int
    store_id : int
    amount : int

class Customers(BaseModel):
    name : str

class Store(BaseModel):
    store_name : str

class Tickets(BaseModel):
    order_id : int