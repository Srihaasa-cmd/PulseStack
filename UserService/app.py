from flask import Flask,jsonify,request
import sqlite3
import logging
app = Flask (__name__)
logging.basicConfig(
    level=logging.INFO,
    format=" %(asctime)s %(levelname)s %(message)s"
)
def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn
users =[]
##home route
@app.route("/")
def home():
    return "Welcome to PulseStack User Service "
    logging.info("Home endpoint called")
##health route
@app.route("/health")
def health():
    return jsonify({"status" : "UP"} )
    logging.info("Home endpoint called")
##get users
@app.route("/users")
def get_users():
   conn = get_db_connection()
   users = conn.execute("SELECT * FROM users").fetchall()
   logging.info("Fetching all users")
   conn.close()
   return jsonify ([dict(user) for user in users])
##get specific user
@app.route("/users/<int:user_id>")
def get_user(user_id):
    conn = get_db_connection()
    user=conn.execute("SELECT * FROM users WHERE id =? ",(user_id,)).fetchone()
    conn.close()
    if user is None :
        return jsonify({"error":"User does not exist"}),404
    return jsonify(dict(user))
@app.route("/users/<int:user_id>", methods=["PUT"])
##update user
def update_user(user_id):

    data = request.get_json()

    if "name" not in data or "email" not in data:
        return jsonify({
            "error": "Name and email are required"
        }), 400
   

    conn = get_db_connection()

    conn.execute(
        "UPDATE users SET name = ?, email = ? WHERE id = ?",
        (data["name"], data["email"], user_id)
    )
    logging.info(f"Updated user with ID {user_id}")

    conn.commit()

    conn.close()

    return jsonify({
        "message": "User updated successfully"
    })
##delete user
@app.route("/users/<int:user_id>", methods=["DELETE"])

def delete_user(user_id):

    conn = get_db_connection()

    cursor = conn.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )
    logging.info(f"Updated user with ID {user_id}")

    conn.commit()

    conn.close()

    if cursor.rowcount == 0:
        return jsonify({
            "error": "User not found"
        }), 404

    return jsonify({
        "message": "User deleted successfully"
    }) 
## register user
@app.route("/register",methods = ["POST"])
def register():
    data = request.get_json()
    if "name" not in data and "email" not in data :
        return jsonify({
            "error": "Name and email are required"
        }), 400
    new_user = {"id":len(users)+1,"name":data["name"]}
    conn = get_db_connection()
    conn.execute("INSERT INTO users(name,email) VALUES(?,?)" ,(data['name'],data['email']))
    logging.info(f"User '{data['name']}' registered successfully")
    conn.commit()
    conn.close()
   
    return jsonify({"message":"User added successfully"}),201
if __name__ == "__main__":
    app.run( host = "0.0.0.0",port = 5001,debug = True)

