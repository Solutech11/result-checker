from flask import Flask,render_template, request, redirect, url_for
from Datb import myDb, myCursor

app=Flask(__name__)


@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/result/<studentID>')
def result (studentID):
    myCursor.execute(f'SELECT * FROM Score WHERE student = "{studentID}"')
    student = myCursor.fetchone()
    
    myCursor.execute(f'SELECT * FROM students WHERE name ="{studentID}"')
    studentDb = myCursor.fetchone()

    return render_template('result.html', student =student, studentDbS= studentDb)

@app.route("/studentlogin", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('student.html')

    if request.method == 'POST':
        _name =request.form['name']
        return redirect(url_for('result',studentID= _name))
    


@app.errorhandler(404)
def not_found(e):
    return render_template("error.html"),404


@app.errorhandler(500)
def p_error(e):
    return render_template("error.html"),500

if __name__ =='__main__':
    app.run(port="3000", debug=True)
