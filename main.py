import uvicorn
from fastapi import FastAPI
import json
from typing import Optional
from schema import *
from config import DB
from connect import SQLite3Connect


app = FastAPI()
# Get APIs
@app.get('/getByCustomerID/{id}')
def getCustomer(id: int):
    con, cur = SQLite3Connect(DB)
    cur = con.cursor()
    ans = list()
    temp = {}
    queryStm = "SELECT * FROM customers where id = ?"
    for row in cur.execute(queryStm, [id]):
        ans.append(row)

    temp = {
        "id" : ans[0][0],
        "name": ans[0][1]
    }
    con.close()
    return json.dumps(temp)

@app.get('/getByCustomerName/{name}')
def getCustomerByName(name: str):
    con, cur = SQLite3Connect(DB)
    temp = {}
    cur = con.cursor()
    ans = list()
    queryStm = "SELECT * FROM customers where name = ?"
    for row in cur.execute(queryStm, [name]):
        ans.append(row)
    if ans:
        temp = {
            "id" :ans[0][0],
            "name": ans[0][1]
        }
    con.close()
    return json.dumps(temp)

@app.get('/getByOrderID/{id}')
def getOrder(id: int):
    con, cur = SQLite3Connect(DB)
    temp = {}
    ans = list()
    queryStm = "SELECT * FROM Orders where id = ?"
    for row in cur.execute(queryStm, [id]):
        ans.append(row)
    if ans:
        temp = {
            "order_id" :ans[0][0],
            "customer_id": ans[0][1],
            "store_id" : ans[0][2]
        }
    con.close()
    return json.dumps(temp)

@app.get('/getByStoreID/{id}')
def getStore(id: int):
    con, cur = SQLite3Connect(DB)
    temp = {}
    ans = list()
    queryStm = "SELECT * FROM store where id = ?"
    for row in cur.execute(queryStm, [id]):
        ans.append(row)
    if ans:
        temp = {
            "id" :ans[0][0],
            "name": ans[0][1]
        }
    con.close()
    return json.dumps(temp)

@app.get('/getByStoreName/{name}')
def getStoreByName(name: str):
    con, cur = SQLite3Connect(DB)
    temp = {}
    ans = list()
    queryStm = "SELECT * FROM store where store_name = ?"
    for row in cur.execute(queryStm, [name]):
        ans.append(row)
    if ans:
        temp = {
            "id" :ans[0][0],
            "name": ans[0][1]
        }
    con.close()
    return json.dumps(temp)

@app.get('/getByTicketsID/{id}')
def getTicket(id: int):
    con, cur = SQLite3Connect(DB)
    temp = {}
    ans = list()
    queryStm = "SELECT * FROM tickets where id = ?"
    for row in cur.execute(queryStm, [id]):
        ans.append(row)
    if ans:
        temp = {
            "ticket_id" :ans[0][0],
            "order_id": ans[0][1]
        }
    con.close()
    return json.dumps(temp)

@app.get('/getByAmountBetween/{min}')
def getAmountBetween(min: int, max: Optional[int] = None):
    con, cur = SQLite3Connect(DB)
    temp = {}
    ans = list()
    if max:
        for row in cur.execute("SELECT * FROM Orders where amount between ? and ?", (min, max)):
            ans.append(row)
        if ans:
            temp = {
                "order_id": ans[0][0],
                "customer_id": ans[0][1],
                "store_id": ans[0][2],            
                "amount" : ans[0][3]
            }
    else:
        queryStm = "SELECT * FROM Orders where amount = ?"
        for row in cur.execute(queryStm, [min]):
            ans.append(row)
        if ans:
            temp = {
                "order_id": ans[0][0],
                "customer_id": ans[0][1],
                "store_id": ans[0][2],            
                "amount" : ans[0][3]
            }
    con.close()
    return json.dumps(temp)

# task 3. Get all customers related to a paticular store or related fields.
@app.get('/getCustomerByStoreId/{id}')
def getCustomerByStoreId(id: int):
    con, cur = SQLite3Connect(DB)
    temp = {}
    ans = list()
    queryStm = "SELECT c.name, s.store_name, c.id, s.id FROM store s, customers c where s.id = ?"
    for row in cur.execute(queryStm, [id]):
        ans.append(row)
    if ans:
        temp = {
            "customer name" :ans[0][0],
            "store name": ans[0][1],
            "customer id": ans[0][2],
            "store id": ans[0][3]
        }
    con.close()
    return json.dumps(temp)

# task 4. Get all orders related to a paticular store or related fields.
@app.get('/getOrderByStoreId/{id}')
def getOrderByStoreId(id: int):
    con, cur = SQLite3Connect(DB)
    ans = list()
    temp = {}
    queryStm = "SELECT * from Orders where store_id = ?"
    for row in cur.execute(queryStm, [id]):
        ans.append(row)
    if ans:
        temp = {
            "order id" :ans[0][0],
            "customer id": ans[0][1],
            "store id": ans[0][2]
        }
    con.close()
    return json.dumps(temp)

# POST APIs
# task 5. Add new consumers, orders, tickets, stores
@app.post('/setCustomer/{customer}')
def setCustomer(Customer_Values: Customers):
    con, cur = SQLite3Connect(DB)
    ans = list()
    temp = {}
    queryStm = '''INSERT INTO customers (name) VALUES (?)'''
    ans = cur.execute(queryStm, (Customer_Values.name,))
    if ans:
        temp = {
            "row inserted" : ans.rowcount
        }
    con.commit()
    con.close()
    return json.dumps(temp)

@app.post('/setOrders/{Orders}')
def setOrder(Order_Values: Orders):
    con, cur = SQLite3Connect(DB)
    ans = list()
    temp = {}
    queryStm = '''INSERT INTO Orders (customer_id, store_id, amount) VALUES (?, ?, ?)'''
    ans = cur.execute(queryStm, (Order_Values.customer_id, Order_Values.store_id, Order_Values.amount))
    if ans:
        temp = {
            "row inserted" : ans.rowcount
        }
    con.commit()
    con.close()
    return json.dumps(temp)

@app.post('/setTickets/{tickets}')
def setTicket(Tickets_Values: Tickets):
    con, cur = SQLite3Connect(DB)
    ans = list()
    temp = {}
    queryStm = '''INSERT INTO tickets (order_id) VALUES (?)'''
    ans = cur.execute(queryStm, [Tickets_Values.order_id])
    if ans:
        temp = {
            "row inserted" : ans.rowcount
        }
    con.commit()
    con.close()
    return json.dumps(temp)

@app.post('/setStores/{stores}')
def setStore(stores_Values: Store):
    con, cur = SQLite3Connect(DB)
    ans = list()
    temp = {}
    queryStm = '''INSERT INTO store (store_name) VALUES (?)'''
    ans = cur.execute(queryStm, (stores_Values.store_name,))
    if ans:
        temp = {
            "row inserted" : ans.rowcount
        }
    con.commit()
    con.close()
    return json.dumps(temp)

# put APIs
# 6. Update records.
@app.put('/updateCustomerById/{id}')
def updateCustomer(id: int, customer_Value: Customers):
    con, cur = SQLite3Connect(DB)
    ans = list()
    temp = {}
    queryStm = '''UPDATE customers SET name = ? where id = ?'''
    ans = cur.execute(queryStm, (customer_Value.name, id))
    if ans:
        temp = {
            "rows updated" : ans.rowcount
        }
    con.commit()
    con.close()
    return json.dumps(temp)

@app.put('/updateStoresById/{id}')
def updateStore(id: int, stores_Value: Store):
    con, cur = SQLite3Connect(DB)
    ans = list()
    temp = {}
    queryStm = '''UPDATE customers SET store_name = ? where id = ?'''
    ans = cur.execute(queryStm, (stores_Value.name, id))
    if ans:
        temp = {
            "rows updated" : ans.rowcount
        }
    con.commit()
    con.close()
    return json.dumps(temp)

@app.put('/updateTicketsById/{id}')
def updateTickets(id: int, ticket_Values: Tickets):
    con, cur = SQLite3Connect(DB)
    ans = list()
    temp = {}
    queryStm = '''UPDATE tickets SET order_id = ? where id = ?'''
    ans = cur.execute(queryStm, (ticket_Values.id, id))
    if ans:
        temp = {
            "rows updated" : ans.rowcount
        }
    con.commit()
    con.close()
    return json.dumps(temp)

@app.put('/updateOrderById/{id}')
def updateOrder(id: int, order_Values: Orders):
    con, cur = SQLite3Connect(DB)
    ans = list()
    temp = {}
    queryStm = '''UPDATE Orders SET customer_id = ?, store_id = ?, amount = ? where id = ?'''
    ans = cur.execute(queryStm, (order_Values.customer_id,  order_Values.store_id, order_Values.amount, id))
    if ans:
        temp = {
            "rows updated" : ans.rowcount
        }
    con.commit()
    con.close()
    return json.dumps(temp)

# task 7. Delete records.(should delete relationships also)
@app.delete('/deleteOrderById/{id}')
def deleteOrder(id: int):
    con, cur = SQLite3Connect(DB)
    ans = list()
    temp = {}
    queryStm = '''Delete from Orders where id = ?'''
    ans = cur.execute(queryStm, [id])
    if ans:
        temp = {
            "rows deleted" : ans.rowcount
        }
    con.commit()
    con.close()
    return json.dumps(temp)

if __name__ == '__main__':
    app.run()