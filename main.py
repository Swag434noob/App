from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Azure!"

if __name__ == '__main__':
    app.run(debug=True)

db = mysql.connector.connect(
    host="mydbserver.mysql.database.azure.com",
    user="adminuser@mydbserver",
    password="MyPassword!",
    database="mydatabase"
)


import mysql.connector
