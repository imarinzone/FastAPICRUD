import uvicorn
from fastapi import FastAPI
import sqlite3, json
from typing import Optional
app = FastAPI()

@app.get('/getByCustomerID/{id}')
def getCustomer(id: int):
    con = sqlite3.connect('todos.db')
    cur = con.cursor()
    ans = list()
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
def getCustomer(name: str):
    con = sqlite3.connect('todos.db')
    temp = ""
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
def getCustomer(id: int):
    con = sqlite3.connect('todos.db')
    temp = ""
    cur = con.cursor()
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
def getCustomer(id: int):
    con = sqlite3.connect('todos.db')
    temp = ""
    cur = con.cursor()
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
def getCustomer(name: str):
    con = sqlite3.connect('todos.db')
    temp = ""
    cur = con.cursor()
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
def getCustomer(id: int):
    con = sqlite3.connect('todos.db')
    temp = ""
    cur = con.cursor()
    ans = list()
    queryStm = "SELECT * FROM tickets where id = ?"
    for row in cur.execute(queryStm, [id]):
        ans.append(row)
    if ans:
        temp = {
            "ticket_id" :ans[0][0],
            "order_id": ans[0][1],
            "amount" : ans[0][2]
        }
    con.close()
    return json.dumps(temp)

@app.get('/getByAmountBetween/{min}')
def getCustomer(min: int, max: Optional[int] = None):
    con = sqlite3.connect('todos.db')
    temp = ""
    cur = con.cursor()
    ans = list()
    queryStm = "SELECT * FROM tickets where amount = ?"
    for row in cur.execute(queryStm, [min]):
        ans.append(row)
    if ans:
        print("works 1")
        temp = {
            "ticket_id" :ans[0][0],
            "order_id": ans[0][1],
            "amount" : ans[0][2]
        }
    if max:
        for row in cur.execute("SELECT * FROM tickets where amount between ? and ?", (min, max)):
            ans.append(row)
        if ans:
            print("works 2")
            temp = {
                "ticket_id" :ans[0][0],
                "order_id": ans[0][1],
                "amount" : ans[0][2]
            }
    con.close()
    return json.dumps(temp)

# task 3. Get all customers related to a paticular store or related fields.
@app.get('/getCustomerByStoreId/{id}')
def getCustomer(id: int):
    con = sqlite3.connect('todos.db')
    temp = ""
    cur = con.cursor()
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
def getCustomer(id: int):
    con = sqlite3.connect('todos.db')
    temp = ""
    cur = con.cursor()
    ans = list()
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

if __name__ == '__main__':
    app.run()