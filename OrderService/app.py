from flask import Flask,jsonify
import sqlite3
import logging
app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format=" %(asctime)s %(levelname)s %(message)s"
)
def get_db_connection():
    conn = sqlite3.connect("orders.db")
    conn.row_factory = sqlite3.Row
    return conn
@app.route("/")
def home():
    return "Welcome to OrderService "
    logging.info("Home endpoint called")
@app.route("/health")
def health():
    return jsonify({"Status":"UP"}) 
    logging.info("health endpoint called")
#get orders 
@app.route("/orders")
def get_orders():
    conn = get_db_connection()
    orders = conn.execute("SELECT * FROM orders").fetchall()
    logging.info("fetching all orders")
    conn.close()
    return jsonify([dict(order) for order in orders])
    
# get specific order
@app.route("/orders/<int:order_id>")
def get_order(order_id):
    conn = get_db_connection()
    order=conn.execute("SELECT * FROM orders WHERE id =? ",(order_id,)).fetchone()
    logging.info("fetched specific order by id ")
    conn.close()
    if order is None :
        return jsonify({"error":"Order does not exist"}),404
    return jsonify(dict(order))

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = 5003,debug = True)