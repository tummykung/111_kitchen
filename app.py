from flask import Flask, render_template, request, redirect, g
# from wtforms import Form, TextField, FloatField, BooleanField, IntegerField, SelectField, validators
import collections
import mysql.connector
import random

app = Flask(__name__)

# database connnections
@app.before_request
def before_request():
    g.cnx = mysql.connector.connect(
        user='root',
        password='',
        database='111_kitchen',
        unix_socket="/tmp/mysql.sock",
        port=3307
    )

@app.teardown_request
def teardown_request(exception):
    g.cnx.close()



# ----- (search for courses = index) ------
@app.route('/', methods=['GET', 'POST'])
def index():
    # form = CourseSearchForm(request.form)
    things = [1,2,3]
    cursor = g.cnx.cursor()
    cursor.execute("select * from 111_kitchen;")
    results = cursor.fetchall()

    random_item_index = random.randrange(0, len(results))
    random_menu = results[random_item_index]

    return render_template(
        'index.html',
        menu=results,
        random_menu=random_menu
    )

if __name__ == '__main__':
    app.debug = True
    app.run(port=1111)
