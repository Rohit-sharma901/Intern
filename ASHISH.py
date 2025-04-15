from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user-level", methods=['POST'])
def home():
  user_position = request.form.get('user_floor_level')
  table_columns = 'id, lift-name, lift-floor' 
  return user_position


if __name__ == '__main__':
  app.run(debug=True)