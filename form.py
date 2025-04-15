from flask import Flask, jsonify, request, url_for, redirect, render_template, flash 
from flask_pymongo import PyMongo
from formv import UserForm

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
app.config['SECRET_KEY'] = 'your_secret_key'

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template("formtemplate2.html")

@app.route('/home', methods=['POST', 'GET'])
def index():
    form = UserForm(request.form)
    if form.validate_on_submit():
        new_record = {
            'UserID': form.userid.data,
            'Username': form.username.data,
            'Current_Company': form.currentcompany.data,
            'Previous_Company': form.previouscompany.data,
            'Duration': form.duration.data,
            'DOB': form.dateofbirth.data
        }
        mongo.db.record.insert_one(new_record)
        return redirect(url_for('success'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}")
    return render_template("formtemplate.html", form=form)

@app.route('/success')
def success():
    return render_template("success.html")



@app.route('/view', methods=['GET', 'POST'])
def view():
    records = []
    if request.method == 'POST':
        userid = request.form.get('userid')
        username = request.form.get('username')
        current_company = request.form.get('currentcompany')
        
        # Construct the search query
        search_query = {}
        if userid:
            search_query['UserID'] = userid
        elif username:
            search_query['Username'] = username
        elif current_company:
            search_query['Current_Company'] = current_company
        
        print(f"Search Query: {search_query}")  # Debugging print statement

        if search_query:
            records = list(mongo.db.record.find(search_query))
            print(f"Records Found: {records}")  # Debugging print statement
    
    # Render the search form and results
    return render_template("view.html", records=records)

if __name__ == '__main__':
    app.run(debug=True)
