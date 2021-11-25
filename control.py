from flask import Flask,render_template, request, redirect, url_for
from Datb import myDb, myCursor
import string
import random

c=0
size=80

randomlink = ''.join(random.choices(string.ascii_letters+string.digits, k= size))
    
randomStrings= str(randomlink)

# print(randomStrings)

app=Flask(__name__)

password = "nahme get am ode"
username = "lincoln"
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
    # if request.method == 'GET':          yyujlhfm  br  
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
    return "wewewwewew"
    
@app.route('/adminLevels/administrative/login', methods =['GET', 'POST'])
def AdministrativeLevelLogin():
    message=''
    username="lincoln"
    password="u wanna see craze"
    if request.method=="POST":
        _username= request.form["Username"]
        _password = request.form["Password"]

        if username == _username and password== _password:
            message='Done'
            return redirect(f'/adminLevels/administrative/{randomStrings}')
        else:
            message= 'incorrect password'
            
        
    return render_template("higherAdmin login.html", message= message)
    

@app.route(f'/adminLevels/administrative/{randomStrings}', methods=['GET', 'POST'])
def mainadminpage():
    if request.method=='GET':
        stringname = randomStrings
        myCursor.execute('SELECT * FROM studentAdmin')
        studentAdmin =myCursor.fetchall()

        myCursor.execute('SELECT * FROM course')
        course = myCursor.fetchall()

        myCursor.execute('SELECT * FROM lecturerAdmin')
        _lecturerAdmin= myCursor.fetchall()
    
        return render_template('higherAdminMain.html' , student=studentAdmin, course= course, linkd=stringname, lecturer= _lecturerAdmin)

    if request.method=='POST':
        _type = request.form['submit'] 
        if _type== "add":
            _name =request.form['names']
            _studentId = request.form['studentID']
            _email = request.form['email'] 

            myCursor.execute(f'INSERT INTO result(Id, student_name) VALUES("{_studentId}", "{_name}")')
            myDb.commit()

            myCursor.execute(f'INSERT INTO students(name) VALUES("{_name}")')
            myDb.commit()

            myCursor.execute(f'INSERT INTO studentAdmin (student_name, student_Id, email) VALUES("{_name}", "{_studentId}", "{_email}")')
            myDb.commit()

            myCursor.execute(f'INSERT INTO course (StudentName) VALUES("{_name}")')
            myDb.commit()
            return redirect(f'/adminLevels/administrative/{randomStrings}')

        if _type == "add lecture":
            _lectname = request.form['Lectname']
            _lectId = request.form['LectId']
            _course1 = request.form['course1']
            _course2 = request.form['course2']
            _lectemail = request.form['emailLect']
            myCursor.execute(f'INSERT INTO lecturerAdmin(Lecturer_name, lecturer_Id, course1, email, course2) VALUES("{_lectname}","{lectId}", "{_course1}", "{_lectemail}", "{_course2}") ')
            myDb.commit()
            return redirect(f'/adminLevels/administrative/{randomStrings}')
            
@app.route('/lecturer/delete/<name>')
def deletelecturer(name):
    myCursor.execute(f'DELETE FROM lecturerAdmin WHERE Lecturer_name="{name}"')
    myDb.commit()
    return redirect(f'/adminLevels/administrative/{randomStrings}')

@app.route('/student/delete/<name>')
def delete(name):
    myCursor.execute(f'DELETE FROM result WHERE student_name="{name}"')
    myDb.commit()

    myCursor.execute(f'DELETE FROM students WHERE name="{name}"')
    myDb.commit()

    myCursor.execute(f'DELETE FROM studentAdmin WHERE student_name= "{name}"')
    myDb.commit()

    myCursor.execute(f'DELETE FROM course WHERE StudentName ="{name}"')
    myDb.commit()
    return redirect(f'/adminLevels/administrative/{randomStrings}')


@app.route('/student/Edit/<name>')
def editing(name):
    return f"i will edit it later mr/mrs {name}"
# @app.route('/adminLevels/administrative/add', methods=['GET', 'POST'])
# def addStudent():
#     if request.method == 'POST':
#         _submtype= request.form['submit']
#         _username= request.form['Username']
#         _password = request.form['Password']
#         if _username==username and _password==password and _submtype=="submit":

#             if request.method == 'POST' and _submtype=="add":
#                 _studName = request.form['names']
#                 _studId =request.form['studentID']
#                 _email = request.form['email']

#                 myCursor.execute(f'INSERT INTO course (StudentName) VALUES({_studName})')
#                 myDb.commit()

#                 myCursor.execute(f'INSERT INTO result (Id, Student_name) VALUES({_studId},{_studName})')
#                 myDb.commit()

#                 myCursor.execute(f'INSERT INTO studentAdmin (student_name, student_Id, email) VALUES({_studName}, {_studId},{_email})')
#                 myDb.commit()

#                 myCursor.execute(f'INSERT INTO students(name) VALUES ({name})')
#                 myDb.commit()
#                 return redirect('')

                
            
#             return render_template('Adminaddstudent.html')
#     if request.method=='GET':
#         return render_template('higherAdmin login addStudent.html')

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html"),404


@app.errorhandler(500)
def p_error(e):
    return render_template("error.html"),500

if __name__ =='__main__':
    app.run(port="3000", debug=True)
print(randomStrings)