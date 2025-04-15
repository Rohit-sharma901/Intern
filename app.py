from flask import Flask, jsonify, request, url_for, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


app = Flask(__name__)
app.config['SECRET_KEY']='secretkey'

class Loginform(FlaskForm):
   username= StringField('username')

   
@app.route('/')
def index():
    form= Loginform()
    return render_template('index.html', form=form)
    return '<h1>Hello!</h1>'

@app.route('/home', defaults={'name': 'default'})
@app.route('/home/<string:name>')
def home(name):
   if name:
    return render_template('home.html', name=name, display=True)
   else:
    return render_template('home1.html')
@app.route('/theform', methods=['POST', 'GET'])
def theform():

    if request.method=='GET':
        return render_template('form.html')
    else:
        name=request.form['name']
        location=request.form['location']
        return redirect(url_for('home', name=name, location=location))

@app.route('/member')
def get_member():
   return 'this is all members'

if __name__ == '__main__':
    app.run(debug=True)
