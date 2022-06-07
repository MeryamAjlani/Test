
from flask import Flask, render_template,request,redirect, url_for

import sqlite3

app =Flask(__name__)
app.secret_key="Secret_test"

app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:''@localhost/crud"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False





def fetch_all():
    connection = sqlite3.connect('../data.db', check_same_thread=False)
    cur = connection.cursor()
    emp = cur.execute("SELECT * FROM EMPLOYEE;").fetchall()
    connection.close()
    return emp

def update_employee(id,name,email,phone):
    connection = sqlite3.connect('../data.db', check_same_thread=False)
    connection.execute(
        "UPDATE EMPLOYEE SET NAME=?, EMAIL=?, PHONE=? WHERE ID=?;", (name,email,phone,id,))
    connection.commit()


def add_employee(name,email,phone):
    connection = sqlite3.connect('../data.db', check_same_thread=False)
    connection.execute(
        "INSERT INTO EMPLOYEE (NAME,EMAIL,PHONE) VALUES (?,?,?);", (name,email,phone,))
    connection.commit()

def delete_employee(id):
    connection = sqlite3.connect('../data.db', check_same_thread=False)
    connection.execute(
        "DELETE FROM EMPLOYEE WHERE ID=?;",(id,))
    connection.commit()    

def fetch_by_id(id):
    connection = sqlite3.connect('../data.db', check_same_thread=False)
    cur = connection.cursor()
    employee= cur.execute("SELECT * FROM EMPLOYEE WHERE ID=?;", (id,)).fetchone()
    connection.close()
    return employee

@app.route('/')
def Index():
    all_data=fetch_all()
    return render_template('index.html',employee=all_data)

@app.route('/add',methods=['POST'])
def add():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        add_employee(name,email,phone)
        return redirect(url_for('Index'))

@app.route('/edit/<id>',methods=['GET','POST'])
def edit(id):
    print(id)
    emp=fetch_by_id(int(id))
    print(emp)
    return render_template('edit.html',emp=emp)

@app.route('/delete/<id>',methods=['POST','GET'])
def delete(id):
    delete_employee(id)
    return redirect(url_for('Index'))

@app.route('/send',methods=['POST'])
def update():
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    id=int(request.form['id'])
    update_employee(id,name,email,phone)
    return redirect(url_for('Index'))



if __name__=="__main__":
    app.run(debug=True)

