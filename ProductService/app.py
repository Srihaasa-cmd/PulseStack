from flask import Flask,jsonify
import sqlite3
import logging
app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format=" %(asctime)s %(levelname)s %(message)s"
)
def get_db_connection():
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row
    return conn
@app.route("/")
def home():
    return "Welcome to ProductService "
    logging.info("Home endpoint called")
@app.route("/health")
def health():
    return jsonify({"Status":"UP"}) 
    logging.info("health endpoint called")
#get products 
@app.route("/products")
def get_products():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products").fetchall()
    logging.info("fetching all products")
    conn.close()
    return jsonify([dict(product) for product in products])
    
# get specific product
@app.route("/products/<int:product_id>")
def get_product(product_id):
    conn = get_db_connection()
    product=conn.execute("SELECT * FROM products WHERE id =? ",(product_id,)).fetchone()
    logging.info("fetched specific product by id ")
    conn.close()
    if product is None :
        return jsonify({"error":"Product does not exist"}),404
    return jsonify(dict(product))

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = 5002,debug = True)


