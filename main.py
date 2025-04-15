from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello"

@app.route("/lift_status", methods=['GET', 'POST'])
def lift_status():
  if request == "POST":
    return "zero"
  else:
    return "one"


if __name__ == '__main__':
  app.run(debug=True)