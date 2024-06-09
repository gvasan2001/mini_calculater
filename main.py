from  flask import Flask , render_template, url_for,request
import mysql.connector


app= Flask(__name__)
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        database="geeklogin")
    return connection

@app.route("/")

def index():
    return render_template("home.html")
@app.route("/register")

def add_user():
    return render_template("register.html")

@app.route("/add_user", methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO users (username, password, email)
        VALUES (%s, %s, %s)
        """, (username, password, email))
    connection.commit()
    cursor.close()
    connection.close()
    return 'User added!'


@app.route("/login")
def login():
    return render_template("login_form.html")
if __name__ == "__main__":
    app.run(debug=True)
# from flask import Flask, render_template, request
# import mysql.connector
#
# app = Flask(__name__)
#
# def get_db_connection():
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="123",
#         database="geeklogin")
#     return connection
#
# @app.route('/')
# def index():
#     return render_template('home.html')
#
# @app.route('/add_user', methods=['POST'])
# def add_user():
#     username = request.form['username']
#     password = request.form['password']
#     email = request.form['email']
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("""
#     INSERT INTO users (username, password, email)
#     VALUES (%s, %s, %s)
#     """, (username, password, email))
#     connection.commit()
#     cursor.close()
#     connection.close()
#     return 'User added!'
#
# if __name__ == '__main__':
#     app.run(debug=True)



# cursor = connection.cursor()
#
# # Create a new table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS  accounts (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(50) NOT NULL,
#     password VARCHAR(255) NOT NULL,
#     email VARCHAR(100) NOT NULL
# )
# """)
#
# # Insert a new user
# cursor.execute("""
# INSERT INTO users (username, password, email)
# VALUES (%s, %s, %s)
# """, ("user2", "pass2", "user1@dsdffgdd.com"))
#
# connection.commit()
#
# # Query the database
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#
# # Close the connection
# cursor.close()
# connection.close()

