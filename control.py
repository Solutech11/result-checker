from flask import Flask,render_template, request, redirect, url_for
from Datb import myDb, myCursor
import string
import random

# higher Admin link
c=0
size=200
randomlink = ''.join(random.choices(string.ascii_letters+string.digits, k= size))  
randomStrings= str(randomlink)


# lecturer link
lectsize=234
lectlink = ''.join(random.choices(string.ascii_letters+string.digits, k= lectsize))
lectStr = lectlink

# student random link
Studsize=234
Studlink = ''.join(random.choices(string.ascii_letters+string.digits, k= lectsize))
StudStr = Studlink

# print(randomStrings)

app=Flask(__name__)

password = "nahme get am ode"
username = "lincoln"
# base page
@app.route('/')
def indexPage():
    return render_template('index.html')

# student result output
@app.route(f'/result/{StudStr}/<studentname>')
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
            return redirect(f'result/{StudStr}/{_name}')
        else:
            msg = "Incorrect details"
    return render_template('student.html', mes=msg, studlnk=StudStr)


# admin level page
@app.route('/adminLevels')
def adminLevels():
    return render_template("adminlevel.html")



            # the higher admin page
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
    _lnk=randomStrings
    stringname = randomStrings
    myCursor.execute('SELECT * FROM studentAdmin')
    studentAdmin =myCursor.fetchall()

    myCursor.execute('SELECT * FROM course')
    course = myCursor.fetchall()

    myCursor.execute('SELECT * FROM lecturerAdmin')
    _lecturerAdmin= myCursor.fetchall()
    

    if request.method=='POST':
        _type = request.form['submit'] 
        # _frm2 = request.form['submits']
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
        elif _type == "addLecturer":
            _lectname = request.form['Lectname']
            _lectId = request.form['LectId']
            _course1 = request.form['course1']
            _course2 = request.form['course2']
            _lectemail = request.form['emailLect']
            
            myCursor.execute( f'INSERT INTO lectureradmin (Lecturer_name, lecturer_Id, course1, email, course2) VALUES("{_lectname}","{_lectId}", "{_course1}", "{_lectemail}", "{_course2}" )' )
            myDb.commit()
            return redirect(f'/adminLevels/administrative/{randomStrings}')
        else:
            return "you are a yahoo"
    
    return render_template('higherAdminMain.html' , student=studentAdmin, course= course, linkd=stringname, lecturer= _lecturerAdmin, _lnk=_lnk)
        
            
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


@app.route(f'/student/Edit/{randomStrings}/<name>', methods=['GET','POST'])
def editing(name):
    _lnk=randomStrings
    if request.method=='POST':
        _name= request.form['name']
        _idStud= request.form['idStud']
        _email = request.form['email']
        myCursor.execute(f'UPDATE students SET name="{_name}" WHERE name="{name}"')
        myDb.commit()
        myCursor.execute(f'UPDATE studentAdmin SET student_name="{_name}", student_Id= "{_idStud}", email="{_email}" WHERE student_name="{name}"')

        myDb.commit()
        myCursor.execute(f'UPDATE course SET StudentName="{name}" WHERE StudentName="{name}" ')
        myDb.commit()
        return redirect(f'/adminLevels/administrative/{_lnk}')

    return render_template('editstudent.html', name=name, _lnk=_lnk)

@app.route(f'/lecturer/Edit/{randomStrings}/<name>', methods=['GET', 'POST'])
def lecturerEdit(name):
    rands= randomStrings
    if request.method=='POST':
        _name = request.form['lectName']
        _id = request.form['lectId']
        _course1 = request.form['course1']
        _course2 = request.form['course2']
        _email = request.form['lectemail']

        myCursor.execute(f'UPDATE lecturerAdmin SET Lecturer_name="{_name}", lecturer_Id="{_id}", course1="{_course1}", course1="{_course2}", email="{_email}" WHERE Lecturer_name="{name}"')
        myDb.commit()

        return redirect(f'/adminLevels/administrative/{randomStrings}')

    myCursor.execute(f'SELECT * FROM lecturerAdmin WHERE Lecturer_name="{name}"')
    cltDB= myCursor.fetchone()
    return render_template('editlecturer.html',lecturer=cltDB, rands=rands)





    # Lecturer Admin page

# lecturer admin level      
@app.route('/adminLevels/lecturerLogin', methods=["GET", "POST"])
def lecturerLevel():
    LectPassword="moslado by teni"
    MSG=''
    if request.method=="POST":
        _name = request.form['LectName']
        _lectID = request.form['lectID']
        _password = request.form['pass']

        myCursor.execute(f'SELECT * FROM lecturerAdmin WHERE Lecturer_name="{_name}" AND lecturer_Id ="{_lectID}"')
        verf= myCursor.fetchone()
        if verf and _password==LectPassword:
            return redirect(f'/AdminLevel/Lecturer/{lectStr}/{_name}')
        else:
            MSG='Incorrect details'
        
    return render_template('lecturerAdminLogin.html', msg=MSG)
    
@app.route(f'/AdminLevel/Lecturer/{lectStr}/<name>')
def lecturer_level(name):
    myCursor.execute(f'SELECT * FROM lecturerAdmin WHERE Lecturer_name="{name}"')
    lect = myCursor.fetchone()

    myCursor.execute('SELECT * FROM course ')
    STUDENTouT= myCursor.fetchall()
    return render_template('lecturerAdmin.html', lect =lect, student= STUDENTouT,lnk=lectStr)

@app.route(f'/AdminLevel/lecturer/{lectStr}/<lecturer>/<student>', methods=['GET', 'POST'])
def student_addscore(lecturer, student):
    msg=''
    if request.method=='POST':
        _course1=request.form['course1']
        _crs= request.form['crs']

        _course2 = request.form['course2']
        csr2 =request.form['crs2']

        if csr2 == 'CSE201':
            myCursor.execute(f'UPDATE course SET CSE201={_course2} WHERE StudentName="{student}"')     
            myDb.commit()   
        elif csr2 =='CSE211':
            myCursor.execute(f'UPDATE course SET CSE211={_course2} WHERE StudentName="{student}"') 
            myDb.commit()       
        elif csr2=='CSE221':
            myCursor.execute(f'UPDATE course SET CSE221={_course2} WHERE StudentName="{student}"')      
            myDb.commit()  
        elif csr2== 'CSE231':
            myCursor.execute(f'UPDATE course SET CSE231={_course2} WHERE StudentName="{student}"')    
            myDb.commit()    
        elif csr2 == 'CSE241':
            myCursor.execute(f'UPDATE course SET CSE241={_course2} WHERE StudentName="{student}"')   
            myDb.commit()     
        elif csr2 == 'CSE251':
            myCursor.execute(f'UPDATE course SET CSE251={_course2} WHERE StudentName="{student}"')        
            myDb.commit()
        
        if _crs=='CSE201':
            myCursor.execute(f'UPDATE course SET CSE201={_course1} WHERE StudentName="{student}"')
            myDb.commit()
            return redirect(f'/AdminLevel/Lecturer/{lectStr}/{lecturer}')
            # myCursor.execute(f'INSERT INTO course(CSE201) VALUES( CSE201="{_course1}")')
            # myCursor.execute(f'INSERT INTO course(CSE211) VALUE()')
        elif _crs=='CSE211':
            myCursor.execute(f'UPDATE course SET CSE211={_course1} WHERE StudentName="{student}"')  
            myDb.commit()
            return redirect(f'/AdminLevel/Lecturer/{lectStr}/{lecturer}')
        elif _crs== 'CSE221':
            myCursor.execute(f'UPDATE course SET CSE221={_course1} WHERE StudentName="{student}"')  
            myDb.commit()
            return redirect(f'/AdminLevel/Lecturer/{lectStr}/{lecturer}')
        elif _crs== 'CSE231':
            myCursor.execute(f'UPDATE course SET CSE231={_course1} WHERE StudentName="{student}"')        
            myDb.commit()
            return redirect(f'/AdminLevel/Lecturer/{lectStr}/{lecturer}')
        elif _crs == 'CSE241':
            myCursor.execute(f'UPDATE course SET CSE241={_course1} WHERE StudentName="{student}"')    
            myDb.commit()
            return redirect(f'/AdminLevel/Lecturer/{lectStr}/{lecturer}')    
        elif _crs == 'CSE251':
            myCursor.execute(f'UPDATE course SET CSE251={_course1} WHERE StudentName="{student}"')        
            myDb.commit()
            return redirect(f'/AdminLevel/Lecturer/{lectStr}/{lecturer}')
        elif _crs== '':
            msg='fill the form right'

        

        
    myCursor.execute(f'SELECT * FROM lecturerAdmin WHERE Lecturer_name="{lecturer}"')
    lectdet= myCursor.fetchone()

    myCursor.execute(f'SELECT * FROM course WHERE StudentName= "{student}"')
    studentdet= myCursor.fetchone()
    return render_template('addscore.html',student=studentdet, lecturer= lectdet, link=lectStr, msg=msg)

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html"),404


@app.errorhandler(500)
def p_error(e):
    return render_template("error.html"),500

if __name__ =='__main__':
    app.run(port="3000", debug=True)
print(randomStrings)