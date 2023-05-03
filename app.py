import os
import psycopg2
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

DATABASE_URL = os.environ["DATABASE_URL"]

class Order(BaseModel):
    customer_name: str
    pizza_type: str
    size: str
    toppings: list

def create_connection():
    return psycopg2.connect(DATABASE_URL)

@app.on_event("startup")
async def startup():
    conn = create_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS orders (id SERIAL PRIMARY KEY, customer_name VARCHAR(255), pizza_type VARCHAR(255), size VARCHAR(10), toppings TEXT[])")

@app.get("/orders")
def get_orders():
    conn = create_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM orders")
            rows = cur.fetchall()
            orders = [{"id": row[0], "customer_name": row[1], "pizza_type": row[2], "size": row[3], "toppings": row[4]} for row in rows]
            return {"orders": orders}

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    conn = create_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM orders WHERE id=%s", (order_id,))
            row = cur.fetchone()
            if row:
                return {"id": row[0], "customer_name": row[1], "pizza_type": row[2], "size": row[3], "toppings": row[4]}
            else:
                return {"error": "Order not found"}

@app.post("/orders")
def create_order(order: Order):
    conn = create_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO orders (customer_name, pizza_type, size, toppings) VALUES (%s, %s, %s, %s) RETURNING id", (order.customer_name, order.pizza_type, order.size, order.toppings))
            row = cur.fetchone()
            conn.commit()
            return {"id": row[0], "message": "Order created successfully"}

@app.put("/orders/{order_id}")
def update_order(order_id: int, new_order: Order):
    conn = create_connection()
    with conn:
        with conn.cursor() as cur:
            # Check if the order with the given ID already exists in the database
            cur.execute("SELECT id FROM orders WHERE id = %s", (order_id,))
            existing_order = cur.fetchone()
            if existing_order is None:
                # If the order doesn't exist, return an error message
                return {"message": f"Order with ID {order_id} not found"}
            else:
                # If the order exists, update its details in the database
                cur.execute("UPDATE orders SET customer_name=%s, pizza_type=%s, size=%s, toppings=%s WHERE id=%s", (new_order.customer_name, new_order.pizza_type, new_order.size, new_order.toppings, order_id))
                conn.commit()
                return {"message": "Order updated successfully"}

@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    conn = create_connection()
    with conn:
        with conn.cursor() as cur:
            # Check if the order with the given ID already exists in the database
            cur.execute("SELECT id FROM orders WHERE id = %s", (order_id,))
            existing_order = cur.fetchone()
            if existing_order is None:
                # If the order doesn't exist, return an error message
                return {"message": f"Order with ID {order_id} not found"}
            else:
                # If the order exists, delete it from the database
                cur.execute("DELETE FROM orders WHERE id=%s", (order_id,))
                conn.commit()
                return {"message": "Order deleted successfully"}

