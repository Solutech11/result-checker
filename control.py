from flask import Flask,render_template, request, redirect, url_for
from Datb import myDb, myCursor

app=Flask(__name__)

# base page
@app.route('/')
def indexPage():
    return render_template('index.html')

# student result output
@app.route('/result/<studentname>')
def result (studentname):
    myCursor.execute(f'SELECT * FROM result WHERE student_name = "{studentname}"')
    student = myCursor.fetchone()

    myCursor.execute(f'SELECT * FROM studentAdmin WHERE student_name ="{studentname}"')
    studentDb = myCursor.fetchone()

    myCursor.execute(f'SELECT * FROM course WHERE StudentName = "{studentname}"')
    courses= myCursor.fetchone()
    return render_template('result.html', student =student, studentDbS= studentDb, courses = courses)

# student login result
@app.route("/studentlogin", methods=['GET', 'POST'])
def login():
    # if request.method == 'GET':
    msg=''
    if request.method == 'POST':
        _name =request.form['name']
        _StudentId = request.form['StudentID']
        myCursor.execute(f'SELECT * FROM studentAdmin WHERE student_name="{_name}" AND student_Id= "{_StudentId}" ')
        verify = myCursor.fetchone()
        if verify:
            return redirect(f'result/{_name}')
        else:
            msg = "Incorrect details"
    return render_template('student.html', mes=msg)


# admin level page
@app.route('/adminLevels')
def adminLevels():
    return render_template("adminlevel.html")

# lecturer admin level      
@app.route('/adminLevels/lecturer')
def lecturerLevel():
    return "wawoo"
    
@app.route('/adminLevels/administrative')
def AdministrativeLevel():
    return "ewee"

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html"),404


@app.errorhandler(500)
def p_error(e):
    return render_template("error.html"),500

if __name__ =='__main__':
    app.run(port="3000", debug=True)
